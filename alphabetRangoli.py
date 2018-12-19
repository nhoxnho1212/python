def print_rangoli(size):
    leng=(size-1)*4 +1
    arr=list()
    for _ in range(size*2-1):
        arr.append('')

    for i in range(size,0,-1):
        cur=chr(i+97-1)
        for x in range(i+1,size+1):
            cur=chr(x+97-1)+'-'+cur+'-'+chr(x+97-1)
        while len(cur)<leng:
            cur='-'+cur+'-'
        arr[size-i]=cur
        arr[i+size-2]=cur
    for i in arr:
        print(i)
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)