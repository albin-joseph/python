from question import Question

class QuizzBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
    
    def get_next_question(self):
        question = self.question_list[self.question_number]
        input(f"Q{self.question_number}: {question.text}(True/False) ")
    
    def still_has_question(self):
        total_of_questions = len(self.question_list)
        if((total_of_questions-1) > self.question_number):
            self.question_number += 1
            return True
        else:
            return False