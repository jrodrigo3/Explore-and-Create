"""
title: Character Class assignment
author: Jonah Rodrigo
date created: July 13, 2022
"""

class Character:
    def __init__(self, name, phrase1, phrase2, level):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0
    
    def speak(self,phraseNum):
        if phraseNum==1:
            print(self.phrase1)
        elif phraseNum==2:
            print(self.phrase2)
        else:
            print("Invalid number has been submited")
        
    def setLevel(self, newLevel):
        oldLevel=self.level
        self.level=newLevel
        print(f"{self.name} has went from level {oldLevel} to level {self.level}")


Ben=Character("Talking Ben","Yes","Hohoho Ben",0)

Ben.speak(1)
Ben.setLevel(2)
Ben.speak(2)