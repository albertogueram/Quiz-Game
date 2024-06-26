import html


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        decrypted_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {decrypted_text}"
        # user_answer = input(f"Q.{self.question_number}: {decrypted_text} (True/False)?: ")
        # self.check_answer(user_answer, self.current_question.answer)

    def check_answer(self, user_answer):
        if user_answer == self.current_question.answer:
            self.score += 1
            return True
        else:
            return False

