def fibo(n):
    if n<=2:
        return 1
    else:
        result = 1
        past = 1
        for _ in range(n-2):
            temp = result
            result += past
            past = temp
        return result

print(fibo(int(input())))


#타인풀이

a=int(input())

tmp=[]

for i in range(a+1) :
    if i == 0 :
        tmp.append(0)
    elif i == 1:
        tmp.append(1)
    else :
        tmp.append(tmp[i-1]+tmp[i-2])

print(tmp[a])