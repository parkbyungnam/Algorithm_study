N = int(input())
mylist = []
my_n = N//2 + 1
def is_prime(N):
    return all([(N%j) for j in range(2,int(N**0.5)+1)]) and N>1

def factoriztion(N):
    if N==1:
        return
    else:
        for i in range(2,my_n):
            if N%i==0:
                mylist.append(i)
                return factoriztion(N//i)
                

if is_prime(N):
    print(N)
else:
    factoriztion(N)
    for my in mylist:
        print(my)


#타인 코드
n = int(input())
i = 2
r = int(n ** 0.5)

while i <= r:
    while not n % i:
        print(i)
        n //= i
    i += 1
if n > 1:
    print(n)