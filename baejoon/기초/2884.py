#알람 시계
hour,minute = map(int,input().split(" "))

minute = minute - 45

if minute < 0:
    minute = minute * -1
    minute = 60 - minute
    if hour == 0:
        hour = 24
    hour -= 1
print(hour,minute)

#다른 사람 답안
a,b=map(int,input().split())
x=a*60+b-45
print(x//60%24,x%60)