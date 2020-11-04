from collections import deque

M,N = map(int,input().split())
graph = []
where_is_1=[]


for i in range(N):
    graph.append(list(map(int,input().split())))
    for j in range(M):
        if graph[i][j] == 1:
            where_is_1.append([i,j])

'''
for i,grap in enumerate(graph):
    for j,gra in enumerate(grap):
        if graph[i][j] == 1:
            where_is_1.append([i,j])
'''

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