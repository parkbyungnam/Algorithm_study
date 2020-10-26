arrX = []
arrY = []
for _ in range(3):
    x,y = map(int,input().split())
    arrX.append(x)
    arrY.append(y)
a = 0
b = 0
for x in arrX:
    if arrX.count(x) == 1:
        a = x
for y in arrY:
    if arrY.count(y) == 1:
        b = y
print(a,b)


#다른 풀이
x = []
y = []

for i in range(3):
    a,b = map(int,input().split())

    if a in x : x.remove(a)
    else : x.append(a)
    if b in y : y.remove(b)
    else : y.append(b)

print(*x,*y)