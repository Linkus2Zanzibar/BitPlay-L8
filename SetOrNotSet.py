def setOrNot(num,n):
    setbit=1
    if(n&setbit) == 1 or(n&setbit) == 0:
        if num&(1<<(n-1)):
            print(" Set ")
        else:
            print(" Not Set ")
num=int(input(" Enter a Number "))
n=int(input(" Enter The Bit Position "))
setOrNot(num,n)


