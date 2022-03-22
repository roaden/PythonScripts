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

print("Squares up to what number?")
maxSquare = checkPositive()

print("Squares up to what number?")
for i in range(5):
    a = 2
    b = 2
    while gcd(a, b) != 1:
        a = (ri(1, maxSquare))
        b = ri(1, maxSquare)
    aSquared = str(a**2)
    bSquared = str(b**2)
    print(f"{aSquared + ' x^2': >10}" "    - " + f"{bSquared + ' y^2' : >10}")

