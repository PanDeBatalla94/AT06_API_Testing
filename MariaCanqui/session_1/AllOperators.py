import math
#Quadratic formula
a = 2
b = -3
c = -4
d = 2

x1 = ((-b) +  math.sqrt((b**2) - 4*a*c)) / (2*a)
x2 = ((-b) -  math.sqrt((b**2) - 4*a*c)) / (2*a)
print("get x: 2x2 - 3x -4")
print("x1 = " + str(x1) + " x2 = " + str(x2))
#module and floor division
print("module " + str( c % a))
print("floor division " + str( c // a))

#Comparison operators
if (a == b):
    print("Equals")
else:
    print("Not equals")

if (a != b):
    print("Not Equals")
else:
    print("Equals")

if (a > c):
    print("A major")
else:
    print("C major")

if (c < a):
    print("C minor")
else:
    print("A minor")

if (c <= a):
    print("C minor equals")
else:
    print("A minor equals")

if (c >= a):
    print("C minor")
else:
    print("A minor")

#Assigment operators

a = 10
a+=1
print("a+=1 " + str(a))

a = 10
a-=1
print("a-=1 " + str(a))

a = 10
a*=2
print("a*=2 " + str(a))

a = 10
a/=2
print("a/=2 " + str(a))

a = 10
a%=2
print("a%=2 " + str(a))

#Membership operators
names = ["alicia", "moira", "ronaldo"]
if ("alicia" in names):
    print("alicia is present")
if ("moira" not in names):
    print("moira is not present")

#identity operators

name1 = "moira"
name2 = "moira"
name3 = "maira"


if (name1 is name2):
    print("Same")
else:
    print("Different")

if (id(name1) == id(name2)):
    print("Same")
else:
    print("Different")





