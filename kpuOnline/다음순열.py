n,k = map(int,input().split())


def next_permutation(a):
    n = len(a)-1
    i = n
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
       
    if i == 0:
        return False
    
    j = n
    while a[i-1] >= a[j]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    
    j = n
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

for _ in range(k):
    a = list(map(int, input().split()))
    if next_permutation(a) == True:
        for i in a:
            print(i, end=' ')
        print()
    else:
        print(-1)
