import itertools

N,M = map(int,input().split())
mylist = [i for i in range(1,N+1)]
result = list(itertools.combinations(mylist,M))
for re in result:
    for r in re:
        print(r,end=' ')
    print()



#타인 풀이

n, m = map(int, input().split())    # n까지 m개
check=[0 for _ in range(n+1)]
result=[0 for _ in range(m)]
 
 
def backtracking(index,n,m):
    if index==m:
        for i in range(m):
            print(result[i], end=' ')
        print()
        return
 
    for i in range(1,n+1):
        if check[i]==1:#이전에 썻다면
            continue
        result[index]=i #해당위치에 넣어줌
        for j in range(i+1):
            check[j]=1  #들어간 숫자보다 작은숫자 다 체크
        backtracking(index+1,n,m)
        for j in range(1,n+1):
            check[j]=0 #다음수로 넘어가기전에 전부 초기화
 
backtracking(0,n,m)
