import speech_recognition as sr
import keyboard



def speech2txt(state):
    print("received")
    r = sr.Recognizer()
    def recognize_audio(audio_data):
        try:
            text = r.recognize_google(audio_data)
            print("Recognized:", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""
        except sr.RequestError as e:
            print("Error requesting recognition; {0}".format(e))
            return ""
    with sr.Microphone() as source:
        is_recording = False
        audio_data = None

        print("Press and hold Spacebar to start recording...")

        while True:
            if keyboard.is_pressed("space") and not is_recording:
                print("Recording...")
                is_recording = True
                audio_data = r.listen(source)
            elif is_recording and not keyboard.is_pressed("space"):
                print("Recording stopped.")
                is_recording = False
                break

    if audio_data is not None:
        print("Recognizing...")
        text = recognize_audio(audio_data)
        return str(text).strip()
    else:
        return ""

if __name__ == "__main__":
    recognized_text = speech2txt()
    print("Final Recognized Text:", recognized_text)
