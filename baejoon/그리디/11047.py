N,K = map(int,input().split())
mylist = [int(input()) for _ in range(N)]
mylist.reverse()
cnt = 0
for coin in mylist:
    cnt += K//coin
    K %= coin

print(cnt)



#다시 풀어보기
N,K = map(int,input().split())
mylist = []
for _ in range(N):
    mylist.append(int(input()))
# mylist = [int(input()) for _ in range(N)]
# 리스트 컴프리핸션
result = 0

mylist.reverse()

for my in mylist:
    result += K // my
    K %= my

print(result)