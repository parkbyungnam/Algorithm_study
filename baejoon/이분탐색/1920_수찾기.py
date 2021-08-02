from bisect import bisect_left

n=int(input())
n_list=list(map(int,input().split()))

m=int(input())
m_list=list(map(int,input().split()))

n_list.sort()

for m_var in m_list:
    index=bisect_left(n_list, m_var)
    if index<n:
        if n_list[index]==m_var:
            print(1)
        else:
            print(0)
    else:
        print(0)



###------ 다른 풀이

n=int(input())
n_list=set(map(int,input().split()))
m=int(input())
m_list=list(map(int,input().split()))

for m_var in m_list:
    if m_var in n_list:
        print(1)
    else:
        print(0)