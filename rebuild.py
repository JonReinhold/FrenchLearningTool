import random
frenchList = [('yes','oui'),('no','non'),('hello','bonjour')]

def wordFeed():
        index = random.randint(0,len(frenchList)-1)
        global word
        word = frenchList[index]
        return word[1]

response = input("What is " + wordFeed() + " in English? ")
if response == word[0]:
    print("Correct!")
else:
    print("Wrong!")
