class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, cid, name):
        self.id = cid
        self.name = name
        self.marks = {}  

students = []
courses = []

def input_students():
    for _ in range(int(input("Number of students: "))):
        sid = input("Student ID: ")
        name = input("Name: ")
        dob = input("Date of Birth: ")
        students.append(Student(sid, name, dob))

def input_courses():
    for _ in range(int(input("Number of courses: "))):
        cid = input("Course ID: ")
        name = input("Course name: ")
        courses.append(Course(cid, name))

def input_marks():
    cid = input("Course ID: ")
    course = next((c for c in courses if c.id == cid), None)
    if not course:
        print("Course not found!")
        return
    for s in students:
        course.marks[s.id] = float(input(f"Marks for {s.name}: "))

def list_students():
    for s in students:
        print(f"ID: {s.id}, Name: {s.name}, DOB: {s.dob}")

def list_courses():
    for c in courses:
        print(f"ID: {c.id}, Name: {c.name}")

def show_marks():
    cid = input("Course ID: ")
    course = next((c for c in courses if c.id == cid), None)
    if not course:
        print("Course not found!")
        return
    for sid, mark in course.marks.items():
        student = next(s for s in students if s.id == sid)
        print(f"{student.name}: {mark}")

while True:
    print("\n1. Add students\n2. Add courses\n3. Enter marks\n4. Show students\n5. Show courses\n6. Show marks\n0. Exit")
    choice = input("Your choice: ")
    if choice == "1": input_students()
    elif choice == "2": input_courses()
    elif choice == "3": input_marks()
    elif choice == "4": list_students()
    elif choice == "5": list_courses()
    elif choice == "6": show_marks()
    elif choice == "0": break
    else: print("Invalid choice")
