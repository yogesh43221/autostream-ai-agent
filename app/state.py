"""
Agent State Definition
Maintains conversation context across turns.
"""
from typing import TypedDict, List, Dict
from langchain_core.messages import BaseMessage


class AgentState(TypedDict):
    """
    State schema for the conversational agent.
    
    Fields:
        messages: Full conversation history
        intent: Current intent (greeting, inquiry, high_intent)
        lead_info: Dictionary with name, email, platform
        tool_called: Flag to prevent duplicate tool execution
        collecting_lead: Flag to track if we're in lead collection mode
    """
    messages: List[BaseMessage]
    intent: str
    lead_info: Dict[str, str]
    tool_called: bool
    collecting_lead: bool
