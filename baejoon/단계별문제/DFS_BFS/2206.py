from collections import deque

N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))

def bfs():
    queue=deque()
    queue.append([0,0,True])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][True] = 1
    while queue:
        x,y,chance = queue.popleft()
        if x==N-1 and y==M-1:
            return visited[x][y][chance]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            elif chance == True and graph[nx][ny] == 1:
                visited[nx][ny][False] = visited[x][y][True] + 1
                queue.append([nx,ny,False])
            elif graph[nx][ny] == 0 and visited[nx][ny][chance] == 0:
                visited[nx][ny][chance] = visited[x][y][chance] + 1
                queue.append([nx,ny,chance])
    return -1

print(bfs())


#타인 풀이
import sys
I = sys.stdin.readline
def bfs(r,c):
    que = [(0,0,False)]
    count = 1
    while que:
        que_ = []
        for r,c,flag in que:
            if r == R-1 and c == C-1:
                return count
            for dr, dc in dir:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < R and 0 <= cc < C:
                    if not flag:
                        if not visitF[rr][cc]:
                            if Map[rr][cc] == '0':
                                visitF[rr][cc] = True
                                que_.append((rr,cc,False))
                            else:
                                visitF[rr][cc] = True
                                que_.append((rr,cc,True))
                    else:
                        if not visitT[rr][cc]:
                            if Map[rr][cc] == '0':
                                visitT[rr][cc] = True
                                que_.append((rr,cc,True))
        
        que = que_
        count += 1
    return -1

dir = [[1,0], [-1,0], [0,1], [0,-1]]
R, C = list(map(int, I().split()))
Map = [list(I()) for _ in range(R)]
visitF = [[False] * C for _ in range(R)]
visitT = [[False] * C for _ in range(R)]

print(bfs(0,0))