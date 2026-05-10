# 🤖 JARVIS - PC Control System

> "Just A Rather Very Intelligent System" - Your Tony Stark-inspired PC Assistant

![JARVIS](https://img.shields.io/badge/JARVIS-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-2.7+-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

JARVIS is a voice-controlled PC assistant inspired by Tony Stark's AI from the Marvel Cinematic Universe. Control your entire computer using natural language commands, from system operations to application launches.

## Features

✨ **Voice Recognition** - Speak commands naturally  
🔊 **Text-to-Speech** - JARVIS responds with speech  
⚙️ **System Control** - Shutdown, restart, sleep, lock  
🚀 **App Launcher** - Open applications by voice  
⏰ **Information Query** - Ask for time, weather, and more  
🧠 **Natural Language** - Understands conversational commands  
⚡ **Tony Stark Personality** - Witty, intelligent responses  

## Installation

### Prerequisites
- Python 2.7 or higher
- Microphone for voice input
- Speaker for audio output

### Setup

```bash
# Clone the repository
git clone https://github.com/Mk869-U/jarvis-pc-control.git
cd jarvis-pc-control

# Install dependencies
pip install -r requirements.txt

# Run JARVIS
python jarvis/jarvis.py
```

## Usage

### Voice Commands

Once JARVIS is running, just speak naturally:

```
"JARVIS, what time is it?"
"JARVIS, open Chrome"
"JARVIS, shutdown"
"JARVIS, sleep mode"
"JARVIS, lock my computer"
```

### Text Commands

If voice is disabled, simply type:

```
You: jarvis, what time is it?
JARVIS: It is currently 10:30 AM, Sir.
```

## Command Examples

### System Commands
- `shutdown` - Shutdown the computer
- `restart` - Restart the computer
- `sleep` - Put computer to sleep
- `lock` - Lock the workstation

### Application Launcher
- `open Chrome`
- `launch Notepad`
- `start Calculator`

### Information
- `What time is it?`
- `Hello` - Get a greeting
- `Help` - See available commands

## Configuration

Edit `jarvis/config.json` to customize:

```json
{
  "voice_enabled": true,
  "recognition_language": "en-US",
  "speak_responses": true,
  "name": "JARVIS",
  "listen_keyword": "jarvis",
  "timeout": 5,
  "owner_name": "Sir"
}
```

## File Structure

```
jarvis-pc-control/
├── jarvis/
│   ├── jarvis.py              # Main application
│   ├── voice_engine.py        # Speech recognition & TTS
│   ├── system_control.py      # System operations
│   ├── command_processor.py   # Command parsing
│   └── config.json            # Configuration
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── LICENSE                     # MIT License
```

## Features Breakdown

### Voice Engine
- Uses Google Speech Recognition API
- Multi-language support
- Pyttsx3 for text-to-speech
- Fallback to text input if voice fails

### System Control
- Cross-platform support (Windows, macOS, Linux)
- Safe shutdown/restart procedures
- Workstation locking
- Sleep mode activation

### Command Processor
- Natural language understanding
- Context-aware responses
- Extensible command structure
- Tony Stark personality responses

## Troubleshooting

### Microphone not detected
```bash
# Install PyAudio (may require system packages)
pip install --upgrade pyaudio
```

### Speech recognition not working
- Ensure you have an active internet connection
- Check microphone permissions
- Try lowering the timeout in config.json

### Text-to-speech not working
- Verify your system has audio output
- Check speaker volume
- Ensure pyttsx3 is properly installed

## Platform Support

| OS | Status | Notes |
|---|---|---|
| Windows | ✅ Full Support | All features working |
| macOS | ✅ Full Support | All features working |
| Linux | ✅ Full Support | Requires additional setup |

## Future Enhancements

- [ ] Weather integration
- [ ] Calendar/schedule management
- [ ] Email notifications
- [ ] Smart home integration
- [ ] Custom command creation
- [ ] Context awareness
- [ ] Learning from user behavior

## Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## License

MIT License - See LICENSE file for details

## Disclaimer

This project is inspired by fictional AI systems and is for educational and entertainment purposes. Always ensure proper security measures are in place before using voice-controlled system commands.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**"If you're nothing without the suit, then you shouldn't have it."** - Tony Stark

*Build something remarkable with JARVIS.*
