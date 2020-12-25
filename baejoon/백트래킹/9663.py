#내 윗줄에 나와 겹치는 라인에 퀸이 있는가?
def overlap(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return True
    return False
        
        
#한줄씩 재귀하며 DFS를 실행
def dfs(x):
    global result
    
    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            if not overlap(x):
                dfs(x + 1)

N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)



#문제 이해 잘못한 코드
N = int(input())
result = 0

def solution(row,col):
    board = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i==row or j==col or row-col==i-j or row+col==i+j:
                board[i][j]=1
    
    if row!=0:
        for i in range(row):
            del board[0]
    
    sum = 0
    for bo in board:
        sum += bo.count(0)

    return sum

for i in range(N):
    for j in range(N):
        result+=solution(i,j)

print(result)







