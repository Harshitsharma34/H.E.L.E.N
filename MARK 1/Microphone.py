import speech_recognition as sr
from Speech import Speaking_engine


def Microphone_engine():
    obj = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")

        audio=obj.listen(source,phrase_time_limit=5)

    print("Recognizing...")

    try:
        text=obj.recognize_google(audio,language='en_US')
        print("You said: ",text)
        return text

    except:
        Speaking_engine("Sorry sir! I could not understand what you are trying to say,please try again")
        return 0


    
