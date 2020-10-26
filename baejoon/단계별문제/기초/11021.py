#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

T = int(input())
for case in range(T):
    a,b = map(int,input().split(" "))
    print(f"Case #{case+1}: {a+b}")

#타인 코드
import sys
num=int(input())

for i in range(num):
    a,b=map(int,sys.stdin.readline().split())
    print("Case #%d:"%(i+1),a+b)