from collections import deque

M, N  = map(int,input().split())
graph = []

for _ in range(M):
    graph.append(list(map(int,input().split())))
'''
where_is_1 = []
for i,grap in enumerate(graph):
    for j,gra in enumerate(grap):
        if graph[i][j] == 1:
            where_is_1.append([i,j])
'''
def bfs():
    global graph
    visited = graph.copy()
    queue = deque()
    for i in range(M):
        queue.append((i,0))
        queue.append((i,11))
    for j in range(N):
        queue.append((0,j))
        queue.append((12,j))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            elif visited[nx][ny] == 1:
                visited[nx][ny] = 0
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
            elif visited[nx][ny] == 0:
                queue.append((nx,ny))

bfs()
