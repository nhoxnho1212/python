def solve(s):
    check=True
    result=''
    for x in s:
        temp=str(x)
        if check and temp!=' ':
            temp=temp.upper()
            check=False
        elif temp==' ':
            check=True
        result+=temp
    return result
if __name__ == "__main__":
    s=input().strip()
    r=solve(s)
    print(r)
    
