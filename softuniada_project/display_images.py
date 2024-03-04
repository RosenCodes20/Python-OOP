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
        font=("Arial", 12),
        command=bottle_one_description
    )

    frame.create_window(180, 360, window=description_of_the_bottle)


def bottle_one_description():
    from authentication import delete_all
    global bottle_one_image, bottle_price, bottle_quantity
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
        font=("Arial", 12),
        command=bottle_two_descriptions
    )

    frame.create_window(425, 360, window=bottle_two_description)
    frame.create_text(425, 300, text=f"Price: {bottle_two_price}lv.", fill="black", font=("Arial", 12))


def bottle_two_descriptions():
    from authentication import delete_all
    global bottle_two_image, bottle_two_price, bottle_two_quantity
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
        font=("Arial", 12),
        command=bottle_three_description
    )

    frame.create_window(685, 360, window=description_button)


def bottle_three_description():
    from authentication import delete_all
    global bottle_three_image, bottle_three_price, bottle_three_quantity
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


def display_image_four():
    global bottle_four_image, bottle_four_price, bottle_four_quantity
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

    frame.create_text(
        940,
        300,
        text=f"Price: {bottle_four_price}lv.",
        fill="black",
        font=("Arial", 12)
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

    frame.create_window(940, 360, window=description_four_button)


def bottle_four_description():
    from authentication import delete_all
    global bottle_four_image, bottle_four_price, bottle_four_quantity
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
    from authentication import continue_as_a_guests
    continue_as_a_guests()