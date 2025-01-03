from typing import Dict, Any, Optional
from datetime import datetime, timedelta

# Constants
SESSION_TIMEOUT = 3600  # 1 hour timeout

class SessionManager:
    def __init__(self):
        self.sessions: Dict[str, Dict[str, Any]] = {}
    
    def create_session(self, session_id: str) -> None:
        """Create a new session"""
        self.sessions[session_id] = {
            'created_at': datetime.now(),
            'last_updated': datetime.now(),
            'candidate_info': {},
            'tech_stack': [],
            'current_stage': 'greeting',
            'responses': []
        }
    
    def update_session(self, session_id: str, data: Dict[str, Any]) -> None:
        """Update an existing session"""
        if session_id in self.sessions:
            self.sessions[session_id].update(data)
            self.sessions[session_id]['last_updated'] = datetime.now()
    
    def get_session_data(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Get session data if session exists and is valid"""
        if session_id in self.sessions:
            if self._is_session_valid(session_id):
                return self.sessions[session_id]
        return None
    
    def _is_session_valid(self, session_id: str) -> bool:
        """Check if session is valid and not expired"""
        if session_id not in self.sessions:
            return False
        
        last_updated = self.sessions[session_id]['last_updated']
        if datetime.now() - last_updated > timedelta(seconds=SESSION_TIMEOUT):
            del self.sessions[session_id]
            return False
        return True 