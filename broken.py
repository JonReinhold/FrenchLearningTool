##old poorly done rough draft saved for sentimental reasons
##current project is in FrenchTool.py

import random
from difflib import SequenceMatcher

def check(w, v):
    return SequenceMatcher(None, w, v).ratio()

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
wordlist = []
badlist = []
eng = []
fre = []
end = []
end2= []

with open('words.txt') as f:
    full = [line.rstrip('\n') for line in f]
for i in full:
        if len(i) < 20:
            if "/" in i or "]" in i:
                badlist.append(i)
            else:
                wordlist.append(i.split("\t"))
                
for i in wordlist:
        eng.append(i[:1])
        fre.append(i[1:])
        
quiz = "begin"

#press quit to exit
while quiz != "quit":
    index = random.randint(0,len(eng))
    quiz = input("Translate "+ str(eng[index])+" ")
    trans = str(fre[index])
    for i in trans:
        if i in chars:
            end.append(i)
        else:
            badlist.append(i)
    for i in quiz:
        if i in chars:
            end2.append(i)
        else:
            badlist.append(i)

    if end == end2:
        print("Correct.")
        end = []
        end2 = []
    else:
        print("That's not quite right..")
        print(fre[index])
        print(check(end, end2))
        end=[]
        end2=[]
