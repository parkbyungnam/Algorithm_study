testCase = int(input())

for _ in range(testCase):
    myData = input()
    myList = []
    Flag = True
    for data in myData:
        if data == '(':
            myList.append(1)
        else:
            if not myList:
                print("NO")
                Flag = False
                break
            else:
                myList.pop()
    if Flag == True:
        if not myList:
            print('YES')
        else:
            print('NO')

#타인 코드
from sys import stdin

n = int(input())
for _ in range(n):
    str_ = stdin.readline().strip()
    stack = 0
    for chr_ in str_:
        if chr_ == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print('YES')
    else:
        print('NO')