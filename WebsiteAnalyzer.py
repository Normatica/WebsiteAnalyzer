#!/usr/bin/python

from fake_useragent import UserAgent
from Tkinter import *
import threading
from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib2
import ttk

def download(url):
    response = urllib2.urlopen(url)
    webContent = response.read()
    f = open('site1.html', 'w')
    f.write(webContent)
    f.close
    f1 = open('site1.html', 'r')
    f2 = open('site2.html', 'w')
    for line in f1:
        f2.write(line.replace('&#064;', '@'))
    f1.close()
    f2.close()
    with open('site2.html', 'r') as f_input:
        hell = re.findall(r'\b([a-z0-9-_.]+?@[a-z0-9-_.]+)\b', f_input.read(), re.I)
        gol = str(hell)
        f = open('mail.txt', 'a')
        f.write(gol)
        f.close
        s = open("mail.txt").read()
        s = s.replace('\'', '\n')
        s = s.replace(']', '')
        s = s.replace('[', '')
        s = s.replace(',', '\n')
        s = s.replace('\n\n', '')
        s = s.replace(' ', '')
        f = open("mail.txt", 'w')
        f.write(s)
        f.close()


def trade_spider(max_pages, url):
    page = 1
    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}
    print(header)
    while page <= max_pages:
        download(url)
        source_code = requests.get(url, allow_redirects=False, headers=header)
        plain_text = source_code.text.encode('ascii', 'replace')
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.find_all("a"):
            href = str(link.get('href'))
            print(href)
            try:
                download(href)
                get_single_item_data(href)
            except:
                pass

        page += 1


def get_single_item_data(item_url):
    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}
    print(header)
    try:
        download(item_url)
        source_code = requests.get(item_url, headers=header)
        plain_text = source_code.text.encode('ascii', 'replace')
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll("a"):
            href = link.get('href')
            print (href)
            try:
                download(href)
                single_item_data(href)
            except:
                pass
    except:
       pass

def single_item_data(item_url):
    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}
    print(header)
    try:
        download(item_url)
        source_code = requests.get(item_url, headers=header)
        plain_text = source_code.text.encode('ascii', 'replace')
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll("a"):
            href = link.get('href')
            print (href)
            try:
                download(href)
            except:
                pass
    except:
       pass
def show_entry_fields():
    attck = e1.get()
    thread = threading.Thread(target=trade_spider, args=(1, attck))
    thread.daemon = True  
    thread.start()
class progress():
    def __init__(self, parent):
            self.progressbar = ttk.Progressbar(master, orient=HORIZONTAL,length=200,mode="determinate",takefocus=True,maximum=100)
            self.progressbar.grid()
            self.t = threading.Thread()
            self.t.__init__(target = self.progressbar.start, args = ())
            self.t.start()
master = Tk()
master.geometry('450x100')
C = Canvas(master, bg="blue", height=2500, width=3000)
filename = PhotoImage(file = "error404.png")
background_label = Label(master, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
Label(master, text="URL: ").grid(row=10, sticky=E)
master.title("Website Analyzer")
e1 = Entry(master)
e1.grid(row=10, column=1)
Button(master, text='Start', command=show_entry_fields).grid(row=100, column=60, sticky=W, pady=2)
Button(master, text='Exit', command=master.quit).grid(row=100, column=0, sticky=W, pady=2)
status = Label(master, text="ERROR404", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=10, columnspan=1)
new = progress(master)
mainloop( )


