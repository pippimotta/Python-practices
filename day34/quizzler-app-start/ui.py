from tkinter import *
from quiz_brain import QuizBrain
from data import question_data

THEME_COLOR = "#375362"
TEXT_FONT = ('Arial', 20, 'italic')
SCORE_FONT = ('Arial', 18, 'normal')


class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.quiz_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='',
            fill=THEME_COLOR,
            font=TEXT_FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score_label = Label(text=f'Score:0', font=SCORE_FONT, fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):  # tap in to Method:next_question in quiz_brain；使用QuizBrain裡的方法 即在此處傳入一個該分類的object作為屬性
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f'Score:{self.quiz.score}')
            self.canvas.itemconfig(self.quiz_text, text=q_text)

        else:
            self.canvas.itemconfig(self.quiz_text, text=f'You have reached the end of the quiz.\nYou got {self.quiz.score}.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)#等1s運行xxxfunction
