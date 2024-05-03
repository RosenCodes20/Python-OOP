from question import Question
from user import User


class Quiz:

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.questions = []
        self.users = []
        self.quiz = []

    def create_quiz(self):
        for quiz in self.quiz:
            if quiz.title == self.title:
                raise ValueError("The quiz is already here!!")

        new_quiz = Quiz(self.title, self.description)

        self.quiz.append(new_quiz)

        return new_quiz

    def add_user(self, username, password, role):
        for users in self.users:
            if users.username == username:
                raise Exception(f"The user with {username} is already here")

        new_user = User(username, password, role)
        new_user.register()
        if new_user.login(username, password):
            self.users.append(new_user)
            return f"Added new user!!"

    def logout_user(self, username):
        try:
            user = next(filter(lambda u: u.username == username, self.users))

        except StopIteration:
            raise Exception("User is not here!!")

        if user.login(user.username, user.password):
            user.logout(user.username)

    def add_question(self, text, options, correct_option, answer):
        for question in self.questions:
            if question.text == text:
                raise Exception("The question is already here")

        new_question = Question(text, options, correct_option, answer)
        self.questions.append(new_question)
        new_question.add_question()
        return f"Added new question!"

    def get_question(self, text):
        try:
            question = next(filter(lambda q: q.text == text, self.questions))

        except StopIteration:
            raise Exception("Cannot find the question in here!!!")

        return question.get_question(question.text)

    def delete_question(self, text):
        try:
            question = next(filter(lambda q: q.text == text, self.questions))

        except StopIteration:
            raise Exception("Cannot find this question!")

        return question.delete_question()

    def start_quiz(self, username, text):
        try:
            user = next(filter(lambda u: u.username == username, self.users))

        except StopIteration:
            raise ValueError("The user is not in the users list!!")

        try:
            question = next(filter(lambda q: q.text == text, self.questions))

        except StopIteration:
            raise Exception("The question is not in questions list")

        if question.test_if_the_answer_is_right(question.text, user):
            user.points += 1
            return f"The user with username {user.username} successfully answered the question and gets a point!"

        else:
            user.points -= 1
            return f"The user with username {user.username} did not managed to answer the questions and is dedicated with 1 point!"

    def end_quiz(self, username):
        try:
            user = next(filter(lambda u:  u.username == username, self.users))

        except StopIteration:
            raise Exception(f"Cannot find user with {username}")

        return f"User with {user.username} ended the quiz with {user.points} point/s!"

    def get_quiz(self, title):
        try:
            quiz = next(filter(lambda q: q.title == title, self.title))

        except StopIteration:
            raise Exception(f"The quiz is not in here!!")

        return f"Quiz title: {quiz.title}" \
               f"Quiz description: {quiz.description}"

    def get_quiz_results(self):
        users = [u for u in self.users]

        for user in users:
            return f"Username: {user.username}\n" \
                   f"Password: {len(user.password) * '*'}\n" \
                   f"Points: {user.points}\n" \
                   f"Role: {user.role}"


quiz = Quiz("Rosen's Quiz", "History")
quiz.create_quiz()
print(quiz.add_user("Rosen", "1234567", "participant"))
print(quiz.add_question("In what year is created Bulgaria", "A:280, B:345, C:681, D:1081", "C", "C"))
print(quiz.get_question("In what year is created Bulgaria"))
print(quiz.start_quiz("Rosen", "In what year is created Bulgaria"))
print(quiz.end_quiz("Rosen"))
print(quiz.get_quiz_results())