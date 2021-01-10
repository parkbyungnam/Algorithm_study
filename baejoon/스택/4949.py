def checkBalance(myString):
    myList = []
    flag = True
    for st in myString:
        if st == '(':
            myList.append('(')
        elif st == ')':
            if not myList:
                flag = False
                break
            else:
                temp = myList.pop()
                if temp != '(':
                    flag = False
                    break

        elif st == '[':
            myList.append('[')
        elif st == ']':
            if not myList:
                flag = False
                break
            else:
                temp = myList.pop()
                if temp != '[':
                    flag = False
                    break
    if not myList and flag:
        return True
    else:
        return False

if __name__=='__main__':
    flag = True
    while flag:
        myString = input()
        if myString == '.':
            flag = False
            break
        else:
            if checkBalance(myString):
                print('yes')
            else:
                print('no')
