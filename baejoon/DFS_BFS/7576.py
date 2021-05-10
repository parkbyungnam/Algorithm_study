#ㄷㅏ시 풀어보기
from collections import deque

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)] #토마토 판 입력
visited = [[False]*m for _ in range(n)] #방문했는지, 방문x=F, 방문ㅇ=T
dx, dy = [1,-1,0,0], [0,0,-1,1]

def bfs():
    queue = deque()
    days = 0 #걸리는 기간
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1: #토마토 있는 공간이라면
                queue.append([i,j]) #큐에 추가
                visited[i][j]=True #토마토 있는 공간에는 방문할 필요가 없으므로
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m: #동서남북 범위 조건
                if not visited[nx][ny] and graph[nx][ny] == 0: #방문x,안익은토마토ㅇ
                    graph[nx][ny] = graph[x][y] + 1
                    visited[nx][ny] = True
                    queue.append([nx,ny])
    for gra in graph:
        for tomato in gra:
            if not tomato:
                return -1
            else:
                days = max(days,tomato)
    return days-1

print(bfs())

            
    

#------------------------------------------------------------------#
from collections import deque

M,N = map(int,input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

where_is_1=[]

for i,grap in enumerate(graph):
    for j,gra in enumerate(grap):
        if graph[i][j] == 1:
            where_is_1.append([i,j])

def bfs():
    global graph
    queue = deque()
    for where in where_is_1:
        queue.append((where[0],where[1]))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    max = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            elif graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                if graph[nx][ny] > max:
                    max = graph[nx][ny]
    temp = 0
    for gra in graph:
        if gra.count(0) >= 1:
            return -1
        elif gra.count(2) != 0:
            temp += 1
    if temp == 0:
        return 0
    return max-1

print(bfs())


#타인 소스

import sys
from collections import deque
input = sys.stdin.readline


def solve():
    m, n = map(int, input().split())
    tomato = []
    haveto = 0
    tmt = deque()
    for i in range(n):
        tomato.append(input().split())
        for j in range(m):
            if tomato[i][j] == '0':
                haveto += 1
            elif tomato[i][j] == '1':
                tmt.append((i, j))
    res = 0
    while tmt and haveto:
        l = len(tmt)
        for _ in range(l):
            x, y = tmt.popleft()
            if x > 0 and tomato[x-1][y] == '0':
                tomato[x-1][y] = 1
                tmt.append((x-1, y))
                haveto -= 1
            if y > 0 and tomato[x][y-1] == '0':
                tomato[x][y-1] = 1
                tmt.append((x, y-1))
                haveto -= 1
            if x < n-1 and tomato[x+1][y] == '0':
                tomato[x+1][y] = 1
                tmt.append((x+1, y))
                haveto -= 1
            if y < m-1 and tomato[x][y+1] == '0':
                tomato[x][y+1] = 1
                tmt.append((x, y+1))
                haveto -= 1
        res += 1
    if haveto:
        print(-1)
    else:
        print(res)


if __name__ == '__main__':
    solve()