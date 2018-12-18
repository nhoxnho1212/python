
import textwrap as tw

def wrapp(string,max_width):
    #function wrap return a list
    NewString=tw.wrap()
    
    return ''.join(map(str(x)+'\n',NewString))

if __name__ == "__main__":
    strings =input()
    max_width=int(input())
    result=wrapp(strings,max_width)
    print(result)