# Menu-Driven Student Information System
student_db = {}

def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    student_db[roll_no] = {"Name": name, "Department": dept}
    print("Student added successfully.")

def view_students():
    if not student_db:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for roll_no, info in student_db.items():
        print("Roll No:", roll_no,
              "| Name:", info["Name"],
              "| Department:", info["Department"])

def search_student():
    roll_no = input("Enter Roll No to search: ")
    if roll_no in student_db:
        print(student_db[roll_no])
    else:
        print("Student not found.")

def delete_student():
    roll_no = input("Enter Roll No to delete: ")
    if roll_no in student_db:
        del student_db[roll_no]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    option = input("Enter your choice: ")
    if option == "1":
        add_student()
    elif option == "2":
        view_students()
    elif option == "3":
        search_student()
    elif option == "4":
        delete_student()
    elif option == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")