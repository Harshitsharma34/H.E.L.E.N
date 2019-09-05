from gtts import gTTS
import playsound
import os

num=1

def Speaking_engine(mytext):
    global num
    num=num+1

    obj=gTTS(text=mytext,lang='en',slow=False)
    file=str(num)+".mp3"
    obj.save(file)

    playsound.playsound(file,True)
    os.remove(file)
