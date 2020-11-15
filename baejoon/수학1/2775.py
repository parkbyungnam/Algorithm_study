apart = [[i for i in range(1,15)]]
for _ in range(14):
    apart.append([1 for _ in range(14)])
for i in range(14):
    for j in range(13):
        apart[i+1][j+1] = apart[i][j+1] + apart[i+1][j]
testCase = int(input())
for _ in range(testCase):
    i = int(input())
    j = int(input())
    print(apart[i][j-1])