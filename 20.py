#amstrong number between interval
n1=int(input(" enter lower limit"))
n2=int(input(" enter upper limit"))
for i in range(n1,n2+1) :
    n=len(str(i))
    sum=0
    tem=i
    while tem>0 :
        rem=tem%10
        sum=sum+(rem)**n
        tem=tem//10
    if i==sum :
        print(i)