# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("spellcheck-python-startcode-main/data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("spellcheck-python-startcode-main/data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    # print(dictionary[0:50])
    # print(aliceWords[0:50])
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()

def Menu():
    User=int(input("""Main Menu
1: Spell Check a Word (Linear Search)
2: Spell Check a Word (Binary Search)
3: Spell Check Alice In Wonderland (Linear Search)
4: Spell Check Alice In Wonderland (Binary Search)
5: Exit
Enter menu selection (1-5): """))

    return User

def SpellCheckLinear():
    Start=time.time()
    dictionary = loadWordsFromFile("spellcheck-python-startcode-main/data-files/dictionary.txt")

    word=input("Please enter a word: ").lower()
    
    for i in range(len(dictionary)):
        if dictionary[i]==word:
            print(f"{word} is IN the dictionary at position {i}. {time.time()-Start} seconds")
            return

    print(f"{word} is NOT in the dictionary. {time.time()-Start} seconds")
    
def CheckAliceLinear():
    Start=time.time()
    dictionary = loadWordsFromFile("spellcheck-python-startcode-main/data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("spellcheck-python-startcode-main/data-files/AliceInWonderLand.txt")
    InDict=0

    for word in aliceWords:
        for i in dictionary:
            if dictionary[i]==word.lower():
                InDict+=1
    
    print(f"Number of words not found in dictionary: {len(aliceWords)-InDict}. {time.time()-Start} seconds")

def SpellCheckBinary():
    Start=time.time()
    dictionary = loadWordsFromFile("spellcheck-python-startcode-main/data-files/dictionary.txt")

    word=input("Please enter a word: ").lower()

    Upper=len(dictionary)-1
    Lower=0
 
    for thing in range(int(len(dictionary)/2)):
        Middle=int((Lower+Upper)/2)
       
        if word == dictionary[Middle]:
            print(f"{word} is IN the dicitonary. {time.time()-Start} seconds")
            return
        elif word < dictionary[Middle]:
            Upper=Middle-1
        else:
            Lower=Middle+1

    print(f"{word} is NOT in the dicitonary. {time.time()-Start} seconds")

def CheckAliceBinary():
    Start=time.time()
    dictionary = loadWordsFromFile("spellcheck-python-startcode-main/data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("spellcheck-python-startcode-main/data-files/AliceInWonderLand.txt")
    InDict=0

    Upper=len(dictionary)-1
    Lower=0
    
    for word in aliceWords:
        word=word.lower()
        for thing in range(int(len(dictionary)/2)):
            Middle=int((Lower+Upper)/2)
        
            if word == dictionary[Middle]:
                InDict+=1
            elif word < dictionary[Middle]:
                Upper=Middle-1
            else:
                Lower=Middle+1

        print(f"Number of words not found in dictionary: {len(aliceWords)-InDict}. {time.time()-Start} seconds")

