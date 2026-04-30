import time
import os
from core.vision import capture_frame
from core.audio_in import listen_and_transcribe
from core.audio_out import speak_text
from core.brain import get_response

WAKE_PHRASES = ("hey siasta", "hi siasta", "ok siasta")
EXIT_COMMANDS = ("exit", "quit", "shutdown", "goodbye")
SLEEP_COMMANDS = ("sleep", "go to sleep", "stand by", "stop listening")


def normalize_text(text):
    return text.strip().lower() if text else ""


def extract_command(transcript):
    normalized = normalize_text(transcript)
    if not normalized:
        return None

    for command in EXIT_COMMANDS:
        if normalized == command:
            return ("exit", "")

    for command in SLEEP_COMMANDS:
        if normalized == command:
            return ("sleep", "")

    for phrase in WAKE_PHRASES:
        if normalized.startswith(phrase):
            user_command = normalized[len(phrase):].strip(" ,.!?")
            return ("wake", user_command)

    return None


def main():
    print("SIASTA is starting up...")
    speak_text("Hello Tushar. Say hey siasta to wake me, or say exit to close me.")
    
    while True:
        transcript = listen_and_transcribe()
        command = extract_command(transcript)

        if command:
            action, inline_prompt = command

            if action == "exit":
                speak_text("Shutting down. Goodbye Tushar.")
                break

            if action == "sleep":
                speak_text("Going into standby mode.")
                time.sleep(1)
                continue

            user_text = inline_prompt
            if not user_text:
                speak_text("I am listening.")
                user_text = listen_and_transcribe()

            if user_text:
                image_path = capture_frame()

                try:
                    ai_response = get_response(user_text, image_path)
                    speak_text(ai_response)
                except Exception as e:
                    print(f"Error getting AI response: {e}")
                    speak_text("I'm sorry, I encountered an error processing your request.")

                if image_path and os.path.exists(image_path):
                    try:
                        os.unlink(image_path)
                    except Exception as e:
                        print(f"Error deleting temp image: {e}")
        elif transcript:
            print("Wake phrase not detected. Say 'Hey SIASTA' to activate me.")
        
        # Small delay to prevent rapid looping
        time.sleep(1)

if __name__ == "__main__":
    main()
