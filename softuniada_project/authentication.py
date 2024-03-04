from json import loads, dump

from canvas import root, frame
from tkinter import Button, Entry
from PIL import ImageTk, Image
from display_images import display_image_one, display_image_two, display_image_three, display_image_four


def get_name():
    users = []
    with open("information_for_user.txt", "r") as users_file:
        for element in users_file:
            users.append(loads(element))

    return users


def delete_all():
    frame.delete("all")


def login_and_registration():
    delete_all()
    frame.create_text(
        550,
        50,
        text="Welcome to my bottle shop!",
        font=("Aerial", 30),
        fill="blue"
    )

    login_button = Button(
        root,
        fg="white",
        bg="blue",
        text="Login",
        width=20,
        height=3,
        font=("Arial", 12),
        command=login
    )

    frame.create_window(550, 150, window=login_button)

    frame.create_text(
        550,
        225,
        text="If you don't have an account:",
        font=("Arial", 12),
        fill="black"
    )

    register_button = Button(
        root,
        fg="white",
        bg="green",
        text="Register",
        width=20,
        height=3,
        font=("Arial", 12),
        command=register
    )

    frame.create_window(
        550,
        300,
        window=register_button
    )

    continue_as_a_guest = Button(
        root,
        fg="white",
        bg="black",
        text="Continue as a guest",
        width=20,
        height=3,
        font=("Arial", 12),
        command=continue_as_a_guests
    )

    frame.create_text(
        550,
        370,
        text="*Notice if you continue as a guest you can only watch and buy nothing!",
        fill="black",
        font=("Arial", 10)
    )

    frame.create_window(550, 425, window=continue_as_a_guest)


def register():
    delete_all()
    frame.create_text(450, 200, text="First name:", fill="black", font=("Arial", 12))
    frame.create_text(450, 250, text="Last name:", fill="black", font=("Arial", 12))
    frame.create_text(450, 300, text="Username:", fill="black", font=("Arial", 12))
    frame.create_text(450, 350, text="Password:", fill="black", font=("Arial", 12))

    frame.create_window(550, 200, window=f_name_register_fill)
    frame.create_window(550, 250, window=l_name_register_fill)
    frame.create_window(550, 300, window=username_register_fill)
    frame.create_window(550, 350, window=password_register_fill)

    register_button = Button(
        root,
        fg="white",
        bg="green",
        text="Register",
        width=20,
        height=3,
        font=("Arial", 12),
        command=add_to_registration_dict
    )
    frame.create_window(540, 410, window=register_button)


def login():
    delete_all()

    frame.create_text(500, 200, text="Username:", font=("Arial", 12))
    frame.create_text(500, 230, text="Password:", font=("Arial", 12))

    frame.create_window(600, 200, window=username_fill)
    frame.create_window(600, 230, window=password_fill)

    login_button = Button(
        root,
        fg="white",
        bg="blue",
        text="Login",
        width=20,
        height=3,
        font=("Arial", 12),
        command=add_to_login_dict
    )
    frame.create_window(560, 280, window=login_button)

    don_t_have_an_account = Button(
        root,
        fg="white",
        bg="green",
        text="Create one",
        width=12,
        height=1,
        command=register
    )

    frame.create_text(520, 350, text="Don't have an account:", font=("Arial", 12))

    frame.create_window(646, 350, window=don_t_have_an_account)


def add_to_registration_dict():
    registration_dict = {
        "First name": f_name_register_fill.get(),
        "Last name": l_name_register_fill.get(),
        "Username": username_register_fill.get(),
        "Password": password_register_fill.get()
    }

    if check_registration(registration_dict):
        with open("information_for_user.txt", "a") as users_file:
            dump(registration_dict, users_file)
            users_file.write("\n")
            delete_all()
            login_and_registration()


