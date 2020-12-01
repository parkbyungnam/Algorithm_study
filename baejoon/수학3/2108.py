from collections import Counter

n = int(input())
mylist = [int(input()) for _ in range(n)]

#중앙값
mylist.sort()

#최빈값



#산술평균출력
print(sum(mylist)//n)

#중앙값 출력
print(mylist[n//2])

#최빈값 출력


#범위 출력
print(mylist[-1]-mylist[0])