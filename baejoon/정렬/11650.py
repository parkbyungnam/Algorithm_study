testCase = int(input())
mylist = []
for _ in range(testCase):
    mylist.append(list(map(int,input().split())))
mylist.sort()
for my in mylist:
    x,y = my
    print(x,y)