class School:

    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = []

    def add_student(self, student):
        if student in self.students:
            return f"Student is already added here!!"

        self.students[student.student_id] = student
        return f"Added new student with id: {student.student_id}"

    def add_course(self, course):
        if course in self.courses:
            return f"Course with {course.name} name already added here!!"

        self.courses[course.course_id] = course
        return f"Added new course with id: {course.course_id}"

    def record_grade(self, grade):
        if grade in self.grades:
            raise Exception("Grade is already added!!")

        self.grades.append(grade)
        return f"Successfully added a grade with id: {grade.grade_id}"

    def student_record_card(self, student):
        if student not in self.students:
            raise Exception("Student is not in here!!")

        students = self.students[student.student_id]

        if not students.grades_received:
            raise Exception(f"Not added grades in here!!")

        else:
            return students.view_transcript()
