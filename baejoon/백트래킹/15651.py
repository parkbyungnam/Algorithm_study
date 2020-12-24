#참고하면 좋은 자료
#https://ghwlchlaks.github.io/permutation-combination-python


N,M = map(int,input().split())
result = [0 for _ in range(M)]

def solution(index,N,M):
    if index==M:
        for re in result:
            print(re,end=" ")
        print()
        return
    else:
        for i in range(1,N+1):
            result[index]=i
            solution(index+1,N,M)

solution(0,N,M)


#타인 풀이

import sys
from itertools import product

def testCase():
    input_val = list(map(int, sys.stdin.readline().split()))
    global N, M
    N, M = input_val

def solve(remain):
    res = list(map(' '.join, product(remain, repeat=M)))
    print('\n'.join(res))

if __name__ == "__main__":
    testCase()
    solve(map(str, list(range(1, N+1))))


#타인 풀이

n,m=map(int,input().split())
 
result=[0 for _ in range(m)]
 
def backtracking(index,n,m):
    if index==m:
        for i in result:
            print(i,end=" ")
        print()
        return
 
    for i in range(1,n+1):
        result[index]=i
        backtracking(index+1,n,m)
 
 
backtracking(0,n,m)
