from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(width=350, height=500)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score} ", font=("Arial", 10, "bold"),
                                 bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text="PRUEBA", width=280,
                                                font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_image = PhotoImage(file="images/true.png")
        self.right_btn = Button(image=right_image, command=self.right_choice,
                                bg=THEME_COLOR, highlightthickness=0)
        self.right_btn.grid(column=1, row=2)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong_image, command=self.wrong_choice,
                                bg=THEME_COLOR, highlightthickness=0)
        self.wrong_btn.grid(column=0, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="END OF GAME!")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def right_choice(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_choice(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)




