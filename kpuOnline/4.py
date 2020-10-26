dic = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':12,'P':11,'Q':10,'R':9,'S':8,'T':7,'U':6,'V':5,'W':4,'X':3,'Y':2,'Z':1}
name = list(input())
result = 0
for na in name:
    result+=dic[na]
print(len(name)+result-1)