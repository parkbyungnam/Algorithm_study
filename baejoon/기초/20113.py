N = int(input())
vote = list(map(int,input().split()))
mylist  = [[idx,0] for idx in range(N+1)]
for vo in vote:
    mylist[vo][1] += 1
mylist.sort(reverse=True, key=lambda x:x[1])
if mylist[0][0] == 0:
    if mylist[0][1] == mylist[1][1] and mylist[1][1]>mylist[2][1]:
        print(mylist[1][0])
    else:
        print('skipped')
elif mylist[0][0] != 0 and mylist[0][1] == mylist[1][1]:
    print('skipped')
else:
    print(mylist[0][0])


#타인 코드
N=int(input())
a=[0]*N
for i in map(int, input().split()):
    if i:
        a[i-1]+=1
b=max(a)
if a.count(b)>1:
    print('skipped')
else:
    print(1+a.index(b))