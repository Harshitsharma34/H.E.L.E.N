from gtts import gTTS 
import webbrowser
import os
import playsound
import speech_recognition as sr
import sys 
import wolframalpha
num=1
def Speaking_engine(mytext): #assistant speaks 
    global num
    num=num+1
    language='en'

    obj=gTTS(text=mytext,lang='en',slow=False)
    file=str(num)+".mp3"
    obj.save(file)

    playsound.playsound(file,True)
    os.remove(file)

    

def Microphone_Engine():#get_audio
    obj = sr.Recognizer()
    audio= ''

    with sr.Microphone() as source:
        print("Speak....")

        audio=obj.listen(source,phrase_time_limit=5)
    print("Stop")

    try:
        text=obj.recognize_google(audio,language='en-US')
        print("User: ", text)
        return text

    except:
        Speaking_engine("Sorry Sir! I could not understand your voice. Please try again one more time")
        return 0


def process_text(input):
    try:
        if "who are you" in input or "who created you" or "define yourself" in input:
            speak=''' Hello, I am a digital assistant and my created is Harshit. I am here to make your
                life easier. You can command me to do any tasks like calculating,opeing applications ,
                scraping etcetra etcetra.'''
            Speaking_engine(speak)
            return
        elif "calculate" in input.lower():
            app_id="V8QYE3-V8W86UARPP"
            client=wolframalpha.Client(app_id)

            indx=input.lower().split.index('calculate')

            query=input.split()[indx + 1:]

            res= client.query(' '.join(query))

            answer = next(res.results).text

            Speaking_engine("The answer is " + answer)
            return
    except Exception as e:
        print(e)
        Speaking_engine("I dont understand what you are saying do you want to quit")
        ans=Microphone_engine()
        if "yes" in str(ans) or "exit" in str(ans):
            sys.exit()




if __name__=="__main__":
    Speaking_engine("Hello,What's Your name Sir?")
    name="Boss"
    name=Microphone_Engine()
    Speaking_engine("Hello, "+str(name)+ ".")
    while(1):
        Speaking_engine("What can I Do for you Sir ?")
        text=Microphone_Engine().lower()
        if text == 0:
            continue
        if "exit" in str(text) or "bye" in str(text) or "quit" in str(text):
            Speaking_engine("Well sure Boss ! ")
            break
        if "how are you" in str(text) or "how you doing" in str(text):
            Speaking_engine("I'm doing great sir...How About you?")
            
        if "i am also doing great" in str (text) or "i'm great" in str(text):
            Speaking_engine("Ohhh !! Great Then")

        process_text(text)


        

    
