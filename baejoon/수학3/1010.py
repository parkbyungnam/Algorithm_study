from functools import reduce
from math import factorial

def nCr(n,r):
    if r>n-r:
        r = n-r
    numerator = reduce(lambda x,y:x*y,range(n,n-r,-1),1)
    denominator = factorial(r)
    return numerator//denominator

testCase = int(input())
for _ in range(testCase):
    n,m = map(int,input().split())
    print(nCr(m,n))