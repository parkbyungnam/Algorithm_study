from collections import deque

question = list(input())
queue = deque()
result = 0
multiply = 1

for ques in reversed(question):
    if ord(ques)==45: # if -
        question.pop()
        while queue:
            element = queue.popleft()
            if ord(element)==43:
                multiply = 1
            else:
                num = int(element)
                result += -1 * num * multiply
                multiply *= 10
        multiply = 1
    else:
        queue.append(question.pop())

multiply = 1

while queue:
    element = queue.popleft()
    if ord(element)==43:
        multiply = 1
    else:
        num = int(element)
        result += num*multiply
        multiply *= 10

print(result)


#타인 코드
arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)

#타인 코드
e = [sum(map(int, x.split('+'))) for x in input().split('-')]
print(e[0]-sum(e[1:]))


#다시 풀어보기
data = input().split('-')
result = 0
for num in data[0].split('+'):
    result += int(num)
for plus in data[1:]:
    for num in plus.split("+"):
        result -= int(num)
print(result)
