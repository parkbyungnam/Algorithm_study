'''
graph = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [1, 0, 1]]
M = 5
N = 3
K = 6
cnt = 0
'''
# 다시 풀기
import sys
sys.setrecursionlimit(10000)

dx,dy = [-1,1,0,0],[0,0,-1,1]

def solutionDfs(x,y):
    if x<0 or y<0 or x>=m or y>=n:
        return False
    if graphs[x][y]:
        graphs[x][y] = False
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            solutionDfs(nx,ny)
        return True
    return False

testCase = int(input())
for _ in range(testCase):
    cnt = 0 # 지렁이 갯수
    m,n,cabbage_num = map(int,input().split())
    graphs = [[False]*n for _ in range(m)] #인접 행렬 만들기
    for _ in range(cabbage_num):
        i,j = map(int,input().split())
        graphs[i][j] = True #배추 공간 인접 행렬 참값으로
    for x in range(m):
        for y in range(n):
            if solutionDfs(x,y):
                cnt += 1
    print(cnt)

#-------------------------------------------------------------------#

import sys
sys.setrecursionlimit(10000)

testCase = int(input())

def dfs(x,y):
    if x<0 or y<0 or x>=M or y>=N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

for _ in range(testCase):
    cnt = 0
    M,N,K = map(int,input().split())
    graph = [[0]*N for _ in range(M)]
    for _ in range(K):
        a,b = map(int,input().split())
        graph[a][b] = 1
    for i in range(M):
        for j in range(N):
            if dfs(i,j) == True:
                cnt += 1
    print(cnt)



#BFS 로 풀기
from collections import deque
import sys
input = sys.stdin.readline

dx,dy=[-1,1,0,0],[0,0,-1,1]

def solutionBfs(x,y):
    if x<0 or y<0 or x>=m or y>=n: #행렬 밖값 배제
        return False
    if graphs[x][y]: #배추가 있는 곳이라면
        queue = deque([[x,y]])
        graphs[x][y] = False
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i] #상하좌우로 이동
                if m>nx>=0 and n>ny>=0: #행렬 밖값 배제
                    if graphs[nx][ny]:
                        queue.append([nx,ny])
                        graphs[nx][ny] = False
        return True #배추가 있는 곳(1)을 넣으면 이어져 있는 곳 0 으로 바꾸고 참반환
    return False

testCase = int(input())

for _ in range(testCase):
    cnt = 0 #지렁이 갯수
    m,n,cabbage_num = map(int,input().split())
    graphs = [[False]*n for _ in range(m)] # 인접 행렬 초기화
    for _ in range(cabbage_num):
        x,y = map(int,input().split())
        graphs[x][y] = True # 배추 위치 넣기
    for x in range(m):
        for y in range(n):
            if solutionBfs(x,y):
                cnt += 1
    print(cnt)