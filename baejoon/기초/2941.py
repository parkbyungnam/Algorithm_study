#예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

#크로아티아 알파벳	변경
#č	c=
#ć	c-
#dž	dz=
#đ	d-
#lj	lj
#nj	nj
#š	s=
#ž	z=
#예를 들어,
# ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다.
# lj와 nj도 마찬가지이다.
# 위 목록에 없는 알파벳은 한 글자씩 센다.

strings = input()
count = 0
if strings.count("dz=")!=0:
    count += strings.count("dz=")
    count += strings.count("c=")
    count += strings.count("c-")
    count += strings.count("d-")
    count += strings.count("lj")
    count += strings.count("nj")
    count += strings.count("s=")
    count += strings.count("z=")-strings.count("dz=")
    count = count + (len(strings)-strings.count("dz=")*3 - (count - strings.count("dz="))*2)
else:
    count += strings.count("c=")
    count += strings.count("c-")
    count += strings.count("d-")
    count += strings.count("lj")
    count += strings.count("nj")
    count += strings.count("s=")
    count += strings.count("z=")
    count = count + (len(strings)-count*2)
print(count)

#다른 풀이
rep=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=input()
for i in rep:s=s.replace(i,'*')
print(len(s))

#다른 풀이
c=input().count
print(c('')-1-sum(map(c,['-','=','nj','lj','dz='])))