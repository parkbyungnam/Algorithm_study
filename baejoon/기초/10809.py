# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

S = input()
arrAlpa = [-1 for _ in range(26)]
for i,v in enumerate(reversed(S)):
    arrAlpa[ord(v)-97]=len(S)-i-1
for i in arrAlpa:
    print(i,end=" ")

#다른 사람 풀이
string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end = ' ')