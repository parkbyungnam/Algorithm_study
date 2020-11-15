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