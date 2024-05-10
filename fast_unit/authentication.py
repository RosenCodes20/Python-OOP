import re
from random import choice
from tkinter import Button, Entry
from fast_unit.canvas import frame, root

numbers_in_class = {'19101': 'Александра Павлинова Лилова', '19102': 'Ана Христова Василева', '19103': 'Борис Ивов Тодоров', '19104': 'Даниел Ивайлов Иванов', '19105': 'Дахил Февзан Дахил', '19106': 'Дениз Красимиров Милев', '19107': 'Ивайло Калоянов Иванов', '19108': 'Иван Данаилов Григоров', '19109': 'Ивон Илиянова Дилова', '19110': 'Илиян Василев Николов', '19111': 'Красимир Иванов Цветанов', '19112': 'Кристиян Михайлов Михайлов', '19113': 'Любомир Павлов Билев', '19114': 'Марк Петър Петров', '19115': 'Мартин Бориславов Стоименов', '19117': 'Павел Марианов Пешев', '19118': 'Петър Ивайлов Николаев', '19119': 'Радослав Цветославов Маринов', '19120': 'Ралица Калоянова Радкова', '19121': 'Теодор Бориславов Борисов', '19122': 'Теодор Сергеев Пацов', '19123': 'Теодора Николаева Недялкова', '19124': 'Цветелин Валентинов Любенов ', '19125': 'Цветелин Пламенов Спасов', '19126': 'Цветина Тихомирова Томова', '19128': 'Цветомир Мирославов Мичов', '19129': 'Йордан Лазаров Иванов', '19130': 'Стефан Йорданов Стаменов', '19201': 'Александър Георгиев Петров', '19202': 'Алексиа Владимирова Цветанова', '19203': 'Биляна Иванова Любомирова', '19204': 'Васил Ивайло Иванов', '19205': 'Виктор Валериев Асенов', '19206': 'Георги Георгиев Манчев', '19207': 'Грета Валериева Йорданова', '19208': 'Денис Добромиров Петков', '19209': 'Денислав Галинов Топалов', '19211': 'Дияна Ивайлова Трифонова', '19212': 'Ивайло Радославов Джамбазов', '19213': 'Ивослав Живков Петков', '19214': 'Йоаннис Панайоту', '19215': 'Карина Антонова Ботева', '19216': 'Константин Пламенов Петков', '19217': 'Лилия Юриева Лазарова ', '19218': 'Мартин Руменов Йонков', '19219': 'Митко Миленов Иванов', '19220': 'Михаела Дилянова Михайлова', '19221': 'Момчил Ивайлов Колев', '19222': 'Никола Цветанов Расташки', '19223': 'Петър Петров Петров', '19224': 'Петър Станиславов Иванов', '19225': 'Росен Пламенов Климентов', '19227': 'Теодор Николаев Колев', '19228': 'Цанко Доков Доков', '19301': 'Валентин Ивайлов Николов', '19302': 'Георги Любомиров Христов', '19303': 'Георги Юлиянов Орешков', '19304': 'Данина Владимирова Кьосева', '19305': 'Емануил Бориславов Димитров', '19306': 'Ерика Аспарухова Кирилова', '19307': 'Жори Ивайлов Жориев', '19309': 'Иван Веселинов Вушовски', '19310': 'Красимир Евгениев Григоров', '19311': 'Кристиан Пламенов Кишкин', '19312': 'Кристиян Ивайлов Геoргиев', '19313': 'Кристиян Кръстев Йорданов', '19314': 'Кристиян Юлиянов Орешков', '19315': 'Мартин Кръстев Йорданов', '19316': 'Мелани Венциславова Стоименова', '19317': 'Петър Руменов Костов', '19318': 'Петър Огнянов Митков', '19319': 'Пламен Здравков Здравков', '19320': 'Симон Николов Господинов', '19321': 'Стивън Вергилов Борисов', '19322': 'Христиана Ивова Велизарова', '19323': 'Християн Иванов Каменов', '19324': 'Цветелин Весков Захариев', '19325': 'Цвети Ивайлова Боженска', '19326': 'Цветина Стефанова Велчева', '19327': 'Цветослав Станиславов Маринов', '19328': 'Юлиан Юлиянов Лазаров', '19329': 'Мартин Николаев Коцев', '19401': 'Александър Сашо Чакъров', '19402': 'Александър Свиленов Белчев', '19405': 'Боян Ивов Фотев', '19406': 'Валери Валериев Богданов', '19407': 'Велислав Станиславов Борисов', '19408': 'Георги Албенов Ангелов', '19409': 'Георги Петров Балджиев', '19410': 'Даниел Николаев Попов', '19411': 'Денис Недялков Бодуров', '19412': 'Денис Стефанов Савев    сам. ф-ма', '19413': 'Доналд Денис Фрейзър', '19414': 'Ели Иванова Ставрева', '19415': 'Йоана Георгиева Декова', '19416': 'Йоана Християнова Христова', '19417': 'Калоян Владимиров Станев', '19418': 'Мартин Емилов Асенов', '19419': 'Мирослав Мирославов Велев', '19420': 'Михаил Свиленов Белчев', '19422': 'Преслав Маринов Стоянов', '19423': 'Радослав Иванов Арабаджиев', '19425': 'Стефан Пламенов Пенчев', '19426': 'Стоян Динков Христов', '19427': 'Теодор Георгиев Янакиев', '19429': '.............................................................................', '19431': 'Яна Юлиянова Василева', '19432': 'Петко Красимиров Петков', '19434': 'Йоан Леонидов Иванов', '19502': 'Александър Василев Йончев', '19503': 'Александър Никифоров Илиев', '19504': 'Ангел Веселинов Чантов', '19505': 'Благовест Филипов Гьошев', '19506': 'Венелин Страхилов Павлов', '19507': 'Веселин Маринов Атанасов', '19509': 'Виктория Петрова Петрова', '19510': 'Герасим Емилов Григоров', '19511': 'Денислав Панчев Драганов', '19512': 'Димитър Чавдаров Дилков', '19513': 'Емил Антонов Коруджиев', '19514': 'Етиен Николаев Минчев', '19515': 'Ивайла Найденова Илиева', '19516': 'Ивайло Павлов Петков', '19517': 'Ивелин Пламенов Иванов', '19518': 'Йордан Ивов Цанов', '19519': 'Катерина Станиславова Петрова', '19520': 'Мартин Димитров Ангелов', '19521': 'Никол Георгиева Бутова', '19522': 'Николай Николаев Иванов', '19523': 'Павлин Красимиров Въчев', '19524': 'Преслава Пламенова Проданова', '19526': 'Филип Георгиев Георгиев', '19527': 'Цветан Петров Николов',  '19529': 'Дейвид Юлианов Зарев', '19530': 'Цецко Илиев Няголов', '19531': 'Силвестър Илиянов Цолов', '19532': 'Владимир Георгиев Тодоров', '18407': 'Велко Стефанов Клисарски'}
numbers_for_first_teacher = []
numbers_for_second_teacher = []
numbers_for_third_teacher = []

