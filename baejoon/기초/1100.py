mylist = []

for _ in range(8):
    mylist.append(list(input()))

for i in range(8):
    for j in range(8):
        if (i+j)%2==1:
            mylist[i][j]='.'

result = 0
for my in mylist:
    result+=my.count('F')

print(result)