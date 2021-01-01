dp = []
testCase = int(input())
for _ in range(testCase):
    dp.append(list(map(int,input().split())))

for i in range(1,testCase):
    for j in range(1,i):
        dp[i][j]+=max(dp[i-1][j],dp[i-1][j-1])
    dp[i][0] += dp[i-1][0]
    dp[i][i] += dp[i-1][i-1]

print(max(dp[testCase-1]))