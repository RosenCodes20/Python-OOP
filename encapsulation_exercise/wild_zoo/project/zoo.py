class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals) and price <= self.__budget:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__animal_capacity > len(self.animals) and price > self.__budget:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_sum = sum([w.salary for w in self.workers])
        if self.__budget >= workers_sum:
            self.__budget -= workers_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_for_animals = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= money_for_animals:
            self.__budget -= money_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ""
        result += f"You have {len(self.animals)} animals\n"

        lions = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        lions_length = len(lions)

        result += f"----- {lions_length} Lions:\n"
        result += "\n".join(map(str, lions))

        tigers = [animal for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        tigers_length = len(tigers)

        result += f"\n----- {tigers_length} Tigers:\n"
        result += "\n".join(map(str, tigers))

        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"]
        cheetah_length = len(cheetahs)

        result += f"\n----- {cheetah_length} Cheetahs:\n"
        result += "\n".join(map(str, cheetahs))

        return result

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]

        keepers = [worker for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        keepers_length = len(keepers)

        for keeper in keepers:
            result.append(f"----- {keepers_length} Keepers:")
            result.append(keeper)

        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        caretakers_length = len(caretakers)

        result.append(f"----- {caretakers_length} Caretakers:")
        for caretaker in caretakers:
            result.append(caretaker)

        vets = [worker for worker in self.workers if worker.__class__.__name__ == "Vet"]
        vets_length = len(vets)

        result.append(f"----- {vets_length} Vets:")
        for vet in vets:
            result.append(vet)

        return "\n".join(map(str, result))