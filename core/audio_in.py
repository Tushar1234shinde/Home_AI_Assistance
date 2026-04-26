import speech_recognition as sr

def listen_and_transcribe():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Use the default microphone
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        
        # Listen for audio
        audio = recognizer.listen(source)
        
        try:
            # Transcribe using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

if __name__ == "__main__":
    text = listen_and_transcribe()
    if text:
        print(f"Transcribed: {text}")