# TASK-01: Checking whether a number is Even OR Odd:

num = int (input("Enter a number: "))
if (num % 2 == 0):
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")


# TASK-02: Printing the sum of numbers 1 to 50 using a loop:
#For-loop:

sum=0
for i in range(1,51):
    sum = sum + i

print("The sum of numbers from 1 to 50 is:",sum)

#While-loop:

sum=0
i=0
while (i<=50):
    sum+=i

print("The sum of numbers from 1 to 50 is:",sum)
