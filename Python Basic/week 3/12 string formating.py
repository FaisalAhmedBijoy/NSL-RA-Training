def print_formatted(number):
    # your code goes here
    w=len(str(bin(number)[2:]))
    for i  in range(1,number+1):
        decimal=str(i)
        octal=oct(i).replace('0o','').rjust(w)
        hexa=hex(i).replace('0x','').rjust(w)
        binary=bin(i).replace('0b','').rjust(w)
        
        print(decimal.rjust(w),octal,hexa.upper(),binary)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)