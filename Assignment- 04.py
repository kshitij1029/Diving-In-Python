#TASK-01: Reading and Handling errors gracefully:
try:
    file01 = open("Sample.txt", "r")
    print("Reading file content:")
    print("Line 1:",file01.readline())
    print("Line 2:",file01.readline())
except FileNotFoundError:
    print("Error: The file 'Sample.txt' was not found.")
finally:
    file01.close()

#TASK-02: Write and Append Data to a File:
file02 = open("Output.txt","w")
FirstLine = input("Enter text to write to the file:")
file02.writelines(FirstLine)
print("Data successfully written to file 'Output.txt'")
file02.write("\n")
file02.close()

file03 = open("Output.txt","a")
AppendLine = input("Enter additional text to append to the file:")
file03.write(AppendLine)
print("Data successfully appended")
file03.close()