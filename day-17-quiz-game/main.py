from question_model import Question
from data import question_data

question_bank =[]
for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

print(question_bank[0].text)
print(question_bank[0].answer)