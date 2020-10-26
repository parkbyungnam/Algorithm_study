N, M = map(int, input().split())
broad = []
dices = []
point = 1
past_location = 1
for _ in range(N):
    broad.append(input())
for _ in range(M):
    dices.append(int(input()))
for index,dice in enumerate(dices):
    if broad[past_location-1]=="+" and past_location+dice<=N:
        past_location+=dice
    elif broad[past_location-1]=="-" and past_location-dice>=1:
        past_location-=dice
        if past_location == 1:
            point+=1
print(point)