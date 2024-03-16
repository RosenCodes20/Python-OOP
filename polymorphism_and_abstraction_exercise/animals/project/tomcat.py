from project.cat import Cat


class Tomcat(Cat):

    def __init__(self, name, age):
        super(Tomcat, self).__init__(name, age, "Male")

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    @staticmethod
    def make_sound():
        return f"Hiss"