"""
Tool Execution Node
Executes mock_lead_capture when all lead info is collected.
"""
from langchain_core.messages import AIMessage
from app.state import AgentState
from app.tools.lead_capture import mock_lead_capture


def tool_node(state: AgentState) -> AgentState:
    """
    Execute lead capture tool if conditions are met.
    
    Conditions:
        - name is present
        - email is present
        - platform is present
        - tool_called is False
    
    Args:
        state: Current agent state
        
    Returns:
        Updated state with tool_called flag set
    """
    lead_info = state.get('lead_info', {})
    
    # Check if all required fields are present
    has_name = bool(lead_info.get('name'))
    has_email = bool(lead_info.get('email'))
    has_platform = bool(lead_info.get('platform'))
    
    # Execute tool only if all conditions met
    if has_name and has_email and has_platform and not state.get('tool_called', False):
        # Execute the tool
        mock_lead_capture(
            name=lead_info['name'],
            email=lead_info['email'],
            platform=lead_info['platform']
        )
        
        # Mark tool as called
        state['tool_called'] = True
        
        # Add confirmation message
        response = "Thank you! Your information has been captured. Our team will reach out to you soon to help you get started with AutoStream!"
        state['messages'].append(AIMessage(content=response))
    
    return state
