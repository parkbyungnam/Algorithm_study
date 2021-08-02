numbers=list()
for _ in range(int(input())):
    numbers.append(int(input()))
numbers.sort(reverse=True)
for number in numbers:
    print(number, end=' ')