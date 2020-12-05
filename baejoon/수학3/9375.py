for _ in range(int(input())):
    myDict = dict()
    for _ in range(int(input())):
        value,key = input().split()
        if key not in myDict:
            myDict[key] = 1
        else:
            myDict[key]+=1
    mylist = list(myDict.values())
    mylist = list(map(lambda x: x+1,mylist))
    result = 1
    for my in mylist:
        result *= my
    print(result-1)