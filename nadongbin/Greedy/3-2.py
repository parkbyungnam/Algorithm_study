list_len, M, K = map(int,input().split())
mylist = list(map(int,input().split()))

mylist.sort(reverse=True)
big1=mylist[0]
big2=mylist[1]

cnt1 = (M//(K+1))*K + (M%(K+1))
cnt2 = M - cnt1

result = big1*cnt1 + big2*cnt2
print(result)


#다시 풀어보기

N,M,K = map(int,input().split())
mylist = list(map(int,input().split()))

mylist.sort(reverse=True)
big1 = mylist[0]
big2 = mylist[1]

big2_count = M//(K+1)
big1_count = M-big2_count

result = big1*big1_count + big2*big2_count

print(result)


#단순하게 푸는 답안 예시
N,M,K = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[N-1]
second = data[N-2]

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -=1

print(result)
