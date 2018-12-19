def print_formatted(number):
    leng=len(str(bin(number)))-2
    
    for i in range(1,number+1):
        DecStr=str(i)
        OctStr=str(oct(i))[2:]
        HexStr=(str(hex(i))[2:]).upper()
        BinStr=str(bin(i))[2:]
        while len(DecStr)<leng:
            DecStr=' '+DecStr
        while len(OctStr)<leng:
            OctStr=' '+OctStr
        while len(HexStr)<leng:
            HexStr=' '+HexStr
        while len(BinStr)<leng:
            BinStr=' '+BinStr
        print("%s %s %s %s" %(DecStr,OctStr,HexStr,BinStr))



if __name__ == '__main__':