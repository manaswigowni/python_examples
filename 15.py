#prime numbers in an interval
n1=int(input(" enter lower limit"))
n2=int(input(" enter higher limit"))
for i in range (n1,n2+1) :
    count=0
    for j in range (2,i) :
        if i%j==0 :
            count+=1
    if count==0 and i!=1 :
        print(i)