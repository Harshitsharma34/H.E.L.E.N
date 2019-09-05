import wolframalpha
from Speech import Speaking_engine
import time
import datetime


app_id = "V8QYE3-V8W86UARPP"
client = wolframalpha.Client(app_id)

def calculation(input):
    

    indx=input.lower().split.index('calculate')

    query=input.split()[indx + 1:]

    res= client.query(' '.join(query))

    answer = next(res.results).text

    Speaking_engine("The answer is " + answer)

def timedate():
    now = datetime.datetime.now()
    t1 = ''


    def tick():
        global t1
        t2 = time.strftime("%I:%M:%S %p")
        if t2 != t1:
            t1 = t2


        def timing():
            tick()
            reply = ("Current time is " + t1)
            Speaking_engine(reply)
            
            
        
        date = now.strftime("%d-%B-%Y")
        day = now.strftime("%A")

def search(input):
    Speaking_engine("What would you like to search for?")
    query=Microphone_engine()
    try:
        try:
            res = client.query(query)
            results = next(res.results).text
            Speaking_engine('WOLFRAM-ALPHA says - ')
            Speaking_engine('Got it.')
            Speaking_engine(results)
                    
        except:
            results = wikipedia.summary(query, sentences=2)
            Speaking_engine('Got it.')
            Speaking_engine('WIKIPEDIA says - ')
            Speaking_engine(results)
        
    except:
        webbrowser.open('www.google.com')
    
