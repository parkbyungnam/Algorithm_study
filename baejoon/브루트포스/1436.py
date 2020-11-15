N = int(input())
cnt = 0
movie_name = 666
while True:
    if '666' in str(movie_name):
        cnt += 1
    if N == cnt:
        print(movie_name)
        break
    movie_name+=1


#타인 풀이

N = int(input())
front = 0
back = 0
fronttemp = 0
backlength = 0
backlimit = 0
pos = -1
state = 'front'


for _ in range(N-1) :
    if state == 'front' :
        front += 1
        pos = str(front*100 + 66).find('666')
        if pos != -1 :
            state = 'back'
            backlength = len(str(front)) - pos
            backlimit = 10**backlength
            fronttemp = front // backlimit
            back = 0
    else :
        back += 1
        if back >= backlimit :
            state = 'front'
            front += 1

if state == 'front' :
    print(front*1000 + 666)
else :
    print((fronttemp*1000 + 666)*backlimit + back)