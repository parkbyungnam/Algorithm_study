mylist = []

for _ in range(8):
    mylist.append(list(input()))

for i,my in enumerate(mylist):
    for j,m in enumerate(my):
        if i+j%2==1:
            m='.'

result = 0
for my in mylist:
    result+=my.count('F')

print(result)