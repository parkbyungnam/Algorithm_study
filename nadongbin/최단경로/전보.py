import heapq

INF=int(1e9)
n,m,c=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))

def solution(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now_node=heapq.heappop(q)
        if distance[now_node]<dist:
            continue
        for i in graph[now_node]:
            next_node,weight=i
            cost=dist+weight
            if cost < distance[next_node]:
                distance[next_node]=cost
                heapq.heappush(q, (cost, next_node))

solution(c)

cnt,max_dist=0,0
for d in distance:
    if d!= INF:
        cnt += 1
        max_dist=max(max_dist,d)
        
print(cnt-1,max_dist)