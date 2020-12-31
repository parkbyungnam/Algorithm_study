#시간 초과
from math import factorial
import functools

def nHr(n,r):
    n += r-1
    r = min(r,n-r)
    up = functools.reduce(lambda x,y:x*y,range(n,n-r,-1),1)
    down = factorial(r)
    return up//down

def solution(n):
    my00 = n//2
    result = 0
    for i in range(my00+1):
        my1 = n-i*2
        result += nHr(i+1,my1)
    print(result)

solution(1000000)

#시간 초과2
def solution(n):
    if n==1:
        print(1)
    else:
        current = 2
        past = 1
        for _ in range(n-2):
            temp = current
            current += past
            past = temp
        print(current%15746)


solution(int(input()))

#다른 풀이
n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3,1000001):
    dp[i] = dp[i-1] + dp[i-2]

print(n)