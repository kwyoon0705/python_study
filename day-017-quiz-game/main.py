from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question = Question(item["question"], item["correct_answer"], item["difficulty"])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_quiz()

print("You've completed the quiz.")
print(f"Your final score was {quiz_brain.score}/{len(question_bank)}")
