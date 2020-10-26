repetition = int(input())
for _ in range(repetition):
    H,W,N = map(int,input().split())
    if N/H == N//H:
        if N%H == 0:
            print(f'{H}{N//H:02d}')
        else:
            print(f'{N%H}{N//H:02d}')    
    else:
        if N%H == 0:
            print(f'{H}{N//H+1:02d}')
        else:
            print(f'{N%H}{N//H+1:02d}')


#다른 풀이
repetition = int(input())
for _ in range(repetition):
    H,W,N = map(int,input().split())
    print(str((N-1)%H+1) + str((N-1)//H+1).rjust(2,"0"))
    #print(f'{(N-1)%H+1}{(N-1)//H+1:02d}')


        #승빈#4944
        #coysstream
