node_cnt = int(input())
edge_cnt = int(input())

connection = []
for _ in range(edge_cnt):
    connection.append(list(map(int,input().split())))

virus = [False for _ in range(node_cnt+1)]

def solution(connection, start, virus):
    virus[start] = True
    for connect in connection:
        if start in connect:
                connect.remove(start)
                if len(connect)>0:
                    solution(connection,connect[0],virus)

solution(connection,1,virus)

print(virus.count(True)-1)


#------------------------------------------------------------------#


#다시 풀어보기
from collections import deque

computer_num = int(input())
edge_num = int(input())
graph = [[] for _ in range(computer_num+1)]
for _ in range(edge_num):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

dfs_visited = [False] * (computer_num+1)
bfs_visited = [False] * (computer_num+1)

cnt = -1

def solution1_dfs(start):
    dfs_visited[start] = True
    global cnt
    cnt += 1
    for i in graph[start]:
        if not dfs_visited[i]:
            solution1_dfs(i)


def solution2_bfs(start):
    queue = deque([start])
    bfs_visited[start] = True
    count = -1
    while queue:
        next_computer=queue.popleft()
        count += 1
        for i in graph[next_computer]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i]=True
    return count


solution1_dfs(1)
print(cnt)
print(solution2_bfs(1))





#다른 사람 풀이
import sys
def dfs(matrix, start):
    for i in matrix[start]:
        if i not in visited:
            visited.add(i)
            dfs(matrix, i)           

N = int(input())
M = int(input())

dic = {}
for i in range(N):
    dic[i+1] = set()
for i in range(M):
    x, y = map(int,sys.stdin.readline().split())
    dic[x].add(y)
    dic[y].add(x)

visited = set()
dfs(dic, 1)

print(len(visited)-1)