'''
for i in range(1,10,2):
    print(i)
for i in range(20,10000,11):
    print(i)
'''
#나의 틀린 풀이
a=0
b=0
arr=[i for i in range(9999)]
while True:
    arr.remove(11*a+2*b)
    b += 1
    if b==10:
        a += 1
        b = 0
    if a==908 and b == 6:
        break
for i in arr:
    print(i)

#타인 풀이

natural_number_set = set(range(1, 10001))
generated_number_set= set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_number_set.add(i)

self_number_set = natural_number_set - generated_number_set

for i in sorted(self_number_set):
    print(i)

    