testCase = int(input())
mylist = []

for i in range(testCase):
    myInput = int(input())
    if myInput == 0:
        mylist.pop()
    else:
        mylist.append(myInput)

print(sum(mylist))