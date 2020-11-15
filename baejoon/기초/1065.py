a=input()
count = 0
arr = list(a)
if len(arr)<=2:
    print(a)
else:
    if len(arr)==4:
        print("144")
    else:
        for i in range(100,int(a)+1):
            temp_arr = list(str(i))
            T1 = int(temp_arr[1])-int(temp_arr[0])
            T2 = int(temp_arr[2])-int(temp_arr[1])
            if T1 == T2:
                count += 1
        print(count+99)

#다른 풀이
print(sum(i<100 or i//10%10*2==i%10+i//100 for i in range(1,int(input())+1)))