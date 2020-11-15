M = int(input())
N = int(input())

def isPrime(n):
    if (all([(n%i) for i in range(2,int(n**0.5)+1)]) and n>1) == True:
        return n
    else:
        return 0

def primeList(m,n):
    return ([isPrime(x) for x in range(m,n+1)])
mylist = primeList(M,N)
primeSum = sum(mylist)
if primeSum==0:
    print(-1)
else:
    print(primeSum)
    print(sorted(list(set(mylist)))[1])
