"""
Greeting Node
Handles casual greetings with friendly responses.
"""
from langchain_core.messages import AIMessage
from app.state import AgentState


def greeting_node(state: AgentState) -> AgentState:
    """
    Generate friendly greeting response.
    
    Args:
        state: Current agent state
        
    Returns:
        Updated state with greeting response
    """
    greeting_responses = [
        "Hello! I'm here to help you with AutoStream, your AI-powered video editing assistant. How can I assist you today?",
        "Hi there! Welcome to AutoStream. Feel free to ask me about our pricing plans, features, or anything else!",
        "Hey! Great to see you. I can help you learn about AutoStream's video editing solutions. What would you like to know?"
    ]
    
    # Use first response for consistency
    response = greeting_responses[0]
    
    state['messages'].append(AIMessage(content=response))
    return state
