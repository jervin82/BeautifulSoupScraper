from bs4 import BeautifulSoup
import requests
from Tkinter import *
import ttk

root = Tk()
root.title('Soup Scraper')

#*** Body ***
bod = Frame(root)
bod.pack()

#Text scraper button
def Textscrape():
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


#Link scraper button
def linkscrape():
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
    output_text2.insert(END, links)
    output_window2.title('Scraper Results')
    output_window2.geometry('600x500')


UrlLabel = Label(bod, text='Please enter URL here:', bg='white', fg='black')
UrlEntry = ttk.Entry(bod)
UrlSubmit = ttk.Button(bod, text='Text', command=Textscrape)
UrlSubmit2 = ttk.Button(bod, text='Links', command=linkscrape)
UrlCancel = ttk.Button(bod, text='Cancel', command=root.quit)

UrlLabel.grid(row=1, column=0)
UrlEntry.grid(row=1, column=1)
UrlSubmit.grid(row=1, column=3)
UrlSubmit2.grid(row=1, column=4)
UrlCancel.grid(row=1, column=5)





root.mainloop()


