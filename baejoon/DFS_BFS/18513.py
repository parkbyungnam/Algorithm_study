# N : 샘터 갯수 K : 집 갯수
# 샘터의 위치
#N, K = map(int,input().split())
#wells = list(map(int,input().split()))
from collections import deque
N, K = 2, 5
wells = [0, 3]
visited = []
unhappy = 0
home_cnt = -1 * N

queue = deque()
def bfs(wells, N, K, home_cnt, unhappy):
    for well in wells:
        queue.append(well)
    unhappy+=1
    if home_cnt==K:
        return unhappy
    temp = queue.popleft()
    if temp not in visited:
        visited.append(temp)
        home_cnt+=1        
    bfs([temp-1,temp+1],N,K,home_cnt,unhappy)

unhappy=bfs(wells,N,K,home_cnt,unhappy)


#다른사람풀이

n,k = 2, 5
toleft = [0,3]
toright = toleft
visited = set(toleft)
ans = 0
while True:
    newleft = []
    for i in toleft:
        j = i - 1
        if j not in visited:
            visited.add(j)
            newleft.append(j)
    toleft = newleft
    newright = []
    for i in toright:
        j = i + 1
        if j not in visited:
            visited.add(j)
            newright.append(j)
    toright = newright
    acc = len(toleft) + len(toright)
    if acc >= k:
        ans += k
        print(ans)
        break
    else:
        ans += k
        k -= acc