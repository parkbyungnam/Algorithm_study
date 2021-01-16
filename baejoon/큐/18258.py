from collections import deque
import sys
input = sys.stdin.readline
testCase=int(input())
queue = deque()
for _ in range(testCase):
    mylist = list(input().split())
    if mylist[0]=='push':
        queue.append(mylist[1])
    elif mylist[0]=='pop':
        print(queue.popleft() if queue else -1)
    elif mylist[0] == 'size':
        print(len(queue))
    elif mylist[0] == 'empty':
        print(0 if queue else 1)
    elif mylist[0] == 'front':
        print(queue[0] if queue else -1)
    elif mylist[0] == 'back':
        print(queue[-1] if queue else -1)