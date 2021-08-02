n=int(input())
mylist=list(map(int,input().split()))

dp=[0]*n

dp[0]=mylist[0]
dp[1]=max(mylist[0],mylist[1])
for i in range(2,n):
    dp[i]=max(dp[i-1],dp[i-2]+mylist[i])

print(dp[-1])