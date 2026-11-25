
students = []

def add_student():
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")
    department = input("Enter Department: ")

    student = {
        "Name": name,
        "Roll No": roll_no,
        "Department": department
    }

    students.append(student)
    print("Student Added Successfully!")

def view_students():
    if not students:
        print("No Students Found!")
    else:
        for student in students:
            print("\n", student)

def search_student():
    roll = input("Enter Roll Number: ")

    for student in students:
        if student["Roll No"] == roll:
            print("Student Found:", student)
            return

    print("Student Not Found!")

def delete_student():
    roll = input("Enter Roll Number: ")

    for student in students:
        if student["Roll No"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
