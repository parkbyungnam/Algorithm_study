#시간 초과
import sys
input = sys.stdin.readline
N = int(input())
mylist = [list(map(int,input().split())) for _ in range(N)]

mylist.sort(key=lambda x : x[0])

def solution():
    result = 0
    while mylist != []:
        cnt = 1
        start = mylist.pop(0)
        end_time = start[1]
        for lst in mylist:
            if end_time<=lst[0]:
                cnt+=1
                end_time=lst[1]
        result = max(cnt,result)
    print(result)

solution()


#다른 풀이
N = int(input())
mylist = [list(map(int,input().split())) for _ in range(N)]

mylist.sort(key=lambda x : x[0])
mylist.sort(key=lambda x : x[1])

def solution():
    result = 0
    start_time = 0
    for schedule in mylist:
        if schedule[0] >= start_time:
            result+=1
            start_time=schedule[1]
    print(result)

solution()


#타인 풀이
import sys
In = sys.stdin.readline

def main():
    n = int(In())
    meetings = [(*map(int, In().split()),) for _ in range(n)]
    meetings.sort()
    n, st = 0, float('inf')
    for m in reversed(meetings):
        if m[1] <= st:
            st = m[0]
            n += 1
    print(n)

main()