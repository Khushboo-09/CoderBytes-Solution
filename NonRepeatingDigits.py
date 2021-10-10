a = int(input())
b = int(input())
count = 0
for i in range(a,b+1):
    s = str(i)
    l = [j for j in s]
    S = set(l)
    if len(l)==len(S):
        count += 1
print(count)
