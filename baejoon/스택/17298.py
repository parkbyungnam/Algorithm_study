#O(n**2) 풀이방법 (당연히 시간초과)
lenList = int(input())
myList = list(map(int,input().split()))

for i in range(lenList):
    myNum = myList[i]
    tempList = myList[i:]
    result = -1
    while tempList:
        temp = tempList.pop(0)
        if temp > myNum:
            result = temp
    print(result, end=' ')

#

numbers = int(input())
num_list = list(map(int, input().split()))
stack = []
result = [-1 for _ in range(numbers)]

for i in range(numbers):
    try:
        while num_list[stack[-1]] < num_list[i]:
            result[stack.pop()] = num_list[i]
    except:
        pass
        
    stack.append(i)
        
for i in range(numbers):
    print(result[i], end = ' ')