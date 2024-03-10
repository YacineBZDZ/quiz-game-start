
class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    def next_question(self):
                new_question = self.question_list[self.question_number]
                self.question_number += 1
                choice = input(f"Q.{self.question_number}: {new_question.text} (True/False) :")
                self.check_answer(choice, new_question.answer)
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower() :
                self.score += 1
                print(f"your right !! \n Your current score is: {self.score}/{self.question_number}\n")
        else:
            print(f'your worng !! \n Your current score is: {self.score}/{self.question_number}')
            print(f"The correct answer was: {correct_answer} \n ")
