import math

N = int(input())
mylist = list(map(int,input().split(" ")))
myRadius = mylist.pop(0)
for yourRadius in mylist:
    myGcd = math.gcd(myRadius,yourRadius)
    print(myRadius//myGcd,yourRadius//myGcd,sep="/")
    #print(f'{myRadius//myGcd}/{yourRadius//myGcd}')

#GCD
def GCD(a,b): return GCD(b,a%b) if b else a