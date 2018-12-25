def wrap(string,max_width):
    #function wrap return a list
    newlist=[]
    while string!='':
        if len(string)<max_width:
            newlist.append(string)
            break
        newlist.append(string[:max_width])
        string=string[max_width:]
    
    return ''.join((str(x)+'\n') for x in newlist)

if __name__ == "__main__":
    strings =input()
    max_width=int(input())
    result=wrap(strings,max_width)
    print(result)