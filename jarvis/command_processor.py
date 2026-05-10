"""
Command Processor - Processes natural language commands
"""

import re
from datetime import datetime


class CommandProcessor:
    """
    Processes user commands and generates appropriate responses
    """
    
    def __init__(self, config):
        """Initialize command processor"""
        self.config = config
        self.last_command = None
        
        self.responses = {
            'greeting': [
                "Good day, Sir. How may I be of service?",
                "At your service, Sir.",
                "Welcome back, Sir. What can I assist you with?"
            ],
            'time': [
                f"It is currently {datetime.now().strftime('%I:%M %p')}, Sir.",
                f"The time is {datetime.now().strftime('%I:%M %p')}."
            ],
            'help': [
                "I can help you with system controls, app launches, and information queries. What would you like to do?"
            ]
        }
    
    def process(self, user_input):
        """
        Process user input and generate response
        """
        user_input_lower = user_input.lower().strip()
        
        # Remove wake word if present
        if user_input_lower.startswith('jarvis'):
            user_input_lower = user_input_lower[6:].strip()
        
        # Check for system commands
        if self._is_greeting(user_input_lower):
            return self._get_random_response('greeting')
        
        elif self._is_time_query(user_input_lower):
            return self._get_random_response('time')
        
        elif self._is_help_request(user_input_lower):
            return self._get_random_response('help')
        
        elif self._is_shutdown_command(user_input_lower):
            self.last_command = {'type': 'system', 'action': 'shutdown'}
            return "Initiating shutdown sequence, Sir. Farewell."
        
        elif self._is_restart_command(user_input_lower):
            self.last_command = {'type': 'system', 'action': 'restart'}
            return "Restarting the system now, Sir."
        
        elif self._is_sleep_command(user_input_lower):
            self.last_command = {'type': 'system', 'action': 'sleep'}
            return "Putting the system to sleep, Sir."
        
        elif self._is_lock_command(user_input_lower):
            self.last_command = {'type': 'system', 'action': 'lock'}
            return "Locking the workstation, Sir."
        
        elif self._is_app_launch(user_input_lower):
            app_name = self._extract_app_name(user_input_lower)
            self.last_command = {'type': 'app', 'app_name': app_name}
            return f"Launching {app_name}, Sir."
        
        else:
            return "I'm not certain what you're asking for, Sir. Could you rephrase that?"
    
    def _get_random_response(self, response_type):
        """Get random response from response pool"""
        import random
        responses = self.responses.get(response_type, [])
        return random.choice(responses) if responses else "Understood, Sir."
    
    def _is_greeting(self, text):
        """Check if input is a greeting"""
        greetings = ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening']
        return any(greeting in text for greeting in greetings)
    
    def _is_time_query(self, text):
        """Check if asking for time"""
        time_words = ['time', 'what time', 'current time']
        return any(word in text for word in time_words)
    
    def _is_help_request(self, text):
        """Check if asking for help"""
        help_words = ['help', 'assist', 'what can you do', 'capabilities']
        return any(word in text for word in help_words)
    
    def _is_shutdown_command(self, text):
        """Check for shutdown command"""
        shutdown_words = ['shutdown', 'turn off', 'power off']
        return any(word in text for word in shutdown_words)
    
    def _is_restart_command(self, text):
        """Check for restart command"""
        restart_words = ['restart', 'reboot']
        return any(word in text for word in restart_words)
    
    def _is_sleep_command(self, text):
        """Check for sleep command"""
        sleep_words = ['sleep', 'standby']
        return any(word in text for word in sleep_words)
    
    def _is_lock_command(self, text):
        """Check for lock command"""
        lock_words = ['lock', 'secure']
        return any(word in text for word in lock_words)
    
    def _is_app_launch(self, text):
        """Check if user wants to launch an app"""
        launch_words = ['open', 'launch', 'start', 'run']
        return any(word in text for word in launch_words)
    
    def _extract_app_name(self, text):
        """Extract application name from command"""
        launch_words = ['open', 'launch', 'start', 'run']
        
        for word in launch_words:
            pattern = f"{word} (.+)"
            match = re.search(pattern, text)
            if match:
                return match.group(1)
        
        return "application"
