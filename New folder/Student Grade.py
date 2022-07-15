# Student Grade
"""
title: Student Grade assignment
author: Jonah Rodrigo
date-created: July 4, 2022
"""

from random import randint

# Variables

StudentGrades=[]
for i in range(35):
    StudentGrades.append(randint(0,100))

# Inputs

def Menu():
    """displays options that can be chosen in the program
    """    

    UserInput=int(input("""
1. Display All Grades
2. Display Honours
3. Stats
4. Randomize Grades
5. Exit

> """))

    return UserInput

# Processes

def PrintHonors():
    """Prints all the grades above or equal to 80% then says the amount of students that have those honors
    """

    print("\nHonors")
    Honor=0

    for grade in StudentGrades:
        if grade>=80:
            print(f"{grade}%")
            Honor+=1
    
    print(f"Number of Honours: {Honor}")

def Stats():
    """Finds the highest and lowest grade and calculates the average of all the 35 students grades
    """

    print("\nStats")

    LowestGrade=StudentGrades[0]
    for i in StudentGrades:
        if LowestGrade>i:
            LowestGrade=i
    
    HighestGrade=StudentGrades[0]
    for i in StudentGrades:
        if HighestGrade<i:
            HighestGrade=i
    
    Average=0
    for i in StudentGrades:
        Average+=i
    Average=int(Average/35)

    print(f"Lowest Grade: {LowestGrade}")
    print(f"Highest Grade: {HighestGrade}")
    print(f"Average: {Average}")

def RandomizeGrades():
    """Remakes the StudentGrades variable to re-randomize 
    """

    global StudentGrades
    StudentGrades=[]
    for i in range(35):
        StudentGrades+=[randint(0,100)]
    print("GRADES HAVE BEEN RANDOMIZED")

# Outputs

def PrintGrades(): 
    """Prints all of the Grades in order of assignment
    """
    print("\nAll Grades")

    for i in StudentGrades:
        print(f"{i}%")


while True:
    Choice=Menu()

    if Choice==1:
        PrintGrades()
    elif Choice==2:
        PrintHonors()
    elif Choice==3:
        Stats()
    elif Choice==4:
        RandomizeGrades()
    elif Choice==5:
        break