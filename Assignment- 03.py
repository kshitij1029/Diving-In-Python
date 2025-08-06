#TASK-01: Calculating factorial of a number:
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter a number:"))
print("The factorial of",n,"is:",factorial(n))


#TASK-02: Using math module:
import math

num=int(input("Enter a number:"))
print("Square root:",math.sqrt(num))
print("Logarithm:",math.log(num))
print("Sine:",math.sin(num))
