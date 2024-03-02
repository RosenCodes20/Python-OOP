from tkinter import Tk, Canvas


def create_root():
    root = Tk()

    root.title("Shop page")

    root.geometry("1200x600")

    root.resizable(False, False)

    root.configure(bg="cyan")

    return root


def create_frame():
    frame = Canvas(root, width=900, height=800, bg="cyan", highlightthickness=0)
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()