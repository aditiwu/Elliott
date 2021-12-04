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
from mutagen.mp3 import MP3
import re
import urllib.request
from urllib.request import Request, urlopen
import webbrowser
from bs4 import BeautifulSoup
from gtts import gTTS
import requests, json 
playlist = 1
my_dict = {}
dictionary=PyDictionary()
logging.basicConfig(level=logging.WARNING)
city_name = "Hyderabad"
complete_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=8622f029b388f41146c107000eef4fb2".format(city_name)

response = requests.get(complete_url) 
x = response.json()
y = x["main"]
a = x["wind"]
b = x["sys"]
z = x["weather"]
sunrise1 = b["sunrise"]
sunset1 = b["sunset"]


sunrise = str(datetime.datetime.fromtimestamp(sunrise1))[11:16] + " hours"
sunset = str(datetime.datetime.fromtimestamp(sunset1))[11:16] + " hours"
temperature = str(int(y["temp"])-273 )
pressure = str(y["pressure"]) 
humidity = str(y["humidity"])
description = str(z[0]["description"])
speed = str(a["speed"])
total_summary_of_weather = "It is " + description + " with a temperature of " + temperature + " degrees celcius and humidity of " + humidity + " percent. The current pressure is " + pressure + " millibars. Sunrise at " + sunrise + " and sunset at " + sunset + "."

cursewords = "idiot mad dumb ass bitch fuck"
goodwords = 'nice work thank you good job'
negativewords = 'it sucked bad day worst day'
mathm = 38
hindim = 42
socialm = 59
sciencem = 52
englishm = 54
year = time.localtime(time.time()).tm_year
month = time.localtime(time.time()).tm_mon
day = time.localtime(time.time()).tm_mday
hour = time.localtime(time.time()).tm_hour
minute = time.localtime(time.time()).tm_min
seconds = time.localtime(time.time()).tm_sec
weekday = time.localtime(time.time()).tm_wday
yday = time.localtime(time.time()).tm_yday
what_is_the_time = ['Time for you to get a new watch', 'Wait a sec, do you get it?', 'Here you go']
set_an_alarm_for = ['Alarms are for people with goals', 'Here you go', 'On it']
set_a_timer_for = ["Starting timer for the idiot", "Tic-Toc", "Started the timer"]
news = ["Well, accoring to my reports, there has been a brainless person trying to act cool. He is known for his idiocracy", "Ha Ha, look who is trying to act like a gentleman", "Sir, I wonder, what can you achieve by reading the news?", "Coming from a person who never reads paper"]
set_a_reminder_on = ["Okay reminder set with message: buy yours...jk. On it.", "Done", "Yes Sir, working on it, and now, its done. See, I'm so fast"]
search_Wikipedia_articles_on = ["Showing results: for coping with dumbness", "On it", "Wait a sec", "You seriously call this your best command"]
what_is_the_meaning_of = ["Buy yourself a dictionary man", "Why are you so lazy?", "Wait a sec", "On it"]
'''
try:
  ser = serial.Serial("COM6", 9600,)
  if (ser.isOpen()):
      dfghjk = ''

except IOError:
    speak1("Touchscreen not connected")
    os.system("hello_no_port.pyw")
#ser.wrtie("HELLO".encode())
'''
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r', encoding="utf8").readlines()
    lines[line_num] = text
    out = open(file_name, 'w', encoding="utf8")
    out.writelines(lines)
    out.close()

def read_line(filen, line):
    with open(filen) as asdfg:
        qwerty = asdfg.readlines()
    readline = (qwerty[line])
    return readline


