import os
from datetime import datetime

class bcolors:
    low = "\033[39m"
    mid = "\033[33m"
    high = "\033[31m"

# Priority
# 1 - Low Priority
# 2 - Mid Priority
# 3 - Critial Priority

# Logfiles
#   system
#   user
#   misc

# Example
# Low Priority System
#   log("system",text,"1")

# Mid Priority System
#   log("system",text,"2")

# High Priority User
#   log("user",text,"3")

def log(logfile,text,priority):
    text = str(text)
    now = datetime.now()
    nowtime = str(now.strftime("%d/%m/%Y %H:%M:%S"))
    if validate(logfile, priority) and filesetup(logfile):
        dir = ("./logs/"+logfile+".log")
        with open(dir, "a") as file:
            writetext = (nowtime + " - PRIORITY: " + priority + " - LOG - " + text + "\n")
            file.write(writetext)
            file.close()

def validate(logfile, priority):
    logfiles = ['system', 'user', 'misc']
    prioritynum = ['1', '2', '3']
    if (logfile in logfiles) and (priority in prioritynum):
        return True
    else:
        print("Critical error: Logfile or priority setting broken somewhere in code. This should not happen")
        return False

def filesetup(logfile):
    dir = ("./logs/"+logfile+".log")
    exists = os.path.exists(dir)
    if exists:
        return True
    elif not exists:
        os.mkdir("./logs/")
        with open(dir, "w") as file:
            now = datetime.now()
            nowtime = str(now.strftime("%d/%m/%Y %H:%M:%S"))
            writetext = ("Created logfile at " + nowtime + "\n")
            file.write(writetext)
            file.close()
            print("Created logfile " + logfile + " at " + nowtime)
            return True
