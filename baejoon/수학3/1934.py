from math import gcd

testCase = int(input())

for _ in range(testCase):
    a,b=map(int,input().split())
    result=gcd(a,b)
    print(a*b//result)