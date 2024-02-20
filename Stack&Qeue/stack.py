from tester import validOp, validInt

class Satck:
    def __init__(self):
        self.mySatck = []
    
    def upDateStack(self):
        while True:
            getOp = validOp('--UPDATE STACK--\n[1] -> Push\n[2] -> Pop\n[0] -> Quit\n>.[1/2/0] ')

            if getOp == 0:
                print('mystack ',self.mySatck)
            
                break
            if getOp == 1:
                getValeu = validInt('valeu ')
                valeu = self.pushStack(self.mySatck, getValeu)
            
            else:
                valeu = self.popStack(self.mySatck)
    
    def pushStack(self,myStack,valeu):
        return myStack.append(valeu)
    
    def popStack(self, myStack):
        return myStack.pop()
    
def main():
    mystack = Satck()
    mystack.upDateStack()

if __name__ == "__main__":
    main()