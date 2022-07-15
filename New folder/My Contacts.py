# My Contacts
"""
title: My Contacts assignment
author: Jonah Rodrigo
date-created: July 5, 2022
"""

fileName='My Contacts.txt'

def Menu():
    User=int(input("""
1. Display Contact Names
2. Search for Contact
3. Edit Contact
4. New Contact
5. Remove Contact
6. Exit 

> """))

    return User

def DisplayContact():
    for i in Contacts:
        print(i[0]+" "+i[1]+" "+i[2])

def FindContact(Mode):
    """Finds the contact in the array of contacts then returns either the contact and the index value or returns a message if no contacts are found
    """

    CTF=input("What is the first and last name of the person you are trying to find?: ")
    FoundContact=-1
    for i in range(Contacts.__len__()):
        if Contacts[i][0]==CTF:
            FoundContact=i

    if Mode==0:
        if FoundContact!=-1:
            print(Contacts[FoundContact][0]+", "+Contacts[FoundContact][1]+", "+Contacts[FoundContact][2]+"; This contact is found at position "+FoundContact)
        else:
            print("No Contact was found with that name")
    
    if Mode==1 and FoundContact==-1:
        print("No Contact was found with that name")

    return FoundContact


def EditContact():
    """Asks the user for the name of the contact then has the user replace the contact information or leave it
    """

    FoundContact=FindContact(1)

    if FoundContact==-1:
        return
    
    print("(leave blank if you do not want to change)")
    NName=input("New Name: ")
    NPhone=input("New Phone Number: ")
    NEmail=input("New Email: ")

    if NName=="":
        Contacts[FoundContact][0]=Contacts[FoundContact][0]
    else:
        Contacts[FoundContact][0]=NName
    
    if NPhone=="":
        Contacts[FoundContact][1]=Contacts[FoundContact][1]
    else:
        Contacts[FoundContact][1]=NPhone
    
    if NEmail=="":
        Contacts[FoundContact][2]=Contacts[FoundContact][2]
    else:
        Contacts[FoundContact][2]=NEmail

def NewContact():
    """Asks the user for all the information in a contact then appends the contact to the contacts list
    """

    Name=input("Name of person: ")
    Phone=input("Phone Number: ")
    Email=input("Email: ")

    Contacts.append([Name,Phone,Email])
    

def RemoveContact():
    """Asks for contacts name then removes it from the list
    """

    FoundContact=FindContact(1)

    if FoundContact==-1:
        return
    else:
        Contacts.pop(FoundContact)


while True:
    file=open(fileName,"r")
    Contacts=file.readlines()
    file.close()
    for line in range(len(Contacts)):
        Contacts[line]=Contacts[line].strip("\n")
        Contacts[line]=Contacts[line].split(", ")

    Choice=Menu()

    if Choice==1:
        DisplayContact()
    if Choice==2:
        FindContact()
    if Choice==3:
        EditContact()
    if Choice==4:
        NewContact()
    if Choice==5:
        RemoveContact()
    if Choice==6:
        break

    file=open(fileName,"w")
    for line in range(len(Contacts)):
        Contacts[line]=", ".join(Contacts[line])
        Contacts[line]+="\n"
    file.writelines(Contacts)
    file.close()