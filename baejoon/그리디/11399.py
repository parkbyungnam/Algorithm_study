N = int(input())
result = 0
mylist = list(map(int,input().split()))
mylist.sort(reverse=True)

for idx,lst in enumerate(mylist):
    result += (idx+1)*lst
print(result)

#다른 풀이
a = int(input())
total = 0
cur = 0
l = list(map(int, input().split()))

l.sort()
for x in l:
    cur += x
    total += cur
print(total)