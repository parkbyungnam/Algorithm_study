x=int(input())
dp=[0]*(x+1)

for i in range(2,x+1):
    dp[i]=dp[i-1]+1
    if i%2==0 and dp[i//2]+1 < dp[i]:
        dp[i]=dp[i//2]+1
    if i%3==0 and dp[i//3]+1 < dp[i]:
        dp[i]=dp[i//3]+1
    if i%5==0 and dp[i//5]+1 < dp[i]:
        dp[i]=dp[i//5]+1
print(dp[x])