n=int(input())
counters=[0]*200000001
n_list=list(map(int,input().split()))

for n_var in n_list:
    counters[n_var+10000000]+=1

m=int(input())
m_list=list(map(int,input().split()))

for m_var in m_list:
    print(counters[m_var+10000000], end=' ')


#
from bisect import bisect_left, bisect_right

n=int(input())
n_list=list(map(int,input().split()))
m=int(input())
m_list=list(map(int,input().split()))

n_list.sort()

for m_var in m_list:
    index_left=bisect_left(n_list,m_var)
    index_right=bisect_right(n_list,m_var)
    print(index_right-index_left, end=' ')



#
from sys import stdin
from collections import Counter
_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

C = Counter(N)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))