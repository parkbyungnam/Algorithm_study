from collections import deque

def dfs():
    dx = [-1,-2,-2,-1,1,2,2,1] # 체스 말 움직임1
    dy = [-2,-1,1,2,2,1,-1,-2] # 체스 말 움직임2
    chess = [[0]*l for _ in range(l)]
    queue = deque([[startX,startY]])
    if startX==endX and startY==endY: #시작과 종점이 같을 때 예외처리
        return 0
    while queue and not chess[endX][endY]: #종료조건
        x, y = queue.popleft()
        for i,j in zip(dx,dy): #zip 을 사용하면 더 빠르게 수행할 수 있다고 한다
            nx = x + i
            ny = y + j
            if 0<=nx<l and 0<=ny<l:
                if not chess[nx][ny]:
                    chess[nx][ny] = chess[x][y]+1
                    queue.append([nx,ny])
    return chess[endX][endY]


testCase = int(input())
for _ in range(testCase):
    l = int(input())
    startX,startY = map(int,input().split())
    endX,endY = map(int,input().split())
    print(dfs())