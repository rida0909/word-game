from tkinter import *

def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1 :
           from choices import animal
           animal.main()
        elif args == 2:
            from choices import colour
            colour.main()
        elif args == 3:
           from choices import fruit
           fruit.main()
        elif args == 4:
            from choices import vehicle
            vehicle.main()
        elif args == 5:
            from choices import shape 
            shape.main()  

    def choice():

        lab_img1 = Button(
            main_window,
            image=img1,
            bg='#e6fff5',
            border=0,
            justify='center',
        )
        choice_1 = Button(
            main_window,
            text = "ANIMALS",
            width = 30,
            height = 2,
            borderwidth = 8,
            font = ("",20),
            fg = "#000000",
            bg = "#58cced",
            cursor = "hand2",
            command = lambda: start_game(1),
        )
        choice_2 = Button(
            main_window,
            text = "COLOURS",
            width = 30,
            height = 2,
            borderwidth = 8,
            font = ("",20),
            fg = "#000000",
            bg = "#58cced",
            cursor = "hand2",
            command = lambda: start_game(2),
        )
        choice_3 = Button(
            main_window,
            text = "FRUITS",
            width = 30,
            height = 2,
            borderwidth = 8,
            font = ("",20),
            fg = "#000000",
            bg = "#58cced",
            cursor = "hand2",
            command = lambda: start_game(3),
        )
        choice_4 = Button(
            main_window,
            text = "VEHICALS",
            width = 30,
            height = 2,
            borderwidth = 8,
            font = ("",20),
            fg = "#000000",
            bg = "#58cced",
            cursor = "hand2",
            command = lambda: start_game(4),
        )
        choice_5 = Button(
            main_window,
            text = "SHAPES",
            width = 30,
            height = 2,
            borderwidth = 8,
            font = ("",20),
            fg = "#000000",
            bg = "#58cced",
            cursor = "hand2",
            command = lambda: start_game(5),
        )

        lab_img1.grid(row=0, column=0, padx=20)
        choice_1.grid(row=0, column =0, padx=350, pady =(50,0))
        choice_2.grid(row=1, column =0, padx=350, pady =(50,0))
        choice_3.grid(row=2, column =0, padx=350, pady =(50,0))
        choice_4.grid(row=3, column =0, padx=350, pady =(50,0))
        choice_5.grid(row=4, column =0, padx=350, pady =(50,0))

    def enter_choice():
        start_btn.destroy()
        lab_img.destroy()
        choice()

    main_window = Tk() 
    main_window.geometry("1200x800+150+10")
    main_window.resizable(0,0)
    main_window.title("JUMBLED WORDS : FIND THE ANSWER")
    main_window.configure(background ="#99ffff")
    main_window.iconbitmap(r'quizee_logo_.ico')

    img0 = PhotoImage(file=r"quizee_logo.png")
    img1 = PhotoImage(file="back.png")

    lab_img = Label(
        main_window,
        image=img0,
        bg="#99ffff",
    )
    lab_img.pack(pady=(200, 0))

    start_btn = Button(
        main_window,
        text = "START",
        width = 20,
        height = 1,
        borderwidth = 8,
        fg = "#000000",
        bg="#58cced",
        font = ("",17),
        cursor = "hand2",
        command = enter_choice,
    )
    start_btn.pack(pady=(100,20))

    main_window.mainloop()

start_main_page()