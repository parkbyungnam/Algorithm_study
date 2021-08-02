array=[6,4,1,2,3,5,7,8]

for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
            array[i],array[j]=array[j],array[i]

print(array)