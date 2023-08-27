from flask_socketio import SocketIO,emit
import numpy as np    
import speech_recognition as sr
import keyboard
import speechtotxt as stt
import prediction_wo_gui as pred
from io import BytesIO
socketio = SocketIO()
current_letter = "" 
current_string = ""
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

@socketio.on("connect")
def handle_connect():
    print("User connected successful")

@socketio.on("video_feed")
def handle_video(src):
    global current_letter
    global current_string
    src = src.split(",")
    chunks = [src[x:x+4] for x in range(0, len(src), 4)]
    larger_chuncks = [chunks[x:x+200] for x in range(0, len(chunks), 200)]
    array = np.array(larger_chuncks, dtype=np.uint8)
    #new_image = Image.fromarray(array)
    res = pred.scan_frame(array)
    try:
        if res != current_letter:
            if res.lower()  == "next" and current_letter != "Backspace":
                current_string += current_letter                                                 
            elif res.lower() == "backspace":
                current_string = current_string[:-1]
            elif res.lower() == "space":
                current_string += " "
            print("Current String",current_string)
            emit("char",{"char":current_string})
    except:
        pass
    with open("speech.txt","w") as f:
        f.write(current_string)
    current_letter = res

@socketio.on("microfeed")
def micro(data):
    print(data)
    print("backend recieved")
    s = BytesIO(data)
    stt.speech2txt(s)

@socketio.on("microstatus")
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

@socketio.on("get_data")
def get_data():
    print("RAN code :123")
    with open("temp_file.txt",'r') as f:
        data = f.read()
        emit("waiting_data",data)

@socketio.on("speak")
def speak():
    print("works")
    with open("speech.txt","r") as f:
          texts = f.read()
    import Text2Speech as t2s
    t2s.TTS(texts,'en')
    emit("speaker_ready")