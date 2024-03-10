from data import question_data
from question_model import Questions
from quiz_brain import QuizBrain

question_bank = []

for quest in question_data:
    new_question = Questions(quest["text"], quest["answer"])
    question_bank.append(new_question)
brain = QuizBrain(question_bank)
while brain.still_has_question():
    brain.next_question()
print(f"You've completed the quiz \n Your final score is {brain.score}/{brain.question_number}")