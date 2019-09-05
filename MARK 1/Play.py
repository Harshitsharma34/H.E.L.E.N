import webbrowser
from Google import get_platform

def playSong(song):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    url = "https://www.youtube.com.tr/search?q={}".format(song)
    webbrowser.get(chrome_path).open(url)   
