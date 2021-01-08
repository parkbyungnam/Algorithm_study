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


#타인 코드
from sys import stdin

stack = []
next(stdin)
for line in stdin:
    command = line.split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if stack: print(stack.pop())
        else: print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack: print(0)
        else: print(1)
    elif command[0] == 'top':
        if stack: print(stack[-1])
        else: print(-1)

#타인 코드2
import sys

# 정수 X를 스택에 넣는 연산이다.
def push(x):
    stack.append(x)

# 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop():
    if(not stack):
        return -1
    else:
        return stack.pop()

# 스택에 들어있는 정수의 개수를 출력한다.
def size():
    return len(stack)

# 스택이 비어있으면 1, 아니면 0을 출력한다.
def empty():
    return 0 if stack else 1

# 스택의 가장 위에 있는 정수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def top():
    return stack[-1] if stack else -1

N = int(input().rstrip())
stack = []

for _ in range(N):
    input_split = input().rstrip().split()

    order = input_split[0]

    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())