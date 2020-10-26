# 영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다.
# 이 문자열에는 몇 개의 단어가 있을까?
# 이를 구하는 프로그램을 작성하시오.
# 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

strings = input()
target = " "
if strings[0]==target and strings[len(strings)-1]==target:
    print(strings.count(target)-1)
elif strings[0]==target or strings[len(strings)-1]==target:
    print(strings.count(target))
else:
    print(strings.count(target)+1)


#봉남 다른 풀이 strip() 사용

strings = input().strip()
target = " "
print(strings.count(target)+1)