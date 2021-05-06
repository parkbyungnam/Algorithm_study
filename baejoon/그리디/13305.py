totalCity = int(input())
roads = list(map(int,input().split()))
prices = list(map(int,input().split()))

prices.pop(-1)

minPrice = min(prices)
currentPrice = prices[0]
result = 0

for i in range(totalCity):
    if currentPrice == minPrice: #현재 가격이 최소값일 때
        result += currentPrice*sum(roads[i:totalCity])
        break
    if currentPrice >= prices[i]: #역대가격보다 이후 가격이 더 저렴할 때
        currentPrice = prices[i]
    result += currentPrice*roads[i]

print(result)




totalCity = int(input())
roads = list(map(int,input().split()))
prices = list(map(int,input().split()))

currentPrice = prices[0]
result = 0

for i in range(totalCity-1):
    if currentPrice >= prices[i]: #역대가격보다 이후 가격이 더 저렴할 때
        currentPrice = prices[i]
    result += currentPrice*roads[i]

print(result)




#다시 풀어보기
N = int(input())
roads = list(map(int,input().split()))
prices = list(map(int,input().split()))
result = 0
minPrice = prices[0]

for i in range(N-1):
    if minPrice > prices[i]:
        minPrice=prices[i]
    result += minPrice*roads[i]

print(result)