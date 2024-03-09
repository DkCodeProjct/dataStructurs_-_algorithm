array2D = [
    [0,2,4,7],
    [5,9,3,1],
    [2,8,3,9]
]

def sumArrayElement(array):
    sum = 0
    for k in array:
        for j in k:
            sum += j
    return sum
            
output = sumArrayElement(array2D)
print(f"sum {output}")