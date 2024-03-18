from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity):
        self.capacity = capacity  # The number of clients а Bank can have.
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        new_loan = self.VALID_LOANS[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type, client_name, client_id, income):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."

        new_client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type, client_id):
        client = next(filter(lambda c: c.client_id == client_id, self.clients))
        loan = next(filter(lambda l: l.__class__.__name__ == loan_type, self.loans))

        if isinstance(client, Student) and not isinstance(loan, StudentLoan):
            raise Exception("Inappropriate loan type!")

        elif isinstance(client, Adult) and not isinstance(loan, MortgageLoan):
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))

        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type):
        loan = [l for l in self.loans if l.__class__.__name__ == loan_type]

        for loans in loan:
            loans.increase_interest_rate()

        return f"Successfully changed {len(loan)} loans."

    def increase_clients_interest(self, min_rate):
        clients = [c for c in self.clients if c.interest < min_rate]
        for client in clients:
            client.increase_clients_interest()

        return f"Number of clients affected: {len(clients)}."

    def get_statistics(self):
        clients_income = [c.income for c in self.clients]
        granted_loans = [len(c.loans) for c in self.clients]
        loans_sum = sum([element.amount for c in self.clients for element in c.loans])
        not_granted_sum = sum([l.amount for l in self.loans])
        clients_interest = sum([c.interest for c in self.clients]) / len(self.clients) if self.clients else 0
        return f"Active Clients: {len(self.clients)}\n" \
               f"Total Income: {sum(clients_income):.2f}\n" \
               f"Granted Loans: {sum(granted_loans)}, Total Sum: {loans_sum:.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n" \
               f"Average Client Interest Rate: {clients_interest:.2f}"
