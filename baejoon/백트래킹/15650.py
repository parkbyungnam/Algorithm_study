import itertools

N,M = map(int,input().split())
mylist = [i for i in range(1,N+1)]
result = list(itertools.combinations(mylist,M))
for re in result:
    for r in re:
        print(r,end=' ')
    print()