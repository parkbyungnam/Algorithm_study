
##회문 번호
def bar(n):
    pLen = 1; lenTotal = 0; palindrome = None   
    while lenTotal < n:
        palindromes = getPalindromes(pLen)
        lenTotal += len(palindromes)
        pLen += 1
    print(palindromes[n - (lenTotal+1)])

def getPalindromes(l):
    if l < 1: return []
    if l == 1: return [x for x in range(10)]
    palindromes = []
    if l % 2 == 0:
        halfLen = l // 2
        for i in range(10 ** (halfLen - 1), 10 ** halfLen):
            palindromes.append(int(str(i) + str(i)[::-1]))
    else:
        halfLen = (l-1) // 2
        for i in range(0, 10):
            for j in range(10 ** (halfLen - 1), 10 ** halfLen):
                palindromes.append(int(str(j) + str(i) + str(j)[::-1]))
    palindromes.sort()
    return palindromes

