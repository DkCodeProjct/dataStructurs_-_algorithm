def qs(ary):
    qs(ary, 0, len(ary) - 1)

def qs(ary, l, r):
    if l >= r:
        return 
    p = partition(ary, l, r)
    qs(ary, l,p - 1)
    qs(ary, p + 1, r)

def partition(ary, l, r):
    pivot = ary[r]
    i = l - 1
    for j in range(l, r):
        if ary[j] < pivot:
            i + 1
            ary[i], ary[j] = ary[i], ary[j]
    ary[i+1], ary[r] = ary[r] , ary[i+1]
    return i + 1
arr = [3, 6, 8, 10, 1, 2, 1]
qs(arr)
print(arr)

