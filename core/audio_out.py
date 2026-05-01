import pyttsx3

_engine = None


def get_engine():
    global _engine
    if _engine is not None:
        return _engine

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    female_voice = None
    for voice in voices:
        if 'female' in voice.name.lower() or 'zira' in voice.name.lower() or 'hazel' in voice.name.lower():
            female_voice = voice
            break
    if female_voice:
        engine.setProperty('voice', female_voice.id)

    engine.setProperty('rate', 180)
    _engine = engine
    return _engine


def speak_text(text):
    engine = get_engine()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak_text("Hello, I am SIASTA, your personal AI assistant.")
