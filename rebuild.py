#set up test list, will pull from file later
import random
frenchList = [('yes','oui'),('no','non'),('hello','bonjour')]

def wordFeed():
        index = random.randint(0,len(frenchList)-1)
        global word
        word = frenchList[index]
        return word[1]
print("Test your knowledge! Type Q to quit.")
while True:
    response = input("What is " + wordFeed() + " in English? ")
    if response == word[0]:
        print("Correct!")
    elif response == "Q":
        break
    else:
        print("Wrong!")

