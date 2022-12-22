from tkinter import messagebox
import time
import pygame
from random import randint, choice
from board import Board
from tkinter import *


class Ludo:
    def __init__(self, root):

        from player import Player
        self.window = root

        self.make_canvas = Canvas(self.window, bg="#E9C67F", width=800, height=630)
        self.make_canvas.pack(fill=BOTH, expand=1)  # Tkinter canvas used to create rectangular Ludo Board

        # storing all the values of all colors , label, Roll button, 1,2,3,4 buttons
        self.roll_predict_coins = []
        # storing number of playing when play with friends is selected
        self.total_people_play = []

        self.red_coin_position = [1, 2, 3, 4]
        self.green_coin_position = [1, 2, 3, 4]
        self.yellow_coin_position = [1, 2, 3, 4]
        self.blue_coin_position = [1, 2, 3, 4]

        coin_index = 0
        # initializing all coins positions to -1
        while coin_index < len(self.red_coin_position):
            self.red_coin_position[coin_index] = -1
            self.green_coin_position[coin_index] = -1
            self.yellow_coin_position[coin_index] = -1
            self.blue_coin_position[coin_index] = -1
            coin_index+= 1

        # bot_coins specific positions of coins of all colors
        self.red_coord_list = [-1, -1, -1, -1]
        self.green_coord_list = [-1, -1, -1, -1]
        self.yellow_coord_list = [-1, -1, -1, -1]
        self.blue_coord_list = [-1, -1, -1, -1]
        # For respective coins to traverse
        self.red_coin_tracker = 0
        self.green_coin_tracker = 0
        self.yellow_coin_tracker = 0
        self.blue_coin_tracker = 0

        self.destination_coin_tracker = 0
        self.turn_after_six = 0

        # initializing the active coins for each color to zero
        self.red_bot_coins_active = 0
        self.blue_bot_coins_active = 0
        self.yellow_bot_coins_active = 0
        self.green_bot_coins_active = 0

        self.six_tracker = 0
        self.time_for = -1
        self.six_list = []

        self.check_if_bot = 0
        # variable which indicates robo's turn to play
        self.count_robo_stage_from_start = 0
        self.robo_bot_coins = []
        self.first_winner = []

        # safe positions at each side
        self.right_star = None
        self.down_star = None
        self.left_star = None
        self.up_star = None

        b = Board(self.make_canvas)
        b.board_set_up()
        print("board_Setup")

        # red color coins
        b.coins(140, 55, 180, 95, 3, "red")
        b.coins(260, 55, 300, 95, 3, "red")
        b.coins(260, 155, 300, 195, 3, "red")
        b.coins(140, 155, 180, 195, 3, "red")

        # blue color coins
        b.coins(140, 435, 180, 475, 3, "#04d9ff")
        b.coins(260, 435, 300, 475, 3, "#04d9ff")
        b.coins(260, 535, 300, 575, 3, "#04d9ff")
        b.coins(140, 535, 180, 575, 3, "#04d9ff")

        # green color coins
        b.coins(500, 55, 540, 95, 3, "#00FF00")
        b.coins(620, 55, 660, 95, 3, "#00FF00")
        b.coins(620, 155, 660, 195, 3, "#00FF00")
        b.coins(500, 155, 540, 195, 3, "#00FF00")

        # yellow color coins
        b.coins(500, 435, 540, 475, 3, "yellow")
        b.coins(620, 435, 660, 475, 3, "yellow")
        b.coins(620, 535, 660, 575, 3, "yellow")
        b.coins(500, 535, 540, 575, 3, "yellow")

        # Labelling Number on each coin
        # red coins labelling
        b.label_coin(1, "red", 150, 60)
        b.label_coin(2, "red", 270, 60)
        b.label_coin(3, "red", 270, 160)
        b.label_coin(4, "red", 150, 160)

        # blue coins labelling
        b.label_coin(1, "#04d9ff", 150, 440)
        b.label_coin(2, "#04d9ff", 270, 440)
        b.label_coin(3, "#04d9ff", 270, 540)
        b.label_coin(4, "#04d9ff", 150, 540)

        # green coins labelling
        b.label_coin(1, "#00FF00", 510, 60)
        b.label_coin(2, "#00FF00", 630, 60)
        b.label_coin(3, "#00FF00", 630, 160)
        b.label_coin(4, "#00FF00", 510, 160)

        # yellow coins labelling
        b.label_coin(1, "yellow", 510, 440)
        b.label_coin(2, "yellow", 630, 440)
        b.label_coin(3, "yellow", 630, 540)
        b.label_coin(4, "yellow", 510, 540)

        self.graphical_red_coin = b.graphical_red_coin
        self.graphical_blue_coin = b.graphical_blue_coin
        self.graphical_green_coin = b.graphical_green_coin
        self.graphical_yellow_coin = b.graphical_yellow_coin
        self.label_red_coin = b.label_red_coin
        self.label_blue_coin = b.label_blue_coin
        self.label_green_coin = b.label_green_coin
        self.label_yellow_coin = b.label_yellow_coin

        b.safe_place()

        # creating roll and coin manager buttons
        roll_btn = Player(self.make_canvas, self)
        red_roll_btn = roll_btn.dice_roll_move("red", 34, 15, 25, 65)
        blue_roll_btn = roll_btn.dice_roll_move("blue", 34, 385, 25, 435)
        green_roll_btn = roll_btn.dice_roll_move("green", 730, 15, 722, 65)
        yellow_roll_btn = roll_btn.dice_roll_move("yellow", 730, 385, 722, 435)
        print("red_btn:", red_roll_btn)
        self.block_number_side = roll_btn.dice_sides

        self.roll_predict_coins = [red_roll_btn, blue_roll_btn, yellow_roll_btn, green_roll_btn]

        print("create_buttons:", self.roll_predict_coins)

        self.Initial_Window()

    def Initial_Window(self):

        '''
            In this method we will create intial window where users can choose one of two options available which are play with computer
            and play with friends

            output: Initial window with play with friends and play with computer button, Input box where users can enter
                    number of players and a start button

        '''
        print("hello:", self.roll_predict_coins[0][1])
        for i in range(4):
            print("new_print: ", self.roll_predict_coins[i][1]['state'])
            self.roll_predict_coins[i][1]['state'] = DISABLED
            print(self.roll_predict_coins)

        top = Toplevel()
        top.geometry("800x600")
        top.maxsize(800, 600)
        top.minsize(800, 600)
        top.config(bg="white")
        top.iconbitmap("Images/ludo_icon.ico")

        head = Label(top, text="-:Total number of players:- ", font=("Arial", 12, "bold", "italic"), bg="orange",
                     fg="chocolate")
        head.place(x=70, y=220)
        coin_index_entry = Entry(top, font=("Arial", 18, "bold", "italic"), relief=SUNKEN, bd=7, width=12)
        coin_index_entry.place(x=320, y=220)
        coin_index_entry.focus()

        def processing():  # Filtering total number of players

            def input_processing(coin_number):
                '''
                    Filtering values when number of players is entered in the input box

                    "Displays error message where entered values are not between 2 and 4"

                '''
                try:
                    return True if (4 >= int(coin_number) >= 2) or type(coin_number) == int else False
                except:
                    return False

            response = input_processing(coin_index_entry.get())
            if response:
                for player_index in range(int(coin_index_entry.get())):
                    self.total_people_play.append(player_index)
                print(self.total_people_play)
                self.player_bot_manager()
                top.destroy()
            else:
                messagebox.showerror("Input Error", "Please enter values between 2 and 4")
                top.destroy()
                self.Initial_Window()

        start_btn = Button(top, text="Start", bg="#262626", fg="#00FF00", font=("Arial", 13, "bold"), relief=RAISED,
                           bd=3, command=processing, state=DISABLED)
        start_btn.place(x=550, y=220)

        def select(value):
            if value:
                self.check_if_bot = 1
                for player_index in range(2):
                    self.total_people_play.append(player_index)
                print(self.total_people_play)

                def display_start_message(time_is):
                    if place_ins['text'] != "":
                        place_ins.place_forget()
                    if command_play['text'] != "":
                        command_play.place_forget()

                    place_ins['text'] = f"  Your game will start within {time_is} sec"
                    place_ins.place(x=100, y=300)

                    if time_is > 5:
                        command_play[
                            'text'] = f"             Computer will Play With Red coin and the Player will play With Sky Blue Coin"
                    elif time_is >= 2 and time_is < 5:
                        command_play[
                            'text'] = f"                           Player will get the first chance to play the game"
                    else:
                        command_play['text'] = f"                                       All the best!!! Enjoy the Game"
                    command_play.place(x=10, y=350)

                time_is = 10
                place_ins = Label(top, text="", font=("Arial", 20, "bold"), fg="#FF0000", bg="#FFFFFF")
                command_play = Label(top, text="", font=("Arial", 12, "bold"), fg="#af7439", bg="#FFFFFF")

                try:
                    while time_is:
                        display_start_message(time_is)
                        time_is -= 1
                        self.window.update()
                        time.sleep(1)
                    top.destroy()
                except:
                    print("Force Stop Error in Operate")
                self.roll_predict_coins[1][1]['state'] = NORMAL
            else:
                start_btn['state'] = NORMAL
                coin_index_entry['state'] = NORMAL

        mvc_btn = Button(top, text="Play With Computer", bg="#2B4AF7", fg="#FCFCFD",
                         font=("Times New Roman", 12, "bold"),
                         relief=RAISED, bd=3, command=lambda: select(1), activebackground="#2B4AF7")
        mvc_btn.place(x=400, y=150)

        mvh_btn = Button(top, text="Play With Friends", bg="#262626", fg="#00FF00",
                         font=("Times New Roman", 12, "bold"),
                         relief=RAISED, bd=3, command=lambda: select(0), activebackground="#262626")
        mvh_btn.place(x=220
                      , y=150)

        pygame.mixer.init()

        pygame.mixer.music.load('sound/sound.mp3')
        global is_on
        pygame.mixer.music.play(loops=0)
        is_on = True

        # my_label = Label(top,
        #                  text="Ludo The Game",
        #                  fg="#f8c294",
        #                  font=("Helvetica", 32))
        #
        # my_label.pack(pady=20)

        def switch():
            global is_on
            # Determine is on or off
            if is_on:
                on_button.config(image=off)
                pygame.mixer.music.stop()
                # my_label.config(text="The Switch is Off", fg="grey")
                is_on = False
            else:
                on_button.config(image=on)
                # my_label.config(text="The Switch is On", fg="green")
                pygame.mixer.music.play(loops=0)
                is_on = True

        on = PhotoImage(file="sound/son.png")
        off = PhotoImage(file="sound/soff.png")

        label1 = Label(top, text="Sound:", font=("Arial", 16, "bold"))
        label1.place(x=635, y=2.0)
        on_button = Button(top, image=on, bd=0, command=switch)
        on_button.place(x=720, y=20)

        top.mainloop()

    def coin_prediction(self, player_coin):
        print("color:", player_coin)
        '''
            In this method we get the values of dice when a player rolls the dice and bot_coins it.

        '''
        try:
            if player_coin == "red":
                roll_predict_coins = self.roll_predict_coins[0]
                print("red_block:", roll_predict_coins)
                if self.check_if_bot and self.count_robo_stage_from_start < 3:
                    self.count_robo_stage_from_start += 1
                if self.check_if_bot and self.count_robo_stage_from_start == 3 and self.six_tracker < 2:
                    dice_value = self.red_coin_tracker = 6
                    self.count_robo_stage_from_start += 1
                else:
                    dice_value = self.red_coin_tracker = randint(1, 6)

            elif player_coin == "blue":
                roll_predict_coins = self.roll_predict_coins[1]
                print("blue_block:", roll_predict_coins)
                dice_value = self.blue_coin_tracker = randint(1, 6)
                if self.check_if_bot and dice_value == 6:
                    for coin_loc in self.red_coin_position:
                        if coin_loc >= 40 and coin_loc <= 46:
                            dice_value = self.blue_coin_tracker = randint(1, 5)
                            break

            elif player_coin == "yellow":
                roll_predict_coins = self.roll_predict_coins[2]
                dice_value = self.yellow_coin_tracker = randint(1, 6)
            else:
                roll_predict_coins = self.roll_predict_coins[3]
                dice_value = self.green_coin_tracker = randint(1, 6)

            roll_predict_coins[1]['state'] = DISABLED

            # Illusion of coin floating
            crnt_val_counter = 12
            while crnt_val_counter > 0:
                move_crnt_val_counter = randint(1, 6)
                roll_predict_coins[0]['image'] = self.block_number_side[move_crnt_val_counter - 1]
                self.window.update()
                time.sleep(0.1)
                crnt_val_counter -= 1

            print("Prediction result: ", dice_value)

            # Permanent predicted value containing image set
            roll_predict_coins[0]['image'] = self.block_number_side[dice_value - 1]
            if self.check_if_bot == 1 and player_coin == "red":
                self.window.update()
                time.sleep(0.4)
            self.click_move_coin_on_current_position(player_coin, dice_value,
                                                     roll_predict_coins)
        except Exception as e:
            print("Force stop error:", e)

    def click_move_coin_on_current_position(self, player_coin, dice_value,
                                            roll_predict_coins):
        bot_parameter = None
        if player_coin == "red":
            crnt_val_coin_position = self.red_coin_position
        elif player_coin == "green":
            crnt_val_coin_position = self.green_coin_position
        elif player_coin == "yellow":
            crnt_val_coin_position = self.yellow_coin_position
        else:
            crnt_val_coin_position = self.blue_coin_position

        coins_inside = 1
        for i in range(4):
            if crnt_val_coin_position[i] == -1:
                coins_inside = 1
            else:
                coins_inside = 0
                break

        if dice_value == 6:
            self.six_tracker += 1
        else:
            self.six_tracker = 0

        if ((coins_inside == 1 and dice_value == 6)):
            self.six_list.append("first_move")

        if ((coins_inside == 1 and dice_value == 6) or (coins_inside == 0)) \
                and self.six_tracker < 3:
            allow = 1
            if player_coin == "red":
                crnt_val = self.red_coord_list
            elif player_coin == "green":
                crnt_val = self.green_coord_list
            elif player_coin == "yellow":
                crnt_val = self.yellow_coord_list
            else:
                crnt_val = self.blue_coord_list

            if dice_value < 6:
                if self.turn_after_six == 1:
                    self.time_for -= 1
                    self.turn_after_six = 0
                for i in range(4):
                    if crnt_val[i] == -1:
                        allow = 0
                    elif crnt_val[i] > 100:
                        if crnt_val[i] + dice_value <= 106:
                            allow = 1
                            break
                        else:
                            allow = 0
                    else:
                        allow = 1
                        break
            else:
                for i in range(4):
                    if crnt_val[i] > 100:
                        if crnt_val[i] + dice_value <= 106:
                            allow = 1
                            break
                        else:
                            allow = 0
                    else:
                        allow = 1
                        break
            if allow == 0:
                self.player_bot_manager(None)
            else:
                self.coin_buttons_manager(roll_predict_coins[2])

                if self.check_if_bot == 1 and roll_predict_coins == self.roll_predict_coins[0]:
                    bot_parameter = "give"
                roll_predict_coins[1]['state'] = DISABLED  # Predict btn deactivation

        else:
            roll_predict_coins[1]['state'] = NORMAL  # Predict btn activation
            if self.turn_after_six == 1:
                self.time_for -= 1
                self.turn_after_six = 0
            self.player_bot_manager()

        if dice_value == 6 and self.six_tracker < 3 and \
                roll_predict_coins[2][0]['state'] == NORMAL:
            self.time_for -= 1
        else:
            self.six_tracker = 0

        if self.check_if_bot == 1 and bot_parameter:
            self.bot_operations(bot_parameter)

    # Player Scope controller
    def player_bot_manager(self, bot_parameter=None):
        if self.time_for == -1:
            pass
        else:
            self.roll_predict_coins[self.total_people_play[self.time_for]][1]['state'] = DISABLED
        if self.time_for == len(self.total_people_play) - 1:
            self.time_for = -1

        self.time_for += 1
        self.roll_predict_coins[self.total_people_play[self.time_for]][1]['state'] = NORMAL

        if self.check_if_bot == 1 and self.time_for == 0:
            bot_parameter = "Roll"
        if bot_parameter:
            self.bot_operations(bot_parameter)

    def coin_buttons_manager(self, buttons_list, buttons_state=1):
        if buttons_state:
            for btn in buttons_list:
                btn['state'] = NORMAL
        else:
            for btn in buttons_list:
                btn['state'] = DISABLED

    def game_manager(self, color_coin, coin_number):
        bot_parameter = None

        if color_coin == "red":
            print("Red color")
            self.coin_buttons_manager(self.roll_predict_coins[0][2], 0)

            if self.red_coin_tracker == 106:
                messagebox.showwarning("Woohoo!Coin Reached Home. ")

            elif self.red_coin_position[int(coin_number) - 1] == -1 and self.red_coin_tracker == 6:
                self.initial_position_red(coin_number)
                self.red_coord_list[int(coin_number) - 1] = 1

            elif self.red_coin_position[int(coin_number) - 1] > -1:
                coin_index_coord = self.make_canvas.coords(self.graphical_red_coin[int(coin_number) - 1])
                red_start_label_x = coin_index_coord[0] + 10
                red_start_label_y = coin_index_coord[1] + 5
                self.label_red_coin[int(coin_number) - 1].place(x=red_start_label_x, y=red_start_label_y)

                if self.red_coin_position[int(coin_number) - 1] + self.red_coin_tracker <= 106:
                    self.red_coin_position[int(coin_number) - 1] = self.coin_traversal(
                        self.red_coin_position[int(coin_number) - 1], self.graphical_red_coin[int(coin_number) - 1],
                        self.label_red_coin[int(coin_number) - 1], red_start_label_x, red_start_label_y, "red",
                        self.red_coin_tracker)
                    if self.check_if_bot and self.red_coin_position[
                        int(coin_number) - 1] == 106 and color_coin == "red":
                        self.robo_bot_coins.remove(int(coin_number))
                        print("After removing: ", self.robo_bot_coins)

                else:
                    if not self.check_if_bot:
                        messagebox.showerror("Not possible", "Sorry, not permitted")
                    self.coin_buttons_manager(self.roll_predict_coins[0][2])

                    if self.check_if_bot:
                        bot_parameter = "give"
                        self.bot_operations(bot_parameter)
                    return
                if self.red_coin_position[int(coin_number) - 1] == 22 or self.red_coin_position[
                    int(coin_number) - 1] == 9 or self.red_coin_position[int(coin_number) - 1] == 48 or \
                        self.red_coin_position[int(coin_number) - 1] == 35 or self.red_coin_position[
                    int(coin_number) - 1] == 14 or self.red_coin_position[int(coin_number) - 1] == 27 or \
                        self.red_coin_position[int(coin_number) - 1] == 40 or self.red_coin_position[
                    int(coin_number) - 1] == 1:
                    pass

                else:
                    if self.red_coin_position[int(coin_number) - 1] < 100:
                        self.player_elimination(self.red_coin_position[int(coin_number) - 1], color_coin,
                                                self.red_coin_tracker)

                self.red_coord_list[int(coin_number) - 1] = self.red_coin_position[int(coin_number) - 1]
            else:
                messagebox.showerror("Incorrect Selection of Coin to Traverse ")
                self.coin_buttons_manager(self.roll_predict_coins[0][2])

                if self.check_if_bot == 1:
                    bot_parameter = "give"
                    self.bot_operations(bot_parameter)
                return
            self.roll_predict_coins[0][1]['state'] = NORMAL

        elif color_coin == "yellow":

            self.coin_buttons_manager(self.roll_predict_coins[2][2], 0)

            if self.yellow_coin_tracker == 106:
                messagebox.showwarning("Woohoo!Coin Reached Home. ")

            elif self.yellow_coin_position[int(coin_number) - 1] == -1 and self.yellow_coin_tracker == 6:
                self.initial_position_yellow(coin_number)
                self.yellow_coord_list[int(coin_number) - 1] = 27

            elif self.yellow_coin_position[int(coin_number) - 1] > -1:
                coin_index_coord = self.make_canvas.coords(self.graphical_yellow_coin[int(coin_number) - 1])
                yellow_start_label_x = coin_index_coord[0] + 10
                yellow_start_label_y = coin_index_coord[1] + 5
                self.label_yellow_coin[int(coin_number) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)

                if self.yellow_coin_position[int(coin_number) - 1] + self.yellow_coin_tracker <= 106:
                    self.yellow_coin_position[int(coin_number) - 1] = self.coin_traversal(
                        self.yellow_coin_position[int(coin_number) - 1],
                        self.graphical_yellow_coin[int(coin_number) - 1], self.label_yellow_coin[int(coin_number) - 1],
                        yellow_start_label_x, yellow_start_label_y, "yellow", self.yellow_coin_tracker)
                else:
                    messagebox.showerror("Coin Already Reached Home or Path not Permitted ")

                    self.coin_buttons_manager(self.roll_predict_coins[2][2])
                    return

                if self.yellow_coin_position[int(coin_number) - 1] == 22 or self.yellow_coin_position[
                    int(coin_number) - 1] == 9 or self.yellow_coin_position[int(coin_number) - 1] == 48 or \
                        self.yellow_coin_position[int(coin_number) - 1] == 35 or self.yellow_coin_position[
                    int(coin_number) - 1] == 1 or self.yellow_coin_position[int(coin_number) - 1] == 14 or \
                        self.yellow_coin_position[int(coin_number) - 1] == 40 or self.yellow_coin_position[
                    int(coin_number) - 1] == 27:
                    pass
                else:
                    if self.yellow_coin_position[int(coin_number) - 1] < 100:
                        self.player_elimination(self.yellow_coin_position[int(coin_number) - 1], color_coin,
                                                self.yellow_coin_tracker)

                self.yellow_coord_list[int(coin_number) - 1] = self.yellow_coin_position[int(coin_number) - 1]

            else:
                messagebox.showerror("Wrong choice", "Sorry, This coin in not permitted to travel now")
                self.coin_buttons_manager(self.roll_predict_coins[2][2])
                return

            self.roll_predict_coins[2][1]['state'] = NORMAL

        elif color_coin == "blue":
            self.coin_buttons_manager(self.roll_predict_coins[1][2], 0)

            if self.red_coin_tracker == 106:
                messagebox.showwarning("Woohoo!Coin Reached Home. ")

            elif self.blue_coin_position[int(coin_number) - 1] == -1 and self.blue_coin_tracker == 6:
                self.initial_position_blue(coin_number)
                self.blue_coord_list[int(coin_number) - 1] = 40

            elif self.blue_coin_position[int(coin_number) - 1] > -1:
                coin_index_coord = self.make_canvas.coords(self.graphical_blue_coin[int(coin_number) - 1])
                print("coin_index_coord:", coin_index_coord)
                blue_start_label_x = coin_index_coord[0] + 10
                blue_start_label_y = coin_index_coord[1] + 5
                self.label_blue_coin[int(coin_number) - 1].place(x=blue_start_label_x,
                                                                 y=blue_start_label_y)

                if self.blue_coin_position[int(coin_number) - 1] + self.blue_coin_tracker <= 106:
                    self.blue_coin_position[int(coin_number) - 1] = self.coin_traversal(
                        self.blue_coin_position[int(coin_number) - 1],
                        self.graphical_blue_coin[int(coin_number) - 1], self.label_blue_coin[int(coin_number) - 1],
                        blue_start_label_x, blue_start_label_y, "blue", self.blue_coin_tracker)
                else:
                    messagebox.showerror("Not possible", "No path available")
                    self.coin_buttons_manager(self.roll_predict_coins[1][2])
                    return

                if self.blue_coin_position[int(coin_number) - 1] == 22 or self.blue_coin_position[
                    int(coin_number) - 1] == 9 or self.blue_coin_position[int(coin_number) - 1] == 48 or \
                        self.blue_coin_position[int(coin_number) - 1] == 35 or self.blue_coin_position[
                    int(coin_number) - 1] == 1 or self.blue_coin_position[int(coin_number) - 1] == 14 or \
                        self.blue_coin_position[int(coin_number) - 1] == 27 or self.blue_coin_position[
                    int(coin_number) - 1] == 40:
                    pass
                else:
                    if self.blue_coin_position[int(coin_number) - 1] < 100:
                        self.player_elimination(self.blue_coin_position[int(coin_number) - 1], color_coin,
                                                self.blue_coin_tracker)

                self.blue_coord_list[int(coin_number) - 1] = self.blue_coin_position[int(coin_number) - 1]

            else:
                messagebox.showerror("Wrong choice", "Sorry, This coin in not permitted to travel now")
                self.coin_buttons_manager(self.roll_predict_coins[1][2])
                return

            self.roll_predict_coins[1][1]['state'] = NORMAL
        elif color_coin == "green":
            self.coin_buttons_manager(self.roll_predict_coins[3][2], 0)

            if self.green_coin_tracker == 106:
                messagebox.showwarning("Destination reached", "Reached at the destination")

            elif self.green_coin_position[int(coin_number) - 1] == -1 and self.green_coin_tracker == 6:
                self.initial_position_green(coin_number)
                self.green_coord_list[int(coin_number) - 1] = 14

            elif self.green_coin_position[int(coin_number) - 1] > -1:
                coin_index_coord = self.make_canvas.coords(self.graphical_green_coin[int(coin_number) - 1])
                green_start_label_x = coin_index_coord[0] + 10
                green_start_label_y = coin_index_coord[1] + 5
                self.label_green_coin[int(coin_number) - 1].place(x=green_start_label_x, y=green_start_label_y)

                if self.green_coin_position[int(coin_number) - 1] + self.green_coin_tracker <= 106:
                    self.green_coin_position[int(coin_number) - 1] = self.coin_traversal(
                        self.green_coin_position[int(coin_number) - 1], self.graphical_green_coin[int(coin_number) - 1],
                        self.label_green_coin[int(coin_number) - 1], green_start_label_x, green_start_label_y,
                        "green", self.green_coin_tracker)
                else:
                    messagebox.showerror("Not possible", "No path available")
                    self.coin_buttons_manager(self.roll_predict_coins[3][2])
                    return

                if self.green_coin_position[int(coin_number) - 1] == 22 or self.green_coin_position[
                    int(coin_number) - 1] == 9 or self.green_coin_position[int(coin_number) - 1] == 48 or \
                        self.green_coin_position[int(coin_number) - 1] == 35 or self.green_coin_position[
                    int(coin_number) - 1] == 1 or self.green_coin_position[int(coin_number) - 1] == 27 or \
                        self.green_coin_position[int(coin_number) - 1] == 40 or self.green_coin_position[
                    int(coin_number) - 1] == 14:
                    pass
                else:
                    if self.green_coin_position[int(coin_number) - 1] < 100:
                        self.player_elimination(self.green_coin_position[int(coin_number) - 1], color_coin,
                                                self.green_coin_tracker)

                self.green_coord_list[int(coin_number) - 1] = self.green_coin_position[int(coin_number) - 1]

            else:
                messagebox.showerror("Wrong choice", "Sorry, Your coin in not permitted to travel")
                self.coin_buttons_manager(self.roll_predict_coins[3][2])
                return

            self.roll_predict_coins[3][1]['state'] = NORMAL

        print(self.red_coord_list)
        print(self.green_coord_list)
        print(self.yellow_coord_list)
        print(self.blue_coord_list)
        if self.check_if_bot == 1:
            print("Robo bot_coins is: ", self.robo_bot_coins)

        allow_granted_to_proceed = True

        if color_coin == "red" and self.red_coin_position[int(coin_number) - 1] == 106:
            allow_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif color_coin == "green" and self.green_coin_position[int(coin_number) - 1] == 106:
            allow_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif color_coin == "yellow" and self.yellow_coin_position[int(coin_number) - 1] == 106:
            allow_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif color_coin == "blue" and self.blue_coin_position[int(coin_number) - 1] == 106:
            allow_granted_to_proceed = self.check_winner_and_runner(color_coin)

        if allow_granted_to_proceed:
            self.player_bot_manager(bot_parameter)

    def initial_position_red(self, coin_number):
        self.make_canvas.delete(self.graphical_red_coin[int(coin_number) - 1])
        self.graphical_red_coin[int(coin_number) - 1] = \
            self.make_canvas.create_oval(100 + 40, 15 + (40 * 6),
                                         100 + 40 + 40,
                                         15 + (40 * 6) + 40, fill="red",
                                         width=3,
                                         outline="black")

        self.label_red_coin[int(coin_number) - 1].place_forget()
        red_start_label_x = 100 + 40 + 10
        red_start_label_y = 15 + (40 * 6) + 5
        self.label_red_coin[int(coin_number) - 1].place(x=red_start_label_x, y=red_start_label_y)

        self.red_coin_position[int(coin_number) - 1] = 1
        self.window.update()
        time.sleep(0.2)

    def initial_position_yellow(self, coin_number):
        self.make_canvas.delete(self.graphical_yellow_coin[int(coin_number) - 1])
        self.graphical_yellow_coin[int(coin_number) - 1] = self.make_canvas.create_oval(
            100 + (40 * 6) + (40 * 3) + (40 * 4),
            15 + (40 * 8),
            100 + (40 * 6) + (40 * 3) + (40 * 5),
            15 + (40 * 9), fill="yellow",
            width=3)

        self.label_yellow_coin[int(coin_number) - 1].place_forget()
        yellow_start_label_x = 100 + (40 * 6) + (40 * 3) + (40 * 4) + 10
        yellow_start_label_y = 15 + (40 * 8) + 5
        self.label_yellow_coin[int(coin_number) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)

        self.yellow_coin_position[int(coin_number) - 1] = 27
        self.window.update()
        time.sleep(0.2)

    def initial_position_green(self, coin_number):
        self.make_canvas.delete(self.graphical_green_coin[int(coin_number) - 1])
        self.graphical_green_coin[int(coin_number) - 1] = self.make_canvas.create_oval(100 + (40 * 8), 15 + 40,
                                                                                       100 + (40 * 9), 15 + 40 + 40,
                                                                                       fill="#00FF00", width=3)

        self.label_green_coin[int(coin_number) - 1].place_forget()
        green_start_label_x = 100 + (40 * 8) + 10
        green_start_label_y = 15 + 40 + 5
        self.label_green_coin[int(coin_number) - 1].place(x=green_start_label_x, y=green_start_label_y)

        self.green_coin_position[int(coin_number) - 1] = 14
        self.window.update()
        time.sleep(0.2)

    def initial_position_blue(self, coin_number):
        print("graphical_blue_coin:", self.graphical_blue_coin)
        self.make_canvas.delete(self.graphical_blue_coin[int(coin_number) - 1])
        self.graphical_blue_coin[int(coin_number) - 1] = self.make_canvas.create_oval(100 + 240, 340 + (40 * 5) - 5,
                                                                                      100 + 240 + 40,
                                                                                      340 + (40 * 6) - 5,
                                                                                      fill="#04d9ff", width=3)

        self.label_blue_coin[int(coin_number) - 1].place_forget()
        blue_start_label_x = 100 + 240 + 10
        blue_start_label_y = 340 + (40 * 5) - 5 + 5
        self.label_blue_coin[int(coin_number) - 1].place(x=blue_start_label_x, y=blue_start_label_y)

        self.blue_coin_position[int(coin_number) - 1] = 40
        self.window.update()
        time.sleep(0.2)

    def coin_traversal(self, coin_position, current_coin, coin_num_label, coin_num_label_x, coin_num_label_y, color_coin,
                       dice_value):
        print("param:", coin_position, current_coin, coin_num_label, coin_num_label_x, coin_num_label_y, color_coin,
              dice_value)
        try:
            coin_num_label.place(x=coin_num_label_x, y=coin_num_label_y)
            while True:
                if dice_value == 0:
                    break
                elif (coin_position == 51 and color_coin == "red") or (
                        coin_position == 12 and color_coin == "green") or (
                        coin_position == 25 and color_coin == "yellow") or (
                        coin_position == 38 and color_coin == "blue") or coin_position >= 100:
                    if coin_position < 100:
                        coin_position = 100

                    coin_position = self.movement_controller(current_coin, coin_num_label, coin_num_label_x,
                                                                      coin_num_label_y, dice_value, coin_position,
                                                                      color_coin)

                    if coin_position == 106:

                        if self.check_if_bot == 1 and color_coin == "red":
                            messagebox.showinfo("Final Destination reached",
                                                "Hey! I am at the final point of the game....")
                        else:
                            messagebox.showinfo("Final Destination reached",
                                                "Congratulations! You are at the final point of the game...")
                        if dice_value == 6:
                            self.turn_after_six = 1
                        else:
                            self.time_for -= 1
                    break

                coin_position += 1
                dice_value -= 1
                coin_num_label.place_forget()

                print(coin_position)

                if coin_position <= 5:
                    self.make_canvas.move(current_coin, 40, 0)
                    coin_num_label_x += 40
                elif coin_position == 6:
                    self.make_canvas.move(current_coin, 40, -40)
                    coin_num_label_x += 40
                    coin_num_label_y -= 40
                elif 6 < coin_position <= 11:
                    self.make_canvas.move(current_coin, 0, -40)
                    coin_num_label_y -= 40
                elif coin_position <= 13:
                    self.make_canvas.move(current_coin, 40, 0)
                    coin_num_label_x += 40
                elif coin_position <= 18:
                    self.make_canvas.move(current_coin, 0, 40)
                    coin_num_label_y += 40
                elif coin_position == 19:
                    self.make_canvas.move(current_coin, 40, 40)
                    coin_num_label_x += 40
                    coin_num_label_y += 40
                elif coin_position <= 24:
                    self.make_canvas.move(current_coin, 40, 0)
                    coin_num_label_x += 40
                elif coin_position <= 26:
                    self.make_canvas.move(current_coin, 0, 40)
                    coin_num_label_y += 40
                elif coin_position <= 31:
                    self.make_canvas.move(current_coin, -40, 0)
                    coin_num_label_x -= 40
                elif coin_position == 32:
                    self.make_canvas.move(current_coin, -40, 40)
                    coin_num_label_x -= 40
                    coin_num_label_y += 40
                elif coin_position <= 37:
                    self.make_canvas.move(current_coin, 0, 40)
                    coin_num_label_y += 40
                elif coin_position <= 39:
                    self.make_canvas.move(current_coin, -40, 0)
                    coin_num_label_x -= 40
                elif coin_position <= 44:
                    self.make_canvas.move(current_coin, 0, -40)
                    coin_num_label_y -= 40
                elif coin_position == 45:
                    self.make_canvas.move(current_coin, -40, -40)
                    coin_num_label_x -= 40
                    coin_num_label_y -= 40
                elif coin_position <= 50:
                    self.make_canvas.move(current_coin, -40, 0)
                    coin_num_label_x -= 40
                elif 50 < coin_position <= 52:
                    self.make_canvas.move(current_coin, 0, -40)
                    coin_num_label_y -= 40
                elif coin_position == 53:
                    self.make_canvas.move(current_coin, 40, 0)
                    coin_num_label_x += 40
                    coin_position = 1

                coin_num_label.place_forget()
                coin_num_label.place(x=coin_num_label_x, y=coin_num_label_y)

                self.window.update()
                time.sleep(0.2)

            return coin_position
        except:
            print("Force Stop Error Came in motion of coin")

    def movement_controller(self, current_coin, coin_num_label, coin_num_label_x, coin_num_label_y, dice_value,
                            current_pos, color_coin):
        if color_coin == "red" and current_pos >= 100:
            if int(current_pos) + int(dice_value) <= 106:
                current_pos = self.red_player_movement(current_coin, coin_num_label, coin_num_label_x, coin_num_label_y,
                                                       dice_value, current_pos)

        elif color_coin == "green" and current_pos >= 100:
            if int(current_pos) + int(dice_value) <= 106:
                current_pos = self.green_player_movement(current_coin, coin_num_label, coin_num_label_x,
                                                         coin_num_label_y,
                                                         dice_value, current_pos)

        elif color_coin == "yellow" and current_pos >= 100:
            if int(current_pos) + int(dice_value) <= 106:
                current_pos = self.yellow_player_movement(current_coin, coin_num_label, coin_num_label_x,
                                                          coin_num_label_y,
                                                          dice_value, current_pos)

        elif color_coin == "blue" and current_pos >= 100:
            if int(current_pos) + int(dice_value) <= 106:
                current_pos = self.blue_player_movement(current_coin, coin_num_label, coin_num_label_x,
                                                        coin_num_label_y,
                                                        dice_value, current_pos)

        return current_pos

    def blue_player_movement(self, current_coin, coin_num_label, coin_num_label_x, coin_num_label_y, dice_value,
                             current_pos):
        while dice_value > 0:
            current_pos += 1
            dice_value -= 1
            self.make_canvas.move(current_coin, 0, -40)
            coin_num_label_y -= 40
            coin_num_label.place(x=coin_num_label_x, y=coin_num_label_y)
            self.window.update()
            time.sleep(0.2)
        return current_pos

    def green_player_movement(self, current_coin, coin_num_label, coin_num_label_x, coin_num_label_y, dice_value,
                              current_pos):
        while dice_value > 0:
            current_pos += 1
            dice_value -= 1
            self.make_canvas.move(current_coin, 0, 40)
            coin_num_label_y += 40
            coin_num_label.place(x=coin_num_label_x, y=coin_num_label_y)
            self.window.update()
            time.sleep(0.2)
        return current_pos

    def red_player_movement(self, current_coin, coin_num_label, coin_num_label_x, coin_num_label_y, dice_value,
                            current_pos):
        while dice_value > 0:
            current_pos += 1
            dice_value -= 1
            self.make_canvas.move(current_coin, 40, 0)
            coin_num_label_x += 40
            coin_num_label.place(x=coin_num_label_x, y=coin_num_label_y)
            self.window.update()
            time.sleep(0.2)
        return current_pos

    def yellow_player_movement(self, current_coin, coin_num_label, coin_num_label_x, coin_num_label_y, dice_value,
                               current_pos):
        while dice_value > 0:
            current_pos += 1
            dice_value -= 1
            self.make_canvas.move(current_coin, -40, 0)
            coin_num_label_x -= 40
            coin_num_label.place(x=coin_num_label_x, y=coin_num_label_y)
            self.window.update()
            time.sleep(0.2)
        return current_pos

    ### Killing the Opponent player

    def player_elimination(self, coin_position, coin_color, path_to_traverse_before_overlap):
        if coin_color != "red":
            for coin_index_coin_number in range(len(self.red_coord_list)):
                if self.red_coord_list[coin_index_coin_number] == coin_position:
                    if path_to_traverse_before_overlap == 6:
                        self.turn_after_six = 1
                    else:
                        self.time_for -= 1

                    self.make_canvas.delete(self.graphical_red_coin[coin_index_coin_number])
                    self.label_red_coin[coin_index_coin_number].place_forget()
                    self.red_coin_position[coin_index_coin_number] = -1
                    self.red_coord_list[coin_index_coin_number] = -1
                    if self.check_if_bot == 1:
                        self.robo_bot_coins.remove(coin_index_coin_number + 1)
                        if self.red_coin_position.count(-1) >= 1:
                            self.count_robo_stage_from_start = 2

                    if coin_index_coin_number == 0:
                        coin_recreate = self.make_canvas.create_oval(100 + 40, 15 + 40, 100 + 40 + 40, 15 + 40 + 40,
                                                                     width=3, fill="red", outline="black")
                        self.label_red_coin[coin_index_coin_number].place(x=100 + 40 + 10, y=15 + 40 + 5)
                    elif coin_index_coin_number == 1:
                        coin_recreate = self.make_canvas.create_oval(100 + 40 + 60 + 60, 15 + 40,
                                                                     100 + 40 + 60 + 60 + 40,
                                                                     15 + 40 + 40, width=3, fill="red", outline="black")
                        self.label_red_coin[coin_index_coin_number].place(x=100 + 40 + 60 + 60 + 10, y=15 + 40 + 5)
                    elif coin_index_coin_number == 2:
                        coin_recreate = self.make_canvas.create_oval(100 + 40 + 60 + 60, 15 + 40 + 100,
                                                                     100 + 40 + 60 + 60 + 40, 15 + 40 + 40 + 100,
                                                                     width=3,
                                                                     fill="red", outline="black")
                        self.label_red_coin[coin_index_coin_number].place(x=100 + 40 + 60 + 60 + 10, y=15 + 40 + 100 + 5)
                    else:
                        coin_recreate = self.make_canvas.create_oval(100 + 40, 15 + 40 + 100, 100 + 40 + 40,
                                                                     15 + 40 + 40 + 100, width=3, fill="red",
                                                                     outline="black")
                        self.label_red_coin[coin_index_coin_number].place(x=100 + 40 + 10, y=15 + 40 + 100 + 5)

                    self.graphical_red_coin[coin_index_coin_number] = coin_recreate

        if coin_color != "green":
            for coin_index_coin_number in range(len(self.green_coord_list)):
                if self.green_coord_list[coin_index_coin_number] == coin_position:
                    if path_to_traverse_before_overlap == 6:
                        self.turn_after_six = 1
                    else:
                        self.time_for -= 1

                    self.make_canvas.delete(self.graphical_green_coin[coin_index_coin_number])
                    self.label_green_coin[coin_index_coin_number].place_forget()
                    self.green_coin_position[coin_index_coin_number] = -1
                    self.green_coord_list[coin_index_coin_number] = -1

                    if coin_index_coin_number == 0:
                        coin_recreate = self.make_canvas.create_oval(340 + (40 * 3) + 40, 15 + 40,
                                                                     340 + (40 * 3) + 40 + 40, 15 + 40 + 40, width=3,
                                                                     fill="#00FF00", outline="black")
                        self.label_green_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 5)
                    elif coin_index_coin_number == 1:
                        coin_recreate = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40,
                                                                     340 + (40 * 3) + 40 + 60 + 40 + 40 + 20,
                                                                     15 + 40 + 40, width=3, fill="#00FF00",
                                                                     outline="black")
                        self.label_green_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30,
                                                                      y=15 + 40 + 5)
                    elif coin_index_coin_number == 2:
                        coin_recreate = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40 + 100,
                                                                     340 + (40 * 3) + 40 + 60 + 40 + 40 + 20,
                                                                     15 + 40 + 40 + 100, width=3, fill="#00FF00",
                                                                     outline="black")
                        self.label_green_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30,
                                                                      y=15 + 40 + 100 + 5)
                    else:
                        coin_recreate = self.make_canvas.create_oval(340 + (40 * 3) + 40, 15 + 40 + 100,
                                                                     340 + (40 * 3) + 40 + 40, 15 + 40 + 40 + 100,
                                                                     width=3, fill="#00FF00", outline="black")
                        self.label_green_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 100 + 5)

                    self.graphical_green_coin[coin_index_coin_number] = coin_recreate

        if coin_color != "yellow":
            for coin_index_coin_number in range(len(self.yellow_coord_list)):
                if self.yellow_coord_list[coin_index_coin_number] == coin_position:
                    if path_to_traverse_before_overlap == 6:
                        self.turn_after_six = 1
                    else:
                        self.time_for -= 1

                    self.make_canvas.delete(self.graphical_yellow_coin[coin_index_coin_number])
                    self.label_yellow_coin[coin_index_coin_number].place_forget()
                    self.yellow_coin_position[coin_index_coin_number] = -1
                    self.yellow_coord_list[coin_index_coin_number] = -1

                    if coin_index_coin_number == 0:
                        coin_recreate = self.make_canvas.create_oval(340 + (40 * 3) + 40, 340 + 80 + 15,
                                                                     340 + (40 * 3) + 40 + 40, 340 + 80 + 40 + 15,
                                                                     width=3, fill="yellow", outline="black")
                        self.label_yellow_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 10,
                                                                       y=30 + (40 * 6) + (40 * 3) + 40 + 10)
                    elif coin_index_coin_number == 1:
                        coin_recreate = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340 + 80 + 15,
                                                                     340 + (40 * 3) + 40 + 60 + 40 + 40 + 20,
                                                                     340 + 80 + 40 + 15, width=3, fill="yellow",
                                                                     outline="black")
                        self.label_yellow_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30,
                                                                       y=30 + (40 * 6) + (40 * 3) + 40 + 10)
                    elif coin_index_coin_number == 2:
                        coin_recreate = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20,
                                                                     340 + 80 + 60 + 40 + 15,
                                                                     340 + (40 * 3) + 40 + 60 + 40 + 40 + 20,
                                                                     340 + 80 + 60 + 40 + 40 + 15, width=3,
                                                                     fill="yellow",
                                                                     outline="black")
                        self.label_yellow_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30,
                                                                       y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)
                    else:
                        coin_recreate = self.make_canvas.create_oval(340 + (40 * 3) + 40, 340 + 80 + 60 + 40 + 15,
                                                                     340 + (40 * 3) + 40 + 40,
                                                                     340 + 80 + 60 + 40 + 40 + 15, width=3,
                                                                     fill="yellow",
                                                                     outline="black")
                        self.label_yellow_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 10,
                                                                       y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)

                    self.graphical_yellow_coin[coin_index_coin_number] = coin_recreate

        if coin_color != "blue":
            for coin_index_coin_number in range(len(self.blue_coord_list)):
                if self.blue_coord_list[coin_index_coin_number] == coin_position:
                    if path_to_traverse_before_overlap == 6:
                        self.turn_after_six = 1
                    else:
                        self.time_for -= 1

                    self.make_canvas.delete(self.graphical_blue_coin[coin_index_coin_number])
                    self.label_blue_coin[coin_index_coin_number].place_forget()
                    self.blue_coin_position[coin_index_coin_number] = -1
                    self.blue_coord_list[coin_index_coin_number] = -1

                    if coin_index_coin_number == 0:
                        coin_recreate = self.make_canvas.create_oval(100 + 40, 340 + 80 + 15, 100 + 40 + 40,
                                                                     340 + 80 + 40 + 15, width=3, fill="#04d9ff",
                                                                     outline="black")
                        self.label_blue_coin[coin_index_coin_number].place(x=100 + 40 + 10,
                                                                     y=30 + (40 * 6) + (40 * 3) + 40 + 10)
                    elif coin_index_coin_number == 1:
                        coin_recreate = self.make_canvas.create_oval(100 + 40 + 60 + 40 + 20, 340 + 80 + 15,
                                                                     100 + 40 + 60 + 40 + 40 + 20, 340 + 80 + 40 + 15,
                                                                     width=3, fill="#04d9ff", outline="black")
                        self.label_blue_coin[coin_index_coin_number].place(x=100 + 40 + 60 + 60 + 10,
                                                                     y=30 + (40 * 6) + (40 * 3) + 40 + 10)
                    elif coin_index_coin_number == 2:
                        coin_recreate = self.make_canvas.create_oval(100 + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15,
                                                                     100 + 40 + 60 + 40 + 40 + 20,
                                                                     340 + 80 + 60 + 40 + 40 + 15, width=3,
                                                                     fill="#04d9ff", outline="black")
                        self.label_blue_coin[coin_index_coin_number].place(x=100 + 40 + 60 + 60 + 10,
                                                                     y=30 + (40 * 6) + (
                                                                             40 * 3) + 40 + 60 + 40 + 10)
                    else:
                        coin_recreate = self.make_canvas.create_oval(100 + 40, 340 + 80 + 60 + 40 + 15, 100 + 40 + 40,
                                                                     340 + 80 + 60 + 40 + 40 + 15, width=3,
                                                                     fill="#04d9ff", outline="black")
                        self.label_blue_coin[coin_index_coin_number].place(x=100 + 40 + 10, y=30 + (40 * 6) + (
                                40 * 3) + 40 + 60 + 40 + 10)

                    self.graphical_blue_coin[coin_index_coin_number] = coin_recreate


    def check_winner_and_runner(self, color_coin):
        coins_home = 0  # Check for all specific color coins
        if color_coin == "red":
            coins_list = self.red_coord_list
            index_pos = 0  # Player index
        elif color_coin == "green":
            coins_list = self.green_coord_list
            index_pos = 3  # Player index
        elif color_coin == "yellow":
            coins_list = self.yellow_coord_list
            index_pos = 2  # Player index
        else:
            coins_list = self.blue_coord_list
            index_pos = 1  # Player index

        for coin_index in coins_list:
            if coin_index == 106:
                coins_home = 1
            else:
                coins_home = 0
                break

        if coins_home == 1:
            self.destination_coin_tracker += 1
            if self.destination_coin_tracker == 1:
                self.first_winner = [color_coin,"Winner of the Game"]
                if self.check_if_bot == 1 and color_coin == "red":
                    string1 = color_coin + "  Winner of the Game"
                    messagebox.showinfo(string1,string1)
                else:
                    string1 = color_coin+"  Winner of the Game"
                    messagebox.showinfo(string1,string1)
            elif self.destination_coin_tracker == 2:
                string2 = color_coin + "  1st Runner Up of the Game"
                if self.check_if_bot == 1 and color_coin == "red":
                     messagebox.showinfo(string2,string2)
                else:
                    messagebox.showinfo(string2,string2)
            elif self.destination_coin_tracker == 3:
                string3 = color_coin + "  2nd Runner Up of the Game"
                if self.check_if_bot == 1 and color_coin == "red":
                    messagebox.showinfo(string3,string3)
                else:
                    messagebox.showinfo(string3,string3)

            self.roll_predict_coins[index_pos][1]['state'] = DISABLED
            self.total_people_play.remove(index_pos)

            if len(self.total_people_play) == 1:
                string4 = "Better Luck Next Time"
                messagebox.showinfo(string4)
                self.roll_predict_coins[0][1]['state'] = DISABLED
                return False
            else:
                self.time_for -= 1
        else:
            print("No Winner")

        return True

    def bot_operations(self, ind="give"):
        if ind == "give":
            coins_inside = 1
            for i in range(4):
                if self.red_coin_position[i] == -1:
                    coins_inside = 1
                else:
                    coins_inside = 0
                    break

            if coins_inside == 1:
                if self.red_coin_tracker == 6:
                    guessed_coin = choice([1, 2, 3, 4])
                    self.robo_bot_coins.append(guessed_coin)
                    self.game_manager("red", guessed_coin)
                else:
                    pass
            else:
                crnt_val = self.red_coin_position
                coin_index_ref = self.blue_coin_position

                if len(self.robo_bot_coins) == 1:
                    if self.red_coin_tracker < 6:
                        if (self.count_robo_stage_from_start > 3) and (
                                crnt_val[self.robo_bot_coins[0] - 1] >= 33 and crnt_val[self.robo_bot_coins[0] - 1] <= 38):
                            self.count_robo_stage_from_start = 2
                        self.game_manager("red", self.robo_bot_coins[0])
                    else:
                        enable_fwd = 0
                        for coin in coin_index_ref:
                            if coin > -1 and coin < 101:
                                if (
                                        coin != 40 or coin != 35 or coin != 27 or coin != 22 or coin != 14 or coin != 9 or coin != 1 or coin != 48) and coin - \
                                        crnt_val[self.robo_bot_coins[0] - 1] >= 6 and coin - crnt_val[self.robo_bot_coins[0] - 1] <= 12:
                                    enable_fwd = 1
                                    break
                                else:
                                    enable_fwd = 0
                            else:
                                enable_fwd = 0

                        if enable_fwd == 0:
                            bot_coins = [1, 2, 3, 4]
                            bot_coins.remove(self.robo_bot_coins[0])
                            guessed_coin = choice(bot_coins)
                            self.robo_bot_coins.append(guessed_coin)
                            self.game_manager("red", guessed_coin)
                        else:
                            self.game_manager("red", self.robo_bot_coins[0])
                else:
                    def normal_movement_according_condition():

                        normal_movement = 1

                        for coin in self.robo_bot_coins:
                            if crnt_val[
                                coin - 1] + self.red_coin_tracker <= 106:
                                pass
                            else:
                                normal_movement = 0
                                break

                        if normal_movement:
                            bot_values = [coin for coin in self.robo_bot_coins]
                        else:
                            bot_values = [coin for coin in self.robo_bot_coins if
                                               crnt_val[coin - 1] + self.red_coin_tracker <= 106]

                        for coin in bot_values:
                            if len(bot_values) > 1 and crnt_val[
                                coin - 1] < 101:
                                if (crnt_val[coin - 1] in coin_index_ref) and (
                                        crnt_val[coin - 1] != 1 or crnt_val[coin - 1] != 9 or crnt_val[coin - 1] != 14 or crnt_val[
                                    coin - 1] != 22 or crnt_val[coin - 1] != 27 or crnt_val[coin - 1] != 35 or crnt_val[
                                            coin - 1] != 40 or crnt_val[coin - 1] != 48):
                                    bot_values.remove(coin)
                                elif crnt_val[coin - 1] <= 39 and crnt_val[coin - 1] + self.red_coin_tracker > 39:
                                    for loc_coin_other in coin_index_ref:
                                        if (loc_coin_other >= 40 and loc_coin_other <= 46) and (
                                                crnt_val[coin - 1] + self.red_coin_tracker > loc_coin_other):
                                            bot_values.remove(coin)
                                            break

                        process_forward = 1
                        for coin in bot_values:
                            if crnt_val[coin - 1] + self.red_coin_tracker in coin_index_ref:
                                process_forward = 0
                                self.game_manager("red", coin)
                                break
                        if process_forward:
                            coin_index_len = len(bot_values)
                            bot_coins = {}
                            if coin_index_ref:
                                for robo in bot_values:
                                    for coin_other in coin_index_ref:
                                        if coin_other > -1 and coin_other < 100:
                                            if coin_index_len > 1 and (crnt_val[robo - 1] > 38 and coin_other <= 38) or \
                                                    ((crnt_val[robo - 1] == 9 or crnt_val[robo - 1] == 14 or crnt_val[
                                                        robo - 1] == 27 or
                                                      crnt_val[robo - 1] == 35 or crnt_val[robo - 1] == 40 or crnt_val[
                                                          robo - 1] == 48 or
                                                      crnt_val[robo - 1] == 22) and (coin_other <= crnt_val[robo - 1] or
                                                                                 (coin_other > crnt_val[
                                                                                     robo - 1] and coin_other <= crnt_val[
                                                                                      robo - 1] + 3))):
                                                coin_index_len -= 1
                                            else:
                                                bot_coins[crnt_val[robo - 1] - coin_other] = (
                                                    robo, coin_index_ref.index(coin_other) + 1)
                            if bot_coins:
                                bot_coins_positive_dis = {}
                                bot_coins_negative_dis = {}
                                coin_index_max = 0
                                coin_index_min = 0

                                try:
                                    bot_coins_positive_dis = dict((k, v) for k, v in bot_coins.items() if k > 0)
                                    coin_index_min = min(bot_coins_positive_dis.items())
                                except:
                                    pass
                                try:
                                    bot_coins_negative_dis = dict((k, v) for k, v in bot_coins.items() if k < 0)
                                    coin_index_max = max(bot_coins_negative_dis.items())
                                except:
                                    pass
                                work_comp_in_pos = 0
                                coin_index_len = len(bot_coins_positive_dis)
                                index_from_last = -1

                                while coin_index_len:
                                    if coin_index_min and coin_index_min[0] <= 6:

                                        work_comp_in_pos = 1
                                        self.game_manager("red", coin_index_min[1][0])
                                        break
                                    else:
                                        index_from_last -= 1
                                        try:
                                            coin_index_min = min(sorted(bot_coins_positive_dis.items())[index_from_last])
                                        except:
                                            break
                                    coin_index_len -= 1
                                work_comp_in_neg = 0
                                if not work_comp_in_pos:
                                    coin_index_len = len(bot_coins_negative_dis)
                                    index_from_last = len(bot_coins_negative_dis) - 1
                                    while coin_index_len:
                                        if coin_index_max and crnt_val[coin_index_max[1][0] - 1] + self.red_coin_tracker <= coin_index_ref[
                                            coin_index_max[1][1] - 1]:
                                            work_comp_in_neg = 1
                                            self.game_manager("red", coin_index_max[1][0])
                                            break
                                        else:
                                            index_from_last -= 1
                                            try:
                                                coin_index_max = max(sorted(bot_coins_negative_dis.items())[index_from_last])
                                            except:
                                                break
                                        coin_index_len -= 1
                                if not work_comp_in_neg and not work_comp_in_pos:
                                    bot_list = bot_values[0]
                                    for coin_index in range(1, len(bot_values)):
                                        if crnt_val[bot_values[coin_index] - 1] > crnt_val[bot_list - 1]:
                                            bot_list = bot_values[coin_index]

                                    self.game_manager("red", bot_list)
                            else:
                                bot_list = bot_values[0]
                                for coin_index in range(1, len(bot_values)):
                                    if crnt_val[bot_values[coin_index] - 1] > crnt_val[bot_list - 1]:
                                        bot_list = bot_values[coin_index]
                                self.game_manager("red", bot_list)
                        else:
                            pass

                    if self.red_coin_tracker < 6:
                        normal_movement_according_condition()
                    else:
                        coin_proceed = 0

                        for coin in self.robo_bot_coins:
                            if crnt_val[coin - 1] + self.red_coin_tracker in self.blue_coin_position:
                                coin_proceed = coin
                                break

                        if not coin_proceed:
                            if -1 in self.red_coin_position:
                                coins_list = [1, 2, 3, 4]
                                for coin in self.robo_bot_coins:
                                    coins_list.remove(coin)
                                coin_index_pred = choice(coins_list)
                                self.robo_bot_coins.append(coin_index_pred)
                                self.game_manager("red", coin_index_pred)
                            else:
                                normal_movement_according_condition()
                        else:
                            self.game_manager("red", coin_proceed)
        else:
            self.coin_prediction("red")


if __name__ == '__main__':
    window = Tk()
    window.geometry("800x630")
    window.maxsize(800, 630)
    window.minsize(800, 630)
    window.title("Ludo Board Game")
    window.iconbitmap("Images/ludo_icon.ico")
    Ludo(window)
    window.mainloop()