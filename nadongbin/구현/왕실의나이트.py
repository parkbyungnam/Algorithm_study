a=input()
x=ord(a[0])-96
y=int(a[1])
dx=[1,2,1,2,-1,-2,-1,-2]
dy=[-2,-1,2,1,2,1,-2,-1]
count=0
for i in range(8):
    nx, ny = x+dx[i], y+dy[i]
    if 0<nx<=8 and 0<ny<=8:
        count+=1
print(count)