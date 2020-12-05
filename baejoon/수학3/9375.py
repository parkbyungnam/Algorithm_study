import math

for _ in range(int(input())):
    myDict = dict()
    for _ in range(int(input())):
        value,key = input().split()
        if key not in myDict:
            myDict[key] = 1
        else:
            myDict[key]+=1
    a = len(myDict.keys())
    b = sum(list(myDict.values()))
    print(math.factorial(a)*math.factorial(b)-1)