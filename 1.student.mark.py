students = []
courses = []
marks = {}

def input_students():
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter date of birth (DD/MM/YYYY): ")
        students.append({"id": student_id, "name": name, "dob": dob})

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses.append({"id": course_id, "name": name})
        marks[course_id] = {}

def input_marks():
    if not courses:
        print("No course")
        return
    course_id = input("Enter course ID: ")
    course = next((c for c in courses if c["id"] == course_id), None)
    if not course:
        print("Course not found")
        return
    for student in students:
        mark = float(input(f"Enter marks for {student['name']} (ID: {student['id']}): "))
        marks[course_id][student["id"]] = mark

def list_students():
    print("Student list:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Date of Birth: {student['dob']}")

def list_courses():
    print("Course list:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def show_marks():
    course_id = input("Enter course ID: ")
    if course_id not in marks:
        print("Course not found!")
        return
    print(f"Marks for course {course_id}:")
    for student_id, mark in marks[course_id].items():
        student = next((s for s in students if s["id"] == student_id), None)
        if student:
            print(f"ID: {student['id']}, Name: {student['name']}, Marks: {mark}")

while True:
    print("\nStudent Marks Management")
    print("Input student information")
    print("Input course information")
    print("Input marks for a course")
    print("Display student list")
    print("Display course list")
    print("Display marks for a course")
    print("Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        input_students()
    elif choice == "2":
        input_courses()
    elif choice == "3":
        input_marks()
    elif choice == "4":
        list_students()
    elif choice == "5":
        list_courses()
    elif choice == "6":
        show_marks()
    elif choice == "0":
        print("Exit")
        break
    else:
        print("Invalid")
