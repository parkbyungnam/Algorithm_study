n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))
for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]
print(min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))



# 문제를 잘못 이해하고 풀었음.
# 잘못된 풀이.

def solution(dp):
    result = [0]*6  
    index = [0,0,1,1,2,2]
    for i in range(0,6,2):
        for d in dp:
            if index[i]==3:
                index[i]=0
            result[i] += d[index[i]]
            index[i]+=1

    for i in range(1,6,2):
        for d in dp:
            if index[i]==-1:#0 2 1 방향
                index[i]==2
            result[i] += d[index[i]]
            index[i]-=1
    print(result)
    return min(result)

dp = []
for _ in range(int(input())):
    dp.append(list(map(int,input().split())))
print(solution(dp))