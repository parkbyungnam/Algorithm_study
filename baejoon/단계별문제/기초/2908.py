q1,q2 = map(list,input().split(" "))
t1 = int(q1[2])*100 + int(q1[1])*10 + int(q1[0])
t2 = int(q2[2])*100 + int(q2[1])*10 + int(q2[0])
if t1 > t2:
    print(t1)
else:
    print(t2)

#타인 풀이
a, b =input().split()

def reading(k):
    k = k[::-1]
    return int(k)

print(max([reading(a),reading(b)]))

#타인 풀이 2
A,B = input().split()

print(max(A[::-1], B[::-1]))