import speech_recognition as sr
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
def micro(status):
    if status == 1:
        with sr.Microphone() as source:
            audio_data = None
            audio_data = r.listen(source)
    else:
        print("Recording stopped.")
        if audio_data is not None:
                print("Recognizing...")
                text = recognize_audio(audio_data)
                return str(text).strip()
        else:
                return ""
        

micro(1)
input("converto ?")
micro(2)