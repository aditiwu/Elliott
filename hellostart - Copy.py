import datetime
import math
import time
import speech_recognition as sr
import os
import wikipedia
import periodictable as pt
import logging
from PyDictionary import PyDictionary
import os
import serial
import glob
import requests
import random
import time
import ai
from mutagen.mp3 import MP3
import re
import urllib.request
from urllib.request import Request, urlopen
import webbrowser
from bs4 import BeautifulSoup
from gtts import gTTS
import requests, json 
def listen1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("ELLIOT: Say something!")
        #ser.write("ELLIOT: Say something!")
        audio = r.listen(source)

    inpt = ''


    #------------------------------------------------------------------RECOGNIZES THE VOICE--------------------------------------------------------------------------------
    '''xyz = 1
    while True:
        try:
            print("YOU: " + r.recognize_google(audio))
            #ser.write("YOU: " + r.recognize_google(audio))
            inpt = r.recognize_google(audio)
            break
        except sr.UnknownValueError:
            print("NOT UNDERSTANDING")
            pass
        except sr.RequestError as e:
            print("NO WIFI")
            pass'''
    inpt = input("Enter Command: ")
    return inpt
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("ELLIOT: Say something!")
        #ser.write("ELLIOT: Say something!")
        audio = r.listen(source)

    inpt = ''

    #------------------------------------------------------------------RECOGNIZES THE VOICE--------------------------------------------------------------------------------
    '''try:
        print("YOU: " + r.recognize_google(audio))
        #ser.write("YOU: " + r.recognize_google(audio))
        inpt = r.recognize_google(audio)
    except sr.UnknownValueError:
        ai.command("say Google Speech Recognition does not print gibberish")
        inpt = input("Enter Command: ")
    except sr.RequestError as e:
        ai.command("say Your WiFi is down bro, everyone has a weakness, this is mine, get it back, I am good for nothing without the WiFi. I can't understand anything you say bro, save me; {0}".format(e))
        inpt = input("Enter Command: ")'''
    inpt = input("Enter Command: ")
    return inpt





#-------------------------------------------------------------------------EVENTS--------------------------------------------------------------------------------------------------

daten = datetime.date.today().month
dater = datetime.date.today().day
year = datetime.date.today().year
print(year)
print(dater)
print(daten)
c = str(dater)+"-"+str(daten)+"-"+str(year)
d = str(c)
e = d+".txt"
f = str(e)
if os.path.exists(f) == True:
    g = open(f, "r")
    ai.command("say "+g.read())
    ai.command("say "+g.read())
    randomassvar = 1        
else:
    ai.command("say No events today, get yourself a brain, start studying for exams, um watch Chhota Bheem or something, read a book")
    randomassvar = 1

#-------------------------------------------------------------------------TOMORROW EVENTS--------------------------------------------------------------------------------------------------


dater = datetime.date.today().day
daten = datetime.date.today().month
if daten==1 or daten==3 or daten==5 or daten==7 or daten==8 or daten==10 or daten==12:
    if dater == 31:
        month = daten+1
        day = 1
    else:
        month = daten
        day = dater+1
elif daten==4 or daten==6 or daten==9 or daten==11:
    if dater == 30:
        month = daten+1
        day = 1
    else:
        month = daten
        day = dater+1
elif daten==2:
    if dater == 28 and year%4!=0:
        month = daten+1
        day = 1
    elif dater == 29 and year%4==0:
        month = daten+1
        day = 1
    else:
        month = daten
        day = dater+1
year = datetime.date.today().year
c = str(day)+"-"+str(month)+"-"+str(year)
print("ELLIOT: Enter tomorrow's events")
text = listen()
d = str(c)
e = d+".txt"
f = str(e)
text1 = ""+text
text2 = ". "+text
if os.path.exists(f) == True:
    with open(f,'a') as g:
        g.write(text2)
else:
     with open(f,'a') as g:
        g.write(text1)

#-------------------------------------------------------------------------QUOTE--------------------------------------------------------------------------------------------------


html = urllib.request.urlopen('http://www.eduro.com/')
soup = BeautifulSoup(html)
data = soup.findAll(text=True)
 
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True
 
result = filter(visible, data)
x = list(result)
a = 47
ai.command("say "+x[a])

#-------------------------------------------------------------------------NEWS--------------------------------------------------------------------------------------------------


print("ELLIOT: Say yes or no for news")
x = listen()
if "no" not in x:
    logging.basicConfig(level=logging.WARNING)
    req = Request('https://www.inshorts.com/en/read', headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html)
    data = soup.findAll(text=True)
     
    def visible(element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        elif re.match('<!--.*-->', str(element.encode('utf-8'))):
            return False
        return True
     
    result = filter(visible, data)
    x = list(result)
    x = [w.replace('\n', '') for w in x]
    x = [w.replace('\t', '') for w in x]
    x = [w.replace("'", '') for w in x]
    x = [w.replace('\xa0', '') for w in x]
    x = [w.replace('xa0of', '') for w in x]
    y = len(x)
    y = len(x)
    a = 0
    while a<y:
        if 'For the best experience use' in x[a]:
            break
        else:
            a+=1
    b=y-1
    while b<y:
        if 'For the best experience use' in x[b]:
            break
        else:
            b-=1
    j = x[a:y]
    i = ' '.join(str(e) for e in j)
    l = '\n'.join(str(e) for e in j)
    ai.speaklong(i,l)

#-------------------------------------------------------------------------GOALS TO DO--------------------------------------------------------------------------------------------------


with open('goals'+'.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
list23 = content
ai.speak("Here's the goal that is still ought to be complete: "+str(list23[0]))

#-------------------------------------------------------------------------GOALS TOMORROW--------------------------------------------------------------------------------------------------

print("ELLIOT: Enter tomorrow's goal")
raw = listen()
list23 = [w.replace(list23[0], raw) for w in list23]
f = open('goals'+".txt", "w")
for i in list23:
    f.write(str(i)+'\n')
f.close()

#-------------------------------------------------------------------------TIME TABLE FOR TODAY--------------------------------------------------------------------------------------------------


with open('today'+'.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]        
list23 = ' '.join(str(e) for e in content)
ai.speak("Here's the goal that is still ought to be complete: "+list23)

#-------------------------------------------------------------------------TIME TABLE FOR TOMORROW--------------------------------------------------------------------------------------------------

print("ELLIOT: Enter tomorrow's time table")
xq=[]
while True:
    raw = listen()
    if "quit" in raw:
        break
    else:
        ra = raw.split(" ")
        hours = ra[1]
        minutes = ra[4]
        statement = ra[6:]
        sta = ' '.join(str(e) for e in statement)
        time = str(hours) + ":" + str(minutes)
        xq.append(time)
        xq.append(sta)
list23 = xq
open('toady.txt', 'w').close()
f = open('today'+".txt", "w")
for i in list23:
    f.write(str(i)+'\n')
f.close()

#-------------------------------------------------------------------------WHEN TO WAKE UP--------------------------------------------------------------------------------------------------

x = input("Enter the time when I should wake you up tomorrow(format- h:m): ")
lines = open("timea.txt", 'r').readlines()
lines[0] = str(x)
out = open("timea.txt", 'w')
out.writelines(lines)
out.close()

#-------------------------------------------------------------------------HOW WAS YOUR DAY--------------------------------------------------------------------------------------------------
print("How was your day")
inpr = listen()
if "bad" in inpr:
    inp = listen("Why, what happened?")
    ai.command("how to cope with "+inp)
else:
    ai.command("say Very well then")

os.system("hello_time.pyw")
