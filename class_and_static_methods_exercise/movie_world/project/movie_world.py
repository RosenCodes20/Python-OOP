class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            for dvd in self.dvds:
                if customer.id == customer_id:
                    if dvd.id == dvd_id:
                        if dvd in customer.rented_dvds:
                            return f"{customer.name} has already rented {dvd.name}"

                        if dvd.is_rented:
                            return "DVD is already rented"

                        if customer.age < dvd.age_restriction:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

                        customer.rented_dvds.append(dvd)
                        dvd.is_rented = True
                        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for dvd in self.dvds:
            for customers in self.customers:
                if dvd.id == dvd_id:
                    if customers.id == customer_id:
                        if dvd not in customers.rented_dvds:
                            return f"{customers.name} does not have that DVD"

                        customers.rented_dvds.remove(dvd)
                        dvd.is_rented = False
                        return f"{customers.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = [*[str(customer) for customer in self.customers], *[str(dvd) for dvd in self.dvds]]
        return "\n".join(map(str, result))
