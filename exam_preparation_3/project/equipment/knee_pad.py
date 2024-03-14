from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PROTECTION = 120
    PRICE = 15.0

    def __init__(self):
        super(KneePad, self).__init__(self.PROTECTION, self.PRICE)

    def increase_price(self):
        self.price += self.price * 0.2