import itertools

N,M=map(int,input().split())
mylist = [i for i in range(1,N+1)]
result = list(itertools.permutations(mylist,M))
for re in result:
    for r in re:
        print(r,end=' ')
    print()

#순열
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result



#타인 풀이 1
N, M = map(int, input().split())

num_list = [i + 1 for i in range(N)]
check_list = [False] * N

arr = []

def dfs(cnt):
    # 주어진 개수만큼 채워지면 출력한다
    if(cnt == M):
        print(*arr)
        return
    
    for i in range(0, N):
        if(check_list[i]):
            continue
        
        # i번째는 거쳐갈거라서 True로 바꾼다.
        check_list[i] = True
        arr.append(num_list[i])
        # 현재의 i를 기준으로 가지치기 시작
        dfs(cnt + 1)
        # 이 부분은
        arr.pop()
        # 여기서 print(arr)을 해보면 작동원리를 알 수 있다.
#         print(arr)
#         print(check_list)
        check_list[i] = False
        
dfs(0)

#타인풀이1.5

n, m = map(int, input().split())    # n까지 m개
check=[0 for _ in range(n+1)]
result=[0 for _ in range(m)]
 
def sequence(index,n,m):
    if index==m:
        for i in range(m):
            print(result[i], end=' ')
        print()
        return
 
    for i in range(1,n+1):
        if check[i]==1:#이전에 썻다면
            continue
        result[index]=i #해당위치에 넣어줌
        check[i]=1  #들어간거 체크표시
        sequence(index+1,n,m)
        check[i]=0 #다음수로 넘어가기전에 초기화
 
 
sequence(0,n,m)






#다른사람 풀이 2
from itertools import permutations

N, M = map(int, input().split())
li = map(str, range(1, N+1))
print('\n'.join(list(map(' '.join,permutations(li, M)))))
