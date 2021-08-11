INF=int(1e9)

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[a][b]=1

x,k = map(int,input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

distance=graph[1][k]+graph[k][x]

print(-1) if distance >= INF else print(distance)


#----
import heapq
from copy import deepcopy

INF = int(1e9)

#회사 개수, 경로 개수
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

def solution(start):
    
    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append((b,1))

        q=[]
        heapq.heappush(q,(0,start))
        distance[start]=0
        while q:
            dist,now_node=heapq.heappop(q)
            if distance[now_node]<dist:
                r
