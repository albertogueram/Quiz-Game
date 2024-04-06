from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(width=350,height=500)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text ="Score: ", font=("Arial", 10, "bold"),
                                 bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text="PRUEBA",
                                                font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)


        right_image = PhotoImage(file="images/true.png")
        self.right_btn = Button(image=right_image, bg=THEME_COLOR, highlightthickness=0)
        self.right_btn.grid(column=1, row=2)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong_image, bg=THEME_COLOR, highlightthickness=0)
        self.wrong_btn.grid(column=0, row=2)

        self.window.mainloop()
