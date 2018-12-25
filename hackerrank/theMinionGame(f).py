def isVowel(letter):
    if letter=='A' or letter=='U' or letter=='E' or letter=='O' or letter=='I':
        return True
    else:
        return False

def minion_game(string):
    countVowels=0
    countConsonants=0
    leng=len(string)
    for i in range(leng):
        count=0
        count=leng-i
        if isVowel(string[i]):
            countVowels+=count
        else:
            countConsonants+=count
    if countVowels>countConsonants:
        print("Kevin %d"%countVowels)
    elif countVowels<countConsonants:
        print("Stuart %d"%countConsonants)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)