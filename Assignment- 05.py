# #TASK-01: Creating dictionary and performing operations:
def dict(d, key):              #Creating dictionary
    d[key] = input("Enter value for " + key + ":")


n = int(input("Enter the no of key-value pairs:"))
d={}
for i in range(n):
    key = input("Enter the key:")
    dict(d,key)

name = input("Enter the student's name:")               #retrieving the data of the dictionary
keys = list(d.keys())
if(name in keys):
    print(f"{name}'s marks is {d[name]}")
else:
    print("Student not found")



#TASK-02: List Slicing:
lst =[]
for i in range(1,11):
    lst.append(i)
print("Original list:",lst)
elst = lst[:5]
print("Extracted elements from list:",elst)
print("Reversed Extracted elements:",elst[::-1])