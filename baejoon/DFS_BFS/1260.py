from collections import deque
import sys
read = sys.stdin.readline


node, edge, startNode = map(int,read().split())
arr = [[]*node for _ in range(node+1)]
for _ in range(edge):
    start,end=map(int,read().split())   
    arr[start].append(end)
    #arr[end].append(start)

dfsVisited = [False]*(node+1)
bfsVisited = [False]*(node+1)

for ar in arr:
    ar.sort()

def dfs(arr, startNode, dfsVisited):
    dfsVisited[startNode] = True
    print(startNode,end=" ")
    for i in arr[startNode]:
        if not dfsVisited[i]:
            dfs(arr, i, dfsVisited)


def bfs(arr, startNode, bfsVisited):
    queue = deque([startNode])
    bfsVisited[startNode] = True
    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for i in arr[v]:
            if not bfsVisited[i]:
                queue.append(i)
                bfsVisited[i] = True

dfs(arr,startNode,dfsVisited)
print()
bfs(arr,startNode,bfsVisited)

#다시풀기
from collections import deque
node_num, edge_num, start_node = map(int,input().split())
graph = [[] for _ in range(node_num+1)]

#인접 리스트 생성
for _ in range(edge_num):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

for gra in graph:
    gra.sort()

dfs_visited = [False]*(node_num+1)
bfs_visited = [False]*(node_num+1)

def dfs(graph, start_node):
    dfs_visited[start_node] = True
    print(start_node, end=' ')
    for i in graph[start_node]:
        if not dfs_visited[i]:
            dfs(graph, i)


def bfs(graph, start_node):
    queue = deque([start_node])
    bfs_visited[start_node]=True
    while queue:
        next_node = queue.popleft()
        print(next_node, end=' ')
        for i in graph[next_node]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i]=True

dfs(graph, start_node)
print()
bfs(graph, start_node)


#타인 풀이
'''
import sys
N, M, V = map(int, sys.stdin.readline().strip().split())
edge = [[] for _ in range(N+1)]

for __ in range(M):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    edge[n1].append(n2)
    edge[n2].append(n1)

for e in edge:
    e.sort(reverse=True)

def dfs():
    d_visit = []
    stack = [V]
    d_check = [0 for _ in range(N+1)]
    while stack:
        v1 = stack.pop()
        if not d_check[v1]:
            d_check[v1] = 1
            d_visit.append(v1)
            stack += edge[v1]
    return d_visit


def bfs():
    b_visit = []
    queue = [V]
    b_check = [0 for _ in range(N+1)]
    b_check[V] = 1
    while queue:
        v2 = queue.pop()
        b_visit.append(v2)
        for i in reversed(edge[v2]):
            if not b_check[i]:
                b_check[i] = 1
                queue = [i] + queue
    return b_visit

print(' '.join(map(str,dfs())))
print(' '.join(map(str,bfs())))
'''