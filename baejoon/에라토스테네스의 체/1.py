def prime_list(n):
    sieve = [True] * n
    m = int(n**0.5)
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i,n,i):
                sieve[j]=False
    return [i for i in range(2,n) if sieve[i]==True]


#소수가 아닐 때 함수를 빠르게 마침.
#시간 복잡도 최소화.
def isPrime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return 0
    return 1

M,N = map(int,input().split())
for i in range(M,N+1):
    if isPrime(i):
        print(i)



# 소수인지 판단
def is_prime(n):
    return all([(n%j) for j in range(2, int(n**0.5)+1)]) and n>1



# 소수의 갯수 리턴
def numberOfPrime(n):
    return [is_prime(x) for x in range(1, n+1)].count(True)
    #return len(list(filter(is_prime, range(1, n+1))))


print(numberOfPrime(10))
print(is_prime(3))