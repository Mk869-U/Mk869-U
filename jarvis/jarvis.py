#!/usr/bin/env python
"""
JARVIS - Just A Rather Very Intelligent System
Tony Stark-inspired PC Control Assistant
"""

import os
import sys
import json
import threading
import time
from voice_engine import VoiceEngine
from system_control import SystemControl
from command_processor import CommandProcessor

class JARVIS:
    """
    Main JARVIS application class
    """
    
    def __init__(self, config_file='config.json'):
        """Initialize JARVIS with configuration"""
        self.config = self.load_config(config_file)
        self.voice_engine = VoiceEngine(self.config)
        self.system_control = SystemControl(self.config)
        self.command_processor = CommandProcessor(self.config)
        self.running = False
        
        self.print_startup_message()
    
    def load_config(self, config_file):
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Config file not found: {config_file}")
            return self.get_default_config()
    
    def get_default_config(self):
        """Return default configuration"""
        return {
            "voice_enabled": True,
            "recognition_language": "en-US",
            "speak_responses": True,
            "name": "JARVIS",
            "listen_keyword": "jarvis",
            "timeout": 5
        }
    
    def print_startup_message(self):
        """Display the JARVIS startup message"""
        print("\n" + "="*60)
        print(" " * 15 + "JARVIS ACTIVATED")
        print("="*60)
        print(f"\n🤖 Welcome, Sir. I am {self.config.get('name', 'JARVIS')}")
        print("   Just A Rather Very Intelligent System")
        print("\n   System Status: Online")
        print("   Voice Recognition: " + ("Enabled" if self.config.get('voice_enabled') else "Disabled"))
        print("   Response Output: " + ("Voice + Text" if self.config.get('speak_responses') else "Text Only"))
        print("\n   Listening for commands... (Say or type 'jarvis' to wake me)\n")
        print("="*60 + "\n")
    
    def start(self):
        """Start JARVIS main loop"""
        self.running = True
        
        try:
            while self.running:
                # Get user input
                user_input = self.get_input()
                
                if user_input.lower() in ['quit', 'exit', 'shutdown']:
                    self.shutdown()
                    break
                
                # Process command
                if user_input.strip():
                    response = self.command_processor.process(user_input)
                    self.output_response(response)
                    
                    # Execute command if necessary
                    if hasattr(self.command_processor, 'last_command'):
                        self.system_control.execute(self.command_processor.last_command)
        
        except KeyboardInterrupt:
            print("\n\n[JARVIS] Shutting down...")
            self.shutdown()
    
    def get_input(self):
        """Get input from user via voice or text"""
        if self.config.get('voice_enabled'):
            return self.voice_engine.listen()
        else:
            return input("You: ").strip()
    
    def output_response(self, response):
        """Output response via text and/or voice"""
        print(f"\n[JARVIS] {response}\n")
        
        if self.config.get('speak_responses'):
            self.voice_engine.speak(response)
    
    def shutdown(self):
        """Shutdown JARVIS gracefully"""
        shutdown_message = "Shutting down, Sir. It has been a pleasure serving you."
        print(f"\n[JARVIS] {shutdown_message}\n")
        
        if self.config.get('speak_responses'):
            self.voice_engine.speak(shutdown_message)
        
        self.running = False


def main():
    """Main entry point"""
    jarvis = JARVIS()
    jarvis.start()


if __name__ == '__main__':
    main()
