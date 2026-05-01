import speech_recognition as sr

_recognizer = sr.Recognizer()
_microphone = None
_ambient_calibrated = False


def get_microphone():
    global _microphone
    if _microphone is None:
        _microphone = sr.Microphone()
    return _microphone


def listen_and_transcribe():
    global _ambient_calibrated

    with get_microphone() as source:
        print("Listening...")

        if not _ambient_calibrated:
            _recognizer.adjust_for_ambient_noise(source)
            _ambient_calibrated = True

        audio = _recognizer.listen(source)

        try:
            text = _recognizer.recognize_google(audio)
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
