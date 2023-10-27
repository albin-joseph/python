from question import Question
from data import question_data

quuestion_bank = []

for q_item in question_data:
    quuestion_bank.append(Question(q_item["text"], q_item["answer"]))
    