def check_registration(registration_dict):
    frame.delete("error")

    for key, value in registration_dict.items():
        if not value.strip():
            frame.create_text(
                525,
                466,
                text=f"Please enter something in {key}",
                fill="red",
                tags="error"
            )
            return False

    users = get_name()

    for user in users:
        if user["First name"] == registration_dict["First name"]:
            frame.create_text(
                525,
                466,
                text=f"First name already taken!",
                fill="red",
                tags="error"
            )
            return False

        elif user["Last name"] == registration_dict["Last name"]:
            frame.create_text(
                525,
                466,
                text=f"Last name already taken!",
                fill="red",
                tags="error"
            )
            return False

        elif user["Username"] == registration_dict["Username"]:
            frame.create_text(
                525,
                466,
                text=f"Username already taken!",
                fill="red",
                tags="error"
            )
            return False

        elif user["Password"] == registration_dict["Password"]:
            frame.create_text(
                525,
                466,
                text=f"Password name already taken!",
                fill="red",
                tags="error"
            )
            return False

    return True


def add_to_login_dict():
    login_dict = {
        "Username": username_fill.get(),
        "Password": password_fill.get()
    }

    if check_login(login_dict):
        frame.create_text(
            560,
            380,
            text="You have successfully logged in!!!",
            fill="green",
            font=("Arial", 12)
        )
        frame.create_text(
            560,
            410,
            text="Do you want to go to the shop?",
            fill="black",
            font=("Arial", 12)
        )

        yes_button = Button(
            root,
            fg="white",
            bg="green",
            text="Yes",
            width=15,
            height=3,
            font=("Arial", 12),
            command=pressed_yes_button
        )
        frame.create_window(480, 460, window=yes_button)

        no_button = Button(
            root,
            fg="white",
            bg="red",
            text="No",
            width=15,
            height=3,
            font=("Arial", 12),
            command=pressed_no_button
        )
        frame.create_window(650, 460, window=no_button)


def check_login(login_dict):
    frame.delete("error")
    for key, value in login_dict.items():
        if not value.strip():
            frame.create_text(
                540,
                380,
                text=f"Please enter something in {key}",
                tags="error",
                fill="red"
            )
            return False

    users = get_name()

    for user in users:
        if user["Username"] == login_dict["Username"] and user["Password"] == login_dict["Password"]:
            return True

    else:
        frame.create_text(
            555,
            380,
            text=f"Invalid username or password!!!",
            tags="error",
            fill="red",
            font=("Arial", 12)
        )
        return False


def pressed_no_button():
    delete_all()
    login_and_registration()


def pressed_yes_button():
    delete_all()
    frame.create_text(
        550,
        30,
        text="Welcome to the shop!!",
        fill="black",
        font=("Arial", 20)
    )

    frame.create_text(
        500,
        510,
        text="Enter your budget:",
        fill="black",
        font=("Arial", 12)
    )

    frame.create_window(630, 510, window=budget)

    enter_the_budget = Button(
        root,
        fg="white",
        bg="green",
        text="Enter the budget",
        width=20,
        height=3,
        command=display_budget
    )
    frame.create_window(588, 560, window=enter_the_budget)

    bottle_one()
    bottle_two()
    bottle_three()
    bottle_four()


def bottle_one():
    global bottle_one_image, bottle_one_price, bottle_one_quantity, bottle_one_price_text, bottle_one_quantity_text
    bottle_one_image_path = "images/IMG_0490.JPG"
    original_image = Image.open(bottle_one_image_path)
    bottle_one_price = 50
    bottle_one_quantity = 10
    new_size = (200, 200)

    resized_image = original_image.resize(new_size)

    resized_image = resized_image.rotate(270)

    bottle_one_image = ImageTk.PhotoImage(resized_image)

    frame.create_image(
        180,
        180,
        image=bottle_one_image
    )
    buy_button = Button(
        root,
        fg="white",
        bg="green",
        text="Buy one",
        width=20,
        height=3,
        font=("Arial", 12),
        command=buy_bottle_one
    )

    description_of_the_bottle = Button(
        root,
        fg="white",
        bg="black",
        text="Bottle one Description",
        width=20,
        height=3,
        font=("Arial", 12),
        command=bottle_one_description
    )

    frame.create_window(180, 380, window=description_of_the_bottle)
    frame.create_window(180, 450, window=buy_button)

    bottle_one_price_text = frame.create_text(
        180,
        300,
        text=f"Price: {bottle_one_price}lv.",
        fill="black",
        font=("Arial", 12)
    )

    bottle_one_quantity_text = frame.create_text(
        180,
        330,
        text=f"Quantity: {bottle_one_quantity} bottles",
        fill="black",
        font=("Arial", 12)
    )


