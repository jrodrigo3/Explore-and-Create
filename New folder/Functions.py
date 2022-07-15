# Functions
"""
title: Functions Assignment
author: Jonah Rodrigo
date-created: July 4, 2022
"""

TheList=[2,4,6,8,10]

# contains
def contains(aList, item):
    for i in range(len(aList)):
        if aList[i]==item:
            print(f"{item} is in the list")
            return True
    print(f"{item} is not in the list")
    return False

# indexOf
def indexOf(aList, item):
    for i in range(len(aList)):
        if aList[i]==item:
            return i
    return -1

# Reverse
def reverse(aList):
    return aList[::-1]

# Swap
def swap(aList, index1, index2):
    Value=aList[index1]

    aList[index1]=aList[index2]
    aList[index2]=Value

    return aList

#indexOfMin
def indexOfMin(aList):
    for i in range(len(aList)):
        if aList[0]>aList[i]:
            Lowest=i
    
    return Lowest

print(TheList)
contains(TheList,4)
print(indexOf(TheList,6))
print(reverse(TheList))
print(swap(TheList,0,4))
print(indexOfMin(TheList))