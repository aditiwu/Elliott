import datetime
import math
import time
import speech_recognition as sr
from gtts import gTTS
import os
import wikipedia
import periodictable as pt
import logging
from PyDictionary import PyDictionary
import os
import ai
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
import os
from gtts import gTTS
playlist = 1
my_dict = {}
dictionary=PyDictionary()
logging.basicConfig(level=logging.WARNING)

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
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
def read_line(filen, line):
    with open(filen) as asdfg:
        qwerty = asdfg.readlines()
    readline = (qwerty[line])
    return readline
def speak1(audioString):
    text = 'Sapi.Speak "'+str(audioString)+'"'
    print("ELLIOT: "+audioString)
    x = "ELLIOT: "+audioString
    #ser.wrtie(x.encode())
    replace_line('speak.vbs', 1, text)
    
    os.system("speak.vbs")
try:
  ser = serial.Serial("COM6", 9600)
  if (ser.isOpen()):
      dfghjk = ''

except IOError:
    speak1("Touchscreen not connected")
    os.system("hello_no_port.pyw")
ser.wrtie("HELLO".encode())

def read_line(filen, line):
    with open(filen) as asdfg:
        qwerty = asdfg.readlines()
    readline = (qwerty[line])
    return readline
    
def speaklonglong(audioString):
    print("ELLIOT: "+audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("audio.mp3")

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
def speak(audioString):
    text = 'Sapi.Speak "'+str(audioString)+'"'
    print("ELLIOT: "+audioString)
    x = "ELLIOT: "+audioString
    ser.wrtie(x.encode())
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
def listen1():
    startvariable = 1
    time.sleep(0.5)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    inpt = ''

    #------------------------------------------------------------------RECOGNIZES THE VOICE--------------------------------------------------------------------------------
    try:
        print("YOU: " + r.recognize_google(audio))
        u = "YOU: " + r.recognize_google(audio)
        inpt = r.recognize_google(audio)
    except sr.UnknownValueError:
        u = "YOU: Hello"
    except sr.RequestError as e:
        u = "YOU: Hello"
    return inpt
def listen(question):
    startvariable = 1
    speak(question)
    time.sleep(0.5)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("ELLIOT: Say something!")
        audio = r.listen(source)

    inpt = ''

    #------------------------------------------------------------------RECOGNIZES THE VOICE--------------------------------------------------------------------------------
    try:
        print("YOU: " + r.recognize_google(audio))
        u = "YOU: " + r.recognize_google(audio)
        inpt = r.recognize_google(audio)
    except sr.UnknownValueError:
        speak("Google Speech Recognition does not speak gibberish")
        inpt = input("Enter Command: ")
    except sr.RequestError as e:
        speak("Your WiFi is down bro, everyone has a weakness, this is mine, get it back, I am good for nothing without the WiFi. I can't understand anything you say bro, save me; {0}".format(e))
        inpt = input("Enter Command: ")
    return inpt
#----------------------------------------------------------------------------------------------LOOP--------------------------------------------------------------------
while True:
    with open('vals.txt') as asdfg:
        qwerty = asdfg.readlines()
    readline = (qwerty[0])
    readline = str(readline)
    if readline == 'holiday':
        not_executed = 1
        while(not_executed):
            dt = list(time.localtime())
            hour = dt[3]
            minute = dt[4]
            with open('timea.txt') as asdfg:
                qwerty = asdfg.readlines()
            readline = (qwerty[0])
            readline = str(readline)
            x = readline.split(":")
            y = int(x[0])
            z = int(x[1])
            if hour == y and minute == z:
                os.system("hellostart_gm.pyw")
                os.system("Coldplay-Clocks.mp3")
                time.sleep(10)
                input("ENTER")
            else:
                dt = list(time.localtime())
                hour = dt[3]
                minute = dt[4]
                break

        
        not_executed = 1
        while(not_executed):
            dt = list(time.localtime())
            hour = dt[3]
            minute = dt[4]
            with open('timea.txt') as asdfg:
                qwerty = asdfg.readlines()
            readline = (qwerty[0])
            readline = str(readline)
            x = readline.split(":")
            y = int(x[0])
            z = int(x[1])
            while (hour >=y and hour<=22) and (not_executed):
                dt = list(time.localtime())
                hour = dt[3]
                minute = dt[4]
                inpot = listen1()
                if "Elliot" in inpot:
                    time.sleep(1)
                    inport = listen("What can I do for you?")
                    ai.command(inport)
                elif "Alexa" in inpot:
                    speak("Ohh so you choose her over me?")
                else:
                    dt = list(time.localtime())
                    hour = dt[3]
                    minute = dt[4]
            else:
                not_executed
                dt = list(time.localtime())
                hour = dt[3]
                minute = dt[4]
                break
        
        while(not_executed):
            dt = list(time.localtime())
            hour = dt[3]
            minute = dt[4]
            if (hour ==23 and minute==0) and (not_executed):
                dt = list(time.localtime())
                hour = dt[3]
                minute = dt[4]
                speak("Sleeping Time, but before that...")
                with open('goals'+'.txt') as f:
                    content = f.readlines()
                content = [x.strip() for x in content]
                list23 = content
                print("Check if you are done with: "+str(list23[0]))
                raw = input("Enter tomorrow's goal: ")
                list23 = [w.replace(list23[0], raw) for w in list23]
                f = open('goals'+".txt", "w")
                for i in list23:
                    f.write(str(i)+'\n')
                f.close()
                x = input("Enter if tomorrow is holiday, full day, half, day: ")
                lines = open("vals.txt", 'r').readlines()
                lines[0] = str(x)
                out = open("vals.txt", 'w')
                out.writelines(lines)
                out.close()
                x = input("Enter the time when I should wake you up tomorrow(format- h:m): ")
                lines = open("timea.txt", 'r').readlines()
                lines[0] = str(x)
                out = open("vals.txt", 'w')
                out.writelines(lines)
                out.close()
                input("Enter")
            else:
                not_executed
                dt = list(time.localtime())
                hour = dt[3]
                minute = dt[4]
                break
    elif readline == 'full day' or readline == 'half day':
        not_executed = 1
        while(not_executed):
            dt = list(time.localtime())
            hour = dt[3]
            minute = dt[4]
            with open('timea.txt') as asdfg:
                qwerty = asdfg.readlines()
            readline = (qwerty[0])
            readline = str(readline)
            x = readline.split(":")
            y = int(x[0])
            z = int(x[1])
            if hour == y and minute == z:
                os.system("Coldplay-Clocks.mp3")
                time.sleep(10)
                dt = list(time.localtime())
                hour = dt[3]
                minute = dt[4]
                input("Enter")
            else:
                dt = list(time.localtime())
                hour = dt[3]
                minute = dt[4]
                break
        not_executed = 1
        while(not_executed):
            dt = list(time.localtime())
            hour = dt[3]
            minute = dt[4]
            if hour == 4 and minute == 0: 
                os.system("hellostart_ge.pyw")
                time.sleep(10)
                input("ENTER")
            else:
                dt = list(time.localtime())
                hour = dt[3]
                minute = dt[4]
                break

        
        not_executed = 1
        while(not_executed):
            dt = list(time.localtime())
            hour = dt[3]
            minute = dt[4]
            with open('timea.txt') as asdfg:
                qwerty = asdfg.readlines()
            readline = (qwerty[0])
            readline = str(readline)
            x = readline.split(":")
            y = int(x[0])
            z = int(x[1])
            while (hour >=4 and hour<=21) and (not_executed):
                dt = list(time.localtime())
                hour = dt[3]
                minute = dt[4]
                inpot = listen1()
                if "Elliot" in inpot:
                    time.sleep(1)
                    inport = listen("What can I do for you?")
                    ai.command(inport)
                elif "Alexa" in inpot:
                    speak("Ohh so you choose her over me?")
                else:
                    dt = list(time.localtime())
                    hour = dt[3]
                    minute = dt[4]
            else:
                dt = list(time.localtime())
                hour = dt[3]
                minute = dt[4]
                not_executed
                break
        
        while(not_executed):
            dt = list(time.localtime())
            hour = dt[3]
            minute = dt[4]
            if (hour ==22 and minute==0) and (not_executed):
                dt = list(time.localtime())
                hour = dt[3]
                minute = dt[4]
                speak("Sleeping Time, but before that...")
                with open('goals'+'.txt') as f:
                    content = f.readlines()
                content = [x.strip() for x in content]
                list23 = content
                print("Check if you are done with: "+str(list23[0]))
                raw = input("Enter tomorrow's goal: ")
                list23 = [w.replace(list23[0], raw) for w in list23]
                f = open('goals'+".txt", "w")
                for i in list23:
                    f.write(str(i)+'\n')
                f.close()
                x = input("Enter if tomorrow is holiday, full day, half, day: ")
                lines = open("vals.txt", 'r').readlines()
                lines[0] = str(x)
                out = open("vals.txt", 'w')
                out.writelines(lines)
                out.close()
                x = input("Enter the time when I should wake you up tomorrow(format- h:m): ")
                lines = open("timea.txt", 'r').readlines()
                lines[0] = str(x)
                out = open("vals.txt", 'w')
                out.writelines(lines)
                out.close()
                input("Enter")
            else:
                not_executed
                dt = list(time.localtime())
                hour = dt[3]
                minute = dt[4]
                break
    else:
        print("Error")
