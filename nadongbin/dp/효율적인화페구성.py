n,m=map(int,input().split())
coin=[int(input()) for _ in range(n)]

d=[10001]*(m+1)

d[0]=0

for i in range(n):
    for j in range(coin[i],m+1):
        if d[j-coin[i]]!=10001:
            d[j]=min(d[j],d[j-coin[i]]+1)

if d[m]==10001:
    print(-1)
else:
    print(d[m])


###

n,m=map(int,input().split())
coins=[int(input()) for _ in range(n)]
d=[-1]*(10001)

for coin in coins:
    d[coin]=1

for i in range(1,m+1):
    if d[i]!=-1:
        for coin in coins:
            if d[coin+i]==-1:
                d[coin+i]=d[i]+1
            else:
                d[i+j]=min(d[i+j],d[i]+1)
print(d[m])

###



n,m=map(int,input().split())
coins=[int(input()) for _ in range(n)]
canMake=[False]*(10001)

for coin in coins:
    canMake[coin]=1

for i in range(1,m+1):
    if canMake[i]:
        for coin in coins:
            if canMake[coin+i] is False:
                canMake[coin+i]=canMake[i]+1
            else:
                canMake[i+j]=min(canMake[i+j],canMake[i]+1)

print(canMake[m])