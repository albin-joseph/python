from question import Question

class QuizzBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
    
    def get_next_question(self):
        question = self.question_list[self.question_number]
        user_answer = input(f"Q{self.question_number+1}: {question.text}(True/False) ")
        self.check_answer(user_answer, question.answer)
        self.question_number += 1
    
    def still_has_question(self):
        return (( len(self.question_list)) > self.question_number)
    
    def check_answer(self,user_answer, correct_answer):
        if(user_answer.lower() == correct_answer.lower()):
            self.score += 1