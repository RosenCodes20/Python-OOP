from project.clients.base_client import BaseClient


class Student(BaseClient):
    INITIAL_INTEREST = 2

    def __init__(self, name, client_id, income):
        super(Student, self).__init__(name, client_id, income, self.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += 1