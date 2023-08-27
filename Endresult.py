from speechtotxt import speech2txt
from translator import my_translated
from Text2Speech import TTS

if __name__ == "__main__":
    # Gets the text to be translated first
    text = speech2txt()

    # Gets the language to be translated to
    language = input("Enter the Language : ")

    # Gets the fully translated text
    result = my_translated(text,language)
    
    # Translates the text to speech and saves the file
    TTS(result,language)

    # Prints the translated language
    print(f"Translated result : {result}")
