"""
    Searches the input string for keywords, or commands.
    If keywords are found, it calls appropriate function.
    List of functions:
    (1) Open maps for a place
    (2) Play Game
    (3) Tell the time.
    (4) Google, or search for a string online.
    (5) Open Google
    (6) Play Song on Youtube
    (7) Reading News feed
    (8) Can play songs from your directory
    (9) Can send mail to multiple recipients
    (10) Can check the weather of any place, info of any known personality  

"""
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Speech import Speaking_engine
from Microphone import Microphone_engine 
from Game import game
import time, datetime
from Play import playSong
from Google import google,google_search,maps
import feedparser
from Email import email
from Computations import calculation,timedate
import os
import wikipedia
import wolframalpha,webbrowser
import datetime


"""greets = ['hi', 'hello', 'hello there', 'hi there', 'hey', 'hey there', 'namaste', 'hola','Howdy']

botintro = ['who are you', "what's your name", 'who am I talking to', 'what are you', 'what is your name',
            'what are you called', 'what do people call you']

weatherRep = ['how is the weather today', 'current weather conditions', 'how is the weather', 'weather conditions',
              'weather forecast']

word_list1 = word_tokenize(greets)

word_list2 = word_tokenize(botintro)

word_list3 = word_tokenize(weatherRep)"""


def helen(data):
    #Splitting each sentence in a list of words.
    word_list = word_tokenize(data)
    
    #Setting up stop_words: words that are redundant.
    stop_words = set(stopwords.words('english'))

    #Creating space for a list of sentences without stop_words.
    if "search" not in word_list and "google" not in word_list and "Search" not in word_list and "Google" not in word_list:
        filtered_sentence = [w for w in word_list if not w in stop_words]
    else:
        filtered_sentence = [w for w in word_list]
    
    if ("bored" in filtered_sentence):
        Speaking_engine("Let's play a game then!!")
        game()
    elif 'time' in filtered_sentence:
        Speaking_engine(time.strftime("%A") + " "+ str(datetime.datetime.now())[:16])    
        timedate()
    elif 'song' in filtered_sentence and filtered_sentence.index('play') < filtered_sentence.index('song'):
        filtered_sentence = [w for w in filtered_sentence if w != "called" and w != "named" and w != "titled"]
        pos = filtered_sentence.index('song') + 1
        Speaking_engine("Opening Youtube Searches for {}".format(filtered_sentence[pos]))
        playSong(filtered_sentence[pos])  

    elif 'game' in filtered_sentence and filtered_sentence.index('play') < filtered_sentence.index('game'):
        game()

    elif 'google' in filtered_sentence or "Google" in filtered_sentence:
        if len(filtered_sentence) > 1:
            if 'open' in filtered_sentence and 'google' in filtered_sentence and filtered_sentence.index('open') < filtered_sentence.index('google'):
                google()
            if 'open' in filtered_sentence and 'Google' in filtered_sentence and filtered_sentence.index('open') < filtered_sentence.index('Google'):
                google()
            else:
                pos = 0
                if 'google' in filtered_sentence:
                    pos = filtered_sentence.index('google') + 1
                elif 'Google' in filtered_sentence:
                    pos = filtered_sentence.index('Google') + 1
                if 'word' in filtered_sentence and filtered_sentence[-1] != 'word':
                    filtered_sentence =[w for w in filtered_sentence if w != "word"]

                search_string = ''.join(filtered_sentence[pos:])
                google_search(search_string)
        else:
            Speaking_engine("If you want me to open google, say 'open google'")
            Speaking_engine("If you want me to search for a word,"
                "say 'google <word>'")

    elif 'search google' in filtered_sentence or 'search on google' in filtered_sentence or 'google' in filtered_sentence:
        if filtered_sentence[-1] == "search":
            Speaking_engine("What would you like me to search?")
            for j in range(5):
                search_string = Microphone_engine()
                if(search_string!='error'):
                    google_search(search_string)
                    break
            return None
        pos = filtered_sentence.index('search') + 1
        search_string = " ".join(filtered_sentence[pos:])
        google_search(search_string)
    elif 'location' in filtered_sentence:
        if filtered_sentence[-1]=="location":
            Speaking_engine("What place should I look for?")
            for j in range(5):
                location = Microphone_engine()
                if(location!="error"):
                    maps(location)
                    break
            return None
           
        pos = filtered_sentence.index('location')+1
        loc = "".join(filtered_sentence[pos:])
        maps(loc)
    elif 'news' in filtered_sentence:
        Speaking_engine("Here are the top 5 stories for you.")
        NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
        for j in range(5):
            entry = NewsFeed.entries[j]
            Speaking_engine("Number {}".format(j+1))
            print(Speaking_engine(entry.title))
            #print(Speaking_engine(entry.summary))
            print("=======================================")
    elif 'email' in filtered_sentence:
        email()
        print("==============================================")
    elif 'time' in filtered_sentence:
        timedate()
    elif 'calculate' in filtered_sentence:
        calculation()
    elif 'application' in filtered_sentence:
        Speaking_engine('Which Application do you want to open')
        input=Microphone_engine()
        open_application(input)
    elif 'play music' in filtered_sentence:
        path='G:\Music\English Chartbusters\ColdPlay'
        music = ['Everglow','Paradise','Adventure Of A Lifetime','Hymn For The Weekend','A Head Full Of Dreams']
        random_music=path+random.choice(music)+'.mp3'
        os.system(random_music)
    elif 'search' in filtered_sentence:
        Speaking_engine("What would you like to search for?")
        query=Microphone_engine()
        try:
            try:
                app_id = "V8QYE3-V8W86UARPP"
                client = wolframalpha.Client(app_id)
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
    else:
        Speaking_engine("I am not aware of this command. Could you please try something else?")
    return None  
        


"""elif 'search' in filtered_sentence:
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
"""                
