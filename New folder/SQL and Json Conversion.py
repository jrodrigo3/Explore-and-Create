import sqlite3
import os
import json

os.chdir("SQLFolder")
connection = sqlite3.connect("DataFile.db")
cursor = connection.cursor()

class Heros():
    def __init__(self, name, realName, debuteDate, comicDebute, mainAbilities):
        self.name=name
        self.realName=realName
        self.debuteDate=debuteDate
        self.comicDebute=comicDebute
        self.mainAbilities=mainAbilities
    
    def ListOfValues(self):
        return [self.name, self.realName, self.debuteDate, self.comicDebute, self.mainAbilities]
    
    def AbilitiesString(self):
        Abilities=""
        print(self.mainAbilities)
        for Ability in range(len(self.mainAbilities)):
            if Ability!=len(self.mainAbilities)-1:
                Abilities+=(self.mainAbilities[Ability])+", "
            else:
                Abilities+=(self.mainAbilities[Ability])
        
        return Abilities

def Menu(Mode):
    """Displays the choices that can be made in the program

    Args:
        Mode (str): determines the possible selectable options
    """    

    if Mode == 1:
        User=int(input("""
1. Display Heros
2. Edit Heros
3. Add Heros
4. Delete Heros
5. Copy SQL Data to JSON
6. Change Mode to JSON
7. Exit
> """))

    elif Mode == 2:
        User=int(input("""
1. Display Heros
2. Edit Heros
3. Add Heros
4. Delete Heros
5. Copy JSON Data to SQL
6. Change Mode to SQL
7. Exit
> """))

    return User

def JSONToHeros():
    """Gathers the JSON data, converts it into Hero objects, and returns the Herolist

    Returns:
        list: List of Hero objects
    """    

    JFile=open("DataFile.json","r")
    JData=json.load(JFile)
    JFile.close()

    HeroList=[]
    Data=JData["Data"]
    for Dictionary in Data:
        items=list(Dictionary.values())
        HeroList.append(Heros(items[0],items[1],items[2],items[3],items[4]))
    
    return HeroList

def HerosToJSON(HeroList):
    """Adds in the new data from the opertations to JSON

    Args:
        HeroList (list): list of hero objects within data
    """

    TempList=[]
    for Hero in HeroList:
        TempList.append({"Hero Name":Hero.name,"Real Name":Hero.realName,"Date of Debute":Hero.debuteDate,"Comic Debuted in":Hero.comicDebute,"Main Abilities":Hero.mainAbilities})

    JFile=open("DataFile.json","w")
    json.dump({"Data":TempList},JFile)
    JFile.close()

def SQLToHeros():
    """Gathers the JSON data, converts it into Hero objects, and returns the Herolist

    Returns:
        list: List of Hero objects
    """    

    HeroList=[]
    for Hero in cursor.execute("select * from Data"):
        HeroList.append(Heros(Hero[0],Hero[1],Hero[2],Hero[3],Hero[4]))
    
    return HeroList

def HerosToSQL(HeroList):
    """Adds in the new data from the opertations to SQL database

    Args:
        HeroList (list): list of hero objects within data
    """

    for Hero in HeroList:
        cursor.execute("UPDATE Data SET realName = ?, debuteDate=?, comicDebute=?, mainAbilities=? WHERE HeroName = ?", (Hero.realName, Hero.debuteDate, Hero.comicDebute, Hero.mainAbilities, Hero.name))
    
    connection.commit()

def DisplayHero(HeroList, Mode):
    """Displays all heros collected in the data

    Args:
        HeroList (list): list of hero objects within data
        Mode (str): communicates whether the data is SQL or JSON
    """    
    
    for Hero in range(len(HeroList)):
        items=HeroList[Hero].ListOfValues()
        
        if Mode=="JSON":
            Abilities=HeroList[Hero].AbilitiesString()
        else:
            Abilities=HeroList[Hero].mainAbilities
        
        print(f"""
{items[1]} a.k.a. {items[0]}
Debuted in {items[3]} in {items[2]}
Main abilities: {Abilities}""")

def EditHero(HeroList, Mode):
    """Changes one of the heros in the data

    Args:
        HeroList (list): list of hero objects within data
        Mode (str): communicates whether the data is SQL or JSON
    """    

    for Hero in range(len(HeroList)):
        print(f"{Hero+1}. {HeroList[Hero].name}")
    
    HeroEdit=int(input("> "))-1

    if Mode=="JSON":
        Abilities=HeroList[HeroEdit].AbliltiesString()
    else:
        Abilities=HeroList[HeroEdit].mainAbilities

    EditInfo=int(input(f"""
{HeroList[HeroEdit].name}:
1. {HeroList[HeroEdit].realName}
2. {HeroList[HeroEdit].comicDebute}
3. {HeroList[HeroEdit].debuteDate}
4. {Abilities}
> """))
    
    Edit=input("What would you like to change it to?: ")

    if EditInfo==1:
        HeroList[HeroEdit].realName=Edit
    elif EditInfo==2:
        HeroList[HeroEdit].comicDebute=Edit
    elif EditInfo==3:
        HeroList[HeroEdit].debuteDate=Edit
    elif EditInfo==4:
        Abilities=Edit
        if Mode=="JSON":
            HeroList[HeroEdit].mainAbilities=Abilities.split(", ")
        else:
            HeroList[HeroEdit].mainAbilities=Abilities
    
    return HeroList

