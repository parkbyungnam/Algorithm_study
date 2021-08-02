def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid + 1
    return None

n, target = list(map(int,input().split()))
array=list(map(int,input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)


## 입력 값
# 10 7
# 1 3 5 7 9 11 13 15 17 19

##출력값
# 4



## 입력 값
# 10 7
# 1 3 5 8 9 11 13 15 17 19

##출력값
# 원소가 존재하지 않습니다.