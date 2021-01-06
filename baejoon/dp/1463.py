#bfs? 나중에 다시 풀어보자.

n = int(input())
dp = [0 for _ in range(n+1)]
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1  
    if i%2 == 0 and dp[i] > dp[i//2] + 1 :
        dp[i] = dp[i//2] + 1
    elif i%3 == 0 and dp[i] > dp[i//3] + 1 :
        dp[i] = dp[i//3] + 1
        
print(dp[n])



n = int(input())
count = 0
while n!=1:
    if n%3 == 0:
        n//=3
        count += 1
    else:
        n-=1
        count += 1
print(count)





1
0

2
1

3
1

4 3 1   4 2 1
2

5 4 3 1   5 4 2 1
3

6 2 1  6 3 1
2

7 6 2 1  7 6 3 1
3

8 4 2 1
3

9 3 1
2

10 9 3 1
3

11 10 9 3 1
4

12 4 2 1
3

13 12 4 2 1
4

14 7 6 2 1
4

15 5 4 3 1
3

16 8 4 2 1    16 15 5 4 3 1

17 16 8 4 2 1

18 6 2 1

19 18 6 2 1

20 10 9 3 1

