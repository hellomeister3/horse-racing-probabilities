# Horse racing - Probabilities
from tkinter import *
from PIL import ImageTk, Image
from random import randint
import time

horses = [['horse_1', 0, 50, 0],['horse_2', 0, 50, 60],['horse_3', 0, 50, 120],['horse_4', 0,50,180],['horse_5', 0,50,240],['horse_6', 0,50,300],['horse_7', 0,50,360],['horse_8', 0,50,420],['horse_9', 0,50,480],['horse_10', 0,50,540],['horse_11', 0,50,600],['horse_12', 0,50,660]]
winner = ''
dice_1 = 0
dice_2 = 0
which_horse = ''

window = Tk()
window.title('Horse Racing')

# frame for widgets
main_frame = Frame(height = 900, width = 1050, bg = 'green')
main_frame.pack()

load_finish = Image.open('finish.png')
render_finish = ImageTk.PhotoImage(load_finish)
img_finish = Label(image = render_finish)
img_finish.image = render_finish
img_finish.place(x=950,y=0)

for k in range(len(horses)):
    load_horse= Image.open('horse_' + str(k+1) + '.png')
    render_horse= ImageTk.PhotoImage(load_horse)
    img_horse = Label(image= render_horse)
    img_horse.image = render_horse
    img_horse.place(x=horses[k][2],y=horses[k][3])
    number = Label(text = str(k+1), font=('TkTextFont', 20))
    number.place(x=horses[k][2]-50, y=horses[k][3])




def remove_horses():
    global horses, img_horse
    for l in range(len(horses)):
        green_box = Label(height = 4, width = 7, bg = 'green')
        green_box.place(x=horses[l][2],y=horses[l][3])

def place_horses():
    global horses, img_horse
    for k in range(len(horses)):
        load_horse= Image.open('horse_' + str(k+1) + '.png')
        render_horse= ImageTk.PhotoImage(load_horse)
        img_horse = Label(image= render_horse)
        img_horse.image = render_horse
        img_horse.place(x=horses[k][2],y=horses[k][3])


def roll_dice():
    global dice_1, dice_2, which_horse, dice_button

    dice_1 = randint(1,6); dice_2 = randint(1,6)
    remove_horses()
    which_horse = (dice_1 + dice_2)-1; horses[which_horse][1] += 1
    horses[which_horse][2] += 100

    load_1= Image.open('side_' + str(dice_1) + '.png')
    render_1= ImageTk.PhotoImage(load_1)
    img_1 = Label(image= render_1)
    img_1.image = render_1
    img_1.place(x=460,y=800)

    load_2= Image.open('side_' + str(dice_2) + '.png')
    render_2= ImageTk.PhotoImage(load_2)
    img_2 = Label(image= render_2)
    img_2.image = render_2
    img_2.place(x=560,y=800)

    place_horses()

    
    for i in range(len(horses)):
            if horses[i][1] == 9:
                winner = 'Horse ' + str(i+1)
                win_label = Label(master = main_frame, text = winner + ' wins!', font=('TkTextFont', 35),  height = 1, width = 12 ,bg = 'blue', fg = 'white')
                win_label.place(x=600,y=0)
                button_over_label = Label(master = main_frame, height=3, width=11, bg= 'green')
                button_over_label.place(x=370,y=850)

dice_button = Button(master = main_frame, text = 'roll dice', height = '2', width = '10', bg = 'blue', fg = 'white', command= roll_dice)
dice_button.place(x=370,y=850)
    
window.mainloop()
