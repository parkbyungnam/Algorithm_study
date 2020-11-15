testCase = int(input())
for _ in range(testCase):
    x,y = map(int,input().split())
    distance = y-x
    A = int(distance**(1/2))
    B = A+1
    if A == 1:
        print(distance)
    elif distance>=A*B+1:
        print(A+B)
    elif distance>= A**2+1:
        print(A*2)
    else:
        print(A*2-1)

#다른 풀이
dist = []
t = int(input())
for _ in range(t):
    num1, num2 = map(int,input().split())
    dist.append(num2 - num1)

for dis in dist:
    y = int(dis**(1/2))
    z = y+1

    if y==1:
        print(dis)
    elif dis >= y*z+1:
        print(y+z)
    elif dis >= y**2+1:
        print(y*2)
    else:
        print(y*2-1)