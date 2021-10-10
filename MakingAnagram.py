from collections import Counter

def MakeAnagram(a,b):
    dict1 = Counter(a)
    dict2 = Counter(b)

    keys1 = dict1.keys()
    keys2 = dict2.keys()

    count1 = len(keys1)
    count2 = len(keys2)

    set1 = set(keys1)
    print(set1)
    print(set(keys2))
    commonkeys = len(set1.intersection(keys2))
    print(commonkeys)
    if commonkeys == 0:
        return count1+count2
    else:
        return (max(count1,count2)-commonkeys)

print(MakeAnagram('cde','abc'))
