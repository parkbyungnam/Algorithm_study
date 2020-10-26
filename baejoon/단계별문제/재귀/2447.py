#재귀를 사용한 올바른 풀이
def stars(n):
    matrix=[]
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))

star = ["***","* *","***"]
n = int(input())
k = 0
while n != 3:
    n = int(n / 3)
    k += 1
    
for i in range(k):
    star = stars(star)
for i in star:
    print(i)

#백준 코드 (가장 빠름)
def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]

def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    a = concatenate(x, x)
    b = concatenate(x, [' '*n]*n)
    return a + b + a

print('\n'.join(star10(int(input()))))

#띄여져 있는 공간 찾기
n=int(input())
arr = [["*"]*n for _ in range(n)]

v=n
cnt=0
while v!=1:
    v/=3
    cnt+=1

for cnt_ in range(cnt):
    idx = [i for i in range(n) if (i // 3 ** cnt_) % 3 == 1] 
    for i in idx:
        for j in idx:
            arr[i][j] = " " 

print('\n'.join([''.join([str(i) for i in row]) for row in arr]))




