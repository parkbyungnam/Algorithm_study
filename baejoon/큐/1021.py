from collections import deque

deq = deque()
N,M = map(int,input().split())
inputList = list(map(int,input().split()))

for i in range(1,N+1):
    deq.append(i)

mycount = 0

for i in range(M):
    location = deq.index(inputList[i])
    center = len(deq)//2
    while deq[0]!=inputList[i]:
        if location<=center:
            mycount+=1
            deq.append(deq.popleft())
        elif location>center:
            mycount+=1
            deq.appendleft(deq.pop())
    deq.popleft()

print(mycount)


#타인 코드

N, M = map(int, input().split())
Q = [i for i in range(1, N+1)]

ans = 0

for target in list(map(int, input().split())):
    p = Q.index(target)
    ans += min(p, len(Q) - p)
    Q = Q[(p+1):] + Q[:p]

print(ans)

