temp = int(input())
for _ in range(2):
    ham = int(input())
    if(temp > ham):
        temp = ham
temp2 = int(input())
for _ in range(1):
    coca = int(input())
    if(temp2 > coca):
        temp2 = coca
print(temp+temp2-50)

#타인 코드
burger=[]
drink=[]
for i in range(3):
    k=int(input())
    burger.append(k)
for j in range(2):
    t=int(input())
    drink.append(t)
print(min(burger)+min(drink)-50)