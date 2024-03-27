from project.student import Student

from unittest import TestCase, main


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student = Student(
            "Rosen",
            {"math": ["1 + 1 = 2"]}
        )

        self.student_two = Student(
            "Georgi"
        )

    def test_correct_init(self):
        self.assertEqual("Rosen", self.student.name)
        self.assertEqual({"math": ["1 + 1 = 2"]}, self.student.courses)
        self.assertEqual({}, self.student_two.courses)

    def test_enroll_method_works_right_not_expecting_errors(self):
        self.student.courses = {}
        result = self.student.enroll("pe", ["basketball"], "N")
        self.assertEqual({"pe": []}, self.student.courses)
        self.assertEqual("Course has been added.", str(result))

    def test_enroll_method_adding_course_to_the_dict(self):
        self.student.courses = {}
        result = self.student.enroll("pe", ["basketball"], "Y")
        self.assertEqual({"pe": ["basketball"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", str(result))

    def test_enroll_method_without_y_parameter(self):
        self.student.courses = {}
        result = self.student.enroll("pe", ["basketball"])
        self.assertEqual({"pe": ["basketball"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", str(result))
        
    def test_enroll_method_adding_course_to_list_in_the_dict(self):
        self.student.courses = {"math": ["1 + 1 = 2"]}

        result = self.student.enroll("math", ["2 + 2 = 4"])

        self.assertEqual({"math": ["1 + 1 = 2", "2 + 2 = 4"]}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", str(result))

    def test_adding_notes_expecting_an_error_if_course_not_in_dict(self):
        self.student.courses = {"pe": ["basketball"]}

        result = self.student.add_notes("pe", "football")

        self.assertEqual({"pe": ["basketball", "football"]}, self.student.courses)
        self.assertEqual("Notes have been updated", str(result))

    def test_adding_notes_method_error_representing_right_string(self):
        self.student.courses = {"pe": ["basketball"]}

        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", ["1 + 1 = 2"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leaving_course_method_expecting_an_exception_if_course_not_int_dict(self):
        self.student.courses = {"pe": ["basketball"]}

        result = self.student.leave_course("pe")

        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", str(result))

    def test_leaving_course_method_error_representation_working(self):
        self.student.courses = {"pe": ["basketball"]}

        with self.assertRaises(Exception) as ex:
            self.student.leave_course("math")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()