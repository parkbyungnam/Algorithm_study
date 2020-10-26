def solution(m, n, puddles):
    route=[[0]*(m+1) for _ in range(n+1)] #초기화
    route[1][1] = 1 #우리집
    for y in range(1, n+1): #
        for x in range(1, m+1):
            if x==1 and y==1:
                continue
            if [x,y] in puddles:
                continue
            route[y][x] = route[y-1][x] + route[y][x-1]
    return(route[-1][-1])%1000000007

m,n = map(int,input().split())
puddles_cnt = int(input())
puddles = []
for _ in range(puddles_cnt):
    a,b = map(int,input().split())
    puddles.append([a,b])
print(solution(m,n,puddles))