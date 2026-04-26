import time
import os
from core.vision import capture_frame
from core.audio_in import listen_and_transcribe
from core.audio_out import speak_text
from core.brain import get_response

def main():
    print("SIASTA is starting up...")
    speak_text("Hello Tushar, I am SIASTA, your personal AI assistant. How may I assist you?")
    
    while True:
        # Capture webcam frame
        image_path = capture_frame()
        
        # Listen for command
        user_text = listen_and_transcribe()
        
        if user_text:
            # Get AI response
            ai_response = get_response(user_text, image_path)
            
            # Speak the response
            speak_text(ai_response)
        
        # Clean up temp image
        if os.path.exists(image_path):
            os.unlink(image_path)
        
        # Small delay to prevent rapid looping
        time.sleep(1)

if __name__ == "__main__":
    main()