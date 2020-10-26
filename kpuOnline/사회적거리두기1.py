N = int(input())
deskArr = list(input())
distance = []
count = 0
for idx, desk in enumerate(deskArr):
    if desk == '0':
        if idx == N-1:
            count += 1
            distance.append(count)
        else:
            count += 1
    else:
        if idx == 0:
            continue
        distance.append(count)
        count = 0
distance.sort()
first = distance[-1]
second = distance[-2]
third = distance[-3]

100000100100000010


N = int(input())
deskArr = list(input())
location1 = []
for idx,desk in enumerate(deskArr):
    if desk == '1':
        location1.append(idx)
if deskArr[0] == '0' and deskArr[-1] == '0':
    distance = []
    if location1 == []:
        print(N-1)
    else:
        cntOne=len(location1)
        if cntOne == 1:
            
        else:
            for i in range(cntOne-1):
                distance.append(location1[i+1]-location1[i])
elif deskArr[0] == '0' and deskArr[-1] == '1':

elif deskArr[0] == '1' and deskArr[-1] == '0':

else:


distance = []
for i in range(len(location1)-1):
    distance.append(location1[i+1]-location1[i])