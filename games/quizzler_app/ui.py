from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizlet")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        # Score
        self.score_label = Label(text="Score: 0", font=(FONT, 15), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Questions canvas
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question = self.canvas.create_text(150, 125, text="test", font=(FONT, 20, "italic"),
                                                fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_pic = PhotoImage(file="./data/true.png")
        self.true_button = Button(image=true_pic, command=self.true_response, border=0, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_pic = PhotoImage(file="./data/false.png")
        self.false_button = Button(image=false_pic, command=self.false_response, border=0, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def true_response(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_response(self):
        self.feedback(self.quiz.check_answer("False"))

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reach the end of the game")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
