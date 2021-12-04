import time
import os


def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
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
    au=au.split(" ")
    au = [w.replace('\n', '') for w in au]
    au = [w.replace('\t', '') for w in au]
    au = [w.replace("'", '') for w in au]
    au = [w.replace('"', '') for w in au]
    au = [w.replace('\xa0', '') for w in au]
    au = [w.replace('xa0of', '') for w in au]
    au = [w.replace('\u018e', '') for w in au]
    au = [w.replace('\u200e', '') for w in au]
    au = [w.replace('\u02c8', '') for w in au]
    
    j = ' '.join(str(e) for e in au)
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
not_executed = 1

while(not_executed):
    dt = list(time.localtime())
    hour = dt[3]
    minute = dt[4]
    with open('timea1.txt') as asdfg:
        qwerty = asdfg.readlines()
    readline = (qwerty[0])
    readline = str(readline)
    x = readline.split(":")
    y = int(x[0])
    z = int(x[1])
    h = x[2]
    
    if hour == y and minute == z:
        
        speak(h)
        os.system("Coldplay-Clocks.mp3")
        time.sleep(10)
        input("ENTER")
    else:
        dt = list(time.localtime())
        hour = dt[3]
        minute = dt[4]
        os.system('hello_time_command.pyw')
