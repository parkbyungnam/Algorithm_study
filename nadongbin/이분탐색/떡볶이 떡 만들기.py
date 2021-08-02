cake_total, require_len = map(int,input().split())
cakes=list(map(int,input().split()))
start,end=0,max(cakes)
result=0
while True:
    if start>end:
        break
    total = 0
    mid=(start+end)//2
    for cake in cakes:
        if cake > mid:
            total += cake - mid
    if total < require_len:
        end = mid-1
    else:
        result=mid
        start=mid+1

print(result)