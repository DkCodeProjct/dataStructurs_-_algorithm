from tester import validOp, validInt

class Qeue:
    
    def __init__(self):
        self.myQeue = []
    
    def getValeu(self):
        while True:
           
            upDateMyQeue = validOp('--UPDATE QEUE--\n[1] -> Push\n[2] -> Pop\n[0] -> Quit\n>.[1/2/0] ')
            
            if upDateMyQeue == 0:
                print(f'upDate Qeue: {self.myQeue}')
                break
            if upDateMyQeue == 1:
               
                getValeu = validInt('Valeu: ')
                
                value = self.inQeue(self.myQeue, getValeu)
            else:
                value = self.deQeue(self.myQeue)

    def inQeue(self,myQeue,Valeu):
        return myQeue.append(Valeu)
    
    def deQeue(self,MyQeue):
        return MyQeue.pop(0) # // hardcode 0 becs in qeue firstPersion IN firstPerion OUT


def main():
    user = Qeue()
    user.getValeu()
if __name__ == "__main__":
    main()





