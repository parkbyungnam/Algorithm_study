from collections import deque

M,N,H = map(int,input().split())

graph = []
where_is_1 = []

for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int,input().split())))
    graph.append(temp)

for i,grap in enumerate(graph):
    for n,gra in enumerate(grap):
        for d,gr in enumerate(gra):
            if gr==1:
                where_is_1.append([i,n,d])

def bfs():
    global graph
    queue = deque()
    for where in where_is_1:
        queue.append(where)
    days = 1
    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx<=-1 or ny <=-1 or nz <=-1 or nx>=H or ny>=N or nz>=M:
                continue
            elif graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = 1 + graph[x][y][z]
                days = max(days,graph[nx][ny][nz])
                queue.append([nx,ny,nz])
    for grap in graph:
        for gra in grap:
            if gra.count(0) != 0:
                return -1
    return days-1

print(bfs())


#타인 풀이
import sys
from collections import deque
input = sys.stdin.readline


def solve():
    m, n, h = map(int, input().split())
    tomato = [[] for _ in range(h)]
    haveto = 0
    tmt = deque()
    for k in range(h):
        for i in range(n):
            tomato[k].append(input().split())
            for j in range(m):
                if tomato[k][i][j] == '0':
                    haveto += 1
                elif tomato[k][i][j] == '1':
                    tmt.append((k, i, j))
    res = 0
    while tmt and haveto:
        l = len(tmt)
        for _ in range(l):
            hh, x, y = tmt.popleft()
            if x > 0 and tomato[hh][x-1][y] == '0':
                tomato[hh][x-1][y] = 1
                tmt.append((hh, x-1, y))
                haveto -= 1
            if y > 0 and tomato[hh][x][y-1] == '0':
                tomato[hh][x][y-1] = 1
                tmt.append((hh, x, y-1))
                haveto -= 1
            if x < n-1 and tomato[hh][x+1][y] == '0':
                tomato[hh][x+1][y] = 1
                tmt.append((hh, x+1, y))
                haveto -= 1
            if y < m-1 and tomato[hh][x][y+1] == '0':
                tomato[hh][x][y+1] = 1
                tmt.append((hh, x, y+1))
                haveto -= 1
            if hh > 0 and tomato[hh-1][x][y] == '0':
                tomato[hh-1][x][y] = 1
                tmt.append((hh-1, x, y))
                haveto -= 1
            if hh < h-1 and tomato[hh+1][x][y] == '0':
                tomato[hh+1][x][y] = 1
                tmt.append((hh+1, x, y))
                haveto -= 1
        res += 1
    if haveto:
        print(-1)
    else:
        print(res)


if __name__ == '__main__':
    solve()
