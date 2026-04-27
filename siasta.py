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
        # Listen for command first so the image captured is relevant to when the user finishes speaking
        user_text = listen_and_transcribe()
        
        if user_text:
            # Capture webcam frame
            image_path = capture_frame()
            
            try:
                # Get AI response
                ai_response = get_response(user_text, image_path)
                
                # Speak the response
                speak_text(ai_response)
            except Exception as e:
                print(f"Error getting AI response: {e}")
                speak_text("I'm sorry, I encountered an error processing your request.")
            
            # Clean up temp image
            if image_path and os.path.exists(image_path):
                try:
                    os.unlink(image_path)
                except Exception as e:
                    print(f"Error deleting temp image: {e}")
        
        # Small delay to prevent rapid looping
        time.sleep(1)

if __name__ == "__main__":
    main()