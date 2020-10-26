#M = 가로
#N = 세로

import sys
input = sys.stdin.readline

M,N = map(int,input().split())
forest = []
for _ in range(M):
    forest.append([*map(int,input().split())])
testCase = int(input())
for _ in range(testCase):
    result = 0
    a1, b1, a2, b2 = map(int,input().split())
    for y in range(b1-1,b2):
        for x in range(a1-1,a2):
            result+=forest[x][y]
    print(result)

#

M,N = map(int,input().split())
forest = []
for _ in range(M):
    forest.append(list(map(int,input().split())))
testCase = int(input())

for _ in range(testCase):
    result = 0
    a1, b1, a2, b2 = map(int,input().split())
    solution(forest,a1,b1,a2,b2)

def solution(forest,a1,b1,a2,b2):
    result = 0
    for y in range(b1-1,b2):
        for x in range(a1-1,a2):
            result+=forest[x][y]
    print(result)



import sys
input = sys.stdin.readline

def solution(forest,a1,b1,a2,b2):
    result = 0
    for y in range(b1-1,b2):
        for x in range(a1-1,a2):
            result+=forest[x][y]
    print(result)

M,N = map(int,input().split())
forest = []
for _ in range(M):
    forest.append([*map(int,input().split())])
testCase = int(input())
for _ in range(testCase):
    result = 0
    a1, b1, a2, b2 = map(int,input().split())
    solution(forest,a1,b1,a2,b2)




#6개 맞은 것
import sys
input = sys.stdin.readline

def solution(forest,a1,b1,a2,b2):

    result = 0
    for y in range(b1-1,b2):
        for x in range(a1-1,a2):
            result+=forest[x][y]
    print(result)

M,N = map(int,input().split())
forest = []
for _ in range(M):
    forest.append([*map(int,input().split())])
testCase = int(input())
for _ in range(testCase):
    a1, b1, a2, b2 = map(int,input().split())
    solution(forest,a1,b1,a2,b2)







#새로운 풀이 
def solution(forest,ar):
    result = 0
    for y in range(ar[1]-1,ar[3]):
        for x in range(ar[0]-1,ar[2]):
            result+=forest[x][y]
    print(result)

M,N = map(int,input().split())
forest = []
for _ in range(M):
    forest.append([*map(int,input().split())])
testCase = int(input())
arr = []
for _ in range(testCase):
    arr.append(list(map(int,input().split())))
for ar in arr:
    solution(forest,ar)

