# 알파벳 대소문자로 된 단어가 주어지면,
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

strings = input().upper()
countArr = [0 for _ in range(26)]
for string in strings:
    countArr[ord(string)-65] += 1
if countArr.count(max(countArr))>=2:
    print("?")
else:
    print(chr(65+countArr.index(max(countArr))))

#타인 풀이
n = input()
n = n.upper()
alpa='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []
for i in alpa:
  result.append(n.count(i))
if result.count(max(result)) > 1:
  print("?")
else:
  print(alpa[result.index(max(result))])