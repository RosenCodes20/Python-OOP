class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value

        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        eight_chars = False
        one_upper = False
        one_digit = False
        digits = 0
        upper = 0
        if len(value) >= 8:
            eight_chars = True

        for letter in value:
            if letter.isdigit():
                digits += 1

            elif letter.isupper():
                upper += 1

        if digits >= 1:
            one_digit = True

        if upper >= 1:
            one_upper = True

        if eight_chars and one_upper and one_digit:
            self.__password = value

        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
