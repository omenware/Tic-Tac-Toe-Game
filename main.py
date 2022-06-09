from tkinter import *
import random
from tkinter import messagebox
import sys

operator_x = 'X'
operator_O = 'O'
list = []
random_button_list = []
user_button_list = []
win = 0
user_canvas_list = []
random_canvas_list = []
turn = 0

window = Tk()
window.title('Tic-Tac-Toe Game')
window.minsize(width= 500, height=500, )
window.configure(bg='black')
my_label = Label(text=f'player = X         computer= O')
my_label.grid(column =2, row=0)


def random_button(b2,c):
    list.remove(b2)
    if len(list) == 0 and c != True:
        window.update()
        messagebox.showinfo(title='Congratulations', message='🙁 GAME OVER')
        sys.exit()
    t = random.choice(list)
    random_button_list.append(t)
    list.remove(t)
    t.grid_forget()
    canvas = Canvas(width=180, height=160)
    canvas.create_text(90, 80, text=operator_O, font=('Arial', 150, 'bold'))
    random_canvas_list.append(canvas)
    if t == button1:
        canvas.grid(column=1, row=1)
    elif t == button2:
        canvas.grid(column=1, row=2)
    elif t == button3:
        canvas.grid(column=1, row=3)
    elif t == button4:
        canvas.grid(column=2, row=1)
    elif t == button5:
        canvas.grid(column=2, row=2)
    elif t == button6:
        canvas.grid(column=2, row=3)
    elif t == button7:
        canvas.grid(column=3, row=1)
    elif t == button8:
        canvas.grid(column=3, row=2)
    elif t == button9:
        canvas.grid(column=3, row=3)

    check = game_over(t, random_button_list)
    if check:
        window.update()
        messagebox.showinfo(title='Congratulations', message='Computer won')
        sys.exit()

    # if c:
    #     for i in random_canvas_list:
    #         i.grid_forget()

# def show(c):
#     if c:
#         messagebox.showinfo(title='Congratulations', message='You win')


def game_over(b, i):
    global win
    if b == button1:
        if button2 in i and button3 in i:
            win = win + 1
            return True

        elif button4 in i and button7 in i:
            win = win + 1
            return True

        elif button5 in i and button9 in i:
            win = win +1
            return True

    elif b == button2:
        if button1 in i and button3 in i :
            win = win +1
            return True
        elif button5 in i and button8 in i:
            win = win +1
            return True

    elif b == button3:
        if button2 in i and button1 in i :
            win = win +1
            return True
        elif button6 in i and button9 in i:
            win = win + 1
            return True
        elif button5 in i and button7 in i:
            win = win + 1
            return True

    elif b == button4:
        if button1 in i and button7 in i:
            win = win +1
            return True
        elif button5 in i and button6 in i:
            win = win +1
            return True

    elif b == button5:
        if button2 in i and button8 in i:
            win = win +1
            return True
        elif button4 in i and button6 in i:
            win = win +1
            return True
        elif button1 in i and button9 in i:
            win = win + 1
            return True
        elif button3 in i and button7 in i:
            win = win +1
            return True

    elif b == button6:
        if button3 in i and button9 in i:
            win = win +1
            return True
        elif button4 in i and button5 in i:
            win = win +1
            return True

    elif b == button7:
        if button4 in i and button1 in i:
            win = win +1
            return True
        elif button8 in i and button9 in i:
            win = win +1
            return True
        elif button3 in i and button5 in i:
            win = win +1
            return True

    elif b == button8:
        if button5 in i and button2 in i:
            win = win +1
            return True
        elif button7 in i and button9 in i:
            win = win +1
            return True

    elif b == button9:
        if button3 in i and button6 in i:
            win = win +1
            return True
        elif button7 in i and button8 in i:
            win = win +1
            return True
        elif button1 in i and button5 in i :
            win = win +1
            return True


# def reset():
#     for i in list:
#         i.grid_forget()
#     window.update()


def hide_button(b):
    global cont
    user_button_list.append(b)
    b.grid_forget()
    canvas = Canvas(width=180, height=160)
    canvas.create_text(90, 80, text=operator_x, font=('Arial',150,'bold'))
    user_canvas_list.append(canvas)
    if b == button1:
        canvas.grid(column=1, row=1)
    elif b == button2:
        canvas.grid(column=1, row=2)
    elif b == button3:
        canvas.grid(column=1, row=3)
    elif b == button4:
        canvas.grid(column=2, row=1)
    elif b == button5:
        canvas.grid(column=2, row=2)
    elif b == button6:
        canvas.grid(column=2, row=3)
    elif b == button7:
        canvas.grid(column=3, row=1)
    elif b == button8:
        canvas.grid(column=3, row=2)
    elif b == button9:
        canvas.grid(column=3, row=3)

    check = game_over(b, user_button_list)
    if check:
        window.update()
        messagebox.showinfo(title='Congratulations', message='Congratulations \n 😀 You Won')
        sys.exit()
    random_button(b,check)


button1 = Button(width=20, height=10, command =lambda: hide_button(button1))
button1.grid(column =1, row =1, padx=2, pady=2)
list.append(button1)

button2 = Button(width=20, height=10, command =lambda: hide_button(button2))
button2.grid(column =1, row =2)
list.append(button2)

button3 = Button(width=20, height=10, command =lambda: hide_button(button3))
button3.grid(column =1, row =3)
list.append(button3)

button4 = Button(width=20, height=10, command =lambda: hide_button(button4))
button4.grid(column =2, row =1)
list.append(button4)

button5 = Button(width=20, height=10, command =lambda: hide_button(button5))
button5.grid(column =2, row =2)
list.append(button5)

button6 = Button(width=20, height=10, command =lambda: hide_button(button6))
button6.grid(column =2, row =3)
list.append(button6)

button7 = Button(width=20, height=10, command =lambda: hide_button(button7))
button7.grid(column =3, row =1)
list.append(button7)

button8 = Button(width=20, height=10, command =lambda: hide_button(button8))
button8.grid(column =3, row =2)
list.append(button8)

button9 = Button(width=20, height=10,command =lambda: hide_button(button9))
button9.grid(column =3, row =3,padx= 2, pady=2)
list.append(button9)

window.mainloop()


