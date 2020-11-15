T = set()
for i in range(10):
    T.add(int(input())%42)
print(len(T))

#타인 코드
b = [int(input())%42 for i in range(10)]
print(len(set(b)))