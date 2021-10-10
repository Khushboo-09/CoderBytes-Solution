n = int(input("Enter number of elements: "))
y = int(input("Enter Limit: "))
arr = list(map(int,input().split()))
s = sum(arr)
arr.sort()
for i in range(n-2,n):
    if arr[i]>y:
        s = s - arr[i] + y
print(s)