N,K = map(int,input().split())
mylist = [int(input()) for _ in range(N)]
mylist.reverse()
cnt = 0
for coin in mylist:
    cnt += K//coin
    K %= coin

print(cnt)