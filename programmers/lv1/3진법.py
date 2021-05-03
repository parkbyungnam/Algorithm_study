def solution(n):
    my_n = n
    my_3 = ''
    while my_n:
        temp=my_n%3
        my_3+=str(temp)
        my_n//=3
    mylen=len(my_3)-1
    values = 0
    for i,my in enumerate(my_3):
        values += int(my)*(3**(mylen-i))
    answer = values
    return answer

print(solution(125))