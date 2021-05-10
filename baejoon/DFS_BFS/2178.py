from collections import deque
N,M = map(int,input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int,input())))


maze = [
 [1, 0, 1, 1, 1, 1],
 [1, 0, 1, 0, 1, 0],
 [1, 0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1, 1]]

N,M = 4,6


def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=N or ny>=M:
                continue
            if maze[nx][ny]==1:
                queue.append((nx,ny))
                maze[nx][ny]=maze[x][y]+1
    return maze[N-1][M-1]

print(bfs(0,0))


#다시풀기
from collections import deque
n,m = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]

def check(x,y): #바깥 범위인지 확인
    if 0<=x<n and 0<=y<m:
        return True
    return False

def bfs(a,b):
    if maze[a][b] == 1: #1이면 미방문이라고 판단
        queue = deque([[a,b]])
        while queue:
            x,y = queue.popleft()
            for i in range(4): #동서남북
                nx, ny = x + dx[i], y + dy[i]
                if check(nx,ny): #바깥 범위 배제
                    if maze[nx][ny] == 1: # 방문하지 않은 곳이라면
                        maze[nx][ny] += maze[x][y] #1칸 이동할 때 이전 값 더해주기
                        queue.append([nx,ny])

bfs(0,0)
print(maze[n-1][m-1])