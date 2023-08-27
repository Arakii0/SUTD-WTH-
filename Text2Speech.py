from gtts import gTTS
with open("speech.txt","r") as f:
    latest_data = f.readlines()[-1]

def TTS(mytext, language):
    mytext= latest_data
    myobj = gTTS(text=mytext, lang=language, slow=False)
    
    # Saving the converted audio in a mp3 file named
    myobj.save("Translated.mp3")
