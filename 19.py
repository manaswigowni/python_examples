#amstrong number
num = int(input(" enter the number"))
n=len(str(num))
sum = 0
temp = num
while temp > 0:
   rem = temp % 10
   sum += rem**n
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")