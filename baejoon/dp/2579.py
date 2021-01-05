#반례는 무엇일까??
totalStair = int(input())
stairs = []
for _ in range(totalStair):
    stairs.append(int(input()))

totalScore = stairs[-1]
flag = False

while totalStair > 2:
    i = totalStair - 1
    if stairs[i-1]>=stairs[i-2] and flag == False:
        totalStair -= 1
        totalScore += stairs[i-1]
        flag = True
    else:
        totalStair -= 2
        totalScore += stairs[i-2]
        flag = False

if totalStair == 2:
    if flag == False:
        totalScore += stairs[0]

print(totalScore)


#타인 풀이
n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])


#연습해본거
totalStair = int(input())
stairs = [0 for _ in range(301)]
for i in range(totalStair):
    temp = int(input())
    stairs[i] = temp
dp = [0 for _ in range(301)]
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0]+stairs[1],stairs[0]+stairs[2])
for i in range(3,totalStair):
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i],dp[i-2]+stairs[i])
print(dp[totalStair - 1])


#타인 풀이
from sys import stdin

a,b,c = 0,0,0

n = int(stdin.readline())
for _ in range(n):
    pb = int(stdin.readline())
    d_0,d_1,d_2 = max(b,c),a+pb,b+pb
    a,b,c = d_0,d_1,d_2

print(max(d_2,d_1))