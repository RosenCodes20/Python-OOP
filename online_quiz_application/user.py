class User:

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
        self.points = 0
        self.users_dict = {}

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value.strip():
            raise ValueError("Please enter some username!!")

        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not value.strip() or len(value) < 6:
            raise ValueError("Please enter some password higher than 6 letters!")

        self.__password = value

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        if value not in ["admin", "participant"]:
            raise ValueError("The role should be admin or participant!!")

        self.__role = value

    def register(self):
        if self.username not in self.users_dict:
            self.users_dict[self.username] = self.password

    def login(self, username, password):
        if username in self.users_dict and self.users_dict[username] == password:
            return True

        return False

    def logout(self, username):
        if username in self.users_dict:
            self.users_dict.pop(username)

