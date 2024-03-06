
costomizeArray = []

print('Creat array: ->\n')
print('how many element do you need..')
getSizeOfArray = int(input('>'))
i = 1
print("Enter Valeus")
while i <= getSizeOfArray:
    
    getValues = int(input('>'))
    i = i + 1
    costomizeArray.append(getValues)
print("array: ",costomizeArray)

while True:
    print('play with array')

    print("0 - > Quit")               
    print('1 -> Check Element Index, 2 -> Update Element')
    print('3 -> Remove Elemel, 4 -> Get len of array')
    print('5 -> Sliced array')
    print('6 -> Sort, 7 -> Reverse')



    getPerform = int(input('>.'))
    if getPerform == 0:
        break
    
    elif getPerform == 1:
        getIndex = int(input("Index: "))
        index = costomizeArray.index(getIndex)
        print(f'{getIndex} Eliment: {index}')
    
    elif getPerform == 2:
        indexElement = int(input("Index OF update Eliment: "))
        getElement = int(input("Update elimen: "))
        costomizeArray[indexElement] = getElement
        print("Upadate array",costomizeArray)
    
    elif getPerform == 3:
        remove = int(input("Remove element: "))
        costomizeArray.remove(remove)
        print("Reomve", costomizeArray)
    
    elif getPerform == 4:
        length = len(costomizeArray)
        print(f"Length: {length}")
    
    elif getPerform == 5:
        index1 = int(input("index1: "))
        index2 = int(input("index2: "))
        sliced = costomizeArray[index1:index2]
        print(f'Sliced array: {sliced}')
    
    elif getPerform == 6:
        costomizeArray.sort()
        print(costomizeArray)
    
    else:
        revers = costomizeArray.reverse()
        print("reversed array: ",revers )
        
        
