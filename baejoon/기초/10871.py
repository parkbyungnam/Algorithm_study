#정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
import sys

num, C = map(int, input().split(" "))
arr2 = map(int, sys.stdin.readline().split())
for i,v in enumerate(arr2):
    if arr2[i]<C:
        print(arr2[i],end=" ")

#타인 코드
import sys

n, x = map(int, sys.stdin.readline().split())
n_numbers = map(int, sys.stdin.readline().split())

smaller_than_x = []

for number in n_numbers:
    if number < x:
        smaller_than_x.append(number)
print(' '.join(map(str, smaller_than_x)))