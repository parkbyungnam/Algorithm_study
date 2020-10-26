word = list(input())
value = []
Flag = True
while Flag == True:
    for wor in word:
        value.append(ord(wor)-97)
    if value == value[::-1]:
        for wor in word:
            print(wor, end="")
        Flag = False
    else:
        size=len(value)
        value2 = value
        value3 = value[::-1]
        for i in range(size):
            value[i]=value2[i]+value3[i]
        for i in range(size-1):
            if value[size-i-1]>25:
                value[size-i-1]=value[size-i-1]-26
                value[size-i-2] += 1
        if value[0] > 25:
            value.insert(0,1)


#

word = list(input())
value = []
Flag = True
for wor in word:
    value.append(ord(wor)-97)
while Flag == True:
    if value == value[::-1]:
        for val in value:
            val+=97
            print(chr(val),end="")
        Flag = False
    else:
        size=len(value)
        value2 = value
        value3 = value[::-1]
        for i in range(size):
            value[i]=value2[i]+value3[i]
        for i in range(size-1):
            if value[size-i-1]>25:
                value[size-i-1]=value[size-i-1]-26
                value[size-i-2] += 1
        if value[0] > 25:
            value.insert(0,1)
