import math

print(math.factorial(int(input())))


#재귀함수풀이
def factorial_recursive(n):
    return n * factorial_recursive(n-1) if n > 1 else 1
factorial_recursive(4)



#틀린 풀이 0!=1
n = int(input())
if n == 0:
    print(0)
else:
    temp = 1
    for i in range(n,0,-1):
        temp = temp * i
    print(temp)

