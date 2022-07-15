"""
title: Data Managment Assignment
author: Jonah Rodrigo
date-created: July 7, 2022
"""

import json

def Menu():
    User=int(input("""
1. Display all books
2. Display favorites
3. Find books of certain genre
4. Sort by alphabetical order
5. Add a book to favorites
6. Remove a book from favorites
7. Exit

> """))

    print("\n")

    return User

File=open("Books.txt","r")
Data=File.read()
File.close()

Data=json.loads(Data)

def displayBooks(Data):
    print("Books:")

    for book in Data['books']:
        Info=list(book.values())
        
        genres=""
        
        for chara in str(Info[3]):
            if chara != "'" and chara != "[" and  chara != "]":
                genres+=chara

        print(f"""
name: {Info[0]}
author: {Info[1]}
date published: {Info[2]}
genre: {genres}
sequels: {Info[4]}
favorite: {Info[5]}""")

def addFavorites(Data):
    
    print("Book titles: ")
    title=[]
    
    for book in Data['books']:
        title.append(book['title'])
        if list(book.values())[5]==False:
            print("-",book["title"])

    favorite=input("\nWhich book would you like to add to your favorites?: ")

    for name in range(len(title)):
        if favorite==title[name]:
            Data['books'][name]['favorite']=True
    
    File=open("Books.txt","w")
    File.write(json.dumps(Data))
    File.close()
    
def displayFavs(Data):
    print("Favorite Books:")

    for book in Data['books']:
        if book["favorite"]==True:  
            Info=list(book.values())
            
            genres=""
            
            for chara in str(Info[3]):
                if chara != "'" and chara != "[" and  chara != "]":
                    genres+=chara

            print(f"""
name: {Info[0]}
author: {Info[1]}
date published: {Info[2]}
genre: {genres}
sequels: {Info[4]}
favorite: {Info[5]}""")

def removeFavorites(Data):
    print("Book titles: ")
    title=[]
    
    for book in Data['books']:
        title.append(book['title'])
        if list(book.values())[5]==True:
            print("-",book["title"])

    favorite=input("\nWhich book would you like to remove to your favorites?: ")

    for name in range(len(title)):
        if favorite==title[name]:
            Data['books'][name]['favorite']=False
    
    File=open("Books.txt","w")
    File.write(json.dumps(Data))
    File.close()

def sortGenre(Data):
    genres=""
    
    for book in Data['books']:
        Info=list(book.values())
        
        for chara in str(Info[3]):
            if chara != "'" and  chara != "]":
                genres+=chara
    
    genres=", ".join(set((", ".join((genres.removeprefix("[")).split("["))).split(", ")))

    print("Choose a genre:")
    print(genres)
    User=input("> ")
    
    print(f"{User} Books:")

    for book in Data['books']:
        for genre in book["genre"]:
            if genre==User:
                Info=list(book.values())
                
                genres=""
                
                for chara in str(Info[3]):
                    if chara != "'" and chara != "[" and  chara != "]":
                        genres+=chara

                print(f"""
name: {Info[0]}
author: {Info[1]}
date published: {Info[2]}
genre: {genres}
sequels: {Info[4]}
favorite: {Info[5]}""")

def sortAlpha(Data):
    print("Books in alphabetical order:")
    
    title=[]

    for book in Data['books']:  
        title.append(book["title"])
    
    unsorted=[]
    for item in title:
        unsorted.append(item)
    
    title.sort()

    for sorted in range(len(title)):
        for i in range(len(unsorted)):
            if title[sorted]==unsorted[i]:
                title[sorted]=i
    
    for name in title:
        Info=list(Data['books'][name].values())

        genres=""
        
        for chara in str(Info[3]):
            if chara != "'" and chara != "[" and  chara != "]":
                genres+=chara

        print(f"""
name: {Info[0]}
author: {Info[1]}
date published: {Info[2]}
genre: {genres}
sequels: {Info[4]}
favorite: {Info[5]}""")

while True:
    Choice=Menu()

    if Choice == 1:
        displayBooks(Data)
    if Choice == 2:
        displayFavs(Data)
    if Choice == 3:
        sortGenre(Data)
    if Choice == 4:
        sortAlpha(Data)
    if Choice == 5:
        addFavorites(Data)
    if Choice == 6:
        removeFavorites(Data)
    if Choice == 7:
        break
