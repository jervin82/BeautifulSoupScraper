from bs4 import BeautifulSoup
import requests
from Tkinter import *
import ttk

root = Tk()
root.title('Soup Scraper')

#*** Body ***
bod = Frame(root, bg='grey')
bod.pack()


#*** Guts ***
def Textscrape():
    """Scrapes destination provided by user and returns text in window"""

    url = UrlEntry.get()
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html5")
    [s.extract() for s in soup('script')]
    file = open('Textfile.txt', 'w')
    file.write(soup.text.encode('utf-8'))
    file.close()

def linkscrape():
    """Scrapes destination provided by user and returns links in window"""

    url = UrlEntry.get()
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html5")
    links = str(soup.findAll('a'))
    file = open('Linkfile.txt', 'w')
    file.write(links)
    file.close()
    

#*** Label ***
UrlLabel = Label(bod, text='Please enter URL here:', bg='grey', fg='black')
UrlLabel.grid(row=1, column=0)

#*** Blank ***
UrlEntry = ttk.Entry(bod)
UrlEntry.insert(0, 'http://')
UrlEntry.grid(row=1, column=1)

#*** Buttons ***
UrlSubmit = ttk.Button(bod, text='Text', command=Textscrape)
UrlSubmit2 = ttk.Button(bod, text='Links', command=linkscrape)
UrlCancel = ttk.Button(bod, text='Cancel', command=root.quit)
UrlSubmit.grid(row=1, column=3)
UrlSubmit2.grid(row=1, column=4)
UrlCancel.grid(row=1, column=5)

root.mainloop()


