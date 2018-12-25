def merge_the_tools(string, k):
    lengSubString=len(string)//k
    leng=len(string)
    cur=0
    while cur<leng:
        result=''
        for i in range(cur,cur+k):
            if string[i] not in result:
                result+=string[i]
        print(result)
        cur+=k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)  