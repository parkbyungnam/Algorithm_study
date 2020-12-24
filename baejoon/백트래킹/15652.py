#참고하면 좋은 자료
#https://ghwlchlaks.github.io/permutation-combination-python


from itertools import combinations_with_replacement
n,m = map(int,input().split())
mylist = [i for i in range(1,n+1)]
result = list(combinations_with_replacement(mylist,m))
for re in result:
    for r in re:
        print(r,end=" ")
    print()



#타인 풀이
from itertools import combinations_with_replacement

n, m = map(int, input().split())

print("\n".join(map(" ".join, combinations_with_replacement(map(str, range(1, n+1)), m))))