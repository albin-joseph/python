from question import Question
from data import question_data
from quizz_brain import QuizzBrain

question_bank = []

for q_item in question_data:
    question_bank.append(Question(q_item["text"], q_item["answer"]))
    
quizz_brain = QuizzBrain(question_bank)
quizz_brain.get_next_question()