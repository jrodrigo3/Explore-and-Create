# Nickname Generator
"""
title: Nickname Generator Assignment
author: Jonah Rodrigo
date-made: July 4, 2022
"""

# Imports
from random import randint

# Variables
Name=["John","Doe"]
NickNames=["Crusher","the Scientist","Twinkle-toes","the Coder","the Jester","the Sloth","Quick-Silver", "Big Ben"]

# Inputs
def Menu():
    """Shows the options to be chosen in the program
    """
    
    Choice=int(input(f"""MAIN MENU ({Name[0]} {Name[1]})
1. Change Name
2. Display a Random Nickname
3. Display All Nicknames
4. Add a Nickname
5. Remove a Nickname
6. Exit
    
>   """))

    return Choice

# Processes
def ChangeName(Name):
    """Changes the base name to have a nickname attached to it
    """

    FirstName=input("First name: ")
    LastName=input("Last name: ")
    Name=[FirstName,LastName]
    
    print(f"Current name is {FirstName} {LastName}")

    return Name

def AddNickname(NickNames):
    """Adds a Nickname of the users choice to the list of possible nicknames
    """

    newNickname=input("Please enter a nickname to add: ")
    try:
        NickNames.index(newNickname)
        print(f"{newNickname} is already in the nickname list")
    except:
        NickNames+=newNickname
        print(f"{newNickname} added to nickname list")


def DeleteNickname(NickNames):
    """Removes a Nickname of the users choice out of the list of possible nicknames
    """

    Nickname=input("Please enter a nickname to remove: ")
    try:
        NickNames.remove(Nickname)
        print(f"{Nickname} removed from the nickname list")
    except:
        print(f"{Nickname} is not in the nickname list")

# Outputs
def AllNicknames():
    """prints all nicknames in the nickname list with the base name
    """
    print("All Nicknames")

    for i in NickNames:
        print(f'{Name[0]} "{i}" {Name[1]}')

def DisplayRandom():
    """Displays the name with one random nickname
    """
    print(f'{Name[0]} "{NickNames[randint(0,NickNames.__len__())]}" {Name[1]}')

while True:
    print("\n")
    Choice=Menu()

    if Choice==1:
        Name=ChangeName(Name)
    elif Choice==2:
        DisplayRandom()
    elif Choice==3:
        AllNicknames()
    elif Choice==4:
        NickNames=AddNickname(NickNames)
    elif Choice==5:
        NickNames=DeleteNickname(NickNames)
    elif Choice==6:
        break
