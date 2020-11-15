N,M = map(int,input().split())
graph = []

for _ in range(N):
    graph.append(list(input()))

def prettyPrint(myList):
    for my in myList:
        print(my)
    print()

def solve():
    change = 32
    cnt = 64
    for dx in range(N-7):
        for dy in range(M-7):
            chess = [row[dy:dy+8] for row in graph[dx:dx+8]]
            cnt1 = 64
            cnt2 = 64
            prettyPrint(chess)
            for i,ches in enumerate(chess):
                for j,ch in enumerate(ches):
                    if (i+j)%2 == 0:
                        if ch == 'W':
                            cnt1 -= 1
                        else:
                            cnt2 -= 1
                    elif (i+j)%2 == 1:
                        if ch == 'B':
                            cnt1 -= 1
                        else:
                            cnt2 -= 1
            cnt = min(cnt,cnt1,cnt2)
    print(cnt)

solve()


#타인 코드
import sys
from itertools import accumulate as acc
input = sys.stdin.readline
n, m = map(int, input().split())
y = [[0]*(m+1)]
for i in range(n):
    ac = [0]
    ac.extend(acc([((s=='W')+i+j) % 2 for j, s in enumerate(input().rstrip())]))
    y.append([k + j for k, j in zip(ac, y[-1])])

res = 32
for i in range(n-7):
    for j in range(m-7):
        u = y[i+8][j+8]-y[i+8][j]-y[i][j+8]+y[i][j]
        res = min(res, u, 64-u)
print(res)

#타인 코드2
import sys
from itertools import accumulate
input = sys.stdin.readline

n, m = map(int, input().split())
f = lambda x: 1 if x == 'W' else 0
b = [[0 for _ in range(m+1)]]
for i in range(n):
    cost = [0]
    cost.extend(accumulate([(f(s)+i+j) % 2 for j, s in enumerate(input().rstrip())]))
    b.append([k+j for k, j in zip(cost, b[-1])])

result = 32
for i in range(8, n+1):
    for j in range(8, m+1):
        x = b[i][j] + b[i-8][j-8] - b[i][j-8] - b[i-8][j]
        result = min(result, x, 64-x)
print(result)