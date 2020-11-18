N = int(input())
mylist = [0 for _ in range(100001)]
for _ in range(N):
    M = int(input())
    mylist[M] += 1

for idx,my in enumerate(mylist):
    if my>=1:
        for _ in range(my):
            print(idx)

#타인 코드

f = open(0) 
f.readline()
li=[0]*10001
for line in f:
    li[int(line)] += 1

for i in range(1, 10001):
    print(f'{i}\n' * li[i], end='')