n = int(input())
temp1 = 0
temp2 = 1
current = 0
if n<2:
    print(n)
else:
    for i in range(2,n+1):
        current = temp1 + temp2
        temp1 = temp2
        temp2 = current
    print(current)


#다른 풀이
def p(n):
    x=0
    y=1
    for i in range(n):
        x,y=y,x+y;
    return x
a=int(input())
print(p(a))