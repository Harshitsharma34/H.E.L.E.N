
import webbrowser
import sys

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]
chrome_path=""

def get_chromePath():
    platform = get_platform()
    path=""
    if platform=='Linux':
        path = '/usr/bin/google-chrome %s'
    elif platform=='OS X':
        path = 'open -a /Applications/Google\ Chrome.app %s'
    elif platform=='Windows':
        path = 'C:\Program Files (x86)\Mozilla Firefox.exe %s'
    return path
def google():
    chrome_path = get_chromePath()
    url = 'https://www.google.com/'
    webbrowser.get(chrome_path).open(url)

def google_search(term):
    chrome_path = get_chromePath()
    url = "https://www.google.com.tr/search?q={}".format(term)
    webbrowser.get(chrome_path).open(url)

def maps(location):
    url="https://www.google.nl/maps/place/"+location+"/&amp"
    chrome_path = get_chromePath()
    webbrowser.get(chrome_path).open(url)
