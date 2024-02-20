mystack = []
def push(mystack, value):
    return mystack.append(value)
def pop(mystack):
    return mystack.pop()

push(mystack, 'a')
push(mystack, 'b')
push(mystack, 'c')
pop(mystack)
pop(mystack)
print(mystack)