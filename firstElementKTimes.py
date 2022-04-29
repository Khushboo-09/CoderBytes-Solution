from collections import defaultdict

def firstElementKTimes(a,n,k):
    dict = defaultdict(int)
    for i in a:
        dict[i] +=1            
        if dict[i]==k:
            return i
    return -1

a = [1, 7, 4, 3, 4, 8, 7]
n=7
k=2
print("First element to occur",k,"times is:",firstElementKTimes(a,n,k))