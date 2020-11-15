#골드바흐 파티션
#골드바흐 수

#좋지 못한 코드
def isPrime(n):
    return all([(n%i) for i in range(2,int(n**0.5)+1)]) and n>1

primeNum = []
for i in range(2,10000):
    if isPrime(i):
        primeNum.append(i)

testCase = int(input())
for _ in range(testCase):
    n = int(input())
    temp = []
    for prime in primeNum:
        if prime>n/2:
            break
        if primeNum.count(n-prime) == 1: #이쪽에서 연산이 너무 빈번하게 일어난다.
            temp.append(prime)
            temp.append(n-prime)
    index=len(temp)/2
    temp = sorted(temp) 
    print(f'{temp[int(index)-1]} {temp[int(index)]}')


#메모리를 조금 더 쓰고 연산을 줄이는 코드

def isPrime(n):
    return all([(n%i) for i in range(2,int(n**0.5)+1)]) and n>1

primeCheckArr = []
for i in range(0,10001):
    primeCheckArr.append(isPrime(i))

testCase = int(input())
for _ in range(testCase):
    n = int(input())
    temp = []
    for i in range(n//2,0,-1):
        if primeCheckArr[i] == True and primeCheckArr[n-i] == True:
            print(i,n-i)
            break
