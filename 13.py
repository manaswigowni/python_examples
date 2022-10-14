#greatest among given three numbers
a,b,c=input("enter three numbers").split(' ')
if int(a)>int(b) and int(a)>int(c) :
    print(" the largest number is ",a)
elif int(b)>int(a) and int(b)>int(c) :
    print(" the largest number is ",b)
elif int(c)>int(b) and int(c)>int(a) :
    print("the largest number is  ",c)