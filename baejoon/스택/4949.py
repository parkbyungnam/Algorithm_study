def checkBalance(myString):
    small = 0
    large = 0
    flag = True
    for st in myString:
        if st == '(':
            small += 1
            flag2 = 1
        elif st == ')':
            small -= 1
        elif st == '[':
            large += 1
            flag2 = 2
        elif st == ']':
            large -= 1
        if small < 0 or large < 0:
            flag = False
    if small == 0 and large == 0 and flag:
        return True
    else:
        return False

flag = True
while flag:
    myString = input()
    if myString == '.':
        flag=False
    else:
        if checkBalance(myString):
            print('yes')
        else:
            print('no')