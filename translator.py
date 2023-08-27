from mtranslate import translate

def my_translated(text, language):
    try:
        translated_text = translate(text, language)
        return translated_text
    except:
        print("Unable to recognize the audio, try again!")
