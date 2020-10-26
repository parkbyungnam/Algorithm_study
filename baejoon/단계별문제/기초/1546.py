C = int(input())
arr = []
arr.extend(list(map(int,input().split())))
avg = sum(arr)/len(arr)
new_avg = avg*100/max(arr)
print(new_avg)

#타인 코드
n = int(input())
a=list(map(int,input().split()))
m = max(a)
for i in range(n):
    a[i] = a[i]/m*100
print(sum(a)/n)