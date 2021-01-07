testCase = int(input())
mylist = [input() for _ in range(testCase)]
myStack = []

for myl in mylist:
    if myl[0] == 'p':
        if myl[1] == 'u': # Push
            temp = int(myl[5:])
            myStack.append(temp)
        else: # Pop
            if not myStack: #리스트가 비어있을 때 
                print(-1)
            else: #리스트가 비어있지 않을 때 pop
                print(myStack.pop())
    elif myl[0] == 's': # Size
        print(len(myStack))
    elif myl[0] == 'e': # Empty
        if not myStack: #리스트가 비어있을 때
            print(1)
        else:
            print(0)
    else: # Top
        if not myStack:
            print(-1)
        else:
            print(myStack[-1])


