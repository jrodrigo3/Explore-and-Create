nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]

def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if anArray[i]==item:
            return i
    return -1

print(linearSearch(nums,100))
print(linearSearch(nums,75))
print(linearSearch(words,"fish"))
print(linearSearch(words,"at"))
print(linearSearch(unsorted,70))

print("\n")

def binarySearch(anArray, item):
    Upper=len(anArray)-1
    Lower=0

    while Upper-Lower>-1:
        Middle=(Lower+Upper)//2
        
        if item == anArray[Middle]:
            return Middle
        elif item < anArray[Middle]:
            Upper=Middle-1
        else:
            Lower=Middle+1
    return -1

print(binarySearch(nums,100))
print(binarySearch(nums,75))
print(binarySearch(words,"fish"))
print(binarySearch(words,"at"))
print(binarySearch(unsorted,70))