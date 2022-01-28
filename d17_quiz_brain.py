


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # TODO: Check if we are at the end of the quiz
    def still_has_questions(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False
        return self.question_number < len(self.question_list)

    # TODO: Check if the answer is correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("correct")
            self.score += 1
        else:
            print(f"incorrect, the right answer was {correct_answer}")


    # TODO: Asking the question
    def next_question(self):
        # my original solution
        # return self.question_list[self.question_number]
        current_question = self.question_list[self.question_number]
        #question_answer = current_question.answer
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        return self.check_answer(answer, current_question.answer)
        #return answer, question_answer


