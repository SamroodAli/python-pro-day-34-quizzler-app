"""Quiz Brain Module"""


class QuizBrain:
    """Class QuizBrain"""
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Check if there are still questions in question_list"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Next question prompt"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        """Check if the answer is correct"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")