N, K = map(int,input().split())
cnt = 0
Flag = True

while Flag:
    if N == 1:
        print(cnt)
        Flag = False
    elif N%K == 0:
        N = N//K
        cnt+=1
    else:
        N = N-1
        cnt += 1


#다른 풀이
n,k =map(int,input().split())

while True:
    #n,k로 나눠지는 수까지 한번에 빼기
    target = (n//k)*k
    result = n-target
    n=target
    #n이 k보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
    if n<k:
        break
    result += 1
    n //= k

#마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)