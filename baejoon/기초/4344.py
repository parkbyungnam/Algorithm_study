for _ in range(int(input())):
    temp = []
    a=list(map(int,input().split()))
    avg = sum(a,-a[0])/(len(a)-1)
    for i in range(1,len(a)):
        if a[i]>avg:
            temp.append(a[i])
    P = len(temp) / a[0] * 100
    print(f'{P:0.3f}%')
