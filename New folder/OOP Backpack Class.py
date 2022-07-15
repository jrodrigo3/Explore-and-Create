"""
title: Object Oriented Programming Backpack Class
author: Jonah Rodrigo
date-created: July 13, 2022
"""

class Backpack:
    def __init__(self, colour, size, items, open):
        self.colour=colour
        self.size=size
        self.items=[]
        self.open=False
    
    def openBag(self):
        self.open=True
        print("The bag is now open")
    
    def closeBag(self):
        self.open=False
        print("The bag is now closed")
    
    def putin(self,item):
        if self.open==True:
            self.items.append(item)
            print(f"{item} has been added to the bag")
        else:
            print("the bag is not open the item can not be put in")
        
    def takeout(self,item):
        if self.open==True:
            try:
                self.items.remove(item)
                print("The item has been removed from the bag")
            except:
                print("That item is not in the bag")
        
        else:
            print("the bag is not open the item can not be taken out of the bag")

smallBlue=Backpack("blue","small")
medRed=Backpack("red","medium")
largeGreen=Backpack("green","large")

medRed.openBag()
medRed.putin("lunch")
medRed.putin("jacket")
medRed.closeBag()

medRed.openBag()
medRed.takeout("jacket")
medRed.closeBag()