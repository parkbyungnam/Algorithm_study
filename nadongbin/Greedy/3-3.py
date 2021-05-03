n,m = map(int,input().split())
mylist = []
for _ in range(n):
    mylist.append(list(map(int,input().split())))

result = 0
for lst in mylist:
    lst.sort()
    result = max(result,lst[0])

print(result)

#다른 풀이

n,m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(min_value, result)

print(result)


#다시 풀어보기
N,M = map(int,input().split())
mylist=[list(map(int, input().split())) for _ in range(N)]

result = 0
for my in mylist:
    my.sort()
    result = max(result,my[0])

print(result)