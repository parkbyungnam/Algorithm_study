# 세 개의 자연수 A, B, C가 주어질 때 A×B×C를 계산한 결과에 0부터 9까지
# 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면 
# A × B × C = 150 × 266 × 427 = 17037300 이 되고, 
# 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

arr=[int(input())for _ in range(3)]
temp = 1
count = [0 for _ in range(10)]
for i in range(3):
    temp = temp*arr[i]
arr2=list(str(temp))
for i in range(len(arr2)):
    count[int(arr2[i])]+=1
for i in range(10):
    print(count[i])

#타인 코드
n=[int(input()) for x in range(3)]
m=n[0]*n[1]*n[2]

for x in range(10):
    print(str(m).count(str(x)))