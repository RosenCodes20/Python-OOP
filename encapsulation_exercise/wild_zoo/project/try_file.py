from project.worker import Worker
from project.animal import Animal
from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.vet import Vet
from project.caretaker import Caretaker
from project.zoo import Zoo

z = Zoo("My Zoo", 500, 3, 3)
z.hire_worker(Vet("Leo", 35, 100))
z.hire_worker(Keeper("Tigy", 40, 100))
z.hire_worker(Caretaker("Chi", 24, 100))
res = z.workers_status()
print(res, "You have 3 workers\n----- 1 Keepers:\nName: Tigy, Age: 40, Salary: 100\n----- 1 Caretakers:\nName: Chi, Age: 24, Salary: 100\n----- 1 Vets:\nName: Leo, Age: 35, Salary: 100")

