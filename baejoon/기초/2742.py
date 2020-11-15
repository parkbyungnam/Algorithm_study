#기찍 N
# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

N = int(input())
for a in range(N,0,-1):
    print(a)

#타인 코드
n=int(input())
print("\n".join(map(str, range(n, 0, -1))))