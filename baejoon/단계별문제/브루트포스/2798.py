cardNum, target = map(int,input().split())
card = list(map(int,input().split()))
gap = target
for first in range(0,cardNum-2):
  for second in range(first+1,cardNum-1):
    for third in range(second+1,cardNum):
      sum = card[first] + card[second] + card[third]
      temp=target-sum
      if temp<gap and temp>=0:
        gap = temp
print(target-gap)


#다른 사람 풀이



def P(n,m,card):
    	t=set()
	for first in range(n-2):
		for second in range(first+1,n-1):
			for third in range(second+1,n):
				s=card[i]+card[o]+card[p]
				if s<=m:
					t.add(s)
					break
				elif s==m:
					return s
	return max([*t]) 
print(P(*map(int,input().split()),list(sorted(map(int,input().split()))[::-1])))