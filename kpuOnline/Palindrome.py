def isPrime(n):
    return all([(n%i) for i in range(2,int(n**0.5)+1)]) and n>1

def isPalindrome(n):
    reversed_n = int(str(n)[::-1])
    if (reversed_n + n) // 2 == n:
        return True
    else:
        return False

CheckArr = []
for i in range(0,1000001):
    CheckArr.append(isPrime(i) and isPalindrome(i))

testCase = int(input())
for i in range(testCase,1000001):
    if CheckArr[i]==True:
        print(i)
        break


## 다른 풀이

def isPrime(n):
    return all([(n%i) for i in range(2,int(n**0.5)+1)]) and n>1

def isPalindrome(n):
    reversed_n = int(str(n)[::-1])
    if (reversed_n + n) // 2 == n:
        return True
    else:
        return False

CheckArr = []
for i in range(0,1000001):
    CheckArr.append(isPrime(i))

testCase = int(input())
for i in range(testCase, 1000001):
    if isPalindrome(i) and CheckArr[i]:
        print(i)


## 다른풀이

def isPrime(n):
    return all([(n%i) for i in range(2,int(n**0.5)+1)]) and n>1

def isPalindrome(n):
    reversed_n = int(str(n)[::-1])
    if reversed_n == n:
        return True
    else:
        return False

testCase = int(input())
for i in range(testCase,1000001):
    if isPrime(i) and isPalindrome(i):
        print(i)
        break



## 풀린 풀이
def isPrime(n):
    return all([(n%i) for i in range(2,int(n**0.5)+1)]) and n>1

def nearestPrimePalindrome(n):
    if n%2==0:
        n+=1
    while True:
        if str(n)==str(n)[::-1]:
            if isPrime(n):
                return n
        n+=2

print(nearestPrimePalindrome(int(input())))