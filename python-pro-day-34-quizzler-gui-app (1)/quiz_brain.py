"""Quiz Brain Module"""
import html


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
        # Unescape HTML Entities in questions using html library's unescape
        question_text = html.unescape(self.current_question.text)
        # user_answer = input(f"Q.{self.question_number}: {question_text} (True/False): ")
        # self.check_answer(user_answer)
        return f"Q.{self.question_number}: {question_text}"

    def check_answer(self, user_answer: bool):
        """Check if the answer is correct"""
        correct_answer = bool(self.current_question.answer)
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
