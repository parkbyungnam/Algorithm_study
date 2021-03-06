#import sys

#input = sys.stdin.readline
'''
testCase = int(input())
for _ in range(testCase):
    flag = True #error 판단 깃발
    inputFunction = input() #함수 리스트
    arrayLen = int(input()) #배열 크기값

    if arrayLen: #배열 크기가 0이 아닐 때
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

'''

import sys

input = sys.stdin.readline

testCase = int(input())
for _ in range(testCase):
    isError = False #error 판단 깃발
    isReverse = False #리버스 판단 유무
    inputFunction = input() #함수 리스트
    arrayLen = int(input().rstrip()) #배열 크기값

    if arrayLen: #배열 크기가 0이 아닐 때
        array = list(map(int,input().rstrip()[1:-1].split(',')))
        for f in inputFunction:
            if f=='R': #뒤집기
                isReverse=False if isReverse else True #리버스 체크
            elif f=='D': #popleft 하기
                if array: #빈 리스트 아닐 시
                    if isReverse:
                        del(array[-1])
                    else:
                        del(array[0])
                else: #빈 리스트에서 추출 시 에러
                    isError = True
                    break
        if isError: #빈리스트에서 추출했을 때
            print('error')
        else:   #정상 작동 했을 때
            if isReverse:
                array.reverse()
            print('[',end='')
            for arr in array[:-1]:
                print('{0},'.format(arr), end='')
            print('{0}]'.format(array[-1]))

    else: #배열 크기가 0일 때
        temp = input() #리스트 입력값 받기 []
        if inputFunction.count('D'): #추출함수 D 가 있다면
            print('error')
        else:
            print(temp)