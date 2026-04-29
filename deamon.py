import psutil
import time

CheckPath = "WinSlop.exe"
DeamonPath = "WSDeamon.exe"
Exists = False
Counted = 0

for i in psutil.process_iter(): 
        if i.name() == DeamonPath:
            Counted += 1

if Counted < 2:
    CheckPath = DeamonPath
    print("I should re launch this Daemon!")

while True:
    time.sleep(0.5)
    
    Exists = False
    Counted = 0

    for i in psutil.process_iter(): 
        if i.name() == CheckPath:
            Exists = True
            Counted += 1


    if DeamonPath != CheckPath:
        if Exists == False:
            print("You closed my app >:(")
    else:
        if Counted < 2:
            print("You closed my Deamon D:<")