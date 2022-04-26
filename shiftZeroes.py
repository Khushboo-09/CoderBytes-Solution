
# Method -1: With another list
x = [2,0,3,4,5,0,0,9,0,1]
j=0
l=[0]*(len(x))
for i in x:
    if i!=0:
        l[j] +=i
        j += 1
print(l)

# Method -2: Within same list
for t in x:
    if t==0:
        x.remove(t)
        x.append(0)
print(x)

