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



#타인풀이

def dfs(cal, idx, plus, minus, multiple, division):
    global max_num, min_num
    if idx == N:
        if max_num < cal:
            max_num = cal
        if min_num > cal:
            min_num = cal
        return
    else:
        if plus != 0:
            dfs(cal + arr[idx], idx + 1, plus - 1, minus, multiple, division)
        if minus != 0:
            dfs(cal - arr[idx], idx + 1, plus, minus - 1, multiple, division)
        if multiple != 0:
            dfs(cal * arr[idx], idx + 1, plus, minus, multiple - 1, division)
        if division != 0:
            # dfs(cal // arr[idx], idx + 1, plus, minus, multiple, division - 1)
            dfs(int(cal / arr[idx]), idx + 1, plus, minus, multiple, division - 1)


N = int(input())
arr = list(map(int, input().split()))
plus, minus, multiple, division = list(map(int, input().split()))
result = []
max_num = -1000000000
min_num = 1000000000

dfs(arr[0], 1, plus, minus, multiple, division)

print(max_num)
print(min_num)

