class Defence:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target, damage):
        target.health -= damage

    def take_damage(self, damage):
        if self.health - damage <= 0:
            self.health = 0
            return f'{self.name} is destroyed!'

        self.health -= damage

    def repair(self, health_to_add):
        self.health += health_to_add


class Archer(Defence):
    def __init__(self, name, health, range):
        super().__init__(name, health)
        self.range = range

    def defend(self, castle):
        return f"Archer Tower {self.name} is defending {castle.name}"

class Castle(Defence):
    def __init__(self, name, health, drawbridge):
        super().__init__(name, health)
        self.drawbridge = drawbridge
        self.defenders = []
        self.towers = []

    def add_defender(self, warrior):
        if warrior in self.defenders:
            raise Exception('Warrior already in defenders!')
        self.defenders.append(warrior)

    def remove_defender(self, warrior):
        if warrior not in self.defenders:
            raise ValueError('Please enter a right warrior!')

        self.defenders.remove(warrior)

    def add_tower(self, tower):
        if tower in self.towers:
            raise Exception('Tower already in towers')

        self.towers.append(tower)

    def remove_tower(self, tower):
        if tower not in self.towers:
            raise ValueError('Please enter a right tower!')

        self.towers.remove(tower)

class Warrior:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power

class Knight(Warrior):
    def __init__(self, name, health, attack_power, armour, weapon):
        super().__init__(name, health, attack_power)
        self.armour = armour
        self.weapon = weapon

    def defend(self, castle):
        if self.armour > 50:
            return f"Knight {self.name} stands strong at the gates of {castle.name}!"

        return f"Knight {self.name} is defending {castle.name}"

    def fight(self, warrior):

        if warrior.__class__.__name__ == 'Knight':
            warrior.armour -= self.attack_power

            if warrior.armour <= 0:
                warrior.health -= self.attack_power

                if warrior.health < 0:
                    return 'Victory!'

                else:
                    return 'Defeat!'

        else:
            warrior.health -= self.attack_power

            if warrior.health <= 0:
                return 'Victory!'

            else:
                return 'Defeat!'

archer = Archer("Rosen", 100, 50)
castle = Castle('Disney', 200, 60)

castle_two = Castle('Ethiopia', 250, 100)

knight = Knight('Ioan', 200, 100, 80,'sword')
knight_two = Knight('Guri', 150, 80, 60, 'axe')

warrior = Warrior('Ivcho', 200, 100)

archer.attack(castle, 20)

print(castle.health)

print('--------')

archer.take_damage(50)

print(archer.health)

print(archer.take_damage(50))
print('--------')

archer.repair(100)

print(archer.health)
print('--------')

print(archer.defend(castle))

print('--------')


castle.add_defender(archer)
print(castle.defenders)
# print(castle.add_defender(archer)) Raising an exception!!

castle.remove_defender(archer)
print(castle.defenders)

# castle.remove_defender(archer) Raising an exception!!

print('--------')

castle.add_tower(castle_two)
print(castle.towers)

# print(castle.add_tower(castle_two)) Raising an exception!!

castle.remove_tower(castle_two)
print(castle.towers)

# print(castle.remove_tower(castle_two)) Raising an exception!!

print('--------')

print(castle.health)
knight.attack(castle)

print(castle.health)

print('-------')

print(knight.defend(castle))

knight.armour = 49

print(knight.defend(castle))

print('-------')

print(knight.fight(knight_two))

print(knight_two.armour)

print(knight.fight(knight_two))

print(knight_two.health)

print(warrior.health)
print('------')
print(knight.fight(warrior))
print(warrior.health)
print(knight.fight(warrior))
print(warrior.health)
print('--------')