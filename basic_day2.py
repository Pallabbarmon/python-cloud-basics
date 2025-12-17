my_list = ['notebook', 'pen', 'pc']
print(f"{my_list}")

name = input("Enter your name : ")
age = int(input("Enter your age : "))
city = input("Enter your city : ")

my_dict = {"Name" : name, "Age" : age, "City": city}
print(my_dict)

student = []

while True :
    name = input("Enter your name : (Or exit)")
    if name.lower()== "exit":
        break

    marks = int(input("Enter your marks : "))
    dict_student = {
        "name" : name,
        "marks" : marks
    }
    student.append(dict_student)

    print("\nStudent List")

    for s in student:
        print(f"{s['name']} - {s['marks']} marks")