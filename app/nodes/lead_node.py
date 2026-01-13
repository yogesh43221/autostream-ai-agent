"""
Lead Qualification Node
Collects lead information (name, email, platform) when high intent is detected.
"""
from langchain_core.messages import AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from app.state import AgentState
import os
import re


def lead_node(state: AgentState) -> AgentState:
    """
    Collect lead information one field at a time.
    
    Process:
        1. Check which fields are missing (name, email, platform)
        2. Try to extract info from last message
        3. Ask for next missing field
    
    Args:
        state: Current agent state
        
    Returns:
        Updated state with lead_info and response
    """
    lead_info = state.get('lead_info', {})
    if not lead_info:
        lead_info = {}
    
    last_message = state['messages'][-1].content
    
    # Initialize LLM for extraction
    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0
    )
    
    # Check what information we currently have
    has_name = bool(lead_info.get('name'))
    has_email = bool(lead_info.get('email'))
    has_platform = bool(lead_info.get('platform'))
    
    # If this is the FIRST time (no info at all), just ask for name
    if not has_name and not has_email and not has_platform and not state.get('collecting_lead', False):
        state['collecting_lead'] = True
        response = "That's great! I'd love to help you get started with AutoStream. May I have your name?"
        state['messages'].append(AIMessage(content=response))
        return state
    
    # Otherwise, we're collecting info - try to extract from last message
    # Extract name if we don't have it yet
    if not has_name:
        extraction_prompt = f"""Extract the person's name from this message: "{last_message}"

If a name is present, respond with ONLY the name. If no name is found, respond with "NOT_FOUND"."""
        
        result = llm.invoke(extraction_prompt)
        extracted_name = result.content.strip()
        
        if extracted_name != "NOT_FOUND" and len(extracted_name) > 0:
            lead_info['name'] = extracted_name
            has_name = True
    
    # Extract email if we have name but not email
    if has_name and not has_email:
        # Try regex first
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, last_message)
        
        if emails:
            lead_info['email'] = emails[0]
            has_email = True
        else:
            # Try LLM extraction
            extraction_prompt = f"""Extract the email address from this message: "{last_message}"

If an email is present, respond with ONLY the email. If no email is found, respond with "NOT_FOUND"."""
            
            result = llm.invoke(extraction_prompt)
            extracted_email = result.content.strip()
            
            if extracted_email != "NOT_FOUND" and '@' in extracted_email:
                lead_info['email'] = extracted_email
                has_email = True
    
    # Extract platform if we have name and email but not platform
    if has_name and has_email and not has_platform:
        extraction_prompt = f"""Extract the social media platform from this message: "{last_message}"

Common platforms: Instagram, Facebook, YouTube, TikTok, Twitter, LinkedIn

If a platform is mentioned, respond with ONLY the platform name. If no platform is found, respond with "NOT_FOUND"."""
        
        result = llm.invoke(extraction_prompt)
        extracted_platform = result.content.strip()
        
        if extracted_platform != "NOT_FOUND" and len(extracted_platform) > 0:
            lead_info['platform'] = extracted_platform
            has_platform = True
    
    # Update state with collected info
    state['lead_info'] = lead_info
    
    # Generate response based on what we still need
    if not has_name:
        response = "May I have your name?"
    elif not has_email:
        response = f"Thanks, {lead_info['name']}! What's your email address?"
    elif not has_platform:
        response = "Great! Which social media platform do you primarily create content for?"
    else:
        # All information collected - clear flag and prepare for tool execution
        state['collecting_lead'] = False
        response = f"Perfect! I have all your information. Let me get you set up, {lead_info['name']}!"
    
    state['messages'].append(AIMessage(content=response))
    return state
