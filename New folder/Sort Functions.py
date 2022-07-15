nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def bubbleSort(anArray):
    for d in range(1,anArray.__len__()):    
        for i in range(anArray.__len__()-d):
            Value1=anArray[i]
            Value2=anArray[i+1]
            if anArray[i]>anArray[i+1]:
                anArray[i]=Value2
                anArray[i+1]=Value1

# print(nums)
# bubbleSort(nums)
# print(nums)

def selectionSort(anArray):
    for d in range(len(anArray)-1):
        minPosition=d
        for i in range(d,len(anArray)):
            if anArray[i]<anArray[minPosition]:
                minPosition=i
        Value1=anArray[minPosition]
        Value2=anArray[d]
        anArray[d]=Value1
        anArray[minPosition]=Value2

# print(nums)
# selectionSort(nums)
# print(nums)

# def insertSort(anArray):
#     OtherArray=[anArray.pop(0)]

#     for i in range(anArray.__len__()):
#         insertValue=anArray[i]
#         insertPosition=OtherArray.__len__()

#         for i in range(OtherArray.__len__()):
#             if insertValue<OtherArray[i]:
#                 insertPosition-=1
            
#         OtherArray.insert(insertPosition,anArray[i])
    
#     anArray.append(0)
#     for i in range(anArray.__len__()):
#         anArray[i]=OtherArray[i]

def insertionSort(anArray):
    for i in range(1,len(anArray)):
        insertValue=anArray[i]
        insertPos=i
        while insertPos>0 and anArray[insertPos-1]>insertValue:
            anArray[insertPos]=anArray[insertPos-1]
            insertPos-=1
        
        anArray[insertPos]=insertValue


print(nums)
insertionSort(nums)
print(nums)
