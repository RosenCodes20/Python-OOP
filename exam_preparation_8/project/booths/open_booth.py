from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.50

    def reserve(self, number_of_people):
        self.price_for_reservation = self.PRICE_PER_PERSON * number_of_people
        self.is_reserved = True