from itertools import permutations

N,M = map(int,input().split())

mylist = [i for i in range(N,N+1)]
for i in range(N**M):
    for 






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
