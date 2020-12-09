testCase = int(input())
mylist = []
for _ in range(testCase):
    word = list(input())
    if word not in mylist:
        mylist.append(word)
mylist.sort()
mylist.sort(key=lambda x:len(x))
for my in mylist:
    for m in my:
        print(m,end='')
    print()


#다른 사람 풀이
#tip  문자열을 입력받을 떄는 rstrip()을 해주는 편이 좋다.
import sys
word=set()
for i in range(int(input())):
    word.add(sys.stdin.readline().rstrip())
word=list(word)
word.sort()
word.sort(key=lambda x:len(x))
print("\n".join(word))