def bottle_two():
    global bottle_two_image, bottle_two_price, bottle_two_quantity, bottle_two_price_text, bottle_two_quantity_text
    bottle_two_image_path = "images/IMG_0491.JPG"
    original_image = Image.open(bottle_two_image_path)
    bottle_two_price = 70
    bottle_two_quantity = 10
    new_size = (200, 200)

    resized_image = original_image.resize(new_size)

    resized_image = resized_image.rotate(270)

    bottle_two_image = ImageTk.PhotoImage(resized_image)

    frame.create_image(
        435,
        180,
        image=bottle_two_image
    )

    buy_a_bottle_button = Button(
        root,
        fg="white",
        bg="green",
        text="Buy one",
        width=20,
        height=3,
        font=("Arial", 12),
        command=buy_bottle_two
    )

    bottle_two_description = Button(
        root,
        fg="white",
        bg="black",
        text="Bottle two description",
        width=20,
        height=3,
        font=("Arial", 12),
        command=bottle_two_descriptions
    )

    frame.create_window(425, 450, window=buy_a_bottle_button)
    frame.create_window(425, 380, window=bottle_two_description)

    bottle_two_price_text = frame.create_text(425, 300, text=f"Price: {bottle_two_price}lv.", fill="black",
                                              font=("Arial", 12))
    bottle_two_quantity_text = frame.create_text(425, 330, text=f"Quantity: {bottle_two_quantity} bottles.",
                                                 fill="black", font=("Arial", 12))


def bottle_three():
    global bottle_three_image, bottle_three_price, bottle_three_quantity, bottle_three_price_text, bottle_three_quantity_text
    bottle_three_image_path = "images/IMG_0493.JPG"
    original_image = Image.open(bottle_three_image_path)
    bottle_three_price = 90
    bottle_three_quantity = 10
    new_size = (200, 200)

    resized_image = original_image.resize(new_size)

    resized_image = resized_image.rotate(270)

    bottle_three_image = ImageTk.PhotoImage(resized_image)

    frame.create_image(
        685,
        180,
        image=bottle_three_image
    )

    bottle_three_price_text = frame.create_text(
        685,
        300,
        text=f"Price: {bottle_three_price}lv.",
        font=("Arial", 12)
    )

    bottle_three_quantity_text = frame.create_text(
        685,
        330,
        text=f"Quantity: {bottle_three_quantity} bottles",
        font=("Arial", 12)
    )

    buy_one_button = Button(
        root,
        fg="white",
        bg="green",
        text="Buy one",
        width=20,
        height=3,
        font=("Arial", 12),
        command=buy_bottle_three
    )

    description_button = Button(
        root,
        fg="white",
        bg="black",
        text="Bottle three description",
        width=20,
        height=3,
        font=("Arial", 12),
        command=bottle_three_description
    )

    frame.create_window(685, 380, window=description_button)
    frame.create_window(685, 450, window=buy_one_button)


