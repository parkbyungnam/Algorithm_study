from operator import itemgetter

testCase = int(input())
mylist = []
for _ in range(testCase):
    mylist.append(list(map(int,input().split())))
sortedlist = sorted(mylist,key=itemgetter(1,0))
for i in sortedlist:
    x,y=i
    print(x,y)