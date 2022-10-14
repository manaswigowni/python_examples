# to check whether given number is prime or not
num=int(input(" enter the number"))
count=0
for i in range(2,num) :
    if num%i==0 :
        count+=1
if count==0  :
    print("prime number")
else :
    print(" not a prime number")