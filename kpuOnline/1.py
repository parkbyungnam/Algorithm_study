arr = input()
arr = list(arr)
arr.reverse()
output = []

def solution(arr,output):
    #while arr != []:
    temp = arr.pop()   
    if 'a'<temp<'z':
        output.append(temp)
        solution(arr,output)
    if temp=='+' or temp=="-":



#다른풀이

arr= input()
arr = list(arr)

for ar in arr:
    if ar=='-' or ar=='+':
        arr[]

