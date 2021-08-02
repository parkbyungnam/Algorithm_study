mylist=list()
for _ in range(int(input())):
    a,b=input().split()
    mylist.append([a,int(b)])
mylist.sort(key=lambda x: x[1])
for my in mylist:
    print(my[0], end=' ')