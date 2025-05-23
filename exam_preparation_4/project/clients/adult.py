from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INITIAL_INTEREST = 4

    def __init__(self, name, client_id, income):
        super(Adult, self).__init__(name, client_id, income, self.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += 2