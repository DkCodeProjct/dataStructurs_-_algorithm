class quickSort:
    def __init__(self, ary):
        self.ary = ary
    
    def quicksort(self):
        self.qs(0, len(self.ary) - 1)
    
    def qs(self,l,r):
        if l >= r:
            return
        p = self.partition(l,r)
        self.qs(l, p - 1)
        self.qs(p + 1, r)
    
    def partition(self,l,r):
        pivot = self.ary[r]
        i = l - 1
        for j in range(l,r):
            if self.ary[j] < pivot:
                i += 1
                self.ary[j], self.ary[i] = self.ary[i], self.ary[j]
        self.ary[i + 1], self.ary[r] = self.ary[r], self.ary[i + 1]
        return i + 1



ary = [3,2,6,8,58,9]
qs = quickSort(ary)
qs.quicksort()
print(ary)