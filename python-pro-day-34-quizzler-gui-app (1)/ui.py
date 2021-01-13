from tkinter import Tk, Label, Button, PhotoImage, Canvas
"""UI Interface, Theme and colors"""
THEME_COLOR = "#375362"
SCORE_FONT = ("Ariel", 20, "italic")
QUESTION_FONT = ("Ariel", 15, "italic")


class QuizInterface:
    """Interface class"""

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.minsize(height=250, width=300)

        # Label = Grid system
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR, font=SCORE_FONT)
        self.score_label.grid(row=0, column=1)

        # Question Label
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some question text",
            fill=THEME_COLOR,
            font=QUESTION_FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # PhotoImages
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        # Buttons True or False
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
