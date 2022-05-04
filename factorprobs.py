from random import randint as ri
from math import gcd

def checkPositive():
    while(True):
        try:
           posNum = int(input())
           if posNum > 0:
               return posNum
           else:
               print("Positive number please.")
        except ValueError:
            print("A positive integer please.")


print("How many problems?")
numProblems = checkPositive()

print("Coefficients up to what number?")
maxCoefficient = checkPositive()

for i in range(numProblems):
    a = ri(1,maxCoefficient)
    if ri(0,1):
        a = -a
    b = ri(1, maxCoefficient)
    if ri(0,1):
        b = -b
    print("x^2 + "+ str(a + b)+ " x + "  + str(a*b) + " = (x + " + str(a) + " ) ( x + " + str(b) + " )" )
