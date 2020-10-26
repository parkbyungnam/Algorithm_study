#분해합

N = int(input())
nSize = len(str(N))
searchStart=N-nSize*9
result = 0
if searchStart<0:
    searchStart=0
for i in range(searchStart,N):
    arr = list(map(int,str(i)))
    temp = i
    for ar in arr:
        temp += ar
    if temp == N:
        result = i
        break
print(result)


#다른 사람 풀이
N = int(input())

for i in range(max(1, N-54), N+1):
    if N == i + sum(list(map(int, str(i)))):
        print(i)
        exit(0)
print(0)

