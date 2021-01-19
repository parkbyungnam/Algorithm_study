from collections import deque
import sys

input = sys.stdin.readline
testCase = int(input())

deq = deque()
for _ in range(testCase):
    mylist = list(input().split())
    if mylist[0]=='push_back':
        deq.append(mylist[1])
    elif mylist[0]=='push_front':
        deq.appendleft(mylist[1])
    elif mylist[0]=='pop_front':
        print(deq.popleft() if deq else -1)
    elif mylist[0]=='pop_back':
        print(deq.pop() if deq else -1)
    elif mylist[0]=='size':
        print(len(deq))
    elif mylist[0]=='empty':
        print(0 if deq else 1)
    elif mylist[0]=='front':
        print(deq[0] if deq else -1)
    elif mylist[0]=='back':
        print(deq[-1] if deq else -1)