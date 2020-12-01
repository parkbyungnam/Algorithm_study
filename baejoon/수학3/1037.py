N = int(input())
mylist = list(map(int,input().split(" ")))
mylist.sort()
print(mylist[0]*mylist[-1])