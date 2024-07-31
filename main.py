from question_model import Questiion
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    answer_text = question["answer"]
    new_question = Questiion(q_text= question_text, q_answer= answer_text)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Congratulation!!! You have completed the quiz.... ")
print(f"Your final score is {quiz.score}/{len(question_bank)}")
