import random 
from fuzzywuzzy import fuzz

frenchList = [['yes', 'oui', 0], ['no', 'non', 0], ['hello', 'bonjour', 0], ['not', 'pas', 0],
              ['you', 'vous', 0], ['in', 'dans', 0], ['dictionary', 'dictionnaire', 0]]
orderedFrenchList = []
linebreak = "*"*45


def wordfeed():
        index = random.randint(0,len(frenchList)-1)
        global word
        word = frenchList[index]
        return word[1]

print(linebreak + "\n Test your knowledge! \n Type H for help or Q to quit. ")
print(linebreak)


def main():
    while True:
        response = input("What is " + wordfeed() + " in English? \n" + "Previously you got this word " + str(word[2]) + "% correct. ")
        if response == word[0]:
            print("Correct!")
            word[2] = 100
        elif response.upper() == "Q":
            print("See you next time!")
            break
        elif response.upper() == "H":
            print(linebreak + "\n "
                  "Translate the French words and they will be sorted "
                  "\n and asked again based on how well you know them. \n Press Q to exit.")
            print(linebreak)
        else:
            print("Incorrect!")
            similarity = fuzz.ratio(response, word[0])
            print("Your answer was " + str(100 - similarity) + "% off.")
            word[2] = similarity
# begin
main()
