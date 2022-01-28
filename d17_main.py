from d17_data import question_data
from d17_quiz_brain import QuizBrain
from d17_question_model import Question

'''
some scratch work i did trying to get this before it was fully explained. 
questions = []
i = 0
while i < 3:
    x = choice(question_data)
    print(x)
    question = x["text"]
    answer = x["answer"]
    questions.append(Question(question, answer))
    i += 1
'''

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)

# for object in question_bank:
#     print(object.text)
#     print(object.answer)

quiz = QuizBrain(question_bank)

# my original solution
# Should have done more in the method...
# input(f"Q.{quiz_brain.question_number + 1} {quiz_brain.next_question(quiz_brain.question_number).text} (true/false).")


while quiz.still_has_questions():
    #answer = quiz.next_question()
    #score += quiz.check_answer(answer[0], answer[1])
    #score += quiz.next_question()
    quiz.next_question()

print(f"Your score is {quiz.score} out of {len(question_bank)}")

'''
I was able to complete most of this without assistance with the challenges but in many cases I relied too heavily on 
main.py instead of leveraging the classes. 
'''
