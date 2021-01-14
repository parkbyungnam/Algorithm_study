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


#타인 코드
from sys import stdin as st
def nQ(a,b,c):
    ks=iter(sorted(list(set(b)),reverse=True))
    oQ,curI,lastI,frstI=0,0,-1,0
    while True:
        if frstI==curI:
            curK=next(ks)
            curI=(lastI+1)%c
            frstI=curI
        if b[curI]==curK:
            oQ+=1
            lastI=curI
            if curI==a:
                return oQ
        curI+=1
        curI%=c
caseN=int(st.readline())
for i in range(caseN):
    N, Loc=map(int,st.readline().split())
    que=list(map(int,st.readline().split()))
    print(nQ(Loc,que,N))