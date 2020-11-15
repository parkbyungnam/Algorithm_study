# (몸무게, 키)
# 틀린 풀이
# 정답을 모르겠음. 수정 시 삭제 예정
from operator import itemgetter

testCase = int(input())
people = []
for _ in range(testCase):
    people.append(list(map(int,input().split())))
weight = []
height = []
total = []

for index,person in enumerate(people):
    person.append(index)

people.sort(key=lambda x:x[0])
rank = people[0][0]
index = 1
for person in people:
    if rank==person[0]:
        weight.append([index,person[2]])
    else:
        index+=1
        weight.append([index,person[2]])


people.sort(key=itemgetter(1))
rank = people[0][1]
index = 1
for index,person in enumerate(people):
    if rank==person[1]:
        height.append([index,person[2]])
    else:
        index+=1
        height.append([index,person[2]])

weight.sort(key=lambda x:x[1])
height.sort(key=lambda x:x[1])

for index in range(testCase):
    total.append([weight[index][0]+height[index][0],index])
total.sort(key=lambda x:-x[0])

temp = total[0][0]
rank = 1
up = 0
for score in total:
    if temp==score[0]:
        score.append(rank)
        up += 1
    elif temp>score[0]:
        temp=score[0]
        rank += up
        score.append(rank)
total.sort(key=lambda x:x[1])
for arr in total:
    print(arr[2],end=" ")



#다른 사람 풀이
testCase = int(input())

people = []
for _ in range(testCase):
    weight, height = map(int, input().split())
    people.append((weight, height))

for c in people : #0
    rank = 1 #1 
    for n in people:
        if (c[0]<n[0]) & (c[1]<n[1]): #3 w, h 모두 큰 경우
            rank += 1
    print(rank)