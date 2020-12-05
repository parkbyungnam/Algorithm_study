import math

N = int(input())
fN = math.factorial(N)

for i in range(0,len(str(fN))):
    if fN%(10**(i+1))!=0:
        print(i)
        break