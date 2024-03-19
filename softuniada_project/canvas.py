from tkinter import Tk, Canvas


def create_root():
    root = Tk()

    root.title("Shop page")

    root.geometry("1400x600")

    root.resizable(False, False)

    root.configure(bg="cyan")

    return root


def create_frame():
    frame = Canvas(root, width=1400, height=600, bg="cyan", highlightthickness=0)
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()