flag = True
while flag is True:
    a,b = map(int,input().split(" "))
    if a == 0 and b == 0:
        flag = False
    else:
        print(a+b)


#다른 사람 코드
import sys

while True:
	(a, b) = map(int, sys.stdin.readline().split())
	if (a == 0 and b == 0):
		break
	print(a+b)