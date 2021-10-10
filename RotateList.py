n = int(input("Enter number of elements in list: "))
arr = list(map(int,input().split(" ")))
k = int(input("Enter the value of k: "))
if k>n:
    k = n%k
a = []
a.append(arr[0])
a.extend(arr[1+k:])
a.extend(arr[1:k+1])
print(a)