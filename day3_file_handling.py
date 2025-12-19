# File Handling

file = open("students.txt", "a")

name = input("Enter student name: ")
marks = input("Enter marks: ")

file.write(f"{name},{marks}\n")
file.close()

print("Data saved successfully!")

# Read files
file = open("students.txt", "a")

file = open("students.txt", "r")

content = file.read()
print(content)

file.close()
