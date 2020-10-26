# N찍기
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.


N = int(input())
for i in range(N):
    print(i+1)


#타인 코드
n=int(input())
print("\n".join(map(str,range(1,n+1))))