file = open("students.txt", "a")
name = input("Enter student name: ")
marks = input("Enter marks: ")
file.write(f"{name},{marks}\n")
file.close()
print("Data saved successfully!")

file = open("students.txt","r")
lines  = file.readlines()
file.close()

for line in lines:
    line = line.strip()
    if line:
        parts = line.split(",")
        if len(parts) == 2:
            name = parts[0]
            marks_str = parts[1]
            
            try:
                marks = float(marks_str)
                if marks >= 60:
                    print(f"🎓 {name}: {marks}")
            except:
                pass 