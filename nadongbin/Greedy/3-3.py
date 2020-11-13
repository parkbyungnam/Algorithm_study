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