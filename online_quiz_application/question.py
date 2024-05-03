from user import User


class Question:

    def __init__(self, text, options, correct_option, answer):
        self.text = text
        self.options = options
        self.correct_option = correct_option
        self.answer = answer
        self.questions = {}

    def add_question(self):
        if self.text not in self.questions:
            self.questions[self.text] = {"Options": self.options, "Correct option": self.correct_option,
                                         "Answer": self.answer}

        else:
            raise Exception("The question is already here!")

    def delete_question(self, text):
        if text in self.questions:
            self.questions.pop(text)
            return f"Successfully removed question"
        else:
            raise Exception(f"Text not in here!!")

    def get_question(self, text):
        result = "Here's the question:\n"

        if text in self.questions:
            result += f"Question: {text}\n" \
                      f"Options: {self.questions[text]['Options']}\n" \
                      f"Correct option: {self.questions[text]['Correct option']}\n" \
                      f"Answer: {self.questions[text]['Answer']}"

        else:
            raise ValueError("The text is not added!")

        return result

    def test_if_the_answer_is_right(self, text, user: User):
        if user.login(user.username, user.password):
            if text in self.questions:
                if self.questions[text]["Answer"] == self.questions[text]["Correct option"]:
                    return True
                else:
                    return False

            else:
                raise ValueError("The question is not in here")
