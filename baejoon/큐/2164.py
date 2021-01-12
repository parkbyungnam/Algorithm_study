from collections import deque

N = int(input())
queue = deque(i for i in range(1,N+1))
result = 0
while queue:
    temp = queue.popleft()
    if not queue:
        print(temp)
        break
    else:
        queue.append(queue.popleft())
