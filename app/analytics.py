"""
Conversation Analytics Module
Tracks agent performance metrics for optimization.
"""
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List


class ConversationAnalytics:
    """
    Simple analytics tracker for conversation metrics.
    
    Tracks:
        - Total conversations
        - Lead conversion rate
        - Average turns to conversion
        - Drop-off points
    """
    
    def __init__(self, log_file: str = "analytics.json"):
        """Initialize analytics tracker."""
        self.log_file = Path(log_file)
        self.sessions: List[Dict] = []
        self._load_sessions()
    
    def _load_sessions(self):
        """Load previous sessions from file."""
        if self.log_file.exists():
            try:
                with open(self.log_file, 'r') as f:
                    self.sessions = json.load(f)
            except Exception:
                self.sessions = []
    
    def _save_sessions(self):
        """Save sessions to file."""
        try:
            with open(self.log_file, 'w') as f:
                json.dump(self.sessions, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save analytics: {e}")
    
    def log_session(self, state: Dict, turn_count: int):
        """
        Log a completed conversation session.
        
        Args:
            state: Final agent state
            turn_count: Number of conversation turns
        """
        session = {
            'timestamp': datetime.now().isoformat(),
            'turns': turn_count,
            'lead_captured': state.get('tool_called', False),
            'lead_info': state.get('lead_info', {}),
            'final_intent': state.get('intent', ''),
            'completed': turn_count < 10  # Assuming max 10 turns
        }
        
        self.sessions.append(session)
        self._save_sessions()
    
    def get_stats(self) -> Dict:
        """
        Calculate aggregate statistics.
        
        Returns:
            Dictionary with analytics metrics
        """
        if not self.sessions:
            return {
                'total_conversations': 0,
                'leads_captured': 0,
                'conversion_rate': "0%",
                'avg_turns_to_conversion': 0,
                'completion_rate': "0%"
            }
        
        total = len(self.sessions)
        captured = sum(1 for s in self.sessions if s['lead_captured'])
        completed = sum(1 for s in self.sessions if s['completed'])
        
        # Calculate average turns for successful conversions
        successful_turns = [s['turns'] for s in self.sessions if s['lead_captured']]
        avg_turns = sum(successful_turns) / len(successful_turns) if successful_turns else 0
        
        return {
            'total_conversations': total,
            'leads_captured': captured,
            'conversion_rate': f"{(captured/total*100):.1f}%",
            'avg_turns_to_conversion': round(avg_turns, 1),
            'completion_rate': f"{(completed/total*100):.1f}%"
        }
    
    def print_report(self):
        """Print a formatted analytics report."""
        stats = self.get_stats()
        
        print("\n" + "="*50)
        print("📊 CONVERSATION ANALYTICS REPORT")
        print("="*50)
        print(f"Total Conversations:     {stats['total_conversations']}")
        print(f"Leads Captured:          {stats['leads_captured']}")
        print(f"Conversion Rate:         {stats['conversion_rate']}")
        print(f"Avg Turns (Success):     {stats['avg_turns_to_conversion']}")
        print(f"Completion Rate:         {stats['completion_rate']}")
        print("="*50 + "\n")


# Example usage
if __name__ == "__main__":
    # Demo
    analytics = ConversationAnalytics()
    
    # Simulate some sessions
    analytics.log_session({
        'tool_called': True,
        'lead_info': {'name': 'John', 'email': 'john@example.com', 'platform': 'Instagram'},
        'intent': 'high_intent'
    }, turn_count=7)
    
    analytics.log_session({
        'tool_called': False,
        'lead_info': {},
        'intent': 'inquiry'
    }, turn_count=3)
    
    analytics.print_report()
