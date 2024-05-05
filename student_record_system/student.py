class Student:

    def __init__(self, student_id, name, age, gender):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.courses_taken = []
        self.grades_received = {}

    def enroll_course(self, course):
        if course in self.courses_taken:
            return f"Course with {course.name} name is already taken!"

        self.courses_taken.append(course)
        return f"Course with name {course.name} was successfully enrolled!"

    def receive_grade(self, course, grade):
        if grade in self.grades_received:
            return f"Grade is already received!!"

        self.grades_received[course] = grade
        return f"Grade has successfully added to grades list"

    def view_transcript(self):
        for course, grade in self.grades_received.items():
            return f"Course: {course}/Grade: {grade}"