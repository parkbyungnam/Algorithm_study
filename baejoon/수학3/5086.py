Flag = True
while Flag:
    N,M = map(int,input().split())
    if N==0 and M==0:
        Flag = False
    elif N%M == 0:
        print('multiple') #배수
    elif M%N == 0:
        print('factor') #약수
    else:
        print("neiter")

#다른 풀이
Flag = True
while Flag:
    N,M = map(int,input().split())
    if N==0 and M==0:
        Flag = False
    elif (N/M).is_integer():
        print('multiple') #배수
    elif (M/N).is_integer():
        print('factor') #약수
    else:
        print("neiter")