from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score_label = Label(text=f"Score = 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.right_answer)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.wrong_answer)
        self.false_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            question_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the limit of question.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def right_answer(self):
        answer = self.quiz_brain.check_answer("True")
        self.feedback(answer)
        if answer:
            self.score_label.config(text=f"Score = {self.quiz_brain.score}")

    def wrong_answer(self):
        answer = self.quiz_brain.check_answer("False")
        self.feedback(answer)
        if answer:
            self.score_label.config(text=f"Score = {self.quiz_brain.score}")

    def feedback(self, answer):
        if answer:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.next_question)

