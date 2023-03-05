
#Python Maths
# # Q1) Polar Coordinates

import cmath
c=complex(input().strip())
for i in cmath.polar(c):
    print(i)


#Q2) Find Angle MBC


import math
AB = int(input())
BC = int(input())
print(round(math.degrees(math.atan(AB/BC))),chr(176),sep='')


#Q3) Interger Come In All Sizes

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a**b+c**d)


# # Q4) Mod Divmod

a = int(input())
b = int(input())

print(a//b)
print(a%b)
print(divmod(a, b))


# # Q5) Power - Mod Power
a = int(input())
b = int(input())
m = int(input())

print(pow(a,b))
print(pow(a,b,m))


# # Q6) Triangle 1


for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i*(pow(10,i)//9))


# # Q7) Triangle 2

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(pow((pow(10,i)//9),2))

