# 그룹 단어 체커

# 그룹 단어란 단어에 존재하는 모든 문자에 대해서,
# 각 문자가 연속해서 나타나는 경우만을 말한다.
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.



repetition = int(input())
GroupWord = 0
arr = [0 for _ in range(100)]
for _ in range(repetition):
    strings = input()
    set_strings=list(set(strings))
    temp = 0
    for i,set_string in enumerate(set_strings):
        for index,string in enumerate(strings):
            if strings.find(set_string,index)-strings.find(set_string,index+1)<-1:
                temp -= 1
                break
    if temp == 0:
        GroupWord += 1
print(GroupWord)


#다른 풀이
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)

#다른 풀이2
result = int(input())
for _ in range(result):
    word = input()
    for i in range(1, len(word)):
        if word.find(word[i-1]) > word.find(word[i]):
            result -= 1
            break
print(result)