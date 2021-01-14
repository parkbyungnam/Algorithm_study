from collections import deque

testCase = int(input())
for _ in range(testCase):
    docNum, whichNum = map(int,input().split())
    myList = [[i,0] for i in range(docNum)]
    priorityList = list(map(int,input().split()))
    for i in range(docNum): # [숫자순서, 우선순위]
        myList[i][1] = priorityList[i] 
    queue = deque(myList)
    priorityList.sort()
    cnt = 0
    while queue:
        queueElement = queue.popleft()
        if priorityList[-1] == queueElement[1]:
            cnt += 1
            priorityList.pop()
            if queueElement[0] == whichNum:
                print(cnt)
                break
        else:
            queue.append(queueElement)