#정수 라운드 함수로 처리
a = 0.3 + 0.6
print(a)
print(round(a,2))

#거듭제곱
print(2**3)

#리스트
a= [3,5,4,3,2]
#c/c++ : int a[] = {3,5,4,3,2};
#Java : int[] a = {3,5,4,3,2};
print(a)

#리스트 컴프리헨션
#1부터 20까지 홀수만 리스트 원소로 초기화
array = [i for i in range(20) if i % 2 ==1]
print(array)
#사용하지 않는다면
a = []
for i in range(20):
    if i%2 == 1:
        a.append(i)
print(a)

#2차원 리스트 초기화 할 때 효과적으로 사용
array = [[0]*m for _ in range(n)]

n = 4
m = 3
array=[[0]*m for _ in range(n)]
print(array)

#잘못된 에시
array = [[0]*m]*n



a=[1,2,3,4,5,5,5]
remove_set = {3,5}

#2차원 배열
n = int(input())
m = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

#빠르게 입력받기
import sys
data = sys.stdin.readlines()

