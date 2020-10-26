#별찍기
T = int(input())
for i in range(T-1):
    print(" "*i + "*"*((2*T-1)-2*i))
for i in range(T-1,-1,-1):
    print(" "*i + "*"*((2*T-1)-2*i))
#for i in range(T)