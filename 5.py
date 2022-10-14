#code to solve quadratic equation
print(" in a quadratic equation ax^2+bx+c")
a=int(input(" enter  a"))
b=int(input(" enter b"))
c=int(input("enter c"))
r1=((-b+((b**2-4*a*c)**0.5)))/(2*a)
r2=((-b-((b**2-4*a*c)**0.5)))/(2*a)
print(r1)
print(r2)