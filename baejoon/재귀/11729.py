def hanoi(n,a,b,c):
    if n==1:
        print(a,c)
        return
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)

testCase = int(input())
sum = 1
for i in range(testCase-1):
    sum = sum * 2 + 1
print(sum)
hanoi(testCase,1,2,3)