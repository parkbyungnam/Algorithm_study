#n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
a = int(input())
b = 0
for c in range(a+1):
    b += c
print(b)

#다른 코딩
print(sum(range(int(input())+1)))

#다른 코딩2
n = int(input())
print((n**2+n)//2)