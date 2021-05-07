

'''
N = 7
graph = [
 [0, 1, 1, 0, 1, 0, 0],
 [0, 1, 1, 0, 1, 0, 1],
 [1, 1, 1, 0, 1, 0, 1],
 [0, 0, 0, 0, 1, 1, 1],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 1, 1, 1, 1, 1, 0],
 [0, 1, 1, 1, 0, 0, 0]]
total = 0
cnt_arr = []
'''
#다시 풀기
N = int(input())
graphs = [list(map(int,input())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
result = []

def dfs(x,y):
    global cnt
    if x<0 or y<0 or x>=N or y>=N:
        return False
    if graphs[x][y]:
        cnt += 1
        graphs[x][y]=0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            dfs(nx,ny)
        return True
    return False

for i in range(N):
    for j in range(N):
        if graphs[i][j]:
            dfs(i,j)
            result.append(cnt)
            cnt = 0

result.sort()

print(len(result))
for answer in result:
    print(answer)



#---------------------------------------------------------#
#첫번째 풀이
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))
total = 0
cnt_arr = []


def dfs(x,y,total):
    if x<0 or y<0 or x>=N or y>=N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = total+2
        dfs(x-1,y,total)
        dfs(x+1,y,total)
        dfs(x,y-1,total)
        dfs(x,y+1,total)
        return True
    return False


for n in range(N):
    for m in range(N):
        if dfs(n,m,total) == True:
            total = total + 1

print(total)


for i in range(total+1,1,-1):
    temp = 0
    for gra in graph:
        temp = temp + gra.count(i)
    cnt_arr.append(temp)

cnt_arr.sort()
for cnt in cnt_arr:
    print(cnt)

#타인 풀이

import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(sys.stdin.readline())
a = [list(sys.stdin.readline()) for _ in range(n)]
cnt = 0
apt = []


def dfs(x, y):
    global cnt
    a[x][y] = '0'
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if a[nx][ny] == '1':
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if a[i][j] == '1':
            cnt = 0
            dfs(i, j)
            apt.append(cnt)

print(len(apt))
apt.sort()
for i in apt:
    print(i)