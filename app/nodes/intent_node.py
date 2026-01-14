"""
Intent Classification Node
Classifies user intent into: greeting, inquiry, or high_intent
"""
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from app.state import AgentState
import os


def intent_node(state: AgentState) -> AgentState:
    """
    Classify user intent from the last message.
    
    Intent categories:
        - greeting: Casual greetings (hi, hello, how are you)
        - inquiry: Questions about product, pricing, features
        - high_intent: Interest in trying/signing up (want to try, get started)
    
    IMPORTANT: If lead collection is in progress, skip classification
    and maintain high_intent to continue the flow.
    
    Args:
        state: Current agent state
        
    Returns:
        Updated state with intent field
    """
    # Get last user message first
    last_message = state['messages'][-1].content.lower()
    
    # Check if we're in the middle of lead collection
    if state.get('collecting_lead', False):
        # Allow user to ask questions during lead collection
        # Detect if this is a question rather than providing info
        question_indicators = ['?', 'what', 'how', 'why', 'when', 'where', 'tell me', 'explain']
        is_question = any(indicator in last_message for indicator in question_indicators)
        
        if is_question:
            # User is asking a question - temporarily answer it
            state['intent'] = 'inquiry'
            return state
        else:
            # User is providing info - continue lead collection
            state['intent'] = 'high_intent'
            return state
    
    # Get last user message
    last_message = state['messages'][-1].content
    
    # Initialize LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0
    )
    
    # Intent classification prompt
    prompt = f"""Classify the user's intent into exactly one category:

Categories:
- greeting: Casual greetings like "hi", "hello", "how are you"
- inquiry: Questions about product, pricing, features, policies
- high_intent: Expressions of interest like "want to try", "sign up", "get started", "interested"

User message: "{last_message}"

Respond with ONLY the category name (greeting, inquiry, or high_intent)."""
    
    response = llm.invoke(prompt)
    intent = response.content.strip().lower()
    
    # Validate intent
    if intent not in ['greeting', 'inquiry', 'high_intent']:
        intent = 'inquiry'  # Default to inquiry if unclear
    
    state['intent'] = intent
    return state
