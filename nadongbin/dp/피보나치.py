# 재귀적인 풀이

def pibo(x):
    if x==1 or x==2:
        return 1
    else:
        return pibo(x-1) + pibo(x-2)



# 메모이제이션을 활용하여 재귀적으로 풀기, 탑다운(하향식) 방식

d=[0] * 100

def fibo(x):
    if x==1 or x==2:
        return 1
    if d[0] != 0:
        return d[x]
    d[x] = fibo[x-1] + fibo[x-2]
    return d[x]


# 반복적으로 풀기, 바텀업(상향식) 방식
# dp 풀이에서는 왠만하면 가장 효율적임

d=[0]*100

d[1]=1
d[2]=1
n=99

for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]

print(d[n])