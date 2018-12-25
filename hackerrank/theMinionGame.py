#Using dynamic programing

def isVowel(letter):
    if letter=='A' or letter=='U' or letter=='E' or letter=='O' or letter=='I':
        return True
    else:
        return False



def TheMinionGame(string):
    string=str(string)
    leng=len(string)
    listVowels,listConsonants=dict(),dict()
    for cur in range(leng):
        if isVowel(string[cur]):
            listVowels[string[cur]]=list()

            firstIndexSubStr=0
            while firstIndexSubStr!=-1:
                firstIndexSubStr=string.find(string[cur],firstIndexSubStr)
                if firstIndexSubStr!=-1:
                    listVowels[string[cur]].append(firstIndexSubStr)
                    firstIndexSubStr+=1

            for i in range(cur+2,leng+1):
                if string[cur:i] not in listVowels:
                    listVowels[string[cur:i]]=list()
                    for index in listVowels[string[cur:i-1]]:
                        if string[index:index+len(string[cur:i])]==string[cur:i]:
                            listVowels[string[cur:i]].append(index)
        
        else:
            listConsonants[string[cur]]=list()

            firstIndexSubStr=0
            while firstIndexSubStr!=-1:
                firstIndexSubStr=string.find(string[cur],firstIndexSubStr)##
                if firstIndexSubStr!=-1:
                    listConsonants[string[cur]].append(firstIndexSubStr)
                    firstIndexSubStr+=1##

            for i in range(cur+2,leng+1):##
                if string[cur:i] not in listConsonants:
                    listConsonants[string[cur:i]]=list()
                    for index in listConsonants[string[cur:i-1]]:
                        if string[index:index+len(string[cur:i])]==string[cur:i]:
                            listConsonants[string[cur:i]].append(index)
    STUART=0
    KEVIN=0
    for i in listConsonants.values():
        STUART+=len(i)
    for i in listVowels.values():
        KEVIN+=len(i)
    if STUART>KEVIN:
        print('Stuart %d'%STUART)
    elif STUART<KEVIN:
        print('Kevin %d'%KEVIN)
    else:
        print('Draw')

if __name__ == "__main__":
    s=input()
    TheMinionGame(s)

            
            
