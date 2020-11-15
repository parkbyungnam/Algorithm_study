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