#to check given year is leap year or not
year=int(input(" enter te year"))
if ((year%400==0) or ((year%100!=0) and (year%4==0))) :
    print(" it is a leap year")
else :
    print(" not a leap year")