"""Main module"""
from question_model import Question
from data import QUESTIONS_DATA
from quiz_brain import QuizBrain
from ui import QuizInterface

QUESTION_BANK = []
for question in QUESTIONS_DATA:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    QUESTION_BANK.append(new_question)


QUIZ = QuizBrain(QUESTION_BANK)
QUIZ_UI = QuizInterface(QUIZ)

print("You've completed the quiz")
print(f"Your final score was: {QUIZ.score}/{QUIZ.question_number}")
