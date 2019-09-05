import webbrowser
from Speech import Speaking_engine
import os
from selenium import webdriver



def search_web(input): 

	driver = webdriver.Firefox() 
	driver.implicitly_wait(1) 
	driver.maximize_window() 

	if 'youtube' in input.lower(): 

		Speaking_engine("Opening in youtube") 
		indx = input.lower().split().index('youtube') 
		query = input.split()[indx + 1:] 
		driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
		return

	elif 'wikipedia' in input.lower(): 

		Speaking_engine("Opening Wikipedia") 
		indx = input.lower().split().index('wikipedia') 
		query = input.split()[indx + 1:] 
		driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
		return

	else: 

		if 'google' in input: 

			indx = input.lower().split().index('google') 
			query = input.split()[indx + 1:] 
			driver.get("https://www.google.com/search?q =" + '+'.join(query)) 

		elif 'search' in input: 

			indx = input.lower().split().index('google') 
			query = input.split()[indx + 1:] 
			driver.get("https://www.google.com/search?q =" + '+'.join(query)) 

		else: 

			driver.get("https://www.google.com/search?q =" + '+'.join(input.split())) 

		return


# function used to open application 
# present inside the system. 
def open_application(input): 

	if "chrome" in input: 
		Speaking_engine("Google Chrome") 
		os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
		return

	elif "firefox" in input or "mozilla" in input: 
		Speaking_engine("Opening Mozilla Firefox") 
		os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe') 
		return

	elif "word" in input: 
		Speaking_engine("Opening Microsoft Word") 
		os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk') 
		return

	elif "excel" in input: 
		Speaking_engine("Opening Microsoft Excel") 
		os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk') 
		return

	else: 

		Speaking_engine("Application not available") 
		return
