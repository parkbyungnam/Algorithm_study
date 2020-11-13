n = 1260
count = 0

mylist = [500,100,50,10]

for coin in mylist:
    count += n//coin
    n %= coin

print(count)