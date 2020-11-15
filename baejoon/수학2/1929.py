#성공한 코드
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

#시간 초과난 코드
def isPrime(n):
    if (all([(n%i) for i in range(2,int(n**0.5)+1)]) and n>1) == True:
        return n
    else:
        return 0

M,N = map(int,input().split(' '))
arr = [isPrime(x) for x in range(M,N+1)]
arr = sorted(list(set(arr)))
if arr[0] == 0:
    arr.remove(0)
for ar in arr:
    print(ar)


#시간 초과난 코드
def isPrime(n):
    if (all([(n%i) for i in range(2,int(n**0.5)+1)]) and n>1) == True:
        return n
    else:
        return 0

M,N = map(int,input().split(' '))
arr = [isPrime(x) for x in range(M,N+1)]
for ar in arr:
    if ar != 0:
        print(ar)


#시간 초과난 코드
def isPrime(n):
    if (all([(n%i) for i in range(2,int(n**0.5)+1)]) and n>1) == True:
        return n
    else:
        return 0

M,N = map(int,input().split())
for i in range(M,N+1):
    a = isPrime(i)
    if a != 0:
        print(a)
