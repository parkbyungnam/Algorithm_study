import math

N,K = map(int,input().split())
print(math.factorial(N)//(math.factorial(K)*math.factorial(N-K)))


#
def Fact(n):
    mul = 1
    for i in range(1,n+1):
        mul *= i
    return mul