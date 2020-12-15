from operator import itemgetter
testCase = int(input())
mylist = []
for i in range(testCase):
    age,name = input().split()
    mylist.append([int(age),name,i])
mylist.sort(key=itemgetter(0,2))
for my in mylist:
    age,name,i = my
    print(age,name)

# rstrip 확인하자
from operator import itemgetter
import sys

input = sys.stdin.readline
testCase = int(input())
mylist = []
for i in range(testCase):
    age,name = input().rstrip().split()
    mylist.append([int(age),name,i])
mylist.sort(key=itemgetter(0,2))
for my in mylist:
    age,name,i = my
    print(age,name)