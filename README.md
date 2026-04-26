# SIASTA - Personal AI Assistant

SIASTA is a personal AI assistant inspired by JARVIS from Iron Man. She can hear your voice, see through your webcam, and speak back to you.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Add your Google Gemini API key to the `.env` file:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

3. Run the assistant:
   ```
   python siasta.py
   ```

## Features

- **Vision**: Captures frames from your webcam.
- **Audio Input**: Listens to your microphone and transcribes speech.
- **Audio Output**: Speaks responses with a female voice.
- **AI Brain**: Uses Google Gemini 1.5 Pro for intelligent responses.

## Modules

- `core/vision.py`: Webcam capture.
- `core/audio_in.py`: Speech recognition.
- `core/audio_out.py`: Text-to-speech.
- `core/brain.py`: Gemini API integration.
- `siasta.py`: Main application loop.