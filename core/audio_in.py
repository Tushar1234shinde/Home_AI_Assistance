import speech_recognition as sr
import sounddevice as sd

_recognizer = sr.Recognizer()
_ambient_calibrated = False
_sample_rate = 16000
_sample_width = 2
_phrase_time_limit = 5


def record_audio(duration, sample_rate):
    print("Listening...")
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype='int16'
    )
    sd.wait()
    return recording


def listen_and_transcribe():
    global _ambient_calibrated

    try:
        if not _ambient_calibrated:
            print("Calibrating microphone...")
            sd.check_input_settings(samplerate=_sample_rate, channels=1, dtype='int16')
            _ambient_calibrated = True

        recording = record_audio(_phrase_time_limit, _sample_rate)
        audio = sr.AudioData(recording.tobytes(), _sample_rate, _sample_width)
        text = _recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None
    except Exception as e:
        print(f"Microphone error: {e}")
        return None

if __name__ == "__main__":
    text = listen_and_transcribe()
    if text:
        print(f"Transcribed: {text}")
