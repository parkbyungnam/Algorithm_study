import sys
input = sys.stdin.readline
testCase = int(input().rstrip())
for _ in range(testCase):
    a,b = map(int,input().split(','))
    print(a+b)