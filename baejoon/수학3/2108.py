from collections import Counter

n = int(input())
mylist = [int(input()) for _ in range(n)]

#중앙값
mylist.sort()

#최빈값



#산술평균출력
print(sum(mylist)//n)

#중앙값 출력
print(mylist[n//2])

#최빈값 출력


#범위 출력
print(mylist[-1]-mylist[0])



#내풀이

from collections import Counter
import sys

testCase = int(sys.stdin.readline())
mylist = []
for _ in range(testCase):
    mylist.append(int(sys.stdin.readline()))

mylist.sort()
print(round(sum(mylist)/testCase)) #산술평균
print(mylist[testCase//2]) #중앙값

#최빈값
mycount = Counter(mylist).most_common(2)
if len(mycount)==1:
    print(mycount[0][0])
else:
    if mycount[0][1]==mycount[1][1]:
        print(mycount[1][0])
    else:
        print(mycount[0][0])

print(mylist[-1]-mylist[0]) #범위

