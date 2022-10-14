#code to find area of a triangle
s1=int(input(" enter first side of the triangle"))
s2=int(input(" enter second side of the triangle"))
s3=int(input(" enter third side of the triangle"))
s=(s1+s2+s3)/2
area=(s*(s-s1)*(s-s2)*(s-s3))**0.5
print(" area is ",area)