def bottle_four():
    global bottle_four_image, bottle_four_price, bottle_four_quantity, bottle_four_price_text, bottle_four_quantity_text
    bottle_four_image_path = "images/IMG_0488.JPG"
    original_image = Image.open(bottle_four_image_path)
    bottle_four_price = 100
    bottle_four_quantity = 10
    new_size = (200, 200)

    resized_image = original_image.resize(new_size)

    resized_image = resized_image.rotate(270)

    bottle_four_image = ImageTk.PhotoImage(resized_image)

    frame.create_image(
        940,
        180,
        image=bottle_four_image
    )

    bottle_four_price_text = frame.create_text(
        940,
        300,
        text=f"Price: {bottle_four_price}lv.",
        fill="black",
        font=("Arial", 12)
    )

    bottle_four_quantity_text = frame.create_text(
        940,
        330,
        text=f"Quantity: {bottle_four_quantity}bottles",
        fill="black",
        font=("Arial", 12)
    )

    buy_one_button = Button(
        root,
        fg="white",
        bg="green",
        text="Buy one",
        width=20,
        height=3,
        font=("Arial", 12),
        command=buy_bottle_four
    )

    description_four_button = Button(
        root,
        fg="white",
        bg="black",
        text="Bottle four description",
        width=20,
        height=3,
        font=("Arial", 12),
        command=bottle_four_description
    )

    frame.create_window(940, 380, window=description_four_button)
    frame.create_window(940, 450, window=buy_one_button)


def continue_as_a_guests():
    delete_all()

    frame.create_text(
        500,
        50,
        text="Welcome to the guest shop!!",
        font=("Arial", 20)
    )

    back_to_registration_page = Button(
        root,
        fg="white",
        bg="red",
        text="Back to login page",
        width=20,
        height=3,
        font=("Arial", 12),
        command=login_and_registration
    )

    frame.create_text(
        500,
        450,
        text="If you want to go back to the login page press:",
        fill="black",
        font=("Arial", 12)
    )

    frame.create_window(500, 500, window=back_to_registration_page)

    display_image_one()
    display_image_two()
    display_image_three()
    display_image_four()


def bottle_one_description():
    global bottle_one_image
    delete_all()
    bottle_one_image_path = "images/IMG_0490.JPG"
    original_image = Image.open(bottle_one_image_path)
    new_size = (300, 300)

    resized_image = original_image.resize(new_size)

    resized_image = resized_image.rotate(270)

    bottle_one_image = ImageTk.PhotoImage(resized_image)

    frame.create_image(
        550,
        180,
        image=bottle_one_image
    )

    frame.create_text(
        650,
        400,
        text="This is bottle one it's named the pyramid because it has unique blue pyramids."
             "\nIt's like it's made in Egypt."
             "\nIf you like it buy one ;)",
        fill="black",
        font=("Arial", 15)
    )

    back_to_the_shop_button = Button(
        root,
        fg="white",
        bg="red",
        text="Back to the shop",
        width=20,
        height=3,
        font=("Arial", 12),
        command=back_to_the_shop
    )
    frame.create_window(550, 500, window=back_to_the_shop_button)


def bottle_two_descriptions():
    global bottle_two_image
    delete_all()
    bottle_one_image_path = "images/IMG_0491.JPG"
    original_image = Image.open(bottle_one_image_path)
    new_size = (300, 300)

    resized_image = original_image.resize(new_size)

    resized_image = resized_image.rotate(270)

    bottle_two_image = ImageTk.PhotoImage(resized_image)

    frame.create_image(
        550,
        180,
        image=bottle_two_image
    )

    frame.create_text(
        650,
        400,
        text="This is bottle two it's named the spring because it's like the spring is coming and it's very beautiful."
             "\nIt's like it's made in a south country where the weather is always good and never rains."
             "\nIf you are a fan of spring season buy one ;)",
        fill="black",
        font=("Arial", 15)
    )

    back_to_the_shop_button = Button(
        root,
        fg="white",
        bg="red",
        text="Back to the shop",
        width=20,
        height=3,
        font=("Arial", 12),
        command=back_to_the_shop
    )
    frame.create_window(550, 500, window=back_to_the_shop_button)


