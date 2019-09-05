from Speech import Speaking_engine
from Microphone import Microphone_engine
import smtplib


def email():
    
    Speaking_engine('Who is the recipient? ')
    recipient = Microphone_engine()

    if 'mail' in recipient:
        try:
            Speaking_engine('What should I say? ')
            content = Microphone_engine
        
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("harshitsharma34", 'mjolnir@qseft')
            server.sendmail('harshitsharma34', recipient, content)
            server.close()
            Speaking_engine('Email sent!')

        except:
            Speaking_engine('Sorry Sir! I am unable to send your message at this moment!')