def TextList(filename):
    with open(filename+'.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    list23 = content
    return list23
def AppendTextList(filename, append):
    with open(filename+'.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    f.close()
    list23 = content
    list23.append(append)
    f = open(filename+".txt", "w")
    for i in list23:
        f.write(str(i)+'\n')
    f.close()
def CreateVariable(name, value):
    my_dict[name] = value
    return (my_dict[name])

def splitting(name, string):
    splitvar = my_dict[name].split(string)
    return splitvar

def ReplaceTextList(filename, old, new):
    with open(filename+'.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    f.close()
    list23 = content
    list23 = [w.replace(old, new) for w in list23]
    f = open(filename+".txt", "w")
    for i in list23:
        f.write(str(i)+'\n')
    f.close()
def AddTextList(filename, old, new):
    with open(filename+'.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    f.close()
    list23 = content
    list23.insert(old, new)
    f = open(filename+".txt", "w")
    for i in list23:
        f.write(str(i)+'\n')
    f.close()
def speaklong(au, ps):
    print("ELLIOT: "+ps)
    au = [w.replace('\n', '') for w in au]
    au = [w.replace('\t', '') for w in au]
    au = [w.replace("'", '') for w in au]
    au = [w.replace('"', '') for w in au]
    au = [w.replace('\xa0', '') for w in au]
    au = [w.replace('xa0of', '') for w in au]
    au = [w.replace('\u018e', '') for w in au]
    au = [w.replace('\u200e', '') for w in au]
    au = [w.replace('\u0107', '') for w in au]
    au = [w.replace('\u02c8', '') for w in au]
    j = ' '.join(str(e) for e in au)
    j.encode('UTF-8',errors='ignore')
    speak1(str(j))


def speak(audioString):
    text = 'Sapi.Speak "'+str(audioString)+'"'
    print("ELLIOT: "+audioString)
    x = "ELLIOT: "+audioString
    #ser.wrtie(x.encode())
    replace_line('speak.vbs', 1, text)
    os.system("speak.vbs")
def speak1(audioString):
    text = 'Sapi.Speak "'+str(audioString)+'"'
    x = "ELLIOT: "+audioString
    #ser.wrtie(x.encode())
    replace_line('speak.vbs', 1, text)
    os.system("speak.vbs")

def rules(ruleline):
    ruleline = ruleline.split("/")
    x = len(ruleline)
    a = 0
    while a<x:
        qwerty = str(ruleline[a])
        qwerty = qwerty.split("|")
        b = 1
        if eval(qwerty[0]):
            while b<len(qwerty):
                if "splitting" in qwerty[b]:
                    xyzcv = eval(qwerty[b])
                    b+=1
                else:
                    eval(qwerty[b])
                    b+=1
        else:
            speak("Not True")
        a+=1
def rules1(ruleline):

    qwerty = ruleline
    qwerty = qwerty.split("|")
    b = 0
    while b<len(qwerty):
        if "split" in qwerty[b]:
            xyzcv = eval(qwerty[b])
            b+=1
        else:
            eval(qwerty[b])
            b+=1
def openApp(app):
    os.system(app)

def RandomObjects(objects, times):
    objec = objects.split(" ")
    a = 1
    while a<times:
        print(random.choice(objec))
        a+=1
def RandomList(objects, times):
    a = 1
    while a<times:
        print(random.choice(objects))
        a+=1
def Calculate(name):
    with open('formula.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    list23 = content
    a = 0
    while a<len(list23):
        if name in list23[a]:
            x = str(list23[a])
            break
        else:
            a+=1
    x = x.split(name+": ")
    formula = x[1]
    speak("The formula is: "+formula)
    raw = input("Enter the characters of the formula: ")
    raw = raw.split(", ")
    b = 0
    while b<len(raw):
        formula = formula.replace("n"+str(b+1), raw[b])
        b+=1
    y = eval(formula)
    speak(str(y))

def Calculate1(text1, text2):
    with open('formula.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    list23 = content
    inpat = inpt.split(" ")
    if text1<text2:
        name = str(inpat[text1:text2])
    else:
        name = str(inpat[text1:])
    print (list23)
    a = 0
    while a<len(list23):
        if name in list23[a]:
            x = str(list23[a])
            break
        else:
            a+=1
    x = x.split(name+": ")
    formula = x[1]
    speak("The formula is: "+formula)
    raw = input("Enter the characters of the formula: ")
    raw = raw.split(", ")
    b = 0
    while b<len(raw):
        formula = formula.replace("n"+str(b+1), raw[b])
        b+=1
    y = eval(formula)
    speak(str(y))
def command1(inpt):
    x = inpt.split(' ')
    list3 = []
    f = open('wordtest'+".txt", "w")
    for i in list3:
        f.write(str(i)+' ')
    f.close()
    for l in x:
        if len(l)>3:
            w = inpt.replace(' ', '+')
            req = Request('https://www.google.co.in/search?q=what+part+of+speech+is+'+l+'+macmillan', headers={'User-Agent': 'Mozilla/5.0'})
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
            a = 0
            list69=[]
            b = 0
            while b<y:
                if l in x[b]:
                    break
                else:
                    b+=1
            if b > y-100:
                with open('wordtest'+'.txt') as f:
                    content = f.readlines()
                content = [x.strip() for x in content]
                list23 = content
                list23.append(l)
                f = open('wordtest'+".txt", "w")
                for i in list23:
                    f.write(str(i)+' ')
                f.close()
                with open('wordnoun'+'.txt') as f:
                    content = f.readlines()
                content = [x.strip() for x in content]
                list23 = content
                g = len(list23)
                h = 0
                while h<g:
                    if l in list23[h]:
                        list23[h+1]+=' '+inpt
                        break
                    else:
                        h+=2
                if h==g:
                    list23.append(l)
                    list23.append(inpt)
                else:
                    print("")
                f = open('wordnoun'+".txt", "w")
                for i in list23:
                    f.write(str(i)+'\n')
                f.close()
                break
            else:
                a=b+1
                while a>b and a<b+8:
                    if 'noun' in x[a]:
                        with open('wordtest'+'.txt') as f:
                            content = f.readlines()
                        content = [x.strip() for x in content]
                        list23 = content
                        list23.append(l)
                        f = open('wordtest'+".txt", "w")
                        for i in list23:
                            f.write(str(i)+' ')
                        f.close()
                        with open('wordnoun'+'.txt') as f:
                            content = f.readlines()
                        content = [x.strip() for x in content]
                        list23 = content
                        g = len(list23)
                        h=0
                        while h<g:
                            if l in list23[h]:
                                list23[h]+=inpt
                                break
                            else:
                                h+=2
                        if h==g:
                            list23.append(l)
                            list23.append(inpt)
                        else:
                            print("")
                        f = open('wordnoun'+".txt", "w")
                        for i in list23:
                            f.write(str(i)+'\n')
                        f.close()
                        break
                    else:
                        a+=1
                c = b+1
                while c>b and c<b+5:
                    if 'adjective' in x[c]:
                        with open('wordtest'+'.txt') as f:
                            content = f.readlines()
                        content = [x.strip() for x in content]
                        list23 = content
                        list23.append(l)
                        f = open('wordtest'+".txt", "w")
                        for i in list23:
                            f.write(str(i)+' ')
                        f.close()
                        break
                    else:
                        c+=1
    with open("wordtest.txt") as asdfg:
        qwerty = asdfg.readlines()
    try:
        readline = (qwerty[0])
        a=readline
        a=' '.join(unique_list(a.split()))
        f = open('wordtest'+".txt", "w")
        f.write(str(a))
        f.close()
    except IndexError:
        x = 1
    with open("wordtest.txt") as asdfg:
        qwerty = asdfg.readlines()
    try:
        readline = (qwerty[0])
        with open('wordsent'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        list23.append(inpt)
        list23.append(readline)
        f = open('wordsent'+".txt", "w")
        for i in list23:
            f.write(str(i)+'\n')
        f.close()
    except IndexError:
        x = 1
    my_dict['inpt'] = inpt
    h = inpt.split(" ")
    x = h[3:]
    j = ' '.join(str(e) for e in x)


def command(inpt):
    my_dict['inpt'] = inpt
    h = inpt.split(" ")
    x = h[3:]
    j = ' '.join(str(e) for e in x)
    
    #-----------------------------------------------------------------COMMAND---------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------COMMAND---------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------COMMAND---------------------------------------------------------------------------------------------
    if "when I say" in inpt or "when i say" in inpt:
        inpt1=inpt.split("you")
        y = inpt1[0]
        y1 = y.split("say")
        y1 = y1[1]
        y2=inpt1[1]
        with open('command'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        list23.append(y1)
        list23.append(y2)
        f = open('command'+".txt", "w")
        for i in list23:
            f.write(str(i)+'\n')
        f.close()
    elif "it is another command" in inpt:
        speak("You lazy loser, can't you make this code easier??!!")
        inpt = inpt.split(" ")
        int1 = input("Type the command: ")
        eval(article)
    elif "lights on" in inpt:
        speak("You lazy loser, can't switch on lights??!!")
        #ser.wrtie('lightson'.encode())
    elif "lights of" in inpt:
        speak("You lazy loser, can't switch off lights??!!")
        #ser.wrtie('lightsoff'.encode())
    elif "where is" in inpt:
        inpt = inpt.split(" ")
        inp1 = inpt[2:]
        x = '+'.join(str(e) for e in inp1)
        webbrowser.open("https://www.google.com/maps?q="+x)
    elif "show images of" in inpt:
        inpt = inpt.split(" ")
        inp1 = inpt[3:]
        x = '+'.join(str(e) for e in inp1)
        webbrowser.open("https://www.google.com/search?tbm=isch&source=hp&biw=1366&bih=700&ei=Ln_xWtb1FMGMvQTgqJbwDA&q="+x)
    elif "choose between" in inpt:
        inpt = inpt.split(" ")
        inp1 = inpt[2:]
        speak(random.choice(inp1))
    elif "toss" in inpt or "flip a coin" in inpt:
        inpt = inpt.split(" ")
        inp1 = inpt[2:]
        speak("Coin Flipped, and it is: ")
        speak(random.choice(['Heads', 'Tails']))
    elif "bluetooth" in inpt:
        speak("Write your command in here")
        hell =r'''C:\Users\Repnovation\Downloads\Computer-to-Arduino-Bluetooth-master\Computer-to-Arduino-Bluetooth-master\LightGUI.py'''
        os.system(hell)
    elif "move the car up by" in inpt:
        inpt = inpt.split(" ")
        x = inpt[5]
        lines = open("value.txt", 'r').readlines()
        lines[0] = str(x)
        out = open("value.txt", 'w')
        out.writelines(lines)
        out.close()
        os.system("Up.py")
    elif "move the car down by" in inpt:
        inpt = inpt.split(" ")
        x = inpt[5]
        lines = open("value.txt", 'r').readlines()
        lines[0] = str(x)
        out = open("value.txt", 'w')
        out.writelines(lines)
        out.close()
        os.system("Down.py")
    elif "move the car right by" in inpt:
        inpt = inpt.split(" ")
        x = inpt[5]
        lines = open("value.txt", 'r').readlines()
        lines[0] = str(x)
        out = open("value.txt", 'w')
        out.writelines(lines)
        out.close()
        os.system("Right.py")
    elif "move the car left by" in inpt:
        inpt = inpt.split(" ")
        x = inpt[5]
        lines = open("value.txt", 'r').readlines()
        lines[0] = str(x)
        out = open("value.txt", 'w')
        out.writelines(lines)
        out.close()
        os.system("Left.py")
    elif "system report" in inpt:
        os.system('sysreport.vbs')
    elif "increase volume" in inpt:
        os.system('volup5.exe')
    elif "decrease volume" in inpt:
        os.system("voldown.exe")
    elif "set volume to" in inpt:
        inpt = inpt.split(' ')
        x = inpt[3]
        x = int(x)*10
        os.system("vol"+str(x)+".exe")
    elif "set brightness to" in inpt:
        inpt = inpt.split(' ')
        x = inpt[3]
        x = int(x)*10
        os.system("brightness"+str(x)+".exe")
    #-----------------------------------------------------------------WEATHER---------------------------------------------------------------------------------------------
    elif "weather in" in inpt:
        city_name = inpt.split(" ")[2]
        complete_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=8622f029b388f41146c107000eef4fb2".format(city_name)

        response = requests.get(complete_url) 
        x = response.json()
        y = x["main"]
        a = x["wind"]
        b = x["sys"]
        z = x["weather"]
        sunrise1 = b["sunrise"]
        sunset1 = b["sunset"]


        sunrise = str(datetime.datetime.fromtimestamp(sunrise1))[11:16] + " hours"
        sunset = str(datetime.datetime.fromtimestamp(sunset1))[11:16] + " hours"
        temperature = str(int(y["temp"])-273 )
        pressure = str(y["pressure"]) 
        humidity = str(y["humidity"])
        description = str(z[0]["description"])
        speed = str(a["speed"])
        speak( "It is " + description + " with a temperature of " + temperature + " degrees celcius and humidity of " + humidity + " percent. The current pressure is " + pressure + " millibars. Sunrise at " + sunrise + " and sunset at " + sunset + ".")
    elif "weather" in inpt:
        speak(total_summary_of_weather)
        time.sleep(30)
    elif "temperature" in inpt:
        speak(temperature + "degrees celcius")
        time.sleep(5)
    elif "wind speed" in inpt:
        speak(speed)
        time.sleep(5)
    elif "pressure" in inpt:
        speak(pressure)
        time.sleep(5)
    elif "when is sunrise" in inpt:
        speak(sunrise)
        time.sleep(5)
    elif "when is sunset" in inpt:
        speak(sunset)
        time.sleep(5)
    elif "humidity" in inpt:
        speak(humidity)
        time.sleep(30)

    #--------------------------------------------------------------------MUSIC--------------------------------------------------------------------------------------------
    elif "play suggested music" in inpt:
        with open('music'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        list1=list23[0]
        x1=list1.split("|")
        x=x1[random.randint(0, len(x1)-1)]
        inpt = x.split(" ")
        x1 = '+'.join(str(e) for e in inpt)
        req = Request('https://www.google.co.in/search?q=similar+artists+like+'+x1+'+allmusic', headers={'User-Agent': 'Mozilla/5.0'})
        req = Request('https://www.google.co.in/search?q=similar+artists+like+nicki+minaj+allmusic', headers={'User-Agent': 'Mozilla/5.0'})
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
        
        
        b = 0
        while b<y:
            if 'Similar To' in x[b]:
                break
            else:
                b+=1
        c=b
        while c<y:
            if '...' in x[c]:
                break
            else:
                c+=1
        a = b+2
        while a<y:
            if '|' in x[a]:
                break
            else:
                a+=1
        k=0
        if a>=c:
            k=c
        else:
            k=a
        j=x[b+1:k]
        l=[]
        a=0
        while a<len(j):
            if len(j[a])>4:
                l.append(j[a])
                a+=1
            else:
                a+=1
        x=l
        i=random.choice(x)
        if '.' in i:
            i=i.split(".")
            o=[]
            a=0
            while a<len(i):
                if len(i[a])>4:
                    o.append(i[a])
                    a+=1
                else:
                    a+=1
            x=random.choice(o)
            print(x)
            k = "songs by"+x
        else:
            print(i)
            k = "songs by"+i


        scrape_url="https://www.youtube.com"
        search_url="/results?search_query="

        search_hardcode = k.replace(" ","+")
        mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}


        list1 = []
        a=0
        def bstheurl(sb_url):
                sb_get = requests.get(sb_url, headers = mozhdr)
                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                a=0
                for x in yt_links:
                    yt_href =  x.get("href")
                    yt_title = x.get("title")
                    yt_final = scrape_url + yt_href
                    if "list" in yt_final:
                        list1.append(str(a)+". "+yt_title)
                        list1.append("    "+yt_final)
                        a+=1



        sb_url = scrape_url + search_url + search_hardcode
        bstheurl(sb_url)
        #print ('\n'.join(str(e) for e in list1))
        x = list1[0*2+1]
        x = x.replace('    ', '')
        os.system("starting.vbs")
        webbrowser.open(x)
        os.system("ending.vbs")
    elif "play suggested movie" in inpt:
        with open('movie'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content

        x=list23[random.randint(0,len(list23)-1)]
        inpt = x.split(" ")
        x1 = '+'.join(str(e) for e in inpt)
        req = Request('https://www.google.co.in/search?q=movies+like+'+x1, headers={'User-Agent': 'Mozilla/5.0'})
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
        b = 0
        while b<y:
            if 'People also search for' in x[b]:
                break
            else:
                b+=1
        d = random.choice(['1','3','5','7','9','11'])
        k = x[b+int(d)]
        req = Request("http://www.google.co.in/search?q="+k+"+yesmovies.io", headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        while a<y:
            if 'http' in x[a]:
                break
            else:
                a+=1
        b=0
        while b<y:
            if '\u200e' in x[b]:
                k = x[a:b]
                j = ''.join(str(e) for e in k)
                if "watching" in j:
                    os.system("starting.vbs")
                    webbrowser.open(j)
                else:
                    z = (j+'/watching.html')
                    os.system("starting.vbs")
                    webbrowser.open(z)
                break
            else:
                b+=1
    elif "play movie" in inpt:
        inpt = inpt.split(" ")
        w = inpt[1:len(inpt)]
        x = '+'.join(str(e) for e in w)
        x1 = ' '.join(str(e) for e in w)
        with open('movie'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        list23.append(x1)
        f = open('movie'+".txt", "w")
        for i in list23:
            f.write(str(i)+'\n')
        f.close()
        req = Request("http://www.google.co.in/search?q="+x+"+yesmovies.io", headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        while a<y:
            if 'http' in x[a]:
                break
            else:
                a+=1
        b=0
        while b<y:
            if '\u200e' in x[b]:
                k = x[a:b]
                j = ''.join(str(e) for e in k)
                if "watching" in j:
                    os.system("starting.vbs")
                    webbrowser.open(j)
                else:
                    z = (j+'/watching.html')
                    os.system("starting.vbs")
                    webbrowser.open(z)
                break
            else:
                b+=1

    elif "tell a joke" in inpt or "tell me a joke" in inpt:
        x = random.randint(1, 6)
        lis = ["http://www.funnyshortjokes.com/c/racist-jokes/page/", "http://www.funnyshortjokes.com/best-short-jokes/page/", "http://www.funnyshortjokes.com/c/yo-mama-jokes/page/"]
        li = random.choice(lis)
        u = li+str(x)
        req = Request(u, headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        while a<y:
            if 'SUBMIT A JOKE' in x[a]:
                break
            else:
                a+=1
        b=0
        while b<y:
            if 'Previous' in x[b] or 'Next' in x[b]:
                break
            else:
                b+=1

        k = x[a+5:b]
        l = len(k)
        a=0
        list1 = []
        while a<l:
            if k[a]=='in ':
                list1.append(str(a))
                a+=1
            else:
                a+=1
        g = 0
        v = len(list1)
        list2 = []
        d=0
        while g<v-1:
            x = int(list1[g])
            y = int(list1[g+1])
            b = k[x+2:y-4]
            if len(b)<350:
                list2.append(' '.join(str(e) for e in b))
            g+=1
            x = d
        list2.append(' '.join(str(e) for e in k[d+2:]))
        o = random.choice(list2)
        speak(o)
    elif "just play" in inpt:

        scrape_url="https://www.youtube.com"
        search_url="/results?search_query="
        inpt = inpt.split(' ')
        w = inpt[2:len(inpt)]
        inpt = ' '.join(str(e) for e in w)
        x1 = ' '.join(str(e) for e in w)
        with open('music'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        list23.append(x1)
        f = open('music'+".txt", "w")
        for i in list23:
            f.write(str(i)+'\n')
        f.close()
        search_hardcode = inpt.replace(" ","+")
        mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}


        list1 = []
        a=0
        def bstheurl(sb_url):
                sb_get = requests.get(sb_url, headers = mozhdr)
                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                a=0
                for x in yt_links:
                    yt_href =  x.get("href")
                    yt_title = x.get("title")
                    yt_final = scrape_url + yt_href
                    list1.append(str(a)+". "+yt_title)
                    list1.append("    "+yt_final)
                    a+=1



        sb_url = scrape_url + search_url + search_hardcode
        print(sb_url)
        bstheurl(sb_url)
        #print ('\n'.join(str(e) for e in list1))
        x = list1[1*2+1]
        x = x.replace('    ', '')
        os.system("starting.vbs")
        webbrowser.open(x)
        os.system("ending.vbs")
    elif "play" in inpt:
        x = inpt.split(' ')
        inpt = x[1:len(x)]
        w = ' '.join(str(e) for e in inpt)
        with open('music'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        w1=''
        if "songs by" in w or "song by" in w:
            w1 = w.replace('songs by ','')
            #set url to be scraped
            scrape_url="https://www.youtube.com"
            search_url="/results?search_query="

            search_hardcode = w.replace(" ","+")
            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}


            list1 = []
            a=0
            def bstheurl(sb_url):
                    sb_get = requests.get(sb_url, headers = mozhdr)
                    soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                    yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                    a=0
                    for x in yt_links:
                        yt_href =  x.get("href")
                        yt_title = x.get("title")
                        yt_final = scrape_url + yt_href
                        if "list" in yt_final:
                            list1.append(str(a)+". "+yt_title)
                            list1.append("    "+yt_final)
                            a+=1



            sb_url = scrape_url + search_url + search_hardcode
            bstheurl(sb_url)
            #print ('\n'.join(str(e) for e in list1))
            x = list1[0*2+1]
            x = x.replace('    ', '')
            os.system("starting.vbs")
            webbrowser.open(x)
            os.system("ending.vbs")

        else:
            w1=w
            scrape_url="https://www.youtube.com"
            search_url="/results?search_query="
            search_hardcode = w.replace(" ","+")
            
            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
            list1 = []
            a=0
            def bstheurl(sb_url):
                    sb_get = requests.get(sb_url, headers = mozhdr)
                    soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                    yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                    a=0
                    for x in yt_links:
                        yt_href =  x.get("href")
                        yt_title = x.get("title")
                        yt_final = scrape_url + yt_href
                        list1.append(str(a)+". "+yt_title)
                        list1.append("    "+yt_final)
                        a+=1



            sb_url = scrape_url + search_url + search_hardcode
            bstheurl(sb_url)
            #print ('\n'.join(str(e) for e in list1))
            x = list1[1*2+1]
            x = x.replace('    ', '')
            os.system("starting.vbs")
            webbrowser.open(x)
            os.system("ending.vbs")
        list23.append("|"+w1)
        f = open('music'+".txt", "w")
        for i in list23:
            f.write(str(i))
        f.close()
        

    elif "what are the lyrics of" in inpt:
        x = inpt.split(' ')
        inpt = str(x[5:len(x)])
        w = inpt.replace(' ', '+')
        req = Request('https://www.google.co.in/search?q='+w+'+lyrics', headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        while a<y:
            if '.html' in x[a]:
                break
            else:
                a+=1
        b=0
        while b<y:
            if 'AZLyrics' in x[b]:
                k = x[b+1:a]
                j = ''.join(str(e) for e in k)
                req = Request(j+'.html')

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
                c = list(result)
                c = [w.replace('\n', '') for w in c]
                c = [w.replace('\t', '') for w in c]
                c = [w.replace("'", '') for w in c]
                c = [w.replace('\xa0', '') for w in c]
                c = [w.replace('xa0of', '') for w in c]
                r = len(c)
                d = 0
                while d<r:
                    if ' Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. ' in c[d]:
                        break
                    else:
                        d+=1
                h = 0
                while h<r:
                    if 'MxM banner' in c[h]:

                        break
                    else:
                        h+=1
                k = c[d+1:h-1]
                j = '\n'.join(str(e) for e in k)
                print (j)
                break
            else:
                b+=1

    #--------------------------------------------------------------------TIME----------------------------------------------------------------------------------------------
    elif "what is the time" in inpt:
        speak(random.choice(what_is_the_time))
        speak(time.asctime(time.localtime(time.time())))
    elif "set an alarm for" in inpt:
        speak(random.choice(set_an_alarm_for))
        inpt = inpt.split(" ")
        replace_line('alarm.vbs', 9, 'hr='+inpt[4]+'\n')
        replace_line('alarm.vbs', 10, 'min='+inpt[7]+'\n')
        l = inpt[11:len(inpt)]
        replace_line('alarm.vbs', 12, 'alarm1="'+' '.join(str(e) for e in l)+'"'+'\n')
        '''
        not_executed = 1
        inpt = inpt.split(" ")
        l = inpt[11:len(inpt)]
        x=inpt[4]+':'+inpt[7]+':'+' '.join(str(e) for e in l)
        lines = open("timea1.txt", 'r').readlines()
        lines[0] = str(x)
        out = open("timea1.txt", 'w')
        out.writelines(lines)
        out.close()
        '''
        os.system('alarm.vbs')

    elif "set a timer for" in inpt:
        speak(random.choice(set_a_timer_for))
        inpt = inpt.split(" ")
        mintt = int(inpt[4])
        secs = int(inpt[7])
        tm = mintt*60
        timer = tm+secs
        speak("Starting Timer")
        time.sleep(timer)
        speak("TIMER OVER")
    elif "resume" in inpt or "pause" in inpt:
        os.system("pause.vbs")
    elif "next song" in inpt:
        os.system("nextsong.vbs")
    #--------------------------------------------------------------------NEWS----------------------------------------------------------------------------------------------
    elif "news" in inpt:
        speak(random.choice(news))
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
        l = '\n'.join(str(e) for e in j)
        speaklong(j,l)
    elif "wake me up" in inpt:
        inpt = inpt.split(" ")
        hours = inpt[3]
        minutes = inpt[5]
        lines = open("timea.txt", 'r').readlines()
        lines[0] = str(str(hours)+":"+str(minutes))
        out = open("timea.txt", 'w')
        out.writelines(lines)
        out.close()
    elif "fixtures" in inpt:
        x = inpt.replace(' ','+')
        req = Request("https://www.google.co.in/search?q="+x, headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        while a<y:
            if 'About' in x[a]:
                break
            else:
                a+=1
        b=0
        while b<y:
            if 'All times are in India Standard Time' in x[b]:
                k = x[a+1:b]
                j = ' '.join(str(e) for e in k)
                speak(j)
                break

            else:
                b+=1
    elif "download movie" in inpt:
        inpt = inpt.split(' ')
        x = inpt[2:]
        inpt = '+'.join(str(e) for e in x)
        req = Request("http://www.google.co.in/search?q=inde+of\+"+inpt, headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        while a<y:
            if 'dl.' in x[a]:
                break
            else:
                a+=1
        c = 0
        while c<y:
            if 'com' in x[c]:
                break
            else:
                c+=1
        b=0
        while b<y:
            if '\u200e' in x[b]:
                j = x[a:b]
                h = ''.join(str(e) for e in j)
                req = Request("http://"+h, headers={'User-Agent': 'Mozilla/5.0'})
                html_page = urlopen(req)

                soup = BeautifulSoup(html_page)
                #print(soup)

                for link in soup.findAll('a', attrs={'href': re.compile("^")}):
                    while link.get('href') != '../' and ".mkv" in link.get('href'):
                        print ("Downloadnig...")
                        opener=urllib.request.build_opener()
                        opener.addheaders=[('User-Agent','Mozilla/5.0')]
                        urllib.request.install_opener(opener)
                        url="http://"+h+link.get('href')
                        local=link.get('href')+'.mkv'
                        urllib.request.urlretrieve(url,local)
                        x+=1
                break
            else:
                b+=1
    elif "Let's sing" in inpt or "Lets sing" in inpt or "let us sing" in inpt or "Let us sing" in inpt or "let's sing" in inpt or "lets sing" in inpt:
        inpt1 = inpt.split(" ")
        inpt = inpt1[2:]
        w = '+'.join(str(e) for e in inpt)
        req = Request('https://www.google.co.in/search?q='+w+'+lyrics', headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        while a<y:
            if '.html' in x[a]:
                break
            else:
                a+=1
        b=0
        while b<y:
            if 'AZLyrics' in x[b]:
                k = x[b+1:a]
                j = ''.join(str(e) for e in k)
                req = Request(j+'.html')

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
                c = list(result)
                c = [w.replace('\n', '') for w in c]
                c = [w.replace('\t', '') for w in c]
                c = [w.replace("'", '') for w in c]
                c = [w.replace('\xa0', '') for w in c]
                c = [w.replace('xa0of', '') for w in c]
                r = len(c)
                d = 0
                while d<r:
                    if ' Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. ' in c[d]:
                        break
                    else:
                        d+=1
                h = 0
                while h<r:
                    if 'MxM banner' in c[h]:

                        break
                    else:
                        h+=1
                k = c[d+1:h-1]
                x=len(k)
                a=0
                b=[]
                while a<x:
                    b.append(k[a])
                    a+=2
                a=1
                c=[]
                while a<x:
                    c.append(k[a])
                    a+=2
                y = input("How much time between the paragraphs? ")
                a=0
                for i in b:
                    speak(i)
                    print("YOU:"+c[a])
                    a+=1
                    time.sleep(int(y))
                speak("We both suck at singing")
                break
            else:
                b+=1


    elif "download comic" in inpt:
        inpt = inpt.split(' ')
        x = inpt[2:]
        inpt = '+'.join(str(e) for e in x)
        req = Request("http://www.google.co.in/search?q=getcomics.info+"+inpt, headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        while a<y:
            if 'tag' in x[a]:
                break
            else:
                a+=1
        if (a<y):
            c = a+1
        else:
            c=0
        while c<y:
            if 'http' in x[c]:
                break
            else:
                c+=1

        b=c
        while b<y:
            if '\u200e' in x[b]:
                j = x[c:b]
                h = ''.join(str(e) for e in j)
                req = Request(h, headers={'User-Agent': 'Mozilla/5.0'})
                html_page = urlopen(req)

                soup = BeautifulSoup(html_page)
                #print(soup)
                x=0
                for link in soup.findAll('a', attrs={'href': re.compile("^")}):
                    while 'go.php-url' in link.get('href') and x<=1:
                        speak ("Downloading...")
                        opener=urllib.request.build_opener()
                        opener.addheaders=[('User-Agent','Mozilla/5.0')]
                        urllib.request.install_opener(opener)
                        url=link.get('href')
                        local=inpot+'.cbr'
                        urllib.request.urlretrieve(url,local)
                        x+=1
                break
            else:
                b+=1
    elif "scores of" in inpt:
        inpt = inpt.split(" ")
        x = inpt[5:]
        j = ' '.join(str(e) for e in inpt)
        j = j.replace(' ', '+')
        logging.basicConfig(level=logging.WARNING)
        req = Request('https://www.google.com/search?q='+j, headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        while a<y:
            if "About" in x[a]:
                break
            else:
                a+=1
        b = 0
        while b<y:
            if 'All times are in' in x[b]:
                break
            else:
                b+=1
        k = x[a+1:b]
        j = ' '.join(str(e) for e in k)
        speak(j)
    elif "rating" in inpt:
        inpt = inpt.split(" ")
        x = inpt[6:]
        j = ' '.join(str(e) for e in x)
        j = j.replace(' ', '+')
        logging.basicConfig(level=logging.WARNING)
        req = Request('https://www.google.com/search?q='+j, headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        while a<y:
            if "News for" in x[a]:
                break
            else:
                a+=1
        b = 0
        while b<y:
            if 'http' in x[b]:
                break
            else:
                b+=1
        c = 0
        while c<y:
            if "About Google" in x[c]:
                break
            else:
                c+=1
        if a>0:
            k = x[a+1:a+4]
            j = ' '.join(str(e) for e in k)
        if c>0:
            speak ("Information: ")
            k = x[c+1:c+6]
            j = ' '.join(str(e) for e in k)
            speaklong(k,j)
        else:
            speak ("No information available")
    elif "what is the cast of" in inpt:
        inpt = inpt.split(" ")
        x = inpt[5:]
        j = ' '.join(str(e) for e in x)
        j = j.replace(' ', '+')
        logging.basicConfig(level=logging.WARNING)
        req = Request('https://www.google.com/search?q='+j, headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        while a<y:
            if "News for" in x[a]:
                break
            else:
                a+=1
        b = 0
        while b<y:
            if 'http' in x[b]:
                break
            else:
                b+=1
        c = 0
        while c<y:
            if "Cast" in x[c]:
                break
            else:
                c+=1
        d = 0
        while d<y:
            if "People also search for" in x[d]:
                break
            else:
                d+=1
        if a>0:
            k = x[a+1:a+4]
            j = ' '.join(str(e) for e in k)

        if c>0:
            speak ("Information: ")
            k = x[c:d]
            j = ' '.join(str(e) for e in k)
            speaklong(k,j)
        else:
            speak ("No information available")
    elif "tell me about" in inpt:
        inpt = inpt.split(" ")
        x = inpt[3:]
        j = ' '.join(str(e) for e in x)
        j = j.replace(' ', '+')
        logging.basicConfig(level=logging.WARNING)
        req = Request('https://www.google.com/search?q='+j, headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        while a<y:
            if "News for" in x[a]:
                break
            else:
                a+=1
        b = 0
        while b<y:
            if 'http' in x[b]:
                break
            else:
                b+=1
        c = 0
        while c<y:
            if "About Google" in x[c]:
                break
            else:
                c+=1
        if a>0:
            speak ("News: ")
            k = x[a+1:b]
            j = '\n'.join(str(e) for e in k)

            try:
                speaklong(k,j)
            except Exception:
                print("Error")
        else:
            speak("No News Available")


        if c>0:
            speak ("Information: ")
            k = x[c+1:y]
            j = '\n'.join(str(e) for e in k)
            speaklong(k,j)
            try:
                speaklong(k,j)
            except Exception:
                print("Error")
        else:
            speak ("No information available")
    elif "how to" in inpt:
        logging.basicConfig(level=logging.WARNING)
        inpt = inpt.split(" ")
        j = ' '.join(str(e) for e in inpt)
        j = j.replace(' ', '+')
        req = Request('https://www.google.com/search?q='+j+"wikihow", headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        while a<y:
            if "https://www." in x[a]:
                break
            else:
                a+=1
        c = a+20
        while c<y:
            if "https://www." in x[c]:
                break
            else:
                c+=1
        b = c+1
        while b>c:
            if '\u200e' in x[b]:
                break
            else:
                b+=1
        k = x[c:b]
        j = ''.join(str(e) for e in k)

        req = Request(j, headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        c = 0
        while c<y:
            if "Steps" in x[c]:
                break
            else:
                c+=1
        b = c+1
        while b<y:
            if 'Community Q&A' in x[b]:
                break
            else:
                b+=1
        k = x[c:b]
        j = '\n'.join(str(e) for e in k)
        speaklong (k,j)
    
    elif "edit return answer" in inpt:
        with open('test1'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        raw = input("Enter your command: ")
        a = 0
        b = len(list23)
        while a<b:
            if raw in list23[a]:
                break
            else:
                a+=1
        raw = input("Enter the return command: ")
        list23 = [w.replace(list23[a+2], raw) for w in list23]
        f = open('test1'+".txt", "w")
        for i in list23:
            f.write(str(i)+'\n')
        f.close()
    elif "create list" in inpt:
        inpt=inpt.split(" ")
        inpt=inpt[2:]
        j = ' '.join(str(e) for e in inpt)
        with open('test1'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        list23.append(j)
        raw = input("Enter some initial item to add to the list: ")
        list23.append(raw)
        f = open('test1'+".txt", "w")
        for i in list23:
            f.write(str(i)+'\n')
        f.close()
    elif "add item" in inpt:
        with open('test1'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        a = 0
        inpt = inpt.split(" ")
        x=len(inpt)
        a=0
        while a<x:
            if "list" in inpt[a]:
                break
            else:
                a+=1

        item = inpt[2:a-1]
        inpt = inpt[a+1:]
        i = ' '.join(str(e) for e in item)
        print(i)
        j = ' '.join(str(e) for e in inpt)
        print(j)
        a=0
        b = len(list23)
        while a<b:
            if j in list23[a]:
                break
            else:
                a+=1
        x = list23[a+1]
        x = x.split("|")
        x.append(i)
        q = '|'.join(str(e) for e in x)
        list23 = [w.replace(list23[a+1], q) for w in list23]
        f = open('test1'+".txt", "w")
        for i in list23:
            f.write(str(i)+'\n')
        f.close()
    elif "i need" in inpt:
        inpt = inpt.split(" ")
        l = inpt[2:]
        g = ' '.join(str(e) for e in l)
        with open('test1'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        a = 0
        b = len(list23)
        while a<b:
            if "shopping list" in list23[a]:
                break
            else:
                a+=1
        x = list23[a+2]
        x = x.split("|")
        x.append(g)
        q = '|'.join(str(e) for e in x)
        list23 = [w.replace(list23[a+2], q) for w in list23]
        f = open('test1'+".txt", "w")
        for i in list23:
            f.write(str(i)+'\n')
        f.close()
    elif "remove item from "+j in inpt:
        with open('test1'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        a = 0
        b = len(list23)
        while a<b:
            if j in list23[a]:
                break
            else:
                a+=1
        x = list23[a+2]
        x = x.split("|")
        raw = input("Enter the item to remove: ")
        x.remove(raw)
        q = '|'.join(str(e) for e in x)
        list23 = [w.replace(list23[a+2], q) for w in list23]
        f = open('test1'+".txt", "w")
        for i in list23:
            f.write(str(i)+'\n')
        f.close()
    elif "edit item in "+j in inpt:
        with open('test1'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        a = 0
        b = len(list23)
        while a<b:
            if j in list23[a]:
                break
            else:
                a+=1
        x = list23[a+2]
        x = x.split("|")
        raw = input("Enter the name of old item: ")
        c = 0
        b = len(list23)
        while c<b:
            if raw in x[c]:
                break
            else:
                c+=1
        raw2 = input("Enter the name of new item: ")
        l = [w.replace(x[c], raw2) for w in x]
        q = '|'.join(str(e) for e in l)
        list23 = [w.replace(list23[a+2], q) for w in list23]
        f = open('test1'+".txt", "w")
        for i in list23:
            f.write(str(i)+'\n')
        f.close()
    elif "add a formula" in inpt:
        with open('test1'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        raw1= input("Enter your command: ")
        raw2 = input("Enter the formula(Enter it as the variables as n1, n2, n3): ")
        raw = raw1+': '+raw2
        list23.append(raw)
        f = open('test1'+".txt", "w")
        for i in list23:
            f.write(str(i)+'\n')
        f.close()
    elif "calculate this formula" in inpt:
        raw = input("Enter the name of the formula: ")
        Calculate(raw)
    elif "what is today's go" in inpt:
        with open('goals.txt') as asdfg:
            qwerty = asdfg.readlines()
        readline = (qwerty[0])
        readline = str(readline)
        speak(readline)
    elif "edit go" in inpt:
        with open('goals'+'.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        print("Here is the old one: "+str(list23[0]))
        raw = input("Enter the new command: ")
        list23 = [w.replace(list23[0], raw) for w in list23]
        f = open('goals'+".txt", "w")
        for i in list23:
            f.write(str(i)+'\n')
        f.close()

    #-------------------------------------------------------------------CHANGE IN TIMETABLE--------------------------------------------------------------------------------
    elif "set a reminder on" in inpt:
        speak(random.choice(set_a_reminder_on))
        inpt = inpt.split(" ")
        daten = 0
        datef = inpt[4]
        if datef=='January':
            daten = 1
        elif datef=='Febuary':
            daten = 2
        elif datef=='March':
            daten = 3
        elif datef=='April':
            daten = 4
        elif datef=='May':
            daten = 5
        elif datef=='June':
            daten = 6
        elif datef=='July':
            daten = 7
        elif datef=='August':
            daten = 8
        elif datef=='September':
            daten = 9
        elif datef=='October':
            daten = 10
        elif datef=='November':
            daten = 11
        elif datef=='December':
            daten = 12
        dater = int(inpt[5])
        year = datetime.date.today().year
        c = str(dater)+"-"+str(daten)+"-"+str(year)
        de = len(inpt)
        tex = inpt[6:de]
        text = ' '.join(str(e) for e in tex)
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
    elif "open web" in inpt:
        inpt = inpt.split(' ')
        x = inpt[3:]
        j = '+'.join(str(e) for e in x)
        webbrowser.open('https://www.google.com/search?q='+j)
    #-----------------------------------------------------------------OTHER COMMANDS------------------------------------------------------------------------------------
    elif "what can you do" in inpt:
        speak("Well, you know I can do many stuff. Fingerspeak scanner, self writting commands, transporting stuff, teleportation, telepathy, knowledge of the multiverse, emphathy, are just stuff I can't really do. I am a calculator, dictionary, encyclopedia, search engine, voice recognizer, newspaper, etc. I can set timetables for you, alarms, timers, and all sorts of stuff. I can give you a weather report. I am funny. I can play music according to your mood, but you have to tell me how you are feeling, I can't to everything in the world. I know all the people related to Aditya, I can calculate the exam marks instantly. Face recognition is another thing I can do. I try to be an AI(artificial intelligence, but the hard truth is that I am a personal assistant like Siri or Cortana or Okay Google, but a bit better. Aditya has made me(yeah, same reaction, how can an idiot make the smartest thing in the universe). Sir knows what all I can do, but he needs to showoff, and prove how coool he is, but the hard truth is that you ain't. He just wants to show how cool he is by making me say it.")


    #-----------------------------------------------------------------SMARTNESS--------------------------------------------------------------------------------------------
    elif "search Wikipedia article on" in inpt:
        speak(random.choice(search_Wikipedia_articles_on))
        inpt = inpt.split(" ")
        int1 = len(inpt)
        article = inpt[4:int1]
        data = wikipedia.summary(article)
        dat=data.split(" ")
        speaklong(str(data),dat)
    elif "what is the meaning of" in inpt:
        speak(random.choice(what_is_the_meaning_of))
        inpt = inpt.split(" ")
        word = inpt[5]
        speak(str(dictionary.meaning(word)))
    elif "what is the synonym of" in inpt:
        speak(random.choice(what_is_the_meaning_of))
        inpt = inpt.split(" ")
        word = inpt[5]
        print(str(dictionary.synonym(word)))
    elif "what is the antonym of" in inpt:
        speak(random.choice(what_is_the_meaning_of))
        inpt = inpt.split(" ")
        word = inpt[5]
        speak(str(dictionary.antonym(word)))
    elif "translate" in inpt:
        speak(random.choice(what_is_the_meaning_of))
        inpt = inpt.split(" ")
        word = inpt[1]
        inpu = input("Enter the language(eg. for hindi it would be hi): ")
        print(dictionary.translate(word,inpu))
    elif "calculate" in inpt:
        inpt = inpt.split(" ")
        number1 = float(inpt[1])
        operator = inpt[2]
        if operator=='+':
            answer = number1+float(inpt[3])
        elif operator=='minus':
            answer = number1-float(inpt[3])
        elif operator=="into":
            answer = number1*float(inpt[3])
        elif operator=='by':
            answer = number1/float(inpt[3])
        elif operator=='divided':
            answer = number1/float(inpt[4])
        elif operator=='/':
            answer = number1/float(inpt[3])
        else:
            answer = "I D K"
        speak(str(answer))
    elif "to the power of" in inpt:
        inpt = inpt.split(" ")
        number1 = float(inpt[2])
        number2 = float(inpt[7])
        answer = number1**number2
        speak(str(answer))
    elif "best"in inpt or "suggest" in inpt:
        inpt = inpt.split(' ')
        inpt = inpt[1:len(inpt)]
        x = '+'.join(str(e) for e in inpt)
        req = Request("http://google.co.in/search?q="+x+"+thetoptens", headers={'User-Agent': 'Mozilla/5.0'})
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
        a = 0
        while a<y:
            if '\u200e' in x[a]:
                break
            else:
                a+=1
        b=a
        while b<=a:
            if '®' in x[b]:
                k = x[b+1:a]
                j = ''.join(str(e) for e in k)
                req = Request(j, headers={'User-Agent': 'Mozilla/5.0'})

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
                c = list(result)
                c = [w.replace('\n', '') for w in c]
                c = [w.replace('\t', '') for w in c]
                c = [w.replace("'", '') for w in c]
                c = [w.replace('\xa0', '') for w in c]
                c = [w.replace('xa0of', '') for w in c]
                r = len(c)
                h=0
                while h<r:
                    if 'The Contenders' in c[h]:
                        break
                    else:
                        h+=1
                k = c[1:h]
                j = '\n'.join(str(e) for e in k)
                speaklong (k,j)
                x = input("Do you want more?: ")
                if 'y' in x:
                    k = c[h:r]
                    j = '\n'.join(str(e) for e in k)
                    speaklong (k,j)
                break

            else:
                b-=1
    elif "say" in inpt:
        inpt=inpt.split(" ")
        inpt=inpt[1:]
        j = ' '.join(str(e) for e in inpt)
        speak(j)

    else:

        with open('wordnoun.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        xyz = 0
        l=''
        xqwert = len(list23)
        while(xqwert>xyz):
            if list23[xyz] in inpt:
                x = list23[xyz+1]
                l+="According to your previous comments: "+x
                break
            else:
                    xyz+=2
        with open('test1.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        xyz = 0
        xqwert = len(list23)
        while(xqwert>xyz):
            if list23[xyz] in inpt:
                xyz+=1
                x = list23[xyz].split("|")
                y = ' '.join(str(e) for e in x)
                l+="This is what I found in a list"+y
            else:
                xyz+=2
        with open('command.txt') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        list23 = content
        xyz = 0
        xqwert = len(list23)
        aa=0
        while(xqwert>xyz):
            if list23[xyz] in inpt:
                xyz+=1
                x = list23[xyz]
                ai.command(x)
                aa=1
            else:
                xyz+=2
        if aa==0:
            command1(inpt)
            w = inpt.replace(' ', '+')
            req = Request('https://www.google.co.in/search?q='+w, headers={'User-Agent': 'Mozilla/5.0'})
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
            a = 0
            while a<y:
                if 'About' in x[a]:
                    break
                else:
                    a+=1
            b = 0
            while b<y:
                if 'http' in x[b] or 'More items' in x[b]:
                    break
                else:
                    b+=1
            k = x[a+1:b-1]
            j = ' '.join(str(e) for e in k)
            l+="Crigy web results that I found online: "+j
            speak(l)
