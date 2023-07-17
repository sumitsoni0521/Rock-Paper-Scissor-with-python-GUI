from tkinter import *
from PIL import Image, ImageTk
from random import randint

window = Tk()
window.title("Rock Paper Scissor")
window.geometry("1385x485")
window.resizable(False, False)
window.configure(background="white")

image_rock1 = ImageTk.PhotoImage(Image.open("rock1.png"))
image_paper1 = ImageTk.PhotoImage(Image.open("paper1.png"))
image_scissor1 = ImageTk.PhotoImage(Image.open("scissor1.png"))
image_rock2 = ImageTk.PhotoImage(Image.open("rock2.png"))
image_paper2 = ImageTk.PhotoImage(Image.open("paper2.png"))
image_scissor2 = ImageTk.PhotoImage(Image.open("scissor2.png"))


label_player = Label(window, image=image_scissor1)
label_computer = Label(window, image=image_scissor2)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

computer_score = Label(window, text=0, font=("arial", 60, "bold"), bg="white", fg="red")
player_score = Label(window, text=0, font=("arial", 60, "bold"),bg="white", fg="red")
computer_score.grid(row=1, column=1)
player_score.grid(row=1, column=3)

player_indicator = Label(window, font=(
    "arial", 40, "bold"), text="PLAYER", bg="white", fg="blue")
computer_indicator = Label(window, font=(
    "arial", 40, "bold"), text="COMPUTER", bg="white", fg="blue")
player_indicator.grid(row=0, column=3)
computer_indicator.grid(row=0, column=1)


final_message = Label(window, font=("arial", 40, "bold"), bg="red", fg="white")
final_message.grid(row=3, column=2)


def msg_updation(a):
    final_message['text'] = a


def computer_update():
    fianl = int(computer_score['text'])
    fianl += 1
    computer_score['text'] = str(fianl)


def player_update():
    finall = int(player_score['text'])
    finall += 1
    player_score['text'] = str(finall)


def winner_check(p, c):
    if p == c:
        msg_updation("It's a tie")
    elif p == "rock":
        if c == "paper":
            msg_updation("Computer Wins")
            computer_update()
        else:
            msg_updation("Player Wins!! ")
            player_update()
    elif p == "paper":
        if c == "scissor":
            msg_updation("Computer Wins !!")
            computer_update()
        else:
            msg_updation("Player wins!")
            player_update()
    elif p == "scissor":
        if c == "rock":
            msg_updation("Computer Wins !!")
            computer_update()
        else:
            msg_updation("Player wins! ")
            player_update()
    else:
        pass


to_select = ["rock", "paper", "scissor"]


def update_choice(a):
    choice_computer = to_select[randint(0, 2)]
    if choice_computer == "rock":
        label_computer.configure(image=image_rock2)
    elif choice_computer == "paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissor2)
    if a == "rock":
        label_player.configure(image=image_rock1)
    elif a == "paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)
    winner_check(a, choice_computer)


button_rock = Button(window, width=12, height=2, text="Rock",
                     font=("arial", 22, "bold"), bg="#FF83C1", fg="red", command=lambda: update_choice("rock")).grid(row=2, column=1)
button_paper = Button(window, width=12, height=2, text="Paper",
                      font=("arial", 22, "bold"), bg="#FF83C1", fg="red", command=lambda: update_choice("paper")).grid(row=2, column=2)
button_Scissor = Button(window, width=12, height=2, text="Scissor",
                        font=("arial", 22, "bold"), bg="#FF83C1", fg="red", command=lambda: update_choice("scissor")).grid(row=2, column=3)

window.mainloop()