for _ in range(len(numbers_in_class)):
    if numbers_in_class:
        num_one, name_of_the_first_student = choice(list(numbers_in_class.items()))
        del numbers_in_class[num_one]

        num_two, name_of_the_second_student = choice(list(numbers_in_class.items()))
        del numbers_in_class[num_two]

        num_three, name_of_the_third_student = choice(list(numbers_in_class.items()))
        del numbers_in_class[num_three]

        numbers_for_first_teacher.append(f"{num_one}-{name_of_the_first_student}")
        numbers_for_second_teacher.append(f"{num_two}-{name_of_the_second_student}")
        numbers_for_third_teacher.append(f"{num_three}-{name_of_the_third_student}")


def delete_all():
    frame.delete("all")


def main():
    generate_button = Button(
        root,
        fg="white",
        bg="green",
        text="Започни да генерираш",
        width=20,
        height=3,
        font=("Arial", 12),
        command=generation
    )

    frame.create_window(625, 350, window=generate_button)

    frame.create_text(
        520,
        200,
        text="Първа Комисия:",
        font=("Arial", 16)
    )

    frame.create_text(
        520,
        240,
        text="Втора Комисия:",
        font=("Arial", 16)
    )

    frame.create_text(
        520,
        280,
        text="Трета Комисия:",
        font=("Arial", 16)
    )

    frame.create_window(690, 200, window=first_teacher)
    frame.create_window(695, 240, window=second_teacher)
    frame.create_window(692, 280, window=third_teacher)