def AddHero(HeroList, Mode):
    """Adds a hero to the heros list

    Args:
        HeroList (list): list of hero objects within data
        Mode (str): communicates whether the data is SQL or JSON
    """    

    name=input("Hero Name: ")
    realName=input("Real Name: ")
    debutDate=input("Debut Date: ")
    comicDebute=input("Comic Debuted: ")
    mainAbilities=input("Main Abilities: ")

    HeroList.append(Heros(name, realName, debutDate, comicDebute, mainAbilities))

    if Mode=="SQL":
        cursor.execute("INSERT INTO Data VALUES (?, ?, ?, ?, ?)", (name, realName, debutDate, comicDebute, mainAbilities))

def DeleteHero(HeroList, Mode):
    """Removes a hero from the hero list

    Args:
        HeroList (list): list of hero objects within data
        Mode (str): communicates whether the data is SQL or JSON
    """

    print("Which Hero would you like to delete")

    for Hero in range(len(HeroList)):
        print(f"{Hero+1}. {HeroList[Hero].name}")
    
    HeroDelete=int(input("> "))-1

    if Mode=="SQL":
        cursor.execute("DELETE from Data WHERE heroName=?",([HeroList[HeroDelete].name]))
    
    HeroList.pop(HeroDelete)

def CopyTo(HeroList, Mode):
    """Will copy one of the heros to the other data set

    Args:
        HeroList (list): list of hero objects within data
        Mode (str): communicates whether the data is SQL or JSON
    """    

    if Mode=="SQL":
        print("What Hero would you like to copy to JSON?")

        for Hero in range(len(HeroList)):
            print(f"{Hero+1}. {HeroList[Hero].name}")
        
        Copy=int(input("> "))-1

        JFile=open("DataFile.json","r")
        JData=json.load(JFile)
        JFile.close()

        JHeroList=JData["Data"]
        JHeroList.append({"Hero Name":HeroList[Copy].name,"Real Name":HeroList[Copy].realName,"Date of Debute":HeroList[Copy].debuteDate,"Comic Debuted in":HeroList[Copy].comicDebute,"Main Abilities":HeroList[Copy].mainAbilities})

        JFile=open("DataFile.json","w")
        JData=json.dump({"Data":JHeroList}, JFile)
        JFile.close()
    
    elif Mode=="JSON":
        print("What Hero would you like to copy to SQL?")

        for Hero in range(len(HeroList)):
            print(f"{Hero+1}. {HeroList[Hero].name}")
        
        Copy=int(input("> "))-1

        cursor.execute("INSERT INTO Data VALUES (?, ?, ?, ?, ?)", (HeroList[Copy].name, HeroList[Copy].realName, HeroList[Copy].debuteDate, HeroList[Copy].comicDebute, HeroList[Copy].AbilitiesString()))
    
        connection.commit()

FirstRun=1

while True:
    if FirstRun==1:
        Mode=int(input("Use SQL file (1) or JSON file (2)?: "))
        FirstRun=0

    if Mode==2:
        User=Menu(Mode)

        HeroList=JSONToHeros()

        if User == 1:
            DisplayHero(HeroList, "SQL")
        elif User == 2:
            HeroList=EditHero(HeroList, "SQL")
        elif User == 3:
            AddHero(HeroList, "SQL")
        elif User == 4:
            DeleteHero(HeroList, "SQL")
        elif User == 5:
            CopyTo(HeroList, "SQL")
        elif User == 6:
            Mode=int(input("Use SQL file (1) or JSON file (2)?: "))
        elif User == 7:
            break

        HerosToJSON(HeroList)
    
    elif Mode==1:
        User=Menu(Mode)

        HeroList=SQLToHeros()

        if User == 1:
            DisplayHero(HeroList, "SQL")
        elif User == 2:
            HeroList=EditHero(HeroList, "SQL")
        elif User == 3:
            AddHero(HeroList, "SQL")
        elif User == 4:
            DeleteHero(HeroList, "SQL")
        elif User == 5:
            CopyTo(HeroList, "SQL")
        elif User == 6:
            Mode=int(input("Use SQL file (1) or JSON file (2)?: "))
        elif User == 7:
            break

        HerosToSQL(HeroList)
    

connection.close()