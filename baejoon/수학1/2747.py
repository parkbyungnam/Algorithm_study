mylist=[0,1]
N = int(input())
for i in range(2,N+1):
    mylist.append(mylist[i-1]+mylist[i-2])
print(mylist[N])