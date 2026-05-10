"""
System Control - Handles PC system operations
"""

import os
import sys
import subprocess
import platform


class SystemControl:
    """
    Controls system operations like shutdown, app launch, etc.
    """
    
    def __init__(self, config):
        """Initialize system controller"""
        self.config = config
        self.os_type = platform.system()  # 'Windows', 'Darwin', 'Linux'
    
    def execute(self, command):
        """
        Execute system command
        """
        if not command:
            return
        
        cmd_type = command.get('type')
        action = command.get('action')
        
        if cmd_type == 'system':
            self.execute_system_command(action)
        elif cmd_type == 'app':
            self.launch_application(command.get('app_name'))
        elif cmd_type == 'audio':
            self.control_audio(action, command.get('value'))
    
    def execute_system_command(self, action):
        """
        Execute system commands
        """
        try:
            if action == 'shutdown':
                self.shutdown()
            elif action == 'restart':
                self.restart()
            elif action == 'sleep':
                self.sleep()
            elif action == 'lock':
                self.lock()
        except Exception as e:
            print(f"Error executing system command: {e}")
    
    def shutdown(self):
        """Shutdown the system"""
        if self.os_type == 'Windows':
            os.system('shutdown /s /t 30')
        else:
            os.system('shutdown -h +1')
    
    def restart(self):
        """Restart the system"""
        if self.os_type == 'Windows':
            os.system('shutdown /r /t 30')
        else:
            os.system('shutdown -r +1')
    
    def sleep(self):
        """Put system to sleep"""
        if self.os_type == 'Windows':
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        elif self.os_type == 'Darwin':
            os.system('osascript -e "tell application \"System Events\" to sleep"')
        else:
            os.system('systemctl suspend')
    
    def lock(self):
        """Lock the system"""
        if self.os_type == 'Windows':
            os.system('rundll32.exe user32.dll,LockWorkStation')
        elif self.os_type == 'Darwin':
            os.system('osascript -e "tell application \"System Events\" to keystroke \"q\" using {command down, control down}"')
        else:
            os.system('loginctl lock-session')
    
    def launch_application(self, app_name):
        """
        Launch an application
        """
        try:
            if self.os_type == 'Windows':
                os.startfile(app_name)
            elif self.os_type == 'Darwin':
                subprocess.Popen(['open', '-a', app_name])
            else:
                subprocess.Popen([app_name])
        except Exception as e:
            print(f"Could not launch {app_name}: {e}")
    
    def control_audio(self, action, value=None):
        """
        Control audio (volume up/down, mute)
        """
        # This would require additional audio control libraries
        # Placeholder for now
        pass
