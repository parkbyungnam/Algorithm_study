try:
    a = int(input())
    check = a
    temp = -1
    count = 0
    if a<0 or a>100:
        raise ValueError("Invalid input")
except ValueError as e:
    print(e)
else:
    while check!=temp:
        count += 1
        a01 = a%10
        a10 = a//10
        temp = a01*10 + (a10 + a01)%10
        a = temp
    print(count)