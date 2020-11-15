#윤년 확인하기

year = int(input())
if year%4==0 and year%100!=0:
    print(1)
elif year%4==0 and year%100==0 and year%400==0:
    print(1)
else:
    print(0)
