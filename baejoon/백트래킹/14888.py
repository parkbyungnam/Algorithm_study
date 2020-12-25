from itertools import permutations

N = int(input())
numList = list(map(int,input().split()))
operatorCount = list(map(int,input().split()))
operatorList = []
myMax = -1000000000
myMin = 1000000000


for idx, count in enumerate(operatorCount):
    if idx==0:
        temp = ["+"]*count
        operatorList+=temp
    elif idx==1:
        temp = ["-"]*count
        operatorList+=temp
    elif idx==2:
        temp = ["*"]*count
        operatorList+=temp
    elif idx==3:
        temp = ["//"]*count
        operatorList+=temp

myOperator = set(permutations(operatorList,N-1))
for operator in myOperator:
    numList2 = numList.copy()
    for oper in operator:
        a=numList2.pop(0)
        b=numList2.pop(0)
        if oper=='+':
            temp=a+b
        elif oper=='-':
            temp=a-b
        elif oper=='*':
            temp=a*b
        elif oper=='//':
            temp=int(a/b)
        numList2.insert(0,temp)
    temp = numList2.pop()
    myMin=min(myMin,temp)
    myMax=max(myMax,temp)

print(myMax)
print(myMin)