def binary_search(n_list,m_var,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if n_list[mid]==m_var:
        return True
    elif n_list[mid]>m_var:
        binary_search(n_list,m_var,start,mid-1)
    else:
        binary_search(n_list,m_var,mid+1,end)

n=int(input())
n_list=list(map(int,input().split()))

m=int(input())
m_list=list(map(int,input().split()))

n_list.sort()

for m_var in m_list:
    in_list = binary_search(n_list,m_var,0,n-1)
    if not in_list:
        print('no', end=' ')
    else:
        print('yes', end=' ')

# 왜 9 는 None 을 반환하는지 모르겠네..
###





from bisect import bisect_left
n=int(input())
n_list=list(map(int,input().split()))

m=int(input())
m_list=list(map(int,input().split()))

n_list.sort()

for m_var in m_list:
    index=bisect_left(n_list,m_var)
    
    if index<n:
        n_var = n_list[index]
        if n_var==m_var:
            print('yes', end=' ')
        else:
            print('no', end=' ')
    else:
        print('no', end=' ')
