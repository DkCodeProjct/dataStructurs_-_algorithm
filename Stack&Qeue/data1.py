myQeue = []
def push(myQeue, value):
    return myQeue.append(value)
def pop(myQeue):
    return myQeue.pop(0)

push(myQeue, 'a')
push(myQeue, 'b')
push(myQeue, 'c')
pop(myQeue)
print(myQeue)
