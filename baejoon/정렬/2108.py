testCase = int(input())
mylist = []
for _ in range(testCase):
    mylist.append(int(input()))

mylist.sort()
print(sum(mylist)//testCase) #산술평균
print(mylist[testCase//2]) #중앙값

count = 0
for my in mylist:
    myCount = mylist.count(my)
    if myCount>count:
        count = myCount
        countlist = []
        countlist.append(my)
    elif myCount == count:
        countlist.append(my)

if countlist[-1]==countlist[0]:
    print(countlist[0])
else:
    print(countlist[1]) #최빈값

print(mylist[-1]-mylist[0]) #범위