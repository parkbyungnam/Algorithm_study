#import sys

#input = sys.stdin.readline

testCase = int(input())
for _ in range(testCase):
    flag = True #error 판단 깃발
    inputFunction = input() #함수 리스트
    arrayLen = int(input()) #배열 크기값

    if arrayLen: #배열 크기가 0이 아닐 때
        if arrayLen == 1:
            array = list(input().strip('[]'))
        else:
            array = list(map(int,input().strip('[]').split(',')))
        for f in inputFunction:
            if f=='R': #뒤집기
                array.reverse()
            elif f=='D': #popleft 하기
                if array:
                    del(array[0])
                else: #빈 리스트에서 추출 시 에러
                    flag = False
                    break
        if flag == True: #정상 작동 했을 때
            print(array)
        else: #빈리스트에서 추출했을 때 
            print('error')

    else: #배열 크기가 0일 때
        temp = input() #리스트 입력값 받기 []
        if inputFunction.count('D'): #추출함수 D 가 있다면
            print('error')
        else:
            print(temp)
