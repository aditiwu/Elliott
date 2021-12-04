import speech_recognition as sr
from gtts import gTTS
import ai
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
while True:
    x=listen1()
    try:
        if "hello" in x or "Elliot" in x:
            ai.command(listen())
    except:
        print("PROBS")
        
