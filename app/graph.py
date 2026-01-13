"""
LangGraph Workflow Construction
Builds the conversational agent graph with conditional routing.
"""
from langgraph.graph import StateGraph, END
from app.state import AgentState
from app.nodes.intent_node import intent_node
from app.nodes.greeting_node import greeting_node
from app.nodes.rag_node import rag_node
from app.nodes.lead_node import lead_node
from app.nodes.tool_node import tool_node


def route_by_intent(state: AgentState) -> str:
    """
    Route to appropriate node based on classified intent.
    
    IMPORTANT: If lead collection is in progress, continue with lead collection
    instead of re-classifying intent.
    
    Args:
        state: Current agent state
        
    Returns:
        Next node name
    """
    # Check if we're in the middle of lead collection
    lead_info = state.get('lead_info', {})
    has_any_lead_info = bool(lead_info.get('name') or lead_info.get('email') or lead_info.get('platform'))
    has_all_lead_info = bool(lead_info.get('name') and lead_info.get('email') and lead_info.get('platform'))
    
    # If we have some lead info but not all, continue lead collection
    if has_any_lead_info and not has_all_lead_info:
        return 'lead'
    
    # Otherwise, route based on intent
    intent = state.get('intent', 'inquiry')
    
    if intent == 'greeting':
        return 'greeting'
    elif intent == 'inquiry':
        return 'rag'
    elif intent == 'high_intent':
        return 'lead'
    else:
        return 'rag'  # Default to RAG


def should_execute_tool(state: AgentState) -> str:
    """
    Determine if tool should be executed.
    
    Args:
        state: Current agent state
        
    Returns:
        'tool' if ready to execute, 'end' otherwise
    """
    lead_info = state.get('lead_info', {})
    
    # Check if all fields are present and tool not yet called
    has_all_info = (
        bool(lead_info.get('name')) and
        bool(lead_info.get('email')) and
        bool(lead_info.get('platform'))
    )
    
    if has_all_info and not state.get('tool_called', False):
        return 'tool'
    else:
        return 'end'


def create_graph():
    """
    Create and compile the LangGraph workflow.
    
    Returns:
        Compiled graph ready for execution
    """
    # Initialize graph
    workflow = StateGraph(AgentState)
    
    # Add nodes (renamed to avoid state key conflicts)
    workflow.add_node("intent_classifier", intent_node)
    workflow.add_node("greet", greeting_node)
    workflow.add_node("rag_answer", rag_node)
    workflow.add_node("lead_qualifier", lead_node)
    workflow.add_node("execute_tool", tool_node)
    
    # Set entry point
    workflow.set_entry_point("intent_classifier")
    
    # Add conditional routing from intent classifier node
    workflow.add_conditional_edges(
        "intent_classifier",
        route_by_intent,
        {
            "greeting": "greet",
            "rag": "rag_answer",
            "lead": "lead_qualifier"
        }
    )
    
    # Greeting and RAG nodes go to END
    workflow.add_edge("greet", END)
    workflow.add_edge("rag_answer", END)
    
    # Lead node conditionally routes to tool or END
    workflow.add_conditional_edges(
        "lead_qualifier",
        should_execute_tool,
        {
            "tool": "execute_tool",
            "end": END
        }
    )
    
    # Tool node goes to END
    workflow.add_edge("execute_tool", END)
    
    # Compile and return
    return workflow.compile()


if __name__ == "__main__":
    # Test graph creation
    graph = create_graph()
    print("Graph created successfully!")
    print(f"Nodes: {graph.nodes}")
