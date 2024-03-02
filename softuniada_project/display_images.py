from tkinter import Button

from PIL import Image, ImageTk
from canvas import frame, root


def display_image_one():
    global bottle_one_image, bottle_price
    bottle_one_image_path = "images/IMG_0490.JPG"
    original_image = Image.open(bottle_one_image_path)
    bottle_price = 50
    new_size = (200, 200)

    resized_image = original_image.resize(new_size)

    resized_image = resized_image.rotate(270)

    bottle_one_image = ImageTk.PhotoImage(resized_image)

    frame.create_image(
        180,
        180,
        image=bottle_one_image
    )

    frame.create_text(
        180,
        300,
        text=f"Price: {bottle_price}lv.",
        fill="black",
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

    frame.create_window(180, 360, window=description_of_the_bottle)


def display_image_two():
    global bottle_two_image, bottle_two_price
    bottle_one_image_path = "images/IMG_0491.JPG"
    original_image = Image.open(bottle_one_image_path)
    bottle_two_price = 70

    new_size = (200, 200)

    resized_image = original_image.resize(new_size)

    resized_image = resized_image.rotate(270)

    bottle_two_image = ImageTk.PhotoImage(resized_image)

    frame.create_image(
        435,
        180,
        image=bottle_two_image
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

    frame.create_window(425, 360, window=bottle_two_description)
    frame.create_text(425, 300, text=f"Price: {bottle_two_price}lv.", fill="black", font=("Arial", 12))


def display_image_three():
    global bottle_three_image, bottle_three_price
    bottle_one_image_path = "images/IMG_0493.JPG"
    original_image = Image.open(bottle_one_image_path)
    bottle_three_price = 90

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

    description_button = Button(
        root,
        fg="white",
        bg="black",
        text="Bottle three description",
        width=20,
        height=3,
        font=("Arial", 12)
    )

    frame.create_window(685, 360, window=description_button)