def bottle_three_description():
    global bottle_three_image
    delete_all()
    bottle_one_image_path = "images/IMG_0493.JPG"
    original_image = Image.open(bottle_one_image_path)
    new_size = (300, 300)

    resized_image = original_image.resize(new_size)

    resized_image = resized_image.rotate(270)

    bottle_three_image = ImageTk.PhotoImage(resized_image)

    frame.create_image(
        550,
        180,
        image=bottle_three_image
    )

    frame.create_text(
        650,
        400,
        text="This is bottle three it's named Baba Marta because it represents the bulgarian holiday named Baba Marta"
             "\nIt's like it's made in a very very old time and it's like representing the bulgarian traditions."
             "\nIf you are a fan of the bulgarian traditions buy one ;)",
        fill="black",
        font=("Arial", 15)
    )

    back_to_the_shop_button = Button(
        root,
        fg="white",
        bg="red",
        text="Back to the shop",
        width=20,
        height=3,
        font=("Arial", 12),
        command=back_to_the_shop
    )
    frame.create_window(550, 500, window=back_to_the_shop_button)


def bottle_four_description():
    global bottle_four_image
    delete_all()
    bottle_four_image_path = "images/IMG_0488.JPG"
    original_image = Image.open(bottle_four_image_path)
    new_size = (300, 300)

    resized_image = original_image.resize(new_size)

    resized_image = resized_image.rotate(270)

    bottle_four_image = ImageTk.PhotoImage(resized_image)

    frame.create_image(
        550,
        180,
        image=bottle_four_image
    )

    frame.create_text(
        650,
        400,
        text="This is bottle four it's named the forest because it represents the forest by it's flowers and animals."
             "\nIt's like it's made in a argentinian region where the forests are everywhere"
             "\nIf you are a fan of the forests buy one ;)",
        fill="black",
        font=("Arial", 15)
    )

    back_to_the_shop_button = Button(
        root,
        fg="white",
        bg="red",
        text="Back to the shop",
        width=20,
        height=3,
        font=("Arial", 12),
        command=back_to_the_shop
    )
    frame.create_window(550, 500, window=back_to_the_shop_button)


def back_to_the_shop():
    delete_all()
    pressed_yes_button()


def display_budget():
    frame.delete("error")
    global current_budget, budget_text_id, budget_dict
    budget_dict = {"Budget": budget.get()}
    for k, v in budget_dict.items():
        if v.strip():
            current_budget = int(budget.get())
            budget_text_id = frame.create_text(
                1100,
                30,
                text=f"Budget: {budget.get()}lv",
                fill="black",
                font=("Arial", 12)
            )

        else:
            frame.create_text(
                1100,
                30,
                text=f"Please enter a budget!!!!",
                fill="red",
                font=("Arial", 12),
                tags="error"
            )


def buy_bottle_one():
    frame.delete("error")

    global bottle_one_price, bottle_one_quantity, bottle_one_quantity_text, current_budget, budget_text_id, budget_dict
    budget_dict = {"Budget": budget.get()}
    if budget_dict["Budget"].strip():
        if bottle_one_quantity > 0:
            bottle_one_quantity -= 1
            frame.delete(bottle_one_quantity_text)
            bottle_one_quantity_text = frame.create_text(
                180,
                330,
                text=f"Quantity: {bottle_one_quantity} bottles",
                fill="black",
                font=("Arial", 12)
            )

        else:
            raise SystemExit("There is no more bottles. Bye for now..")

        if bottle_one_price > current_budget:
            raise SystemExit("Price exceeds budget. Program will exit.")

        if current_budget > 0:
            current_budget -= bottle_one_price
            frame.delete(budget_text_id)
            budget_text_id = frame.create_text(
                1100,
                30,
                text=f"Budget: {current_budget}lv",
                fill="black",
                font=("Arial", 12)
            )

        else:
            raise SystemExit("You don't have enough money to buy the bottle. Bye for now...")

    else:
        frame.create_text(
            1100,
            30,
            text="Please enter a budget!!!!",
            fill="red",
            font=("Arial", 12),
            tags="error"
        )


