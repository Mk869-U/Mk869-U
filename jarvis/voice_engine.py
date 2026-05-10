"""
Voice Engine - Handles speech recognition and text-to-speech
"""

import sys

try:
    import speech_recognition as sr
    SPEECH_RECOGNITION_AVAILABLE = True
except ImportError:
    SPEECH_RECOGNITION_AVAILABLE = False

try:
    import pyttsx3
    PYTTSX3_AVAILABLE = True
except ImportError:
    PYTTSX3_AVAILABLE = False


class VoiceEngine:
    """
    Handles voice input and output
    """
    
    def __init__(self, config):
        """Initialize voice engine"""
        self.config = config
        self.recognizer = None
        self.tts_engine = None
        
        if SPEECH_RECOGNITION_AVAILABLE:
            self.recognizer = sr.Recognizer()
        
        if PYTTSX3_AVAILABLE:
            self.tts_engine = pyttsx3.init()
            self.tts_engine.setProperty('rate', 150)  # Speaking rate
            self.tts_engine.setProperty('volume', 0.9)  # Volume
    
    def listen(self):
        """
        Listen for voice input
        Returns: Recognized text or empty string
        """
        if not SPEECH_RECOGNITION_AVAILABLE:
            return self.fallback_input()
        
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("[JARVIS] Listening...")
                
                audio = self.recognizer.listen(
                    source,
                    timeout=self.config.get('timeout', 5),
                    phrase_time_limit=10
                )
            
            # Try to recognize speech
            text = self.recognizer.recognize_google(
                audio,
                language=self.config.get('recognition_language', 'en-US')
            )
            
            print(f"You: {text}")
            return text
        
        except sr.UnknownValueError:
            return self.fallback_input("I didn't quite catch that, Sir. Could you repeat?")
        except sr.RequestError as e:
            return self.fallback_input(f"Could not request results: {e}")
        except Exception as e:
            return self.fallback_input()
    
    def fallback_input(self, message=""):
        """
        Fallback to text input if voice fails
        """
        if message:
            print(f"[JARVIS] {message}")
        return input("You: ").strip()
    
    def speak(self, text):
        """
        Speak text using text-to-speech
        """
        if not PYTTSX3_AVAILABLE:
            return
        
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            print(f"Error in text-to-speech: {e}")
