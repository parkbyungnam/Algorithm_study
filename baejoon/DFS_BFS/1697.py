#다시 풀어보기
from collections import deque

n,k = map(int,input().split())

def dfs():
    visited = [0]*100001 #방문했는지 확인
    dx = [-1,1,0]
    dy = [1,1,2]
    queue = deque([n])
    if n==k:
        return 0
    while not visited[k] and queue:
        move = queue.popleft()
        for i in range(3):
            if 0<=move<100001:
                next_move = move*dy[i] + dx[i]
                if 0<=next_move<100001 and not visited[next_move]:
                    visited[next_move] = visited[move] + 1
                    queue.append(next_move)
    return visited[k]

print(dfs())


#------------------------------------------------------------#

from collections import deque
N, K = map(int,input().split())
limited = 100001
dx = [-1,1,0]
ddx = [1,1,2]

def bfs():
    queue = deque()
    visited = [0] * limited
    queue.append(N)
    while True:
        x = queue.popleft()
        if x == K:
            return visited[x]
        for i in range(3):
            nx = x*ddx[i] + dx[i]
            if nx >= 0 and nx < limited and visited[nx] == False:
                visited[nx] = visited[x] + 1
                queue.append(nx)

print(bfs())

#타인 풀이

def c(n,k):
    if n>=k:
        return n-k
    elif k == 1:
        return 1
    elif k%2:
        return 1+min(c(n,k-1),c(n,k+1))
    else:
        return min(k-n, 1+c(n,k//2))
    
n, k = map(int,input().split())
print(c(n,k))