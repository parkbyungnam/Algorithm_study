from operator import itemgetter

testCase = int(input())
mylist = []
for _ in range(testCase):
    mylist.append(list(map(int,input().split())))
sortedlist = sorted(mylist,key=itemgetter(1,0)) #itemgetter , attrgetter
for i in sortedlist:
    x,y=i
    print(x,y)



#참고자료 https://docs.python.org/ko/3/howto/sorting.html