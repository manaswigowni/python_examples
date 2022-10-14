#factorial of given number
num=int(input(" enter the number"))
factorial=1
if n==0 or n==1 :
    factorial=1
else :
    for i in range(2,num+1) :
        factorial=factorial*i
print("factorial=",factorial)