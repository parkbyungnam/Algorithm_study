#벌집문제

N = int(input())
Flag = True
cnt = 1
S = 6
T = 2
if N==1:
    print('1')
else:
    while Flag is True:
        if N < T:
            print(cnt)
            Flag = False
        else:
            cnt += 1
            T += S
            S += 6