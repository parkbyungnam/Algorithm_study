from collections import Counter

testCase = int(input())
mylist = []
for _ in range(testCase):
    mylist.append(int(input()))

mylist.sort()
print(round(sum(mylist)/testCase)) #산술평균
print(mylist[testCase//2]) #중앙값

#최빈값
mycount = Counter(mylist).most_common(2)
if len(mycount)==1:
    print(mycount[0][0])
else:
    if mycount[0][1]==mycount[1][1]:
        print(mycount[1][0])
    else:
        print(mycount[0][0])

print(mylist[-1]-mylist[0]) #범위


#my Count
def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

countLetters('hello world')
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}