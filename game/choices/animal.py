from tkinter import *
from random import *
from tkinter import messagebox
import time

ANIMALS_WORD = ['DRBI', 'DGO', 'OENDYK', 'GFRIEFA', 'GLOILARTA', 'TAC', 'EHSOR', 'OLIN', 'MYOEKN', 'EEB', 'KDUC',
                'RGFO', 'TPNLEHEA', 'ORCDCIELO', 'POLNIHD', 'LARLIGO', 'EMSUO', 'EGTRI', 'ABRITB', 'ATR', ]

ANIMALS_ANSWER = ['BIRD', 'DOG', 'DONKEY', 'GIRAFFE', 'ALLIGATOR', 'CAT', 'HORSE', 'LION', 'MONKEY', 'BEE', 'DUCK',
                  'FROG', 'ELEPHANT', 'CROCODILE', 'DOLPHIN', 'GORILLA', 'MOUSE', 'TIGER', 'RABBIT', 'RAT', ]

word_len = randrange(0,(len(ANIMALS_WORD)))
jumbled_random_words = ANIMALS_WORD[word_len]

points = 0

def main():
    def back():
        my_window.destroy()
        import main_screen
        main_screen.start_main_page()

    def change():
        global word_len
        word_len = randrange(0,(len(ANIMALS_WORD)))
        word.configure(text = ANIMALS_WORD[word_len])
        enter_input.delete(0,END)
        ans_lab.configure(text="")

    def check():
        global points, word_len
        answer = enter_input.get().upper()
        if answer == ANIMALS_ANSWER[word_len]:
            points += 5
            score.configure(text = "score = " +str(points))
            messagebox.showinfo("correct","well done. Go to next?")
            word_len = randrange(0,(len(ANIMALS_WORD)))
            word.configure(text = ANIMALS_WORD[word_len])
            enter_input.delete(0,END)
            ans_lab.configure(text = "")

        else:
            messagebox.showerror("incorrect","try again")
            enter_input.delete(0,END)
    
    def show_answer():
        global points 
        if points > 4:
            points -= 5
            score.configure(text ="score = "+str(points))
            time.sleep(0.5)
            ans_lab.configure(text = ANIMALS_ANSWER[word_len])
        else:
            ans_lab.configure(text = "answer not found")
    
    my_window = Tk()
    my_window.geometry("1200x800+150+10")
    my_window.resizable(0,0)
    my_window.title("JUMBLED WORDS : FIND THE ANSWER")
    my_window.configure(background ="#99ffff")
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
    lab_img.pack(anchor="nw", padx=20, pady =20)

    score =Label(
        text = "score = 0",
        pady = 20,
        fg = "#000000",
        bg = "#99ffff",
        font = "Titillium  14 bold",
    )
    score.pack(anchor = "n")

    word = Label(
        text = jumbled_random_words,
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
        width = 24,
        borderwidth = 10,
        font = ("",18),
        fg = "#000000",
        bg = "#58cced",
        command = check,
    )
    submit.pack(pady=(50,50))

    change = Button(
        my_window,
        text = "CHANGE",
        width = 24,
        borderwidth = 10,
        font = ("",18),
        bg = "#58cced",
        fg = "#000000",
        command = change,
    )
    change.pack()

    ans = Button(
        text = "SHOW ANSWER",
        width = 24,
        borderwidth = 10,
        font = ("",18),
        bg = "#58cced",
        fg = "#000000",
        command = show_answer,
    )
    ans.pack(pady=(50,30))

    ans_lab = Label(
        text ="",
        bg = "#99ffff",
        font = "Courier 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()