'''
graph = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [1, 0, 1]]
M = 5
N = 3
K = 6
cnt = 0
'''

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