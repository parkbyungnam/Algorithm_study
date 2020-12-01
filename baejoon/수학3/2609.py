import math

n,m = map(int,input().split())
my_gcd = math.gcd(n,m)
print(my_gcd)
print(n*m//my_gcd)

#함수 직접 설계

#유클리드 호제법
def my_gcd(x,y):
    while y:
        x,y=y,x%y
    return x