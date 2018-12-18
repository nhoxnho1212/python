if __name__ == "__main__":
    n,m=map(int,input().split(' '))
    

    baseIcon='.|.'
    # a half Array
    for i in range(0,(n-1)//2):
        curList=baseIcon
        for _ in range(0,i):
            curList=baseIcon+curList+baseIcon
        while len(curList)<m:
            curList='-'+curList+'-'
        print(curList)

    BeLine='WELCOME'
    while len(BeLine)<m:
        BeLine='-'+BeLine+'-'
        
    print(BeLine)
        