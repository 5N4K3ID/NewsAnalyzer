#BAGIAN CLEANING KETIKA MEMBUKA URL

import socket
import webbrowser
import urllib.request
import re
import string
import subprocess as sp
from bs4 import BeautifulSoup
from collections import Counter
from nltk.tokenize import word_tokenize
from googlesearch import search
from time import sleep
from urllib.parse import urlparse
from clear_screen import clear

print("                                                          ")
print("                                                          ") 
print("                             @@@@@@@@@@@@                  ")
print("                          @@@@@@@@@@@@@@@@@                ")
print("                       @@@@@@@@@@@@@@@@@@@@@@              ")
print("       %@            @@@@@@@@@@@@@@@@@@@@@@@@@             ")
print("       @@@         @@@@@@@@@ %@@@@@@@@@@@@@@@@             ")
print("      @  @        @@@@@@@           @@@@@@@@@@@            ")
print("     @   %@@@@@@#@@@@@@#              @@@@@@@@@@&          ")
print("    @@@@@@@@@@@@@@@@@@        @@@@      @@@@@@@@ @@@@@@    ")
print("    @@@@@@@@@@#@@@@@@@      @@   @*      @ @@@@@      @@   ")
print("    @@@@ @@@@ @@@@@@@@    @@       @@      @@@@@        @  ")
print("   @@@@       @@@@@@@@@  @           @@    @@@@@   ,@    @ ")
print("   @@@        @@@@@@@@ &@             @@   @@@@@    @    @ ")
print("   @   @   @@ @@@@@@@ @     RAMADHAN  (@   @@@@     @&@    ")
print("     &@        @@@@@@@      IBRAHIM   #@  @@@@ @@   @@@   @")
print("  #@@           @@@@@@                %&  @@@@ @@   @@@   @")
print(" @@            @ @@@@@                 @&  @@@@    @@@@@ @@")
print("          @@@  @@,@@@@                   @@&@@@  &@@@@@@@@ ")
print("           @@@@@@@@@@@@ @@            &@@@ @@@@@@@@@@@@@@  ")
print("            @@@@@@ @@@@@@@        @@  @@@@@@@@@@@@@@@@@@   ")
print("             @@ @@  @@@@@@         @@@@@@@@@@@@@@@@@@@     ")
print("              @&    @@@@@@@    @@@@@@@@@@@@@@@@@@@@        ")
print("               @     @  @@@    @   @@   @@@@               ")
print("               @@        @@@      @@   @@@@ @              ")
print("                @         @@     @@   @@@@@@               ")
print("                          @@@   @     @ @@@                ")
print("                           @@          @@                  ")
print("                            @         @@                   ")
print("                             @       @                     ")
print(" ")
print("tools pantau berita internet ...")

#######
def readwords( filename ):
    f = open(filename)
    words = [ line.rstrip() for line in f.readlines()]
    return words

def bukaURL():
    #print ("membuka link URL\n.\n.\n.")
    response = urllib.request.urlopen(Link) 
    html = response.read()
    soup = BeautifulSoup(html,"html5lib")
    text = soup.get_text(strip=True)
    return text

def BersihkanCrawl():
    text=bukaURL()
    #print ("melakukan crawaling dan cleaning\n.\n.\n.")
    EnterHilang = re.sub('\n', ' ', text)
    SpasiHilang = re.sub(' +', ' ', EnterHilang)
    SpasiHilang2 = re.sub(' +', ' ', SpasiHilang)
    #print ("ini belom di tokenizing")
    #print (text)
    return SpasiHilang2

##def Token():
##    print ("melakukan tokenizing\n.\n.\n.")
##    response = urllib.request.urlopen('https://news.detik.com/berita/d-4562714/pemkot-semarang-gelar-bazar-1000-paket-sembako-murah?_ga=2.25225597.1129279498.1558424589-344740636.1557881228') 
##    html = response.read() 
##    soup = BeautifulSoup(html,"html5lib") 
##    text = soup.get_text(strip=True) 
##    tokens = [t for t in text.split()]
##    #print ("ini jika di tokenizing")
##    #print (tokens)
##    return tokens

def FilterList():
    SpasiHilang2=BersihkanCrawl()
    #tokens=Token()
    #print ("menghitung jumlah kata negatif dan positif\n.\n.\n.")
    positive = readwords('positive.txt')
    negative = readwords('negative.txt')
    paragraph = str(SpasiHilang2)
    token = word_tokenize(paragraph)
    token = [w.lower() for w in token]
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in token]
    words = [word for word in stripped if word.isalpha()]
    kata = str(words)
    detoken = re.sub("', '", ' ', kata)
    count = Counter(detoken.split())
    #print ("---> membaca list kalimat positif dan negatif\n.\n.\n.")
    pos = 0
    neg = 0
    for key, val in count.items():
        key = key.rstrip('.,?!\n') # removing possible punctuation signs
        if key in positive:
            pos += val
            f4= open("listpositif","a+")
            f4.write(str(key)+","+str(val)+"\r")
            f4.close()
        if key in negative:
            neg += val
            f5= open("listnegatif","a+")
            f5.write(str(key)+","+str(val)+"\r")
            f5.close()
    a=str(pos)
    b=str(neg)
    f2= open("positif","a+")
    f2.write(a+"\r")
    f2.close()
    f3= open("negatif","a+")
    f3.write(b+"\r")
    f3.close()
    hasil1 = ("jumlah positif     : "+a)
    hasil2 = ("cenderung negatif  : "+b)
    return (a, b)

def run():
    bukaURL()
    a,b=FilterList()
    print("jumlah positif  : "+a)
    print("jumlah negatif  : "+b+"\n\n\n")


#Link=str("https://news.detik.com/berita/d-4562714/pemkot-semarang-gelar-bazar-1000-paket-sembako-murah?_ga=2.25225597.1129279498.1558424589-344740636.1557881228")

open('positif', 'w').close()
open('negatif', 'w').close()
open('listpositif', 'w').close()
open('listnegatif', 'w').close()

media = input("\nmasukkan situs berita           : ")
isu   = input("masukkan isu yang dicari        : ")
jumlah= input("jumlah link yang akan di crawl  : ")
jumlah= int(jumlah)
clear()

f= open("list.txt","w+")
print("\n=================== LIST LINK =====================")
for url in search(media+" "+isu, stop=jumlah, pause=10):
    f.write(url+"\n")
    print(url)
f.close()
print("=================== LIST LINK =====================\n")

testsite_array = []
with open('list.txt') as my_file:
    for Link in my_file:
        testsite_array.append(Link)
        Link=str(Link)#print(str(line))
        print("\n========================================================================")
        print(" link target |")
        print("-------------|\n")
        print(Link)
        run()
        data = urlparse(Link)
        domain = str(data.netloc)
        IPAddr = socket.gethostbyname(domain)
        print("domain     : "+domain)
        print("ip address : "+IPAddr)
        print("========================================================================")
        sleep(10)

sleep(10)
print("============================")
print("    MEMBUKA WEBSITE LIST    ")
print("============================")
f3 = open("list.txt", "r")
for x in f3:
  #print(x)
  webbrowser.open(x)
f3.close()


