import ai
import os
import time
import datetime
with open('today.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
not_executed = 1
while(not_executed):
    dt = list(time.localtime())
    hour = dt[3]
    minute = dt[4]
    with open('today.txt') as asdfg:
        qwerty = asdfg.readlines()
    content = [x.strip() for x in qwerty]
    try:
        readline = content[0]
        x = readline.split(":")
        y = int(x[0])
        z = int(x[1])
        read = content[1]
        if hour == y and minute == z:
            print("atleast you are here")
            read = read.split(" and ")
            for i in read:
                ai.command(i)
            del content[0]
            del content[0]
            print(content)
            f = open('today'+".txt", "w")
            for i in content:
                f.write(str(i)+'\n')
            f.close()
            time.sleep(60)
            os.system("parallelcode.pyw")
            
            
        else:
            dt = list(time.localtime())
            hour = dt[3]
            minute = dt[4]
    except:
        break

not_executed = 1
while(not_executed):
    dt = list(time.localtime())
    hour = dt[3]
    minute = dt[4]
    if hour == 12 and minute == 40:
        print("Good Night")
        time.sleep(70)
        break
    else:
        dt = list(time.localtime())
        hour = dt[3]
        minute = dt[4]
    


while(not_executed):
    dt = list(time.localtime())
    hour = dt[3]
    minute = dt[4]
    with open('timea.txt') as asdfg:
        qwerty = asdfg.readlines()
    content = [x.strip() for x in qwerty]
    
    readline = content[0]
    x = readline.split(":")
    y = int(x[0])
    z = int(x[1])
    if hour == y and minute == z:
        print("Good Morning")
        time.sleep(70)
        break
    else:
        dt = list(time.localtime())
        hour = dt[3]
        minute = dt[4]
