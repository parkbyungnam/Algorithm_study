#다른 풀이
def solution(n,r):
    output = 0
    while n!=0:
        n = n//r
        output += n
    return output

n,m = map(int, input().split())

print(min(solution(n,2)-solution(n-m,2)-solution(m,2),solution(n,5)-solution(n-m,5)-solution(m,5)))



#틀린 풀이
import math

n,m = map(int,input().split())

num = math.factorial(n)//(math.factorial(m)*math.factorial(n-m))

for i in range(0,len(str(num))):
    if num%(10**(i+1))!=0:
        print(i)
        break