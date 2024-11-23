def numofbits(n):
    ones=0
    zeros=0
    while(n):
        if(n&1==1):
            ones=ones+1
        else:
            zeros=zeros+1
        n>>=1
    print(" Number Of Zeros ",zeros)
    print(" Number Of Ones ",ones)
num=int(input(" Enter a Number "))
numofbits(num)