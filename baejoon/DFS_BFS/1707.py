from collections import deque

def solutionBfs():
    queue=deque(graph)
    while queue:
        a,b= queue.popleft()
        if not bipartite[a] and not bipartite[b]:
            bipartite[a],bipartite[b]=-1,1
        elif not bipartite[a]:
            bipartite[a]=bipartite[b]*-1
        elif not bipartite[b]:
            bipartite[b]=bipartite[a]*-1
    queue=deque(graph)
    while queue:
        a,b= queue.popleft()
        if bipartite[a] == bipartite[b] and a!=b:
            return False
    return True

testCase = int(input())
for _ in range(testCase):
    node_cnt, edge_cnt = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(edge_cnt)]
    bipartite = [0] * (node_cnt+1)
    if solutionBfs():
        print('YES')
    else:
        print("NO")



# --------------------
# -----타인 코드--------
# --------------------

from collections import deque
import sys

input = sys.stdin.readline
k = int(input())

def bfs(start):
    bi[start] = 1
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for i in s[a]:
            if bi[i] == 0:
                bi[i] = -bi[a]
                q.append(i)
            else:
                if bi[i] == bi[a]:
                    return False
    return True

for i in range(k):
    v, e = map(int, input().split())
    isTrue = True
    s = [[] for i in range(v + 1)]
    bi = [0 for i in range(v + 1)]
    for j in range(e):
        a, b = map(int, input().split())
        s[a].append(b)
        s[b].append(a)
    for k in range(1, v + 1):
        if bi[k] == 0:
            if not bfs(k):
                isTrue = False
                break
    print("YES"if isTrue else "NO")

