# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("sort-analyzer-python-starter-main/data-files/random-values.txt")
reversedData = loadDataArray("sort-analyzer-python-starter-main/data-files/reversed-values.txt")
nearlySortedData = loadDataArray("sort-analyzer-python-starter-main/data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("sort-analyzer-python-starter-main/data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
print(randomData[0:50])
print(reversedData[0:50])
print(nearlySortedData[0:50])
print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# insertSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")

def bubbleSort(anArray):
    Start=time.time()

    for d in range(1,anArray.__len__()):    
        for i in range(anArray.__len__()-d):
            Value1=anArray[i]
            Value2=anArray[i+1]
            if anArray[i]>anArray[i+1]:
                anArray[i]=Value2
                anArray[i+1]=Value1

    Finish=time.time()
    print(f"{Finish-Start}s is the time it took to preform that calculation")

# bubbleSort(randomData)
# bubbleSort(reversedData)
# bubbleSort(nearlySortedData)
# bubbleSort(fewUniqueData)

def selectionSort(anArray):
    Start=time.time()

    for d in range(anArray.__len__()-1):
        minPosition=d
        for i in range(d, anArray.__len__()):
            if anArray[i]<anArray[minPosition]:
                minPosition=i
        Value1=anArray[minPosition]
        Value2=anArray[d]
        anArray[d]=Value1
        anArray[minPosition]=Value2

    Finish=time.time()
    print(f"{Finish-Start}s is the time it took to preform that calculation")

# selectionSort(randomData)
# selectionSort(reversedData)
# selectionSort(nearlySortedData)
# selectionSort(fewUniqueData)

def insertSort(anArray):
    Start=time.time()

    OtherArray=[anArray.pop(0)]

    for i in range(anArray.__len__()):
        insertValue=anArray[i]
        insertPosition=OtherArray.__len__()

        for i in range(OtherArray.__len__()):
            if insertValue<OtherArray[i]:
                insertPosition-=1
            
        OtherArray.insert(insertPosition,anArray[i])
    
    anArray.append(0)
    for i in range(anArray.__len__()):
        anArray[i]=OtherArray[i]
    
    Finish=time.time()
    print(f"{Finish-Start}s is the time it took to preform that calculation")

insertSort(randomData)
insertSort(reversedData)
insertSort(nearlySortedData)
insertSort(fewUniqueData)