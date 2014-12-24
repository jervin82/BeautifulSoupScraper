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
    """Scrapes destination provided by user and returns text in new text window"""

    url = UrlEntry.get()
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    scrape = soup.text
    output_window = Toplevel(root)
    sb = Scrollbar(output_window)
    outputtext = Text(output_window)
    sb.pack(side=RIGHT, fill=Y)
    outputtext.pack(side=RIGHT, fill=Y)
    sb.config(command=outputtext.yview)
    outputtext.config(yscrollcommand=sb.set)
    outputtext.insert(END, scrape)
    output_window.title('Scraper Results')
    output_window.geometry('600x500')


def linkscrape():
    """Scrapes destination provided by user and returns links in new text window"""

    url = UrlEntry.get()
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        links = (link.get('href'))
    output_window2 = Toplevel(root)
    sb2 = Scrollbar(output_window2)
    output_text2 = Text(output_window2)
    sb2.pack(side=RIGHT, fill=Y)
    output_text2.pack(side=RIGHT, fill=Y)
    sb2.config(command=output_text2.yview)
    output_text2.config(yscrollcommand=sb2.set)
    output_text2.insert(1.1, links)
    output_window2.title('Scraper Results')
    output_window2.geometry('600x500')

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


