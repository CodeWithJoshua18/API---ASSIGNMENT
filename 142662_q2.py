# This code defines a class `Student` with methods to add assignments and grades.
class Student:
    def __init__(self, name):
        self.name = name
        self.assignments = {
            "assignment": [],
            "grade": []
        }

# Function to add an assignment to a student's record
def add_assignment(student, assignment):
    student.assignments["assignment"].append(assignment)

# Function to add a grade to a student's record
def add_grade(student, grade):
    student.assignments["grade"].append(grade)

# Function to display a student's grades
def display_grades(student):
    print(f"Grades for {student.name}:")
    for assignment, grade in zip(student.assignments["assignment"], student.assignments["grade"]):
        print(f"{assignment}: {grade}")

# Defining a class Instructor with methods to manage students and their grades
class Instructor:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)    

    def add_grade(self, student, assignment, grade):
        if student in self.students:
            add_assignment(student, assignment)    
            add_grade(student, grade)

    def display_grades(self, student):
        if student in self.students:
            display_grades(student)
        else:
            print(f"{student.name} is not enrolled in the course.")
# Example usage
if __name__ == "__main__":
    # Create an instructor
    instructor = Instructor("Dr. Smith")

    # Create a student
    student1 = Student("Shawn")
    student2 = Student("Beth")

    # Add the student to the instructor's list
    instructor.add_student(student1)
    instructor.add_student(student2)

    # Add assignments and grades
    instructor.add_grade(student1, "Math Assignment", 95)
    instructor.add_grade(student2, "OOP Project", 88)

    # Display the student's grades
    instructor.display_grades(student1)
    instructor.display_grades(student2)  