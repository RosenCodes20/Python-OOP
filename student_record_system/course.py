class Course:

    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits
        self.students_enroll = []

    @property
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, value):
        if not value.strip():
            raise ValueError("Please enter some course_id!!")

        self.__course_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Please enter some name!!")

        self.__name = value

    def enroll_student(self, student):
        if student in self.students_enroll:
            return f"Student is already recorded here!!"

        self.students_enroll.append(student)
        return f"Successfully added a student here!!!"