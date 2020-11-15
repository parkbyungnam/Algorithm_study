#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split(" "))))
for (first,last) in arr:
    print(first+last)

#타인 코드
import sys
T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)