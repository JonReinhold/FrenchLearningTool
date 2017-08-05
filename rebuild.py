#set up test list, will pull from file later
import random
frenchList = [('yes','oui'),('no','non'),('hello','bonjour')]

def wordFeed():
        index = random.randint(0,len(frenchList)-1)
        global word
        word = frenchList[index]
        return word[1]

print("**************************************** \n Test your knowledge! \n Type H for help or Q to quit. ")
print("****************************************")
while True:
    response = input("What is " + wordFeed() + " in English? ")
    if response == word[0]:
        print("Correct!")
    elif response == "Q":
        print("Exiting tool...")
        break
    elif response == "H":
        print("****************************************\n "
              "Translate the French words and they will be sorted "
              "\n and asked again based on how well you know them. \n Press Q to exit.")
        print("****************************************")
    else:
        print("Wrong!")

