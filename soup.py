from bs4 import BeautifulSoup
import requests
from Tkinter import *
import ttk

root = Tk()
root.title('Soup Scraper')

#*** Body ***
bod = Frame(root, bg='grey')
bod.pack()
screen = Frame(root, bg='white')
screen.pack()

#*** Guts ***
def Textscrape():
    """Scrapes destination provided by user and returns text in new text window"""

    url = UrlEntry.get()
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    scrape = soup.text
    outputtext = Text(screen)
    outputtext.pack(side=RIGHT)
    outputtext.insert(END, scrape)
    sb = Scrollbar(screen)
    sb.pack(side=RIGHT, fill=Y)
    sb.config(command=outputtext.yview)
    outputtext.config(yscrollcommand=sb.set)


def linkscrape():
    """Scrapes destination provided by user and returns links in new text window"""

    url = UrlEntry.get()
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        links = (link.get('href'))
        print links
        output_text2 = Text(screen)
        output_text2.pack(side=BOTTOM)
        output_text2.insert(10.10, links)
    sb = Scrollbar(screen)
    sb.pack(side=RIGHT, fill=Y)
    sb.config(command=output_text2.yview)
    output_text2.config(yscrollcommand=sb.set)

#*** Label ***
UrlLabel = Label(bod, text='Please enter URL here:', bg='grey', fg='black')
UrlLabel.grid(row=1, column=0)

#*** Blank ***
UrlEntry = ttk.Entry(bod)
UrlEntry.grid(row=1, column=1)

#*** Buttons ***
UrlSubmit = ttk.Button(bod, text='Text', command=Textscrape)
UrlSubmit2 = ttk.Button(bod, text='Links', command=linkscrape)
UrlCancel = ttk.Button(bod, text='Cancel', command=root.quit)
UrlSubmit.grid(row=1, column=3)
UrlSubmit2.grid(row=1, column=4)
UrlCancel.grid(row=1, column=5)







root.mainloop()


