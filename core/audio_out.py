import pyttsx3

def speak_text(text):
    # Initialize the engine
    engine = pyttsx3.init()
    
    # Set properties for female voice
    voices = engine.getProperty('voices')
    # Try to find a female voice
    female_voice = None
    for voice in voices:
        if 'female' in voice.name.lower() or 'zira' in voice.name.lower() or 'hazel' in voice.name.lower():
            female_voice = voice
            break
    if female_voice:
        engine.setProperty('voice', female_voice.id)
    
    # Set speech rate
    engine.setProperty('rate', 180)
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak_text("Hello, I am SIASTA, your personal AI assistant.")