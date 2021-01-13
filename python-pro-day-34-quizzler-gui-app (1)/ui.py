"""UI Interface, Theme and colors"""
from tkinter import Tk, Label, Button, PhotoImage, Canvas
from quiz_brain import QuizBrain

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
        """Get next question from quiz brain"""
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            next_question_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You have reached the end of the questions"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        """True button event handler"""
        is_correct = self.quiz_brain.check_answer("True")
        self.give_feedback(is_correct)

    def is_false(self):
        """False Button event handler"""
        is_correct = self.quiz_brain.check_answer("False")
        self.give_feedback(is_correct)

    def update_score(self):
        """Update score label"""
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")

    def give_feedback(self, is_correct: bool):
        """Give feedback, green if correct, red if false"""
        self.update_score()
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, func=self.get_next_question)
