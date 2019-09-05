import time
from Speech import Speaking_engine
from Helen import helen
from Microphone import Microphone_engine
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
import random
import datetime

greets = ['hi', 'hello', 'hello there', 'hi there', 'hey', 'hey there', 'namaste', 'hola','Howdy']

botintro = ['who are you', "what's your name", 'who am I talking to', 'what are you', 'what is your name',
            'what are you called', 'what do people call you']

weatherRep = ['how is the weather today', 'current weather conditions', 'how is the weather', 'weather conditions',
              'weather forecast','can you tell me the weather of today','weather']

def greetMe():
        time.sleep(2)
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            Speaking_engine('Good Morning! Boss What can I do for you today?')

        if currentH >= 12 and currentH < 18:
            Speaking_engine('Good Afternoon! Boss What can I do for you today?')

        if currentH >= 18 and currentH !=0:
                Speaking_engine('Good Evening!Boss What can I do for you today?')

greetMe()

def main():
    while 1:
        data = Microphone_engine()
        exit_flag = 0
        if data!="" and data!="error":
            if "bye" in data:
                Speaking_engine("Bye, Have a great day!")
                break
            if "helen"==data or "Helen"== data:
                Speaking_engine("Yes right! That's my name. Tell me how may I help you?")
            else:
                helen(data)
                time.sleep(5)
                Speaking_engine("Do you have any other commands?")
                for j in range(5):
                    confirm = Microphone_engine()
                    if "error" not in confirm and "yes" not in confirm:
                        exit_flag=1
                        break
                    elif "yes" in confirm:
                        exit_flag=0
                        break
                if exit_flag == 1:
                    Speaking_engine("Okay then. My work here is done. Have a good day!")
                    break
                else:
                    Speaking_engine("Great!What can I do for you next?")
               
if __name__ == "__main__":
    main()


