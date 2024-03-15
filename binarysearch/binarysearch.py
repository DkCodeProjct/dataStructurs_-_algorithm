def binarySearchAlgo(arry, targt):
    
    leftPointer = 0
    rightPointer = len(arry) - 1
    while leftPointer <= rightPointer: 
        mid = round((leftPointer + rightPointer) / 2)
        if arry[mid] == targt:
            return mid
        elif targt < arry[mid]:
            rightPointer = mid - 1
        else:
            leftPointer = mid + 1
    return - 1

array = [1,33,4,2,6,8,9,32,4,3]
         #Left.Pointer->     #Right.Pointer<-
array.sort()
target = 4

print(binarySearchAlgo(array, target))