

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