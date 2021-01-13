from tkinter import Tk, Label, Button
"""UI Interface, Theme and colors"""
THEME_COLOR = "#375362"


class QuizInterface:
    """Interface class"""

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)

        # Label = Grid system
        score_label = Label(text=f"Score: 0", padx=20, pady=20)
        score_label.grid(row=0, column=1)

        # Question Label
        question_label = Label(text="Question text here", padx=20, pady=20)
        question_label.grid(row=1, column=0, columnspan=2)

        # Buttons True or False
        true_button = Button(text="Click Me")
        true_button.grid(row=2, column=0)

        false_button = Button(text="Click Me")
        false_button.grid(row=2, column=1)


        self.window.mainloop()
