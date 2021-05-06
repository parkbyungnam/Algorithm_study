'''
5 6
101010
111111
000001
111111
111111
'''


from collections import deque

'''
n, m = map(int,input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int,input())))
'''

n, m = 5,6
maze = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]]

def bfs(maze, n, m, a, b):
    queue = deque()
    queue.append((a,b))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dx[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
    return maze[n-1][m-1]

print(bfs(maze,n,m,0,0))





# 다시 풀기
from collections import deque

n,m = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny <0 or nx>=n or ny>=m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
    return maze[n-1][m-1]

print(bfs(0,0))
