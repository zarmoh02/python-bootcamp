from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
GREEN_COLOR = "#008000"
RED_COLOR = "#FF0000"
FONT = ("Arial", 15, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            fill=THEME_COLOR,
            text="question",
            font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        check_button_img = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_button_img, highlightthickness=0, command=self.true_pressed)
        self.check_button.grid(row=2, column=0)
        cross_button_img = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_button_img, highlightthickness=0, command=self.false_pressed)
        self.cross_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text="Score: {self.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz.\nYour final score was:"
                                                            f"{self.quiz.score}/{self.quiz.question_number}")
            self.cross_button.config(state="disabled")
            self.check_button.config(state="disabled")



    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN_COLOR)
        else:
            self.canvas.config(bg=RED_COLOR)
        self.window.after(1000, self.get_next_question)

