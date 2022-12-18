from tkinter import *
from PIL import Image, ImageTk
from ludo_game import Ludo
class Player():
    def __init__(self,make_canvas,ludogame):
        self.make_canvas = make_canvas
        self.ludogame = ludogame
        self.dice_six = ImageTk.PhotoImage(Image.open("Images/6_block.png").resize((35, 35), Image.ANTIALIAS))
        self.dice_five = ImageTk.PhotoImage(Image.open("Images/5_block.png").resize((35, 35), Image.ANTIALIAS))
        self.dice_four = ImageTk.PhotoImage(Image.open("Images/4_block.png").resize((35, 35), Image.ANTIALIAS))
        self.dice_three = ImageTk.PhotoImage(Image.open("Images/3_block.png").resize((35, 35), Image.ANTIALIAS))
        self.dice_two = ImageTk.PhotoImage(Image.open("Images/2_block.png").resize((35, 35), Image.ANTIALIAS))
        self.dice_one = ImageTk.PhotoImage(Image.open("Images/1_block.png").resize((35, 35), Image.ANTIALIAS))
        self.dice_sides = [self.dice_one,self.dice_two,self.dice_three,self.dice_four,self.dice_five,self.dice_six]

    def dice_roll_move(self,color,x0,y0,x1,y1):
        dice_coin_manager = []
        dice_image = Label(self.make_canvas,image=self.dice_sides[0])
        dice_image.place(x=x0, y=y0)
        roll = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Roll",
                             font=("Arial", 8, "bold"), command=lambda: self.ludogame.coin_prediction(color))
        roll.place(x=x1, y=y1)
        if color == "red":
            button_1 = self.coin_buttons(color,1,20,115)
            button_2 = self.coin_buttons(color, 2, 60, 115)
            button_3 = self.coin_buttons(color, 3, 20, 140)
            button_4 = self.coin_buttons(color, 4, 60, 140)
        elif color == "blue":
            button_1 = self.coin_buttons(color, 1, 20, 485)
            button_2 = self.coin_buttons(color, 2, 60, 485)
            button_3 = self.coin_buttons(color, 3, 20, 525)
            button_4 = self.coin_buttons(color, 4, 60, 525)
        elif color == "green":
            button_1 = self.coin_buttons(color, 1, 717, 115)
            button_2 = self.coin_buttons(color, 2, 757, 115)
            button_3 = self.coin_buttons(color, 3, 717, 155)
            button_4 = self.coin_buttons(color, 4, 757, 155)
        elif color == "yellow":
            button_1 = self.coin_buttons(color, 1, 717, 485)
            button_2 = self.coin_buttons(color, 2, 757, 485)
            button_3 = self.coin_buttons(color, 3, 717, 525)
            button_4 = self.coin_buttons(color, 4, 757, 525)
        else:
            pass
        coin_manager = [button_1,button_2,button_3,button_4]
        print("coin_manager:",coin_manager)
        dice_coin_manager.append(dice_image)
        dice_coin_manager.append(roll)
        dice_coin_manager.append(coin_manager)
        print("final_list:",dice_coin_manager)
        return dice_coin_manager

    def coin_buttons(self,color,number,x,y):
        button = Button(self.make_canvas, bg="#262626", fg="#00eb00", text=str(number), font=("Arial", 13, "bold", "italic"),
                       relief=RAISED, bd=3, command=lambda: self.ludogame.main_controller(color, str(number)), state=DISABLED,
                       disabledforeground=color)
        button.place(x=x, y=y)
        print("each_button:",button)
        return button

