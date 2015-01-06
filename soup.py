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
    """Scrapes destination provided by user and returns text in window"""

    url = UrlEntry.get()
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    scrape = soup.text
    outputtext = Text(screen)
    outputtext.pack(side=LEFT)
    outputtext.insert(END, scrape)
    sb1 = Scrollbar(screen)
    sb1.pack(side=RIGHT, fill=Y)
    sb1.config(command=outputtext.yview)
    outputtext.config(yscrollcommand=sb1.set)


def linkscrape():
    """Scrapes destination provided by user and returns links in window"""

    url = UrlEntry.get()
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        links = (link.get('href'))
        print links


def printscrape():
    links2 = linkscrape()
    print links2
    sb2 = Scrollbar(screen)
    sb2.pack(side=RIGHT, fill=Y)
    output_text2 = Text(screen, yscrollcommand=sb2.set)
    output_text2.pack(side=TOP)
    output_text2.insert(10.10, links2)
    sb2.config(command=output_text2.yview)


#*** Label ***
UrlLabel = Label(bod, text='Please enter URL here:', bg='grey', fg='black')
UrlLabel.grid(row=1, column=0)

#*** Blank ***
UrlEntry = ttk.Entry(bod)
UrlEntry.grid(row=1, column=1)

#*** Buttons ***
UrlSubmit = ttk.Button(bod, text='Text', command=Textscrape)
UrlSubmit2 = ttk.Button(bod, text='Links', command=printscrape)
UrlCancel = ttk.Button(bod, text='Cancel', command=root.quit)
UrlSubmit.grid(row=1, column=3)
UrlSubmit2.grid(row=1, column=4)
UrlCancel.grid(row=1, column=5)



root.mainloop()


