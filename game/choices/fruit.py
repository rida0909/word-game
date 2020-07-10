from tkinter import *
from random import *
from tkinter import messagebox
import time

FRUITS_WORDS = ['EALPP', 'VAAGU', 'PEHCA', 'PRAE', 'NGMAO', 'PAAPYA', 'EGNRAO', 'AGESPR', 'WIKI', 'RRYCHE', 'LRTOANWEME',
               'PEELIPNPA', 'BELUEBRRY', 'NABAAN', 'NTUOCCO', 'SCURATD EALPP', 'MONLE', 'EREYBMUL', 'MARTAIND']

FRUITS_ANSWER = ['APPLE', 'GUAVA', 'PEACH', 'PEAR', 'MANGO', 'PAPAYA', 'ORANGE', 'GRAPES', 'KIWI', 'CHERRY',
                 'WATERMELON', 'PINEAPPLE', 'BLUEBERRY', 'BANANA', 'COCONUT', 'CUSTARD APPLE', 'LEMON', 'MULBERRY',
                 'TAMARIND']

word_num = randrange(0, (len(FRUITS_WORDS)))
jumbled_rand_word = FRUITS_WORDS[word_num]

points = 0

def main():

    def back():
        my_window.destroy()
        import main_screen
        main_screen.start_main_page()

    def change():
        global word_num
        word_num = randrange(0,(len(FRUITS_WORDS)))
        word.configure(text = FRUITS_WORDS[word_num])
        enter_input.delete(0,END)
        ans_lab.configure(text="")

    def check():
        global points, word_num
        answer = enter_input.get().upper()
        if answer == FRUITS_ANSWER[word_num]:
            points +=5
            score.configure(text = "score = " +str(points))
            messagebox.showinfo("correct", "wel done. Go to next?")
            word_num = randrange(0,(len(FRUITS_WORDS)))
            word.configure(text = FRUITS_WORDS[word_num])
            enter_input.delete(0,END)
            ans_lab.configure(text = "")
        else:
            messagebox.showerror("incorrect", "try again")
            enter_input.delete(0,END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="score = " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text = FRUITS_ANSWER[word_num])
        else:
            ans_lab.configure(text = "answer not found")

    my_window =Tk()
    my_window.geometry("1200x800+150+10")
    my_window.title("JUMBED WORD : FIND THE ANSWER")
    my_window.configure(background ="#99ffff")
    my_window.resizable(0,0)
    my_window.iconbitmap(r'quizee_logo_.ico')
    img1 = PhotoImage(file="back.png")

    lab_img = Button(
        my_window,
        image = img1,
        bg = "#99ffff",
        justify = "center",
        border = 0,
        command = back,
    )
    lab_img.pack(anchor='nw', padx=20, pady=20)

    score = Label(
        text = "score = 0",
        pady = 20,
        fg = "#000000",
        bg = "#99ffff",
        font = "Titillium  14 bold",
    )
    score.pack(anchor = "n")

    word = Label(
        my_window,
        text = jumbled_rand_word,
        fg = "#000000",
        bg = "#99ffff",
        pady = 20,
        font = "Titillium  50 bold",
    )
    word.pack()

    enter_input = Entry(
        font = "none 26 bold",
        borderwidth = 12,
        justify = "center",
    )
    enter_input.pack()

    submit = Button(
        text = "SUBMIT",
        fg = "#000000",
        bg = "#58cced",
        width = 24,
        borderwidth = 10,
        font = ("" , 18),
        command = check,
    )
    submit.pack(pady = (50,50))

    change = Button(
        my_window,
        text = "CHANGE",
        fg = "#000000",
        bg = "#58cced",
        width = 24,
        borderwidth = 10,
        font = ("" , 18),
        command = change,
    )
    change.pack()

    ans = Button(
        text = "SHOW ANSWER",
        fg = "#000000",
        bg = "#58cced",
        width = 24,
        borderwidth = 10,
        font = ("" , 18),
        command = show_answer,
    )
    ans.pack(pady=(50,50))

    ans_lab = Label(
        text = "",
        bg = "#99ffff",
        font = "Courier 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()