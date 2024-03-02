from json import loads, dump

from canvas import root, frame
from tkinter import Button, Entry
from PIL import ImageTk, Image
from display_images import display_image_one, display_image_two, display_image_three


def get_name():
    users = []
    with open("information_for_user.txt", "r") as users_file:
        for element in users_file:
            users.append(loads(element))

    return users


def delete_all():
    frame.delete("all")


def login_and_registration():
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

        elif user["Username"] != login_dict["Username"] or user["Password"] != login_dict["Password"]:
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
    bottle_one()
    bottle_two()
    bottle_three()


def bottle_one():
    global bottle_one_image, bottle_price, bottle_quantity
    bottle_one_image_path = "images/IMG_0490.JPG"
    original_image = Image.open(bottle_one_image_path)
    bottle_price = 50
    bottle_quantity = 10
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
        font=("Arial", 12)
    )

    description_of_the_bottle = Button(
        root,
        fg="white",
        bg="black",
        text="Bottle one Description",
        width=20,
        height=3,
        font=("Arial", 12)
    )

    frame.create_window(180, 380, window=description_of_the_bottle)
    frame.create_window(180, 450, window=buy_button)

    frame.create_text(
        180,
        300,
        text=f"Price: {bottle_price}lv.",
        fill="black",
        font=("Arial", 12)
    )

    frame.create_text(
        180,
        330,
        text=f"Quantity: {bottle_quantity} bottles",
        fill="black",
        font=("Arial", 12)
    )


def bottle_two():
    global bottle_two_image, bottle_two_price, bottle_two_quantity
    bottle_one_image_path = "images/IMG_0491.JPG"
    original_image = Image.open(bottle_one_image_path)
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
        font=("Arial", 12)
    )

    bottle_two_description = Button(
        root,
        fg="white",
        bg="black",
        text="Bottle two description",
        width=20,
        height=3,
        font=("Arial", 12)
    )

    frame.create_window(425, 450, window=buy_a_bottle_button)
    frame.create_window(425, 380, window=bottle_two_description)

    frame.create_text(425, 300, text=f"Price: {bottle_two_price}lv.", fill="black", font=("Arial", 12))
    frame.create_text(425, 330, text=f"Quantity: {bottle_two_quantity} bottles.", fill="black", font=("Arial", 12))


def bottle_three():
    global bottle_three_image, bottle_three_price, bottle_three_quantity
    bottle_one_image_path = "images/IMG_0493.JPG"
    original_image = Image.open(bottle_one_image_path)
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

    frame.create_text(
        685,
        300,
        text=f"Price: {bottle_three_price}lv.",
        font=("Arial", 12)
    )

    frame.create_text(
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
        font=("Arial", 12)
    )

    description_button = Button(
        root,
        fg="white",
        bg="black",
        text="Bottle three description",
        width=20,
        height=3,
        font=("Arial", 12)
    )

    frame.create_window(685, 380, window=description_button)
    frame.create_window(685, 450, window=buy_one_button)


def continue_as_a_guests():
    delete_all()

    frame.create_text(
        500,
        50,
        text="Welcome to the guest shop!!",
        font=("Arial", 20)
    )

    display_image_one()
    display_image_two()
    display_image_three()


username_fill = Entry(root, bd=0)
password_fill = Entry(root, bd=0, show="*")

f_name_register_fill = Entry(root, bd=0)
l_name_register_fill = Entry(root, bd=0)
username_register_fill = Entry(root, bd=0)
password_register_fill = Entry(root, bd=0, show="*")
