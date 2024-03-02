class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        splitted_name = name.split("@")[0]
        if len(splitted_name) >= self.min_length:
            return True

        return False

    def __is_mail_valid(self, mail):
        if "@" in mail:
            splitted_mail = mail.split("@")[1]
            dot_splitted_mail = splitted_mail.split(".")[0]
            if dot_splitted_mail in self.mails:
                return True

            return False
        else:
            if mail in self.mails:
                return True
            return False

    def __is_domain_valid(self, domain):
        if "." in domain:
            splitted_domain = domain.split(".")[1]
            if splitted_domain in self.domains:
                return True

            return False

        else:
            if domain in self.domains:
                return True

            return False

    def validate(self, email):
        if self.__is_domain_valid(email) and self.__is_mail_valid(email) and self.__is_name_valid(email):
            return True

        return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
