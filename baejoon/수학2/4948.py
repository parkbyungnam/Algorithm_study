#pypy3 로 제출하니 잘됌.
from math import sqrt
def isPrime(n):
    if n==1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

while True:
    count = 0
    testCase = int(input())
    if testCase == 0:
        break
    for i in range(testCase+1,testCase*2+1):
        if isPrime(i):
            count+=1
    print(count)

#타인 코드. 2배는 빠르게 동작함. 에라토스테네스의 체
def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
 
    return [i for i in range(2, n) if sieve[i] == True]
 
while 1:
    n=int(input())
    if n==0:break
    li=prime_list(2*n+1)
    print(len([i for i in li if i>n]))