from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTHS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy, name, price):
        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{name} already exists!")

        new_delicacy = self.VALID_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth, booth_number, capacity):
        for booths in self.booths:
            if booths.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = self.VALID_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):
        try:
            right_booth = next(filter(lambda b: not b.is_reserved and b.capacity >= number_of_people, self.booths))

        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        right_booth.reserve(number_of_people)
        return f"Booth {right_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number, delicacy_name):
        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))

        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))

        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        prices = sum([order.price for order in booth.delicacy_orders])
        bill = booth.price_for_reservation + prices
        self.income += bill
        booth.delicacy_orders.clear()
        booth.price_for_reservation = 0
        booth.is_reserved = False
        return f"Booth {booth_number}:\n"\
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."