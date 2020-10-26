testCase = int(input())
arrlist = list(map(int,input().split()))
while True:
    if 1 in arrlist:
        arrlist.remove(1)
    else:
        break
count = 0
for arrl in arrlist:
    temp = 0
    for arr in range(2, arrl+1):
        if arrl%arr == 0:
            temp += 1
    if temp == 1:
        count += 1
print(count)
#arr = input().split()
#arrlist = list(map(int,arr))
#if arr.find('1'):
#    arr.remove(1)
