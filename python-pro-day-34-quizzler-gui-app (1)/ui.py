from tkinter import Tk, Label, Button, PhotoImage, Canvas
from quiz_brain import QuizBrain
"""UI Interface, Theme and colors"""
THEME_COLOR = "#375362"
SCORE_FONT = ("Ariel", 20, "italic")
QUESTION_FONT = ("Ariel", 15, "italic")


class QuizInterface:
    """Interface class"""

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
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
            width=280,
            fill=THEME_COLOR,
            font=QUESTION_FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # PhotoImages
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        # Buttons True or False
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        next_question_text = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question_text, text=next_question_text)

    def is_true(self):
        correct = self.quiz_brain.check_answer(True)
        if correct:
            self.update_score()
        self.get_next_question()

    def is_false(self):
        correct = self.quiz_brain.check_answer(False)
        if correct:
            self.update_score()
        self.get_next_question()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")
