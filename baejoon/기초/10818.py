#최대 최소값 구하기

T = int(input())
arr = []
arr = list(map(int,input().split(" ")))
print(min(arr), max(arr))


#다른 풀이

T = int(input())
arr = sorted(map(int,input().split(" ")))
print(arr[0], arr[T-1])