def buy_bottle_two():
    frame.delete("error")
    global bottle_two_price, bottle_two_quantity, bottle_two_quantity_text, current_budget, budget_text_id, budget_dict
    budget_dict = {"Budget": budget.get()}
    if budget_dict["Budget"].strip():
        if bottle_two_quantity > 0:
            bottle_two_quantity -= 1
            frame.delete(bottle_two_quantity_text)
            bottle_two_quantity_text = frame.create_text(
                425,
                330,
                text=f"Quantity: {bottle_two_quantity} bottles",
                fill="black",
                font=("Arial", 12)
            )

        else:
            raise SystemExit("There is no more bottles. Bye for now..")

        if bottle_two_price > current_budget:
            raise SystemExit("Price exceeds budget. Program will exit.")

        if current_budget > 0:
            current_budget -= bottle_two_price
            frame.delete(budget_text_id)
            budget_text_id = frame.create_text(
                1100,
                30,
                text=f"Budget: {current_budget}lv",
                fill="black",
                font=("Arial", 12)
            )

        else:
            raise SystemExit("You don't have enough money to buy the bottle. Bye for now...")

    else:
        frame.create_text(
            1100,
            30,
            text="Please enter a budget!!!!",
            fill="red",
            font=("Arial", 12),
            tags="error"
        )


def buy_bottle_three():
    frame.delete("error")
    global bottle_three_price, bottle_three_quantity, bottle_three_quantity_text, current_budget, budget_text_id, budget_dict
    budget_dict = {"Budget": budget.get()}
    if budget_dict["Budget"].strip():
        if bottle_three_quantity > 0:
            bottle_three_quantity -= 1
            frame.delete(bottle_three_quantity_text)
            bottle_three_quantity_text = frame.create_text(
                685,
                330,
                text=f"Quantity: {bottle_three_quantity} bottles",
                fill="black",
                font=("Arial", 12)
            )

        else:
            raise SystemExit("There is no more bottles. Bye for now..")

        if bottle_three_price > current_budget:
            raise SystemExit("Price exceeds budget. Program will exit.")

        if current_budget > 0:
            current_budget -= bottle_three_price
            frame.delete(budget_text_id)
            budget_text_id = frame.create_text(
                1100,
                30,
                text=f"Budget: {current_budget}lv",
                fill="black",
                font=("Arial", 12)
            )

        else:
            raise SystemExit("You don't have enough money to buy the bottle. Bye for now...")

    else:
        frame.create_text(
            1100,
            30,
            text="Please enter a budget!!!!",
            fill="red",
            font=("Arial", 12),
            tags="error"
        )


def buy_bottle_four():
    frame.delete("error")
    global bottle_four_price, bottle_four_quantity, bottle_four_quantity_text, current_budget, budget_text_id, budget_dict
    budget_dict = {"Budget": budget.get()}
    if budget_dict["Budget"].strip():
        if bottle_four_quantity > 0:
            bottle_four_quantity -= 1
            frame.delete(bottle_four_quantity_text)
            bottle_four_quantity_text = frame.create_text(
                940,
                330,
                text=f"Quantity: {bottle_four_quantity} bottles",
                fill="black",
                font=("Arial", 12)
            )

        else:
            raise SystemExit("There is no more bottles. Bye for now..")

        if bottle_four_price > current_budget:
            raise SystemExit("Price exceeds budget. Program will exit.")

        if current_budget > 0:
            current_budget -= bottle_four_price
            frame.delete(budget_text_id)
            budget_text_id = frame.create_text(
                1100,
                30,
                text=f"Budget: {current_budget}lv",
                fill="black",
                font=("Arial", 12)
            )

        else:
            raise SystemExit("You don't have enough money to buy the bottle. Bye for now...")

    else:
        frame.create_text(
            1100,
            30,
            text="Please enter a budget!!!!",
            fill="red",
            font=("Arial", 12),
            tags="error"
        )


username_fill = Entry(root, bd=0)
password_fill = Entry(root, bd=0, show="*")

f_name_register_fill = Entry(root, bd=0)
l_name_register_fill = Entry(root, bd=0)
username_register_fill = Entry(root, bd=0)
password_register_fill = Entry(root, bd=0, show="*")

budget = Entry(root, bd=0)
