from collections import deque
n, k = map(int, input().split())
josephusProblem = deque([])
for i in range(1, n + 1):
    josephusProblem.append(i)
print('<', end='')
while josephusProblem:
    for _ in range(k - 1):
        josephusProblem.append(josephusProblem[0])
        josephusProblem.popleft()
    print(josephusProblem.popleft(), end='')
    if josephusProblem:
        print(', ', end='')
print('>')