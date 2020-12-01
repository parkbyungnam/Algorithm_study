import math

testCase = int(input())
inputData = []
for _ in range(testCase):
    inputData.append(int(input()))

inputData.sort()

myData = inputData[-1] - inputData[0]
divisor = [myData]
for i in range(2,int(math.sqrt(myData))+1):
    if myData % i == 0:
        divisor.append(i)
        divisor.append(myData//i)

divisor = list(set(divisor))
divisor.sort()

for div in divisor:
    for i in range(testCase):
        if i == testCase - 1:
            print(div, end=" ")
        elif inputData[i]%div != inputData[i+1]%div:
            break


#다른사람 풀이

import sys
input = sys.stdin.readline


def gcd(a, b):
    return gcd(b, a % b) if a % b else b


n = int(input())
num = sorted([int(input()) for _ in range(n)])
get = num[1] - num[0]

for i in range(2, n):
    get = gcd(get, num[i]-num[i-1])

res = set()
for i in range(2, int(get**0.5)+1):
    if get % i == 0:
        res.add(i)
        res.add(get//i)
res.add(get)
res = sorted(list(res))
print(' '.join(map(str, res)))

