from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter.ttk import * 

root = Tk()
root.title('Soup Scraper')

#*** Body ***
bod = Frame(root)
bod.pack()


#*** Guts ***
def Textscrape():
    """Scrapes destination provided by user and returns text in window"""

    url = UrlEntry.get()
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, features="html5lib")
    [s.extract() for s in soup('script')]
    file = open('Textfile.txt', 'w')
    file.write(str(soup.text.encode('utf-8')))
    file.close()

def linkscrape():
    """Scrapes destination provided by user and returns links in window"""

    url = UrlEntry.get()
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, features="html5lib")
    links = str(soup.findAll('a'))
    file = open('Linkfile.txt', 'w')
    file.write(links)
    file.close()
    

#*** Label ***
UrlLabel = Label(bod, text='Please enter URL here:')
#UrlLabel.grid(row=1, column=0)

#*** Blank ***
UrlEntry = Entry(bod)
##UrlEntry.insert(0, 'http://')
UrlEntry.grid(row=1, column=1)

#*** Buttons ***
UrlSubmit = Button(bod, text='Text', command=Textscrape)
UrlSubmit2 = Button(bod, text='Links', command=linkscrape)
UrlCancel = Button(bod, text='Cancel', command=root.destroy)
UrlSubmit.grid(row=1, column=3)
UrlSubmit2.grid(row=1, column=4)
UrlCancel.grid(row=1, column=5)

root.mainloop()


