"""
AutoStream Conversational Agent
Main application for terminal-based chat interface.
"""
import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from app.graph import create_graph
from app.state import AgentState
from app.analytics import ConversationAnalytics


def main():
    """Run the conversational agent in terminal."""
    # Load environment variables (override=True forces reload from .env)
    load_dotenv(override=True)
    
    # Check for API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: GOOGLE_API_KEY not found in environment variables.")
        print("Please create a .env file with your Gemini API key.")
        print("Example: GOOGLE_API_KEY=your_key_here")
        return
    
    # Show API key is loaded (first and last 4 chars for security)
    print(f"API Key loaded: {api_key[:4]}...{api_key[-4:]}")
    
    # Create graph
    print("Initializing AutoStream Agent...")
    print("(This may take a moment to load the embedding model)\n")
    
    graph = create_graph()
    
    # Initialize analytics tracker
    analytics = ConversationAnalytics()
    
    # Initialize state
    state: AgentState = {
        'messages': [],
        'intent': '',
        'lead_info': {},
        'tool_called': False,
        'collecting_lead': False
    }
    
    print("="*60)
    print("AutoStream Conversational Agent")
    print("="*60)
    print("Chat with the agent to learn about AutoStream!")
    print("Type 'quit' or 'exit' to end the conversation.\n")
    
    turn_count = 0
    max_turns = 10  # Support up to 10 turns (more than required 5-6)
    
    while turn_count < max_turns:
        # Get user input
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("\nAgent: Thank you for chatting with AutoStream! Have a great day!")
            break
        
        # Add user message to state
        state['messages'].append(HumanMessage(content=user_input))
        
        # Run graph
        try:
            state = graph.invoke(state)
            
            # Get last AI message
            last_ai_message = None
            for msg in reversed(state['messages']):
                if hasattr(msg, 'type') and msg.type == 'ai':
                    last_ai_message = msg.content
                    break
            
            if last_ai_message:
                print(f"\nAgent: {last_ai_message}\n")
            
            turn_count += 1
            
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again.\n")
    
    if turn_count >= max_turns:
        print("\nMaximum conversation turns reached. Thank you for chatting!")
    
    # Log session for analytics
    analytics.log_session(state, turn_count)
    
    print("\n" + "="*60)
    print("Conversation Summary:")
    print(f"Total turns: {turn_count}")
    print(f"Lead captured: {state.get('tool_called', False)}")
    if state.get('tool_called'):
        print(f"Lead info: {state.get('lead_info', {})}")
    print("="*60)
    
    # Show analytics (optional - can be disabled for cleaner output)
    # analytics.print_report()


if __name__ == "__main__":
    main()
