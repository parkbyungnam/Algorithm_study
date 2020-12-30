def fibo0(n):
    if n==1:
        my0 = 0
    elif n<=3:
        my0 = 1
    else:
        past = 1
        my0 = 1
        for _ in range(n-3):
            temp = my0
            my0 += past
            past = temp
    return my0

def fibo1(m):
    if m==0:
        my1 = 0
    else:
        my1 = 1
        past = 1
        for _ in range(m-2):
            temp = my1
            my1 += past
            past = temp
    return my1

def solution(n):
    print(fibo0(n),fibo1(n))

testCase = int(input())
for _ in range(testCase):
    solution(int(input()))