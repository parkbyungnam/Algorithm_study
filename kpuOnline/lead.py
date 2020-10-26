testCase = int(input())
temp = 0
winner = 0
player1 = 0
player2 = 0
for _ in range(testCase):
    Si,Ti = map(int,input().split())
    player1 += Si
    player2 += Ti
    lead = player1 - player2
    abs_lead=abs(lead)
    if temp < abs_lead:
        temp=abs_lead
        if lead==abs_lead:
            winner=1
        else:
            winner=2
print('{} {}'.format(winner,temp),end="")