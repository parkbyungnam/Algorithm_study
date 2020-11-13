list_len, M, K = map(int,input().split())
mylist = list(map(int,input().split()))

mylist.sort(reverse=True)
big1=mylist[0]
big2=mylist[1]

cnt1 = (M//(K+1))*K + (M%(K+1))
cnt2 = M - cnt1

result = big1*cnt1 + big2*cnt2
print(result)