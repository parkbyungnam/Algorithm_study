# 맵 가장자리가 바다라는 조건을 못봄
# 단순 구현으로 풀어보기

def change_d(d):
    return 3 if d==0 else d-1

n,m=map(int,input().split())
x,y,d=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(m)]

# 바라보는 방향 :  북      동      남     서
 
# 가야하는 방향 :  서      북      동     남
d_list =     [[0,-1], [-1,0], [0,1], [1,0]]

maps[x][y]=-1 # 시작 위치 방문 처리  -1: 방문, 0: 미방문, 1: 바다
cnt=1 # 방문한 육지 카운트

while True:
    old_x,old_y=x,y
    
    for _ in range(4):
        dx,dy=d_list[d][0],d_list[d][1]
        nx,ny=x+dx,y+dy

        # 리스트 범위 밖일 때
        if nx<0 or ny<0 or n-1<nx or m-1<ny:
            d=change_d(d)
            continue

        # 미방문 육지일 때
        if maps[nx][ny]==0:
            maps[nx][ny]=-1
            cnt+=1
            x,y=nx,ny
            d=change_d(d)
            break

        # 해당 방향으로 가는 것이 불가능하다면 방향만 전환
        d=change_d(d)
    
    # 주변에 미방문 육지가 없을 때
    if old_x==x and old_y==y:

        if d==0: #북쪽 볼 때
            if x==m-1: #리스트 가장자리 라면
                break
            if maps[x+1][y]==1: #뒷쪽이 바다
                break
            x+=1 # 현재 좌표에서 뒤로 한 칸 이동

        if d==1: #동쪽 볼 때
            if y==0:
                break
            if maps[x][y-1]==1:
                break
            y-=1

        if d==2: #남쪽 볼 때
            if x==0:
                break
            if maps[x-1][y]==1:
                break
            x-=1

        if d==3: #서쪽 볼 때
            if y==m-1: 
                break
            if maps[x][y+1]==1:
                break
            y+=1

print(cnt)






### 공식 풀이 (맵 가장자리가 항상 바다라는 점을 사용)
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)