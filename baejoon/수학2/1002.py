testCase = int(input())
for _ in range(testCase):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    r = [r1, r2]
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:
        if r1+r2<d or max(r)-min(r)>d:
            print(0)
        elif r1+r2==d or max(r)-min(r)==d:
            print(1)
        else:
            print(2)