def generation():
    delete_all()
    remove_students()

    frame.create_text(
        150,
        200,
        text=f"{first_teacher.get()} ще изпитва номерата:",
        font=("Arial", 14)
    )

    frame.create_text(
        150,
        240,
        text=f"{second_teacher.get()} ще изпитва номерата:",
        font=("Arial", 14)
    )

    frame.create_text(
        150,
        280,
        text=f"{third_teacher.get()} ще изпитва номерата:",
        font=("Arial", 14)
    )

    create_file_button = Button(
        root,
        fg="white",
        bg="blue",
        text="Създай файл",
        width=20,
        height=3,
        font=("Arial", 12),
        command=create_file
    )

    frame.create_window(625, 490, window=create_file_button)

    generate_button = Button(
        root,
        fg="white",
        bg="green",
        text="Генерирай",
        width=20,
        height=3,
        font=("Arial", 12),
        command=start_generating
    )

    frame.create_window(625, 350, window=generate_button)


def start_generating():
    frame.create_text(
        816,
        200,
        text=", ".join(map(str, [x[0:5] for x in numbers_for_first_teacher])),
        font=("Arial", 6),
        tag="students_list"
    )

    frame.create_text(
        816,
        240,
        text=", ".join(map(str, [x[0:5] for x in numbers_for_second_teacher])),
        font=("Arial", 6),
        tag="students_list"
    )

    frame.create_text(
        816,
        280,
        text=", ".join(map(str, [x[0:5] for x in numbers_for_third_teacher])),
        font=("Arial", 6),
        tag="students_list"
    )


def remove_students():
    frame.create_text(
        500,
        100,
        text="Напишете студенти, които не са изпратили курсова работа или не могат да се явят на изпит:",
        font=("Arial", 12)
    )

    frame.create_window(900, 100, window=students_to_remove)

    remove_button = Button(
        root,
        fg="white",
        bg="red",
        text="Премахни студентите",
        width=20,
        height=3,
        font=("Arial", 12),
        command=remove
    )
    frame.create_window(625, 420, window=remove_button)


def remove():
    global numbers_for_first_teacher, numbers_for_second_teacher, numbers_for_third_teacher
    string_nums_to_remove = students_to_remove.get()
    nums_regex = r"[0-9]+"
    numbers_for_first_teacher_without_students = [x[0:5] for x in numbers_for_first_teacher]
    numbers_for_second_teacher_without_students = [x[0:5] for x in numbers_for_second_teacher]
    numbers_for_third_teacher_without_students = [x[0:5] for x in numbers_for_third_teacher]
    found_nums = re.findall(nums_regex, string_nums_to_remove)

    for number in found_nums:
        if number in numbers_for_first_teacher_without_students:
            numbers_for_first_teacher = [numbers for numbers in numbers_for_first_teacher if number not in numbers_for_first_teacher]
            numbers_for_first_teacher_without_students.remove(number)

        elif number in numbers_for_second_teacher_without_students:
            numbers_for_second_teacher_without_students.remove(number)

        elif number in numbers_for_third_teacher_without_students:
            numbers_for_third_teacher_without_students.remove(number)

    frame.delete("students_list")

    frame.create_text(
        816,
        200,
        text=", ".join(map(str, numbers_for_first_teacher_without_students)),
        font=("Arial", 6),
        tag="students_list"
    )

    frame.create_text(
        816,
        240,
        text=", ".join(map(str, numbers_for_second_teacher_without_students)),
        font=("Arial", 6),
        tag="students_list"
    )

    frame.create_text(
        816,
        280,
        text=", ".join(map(str, numbers_for_third_teacher_without_students)),
        font=("Arial", 6),
        tag="students_list"
    )


def create_file():
    with open("commission_file.txt", "w", encoding="utf-8") as commission_file:
        commission_file.write(f"Комисия номер 1 - {first_teacher.get()}\n")
        commission_file.write("Дипломанти:\n")
        commission_file.write("\n".join(numbers_for_first_teacher))

        commission_file.write(f"\n\nКомисия номер 2 - {second_teacher.get()}\n")
        commission_file.write("Дипломанти:\n")
        commission_file.write("\n".join(numbers_for_second_teacher))

        commission_file.write(f"\n\nКомисия номер 3 - {third_teacher.get()}\n")
        commission_file.write("Дипломанти:\n")
        commission_file.write("\n".join(numbers_for_third_teacher))


first_teacher = Entry(root, bd=0, width=15)
first_teacher.config(font=("Arial", 16))
second_teacher = Entry(root, bd=0, width=15)
second_teacher.config(font=("Arial", 16))
third_teacher = Entry(root, bd=0, width=15)
third_teacher.config(font=("Arial", 16))
students_to_remove = Entry(root, bd=0)