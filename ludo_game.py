from tkinter import messagebox
import time
import pygame
from random import randint, choice
from board import Board
from tkinter import *


class Ludo:
    def __init__(self, window):

        from player import Player
        self.window = window

        self.ludo_game = Canvas(self.window, bg="#E9C67F", width=800, height=630)
        # Tkinter canvas used to create rectangular Ludo Board
        self.ludo_game.pack(fill=BOTH, expand=1)

        # storing all the values of all colors , label, Roll button, 1,2,3,4 buttons
        self.roll_predict_coins = []
        # storing number of playing when play with friends is selected
        self.total_people_play = []

        self.red_player_pos = [1, 2, 3, 4]
        self.green_player_pos = [1, 2, 3, 4]
        self.yellow_player_pos = [1, 2, 3, 4]
        self.blue_player_pos = [1, 2, 3, 4]

        coin_index = 0
        # initializing all coins positions to -1
        while coin_index < len(self.red_player_pos):
            self.red_player_pos[coin_index] = -1
            self.green_player_pos[coin_index] = -1
            self.yellow_player_pos[coin_index] = -1
            self.blue_player_pos[coin_index] = -1
            coin_index += 1

        # bot_coins specific positions of coins of all colors
        self.red_coin_start_pos = [-1, -1, -1, -1]
        self.green_coin_start_pos = [-1, -1, -1, -1]
        self.yellow_coin_start_pos = [-1, -1, -1, -1]
        self.blue_coin_start_pos = [-1, -1, -1, -1]
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
        self.clock_counter = -1
        self.six_list = []

        self.check_if_bot = 0
        # variable which indicates bot's turn to play
        self.calculate_bot_turns = 0
        self.bot_value_pos = []
        self.first_winner = []

        # safe positions at each side
        self.safe_pos_1 = None
        self.safe_pos_2 = None
        self.safe_pos_3 = None
        self.safe_pos_4 = None

        b = Board(self.ludo_game)
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
        roll_btn = Player(self.ludo_game, self)
        red_roll_btn = roll_btn.dice_roll_move("red", 34, 15, 25, 65)
        blue_roll_btn = roll_btn.dice_roll_move("blue", 34, 385, 25, 435)
        green_roll_btn = roll_btn.dice_roll_move("green", 730, 15, 722, 65)
        yellow_roll_btn = roll_btn.dice_roll_move("yellow", 730, 385, 722, 435)
        print("red_btn:", red_roll_btn)
        self.block_number_side = roll_btn.dice_sides

        self.roll_predict_coins = [red_roll_btn, blue_roll_btn, yellow_roll_btn, green_roll_btn]

        print("create_buttons:", self.roll_predict_coins)

        self.initial_window()

    def initial_window(self):

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

        head = Label(top, text="-:Total number of players:- ", font=("Times New Roman", 12, "bold", "italic"), bg="orange",
                     fg="chocolate")
        head.place(x=70, y=220)
        coin_index_entry = Entry(top, font=("Times New Roman", 18, "bold", "italic"), relief=SUNKEN, bd=7, width=12)
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
                for index_val in range(int(coin_index_entry.get())):
                    self.total_people_play.append(index_val)
                print(self.total_people_play)
                self.player_bot_manager()
                top.destroy()
            else:
                messagebox.showerror("Input Error", "Please enter values only between 2 and 4")
                top.destroy()
                self.initial_window()

        start_btn = Button(top, text="Start", bg="#262626", fg="#00FF00", font=("Times New Roman", 13, "bold"), relief=RAISED,
                           bd=3, command=processing, state=DISABLED)
        start_btn.place(x=550, y=220)

        def select(value):
            if value:
                self.check_if_bot = 1
                for index_val in range(2):
                    self.total_people_play.append(index_val)
                print(self.total_people_play)

                def display_start_message(start_time):
                    if dmnsn_list['text'] != "":
                        dmnsn_list.place_forget()
                    if instructn_list['text'] != "":
                        instructn_list.place_forget()

                    dmnsn_list['text'] = f"  This game starts in {start_time} sec"
                    dmnsn_list.place(x=100, y=300)

                    if start_time > 5:
                        instructn_list[
                            'text'] = f"             Computer will Play With Red coin and the Player will play With " \
                                      f"Sky Blue Coin for this game"
                    elif 2 <= start_time < 5:
                        instructn_list[
                            'text'] = f"                     Player will Roll the dice first for this game"
                    else:
                        instructn_list[
                            'text'] = f"                                       All the best!!! Enjoy the Game"
                    instructn_list.place(x=10, y=350)

                start_time = 10
                dmnsn_list = Label(top, text="", font=("Times New Roman", 20, "bold"), fg="#FF0000", bg="#FFFFFF")
                instructn_list = Label(top, text="", font=("Times New Roman", 12, "bold"), fg="#af7439", bg="#FFFFFF")

                try:
                    while start_time:
                        display_start_message(start_time)
                        start_time -= 1
                        self.window.update()
                        time.sleep(1)
                    top.destroy()
                except:
                    print("Force Stop Error in Operate")
                self.roll_predict_coins[1][1]['state'] = NORMAL
            else:
                start_btn['state'] = NORMAL
                coin_index_entry['state'] = NORMAL

        start_button1 = Button(top, text="Play With Computer", bg="#2B4AF7", fg="#FCFCFD",
                               font=("Times New Roman", 12, "bold"),
                               relief=RAISED, bd=3, command=lambda: select(1), activebackground="#2B4AF7")
        start_button1.place(x=400, y=150)

        start_button2 = Button(top, text="Play With Friends", bg="#262626", fg="#00FF00",
                               font=("Times New Roman", 12, "bold"),
                               relief=RAISED, bd=3, command=lambda: select(0), activebackground="#262626")
        start_button2.place(x=220
                            , y=150)

        pygame.mixer.init()

        pygame.mixer.music.load('sound/sound.mp3')
        global is_on
        pygame.mixer.music.play(loops=0)
        is_on = True

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

        label1 = Label(top, text="Sound:", font=("Times New Roman", 16, "bold"))
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
                if self.check_if_bot and self.calculate_bot_turns < 3:
                    self.calculate_bot_turns += 1
                if self.check_if_bot and self.calculate_bot_turns == 3 and self.six_tracker < 2:
                    dice_value = self.red_coin_tracker = 6
                    self.calculate_bot_turns += 1
                else:
                    dice_value = self.red_coin_tracker = randint(1, 6)

            elif player_coin == "blue":
                roll_predict_coins = self.roll_predict_coins[1]
                print("blue_block:", roll_predict_coins)
                dice_value = self.blue_coin_tracker = randint(1, 6)
                if self.check_if_bot and dice_value == 6:
                    for coin_place in self.red_player_pos:
                        if 40 <= coin_place <= 46:
                            dice_value = self.blue_coin_tracker = randint(1, 5)
                            break

            elif player_coin == "yellow":
                roll_predict_coins = self.roll_predict_coins[2]
                dice_value = self.yellow_coin_tracker = randint(1, 6)
            else:
                roll_predict_coins = self.roll_predict_coins[3]
                dice_value = self.green_coin_tracker = randint(1, 6)

            roll_predict_coins[1]['state'] = DISABLED

            # Iterate all the dice images
            crnt_val_counter = 12
            while crnt_val_counter > 0:
                move_crnt_val_counter = randint(1, 6)
                roll_predict_coins[0]['image'] = self.block_number_side[move_crnt_val_counter - 1]
                self.window.update()
                time.sleep(0.1)
                crnt_val_counter -= 1

            print("Prediction result: ", dice_value)

    
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
            crnt_val_coin_position = self.red_player_pos
        elif player_coin == "green":
            crnt_val_coin_position = self.green_player_pos
        elif player_coin == "yellow":
            crnt_val_coin_position = self.yellow_player_pos
        else:
            crnt_val_coin_position = self.blue_player_pos

        coins_inside = 1
        x_val = 0
        while x_val < 4:
            if crnt_val_coin_position[x_val] == -1:
                coins_inside = 1
            else:
                coins_inside = 0
                break
            x_val += 1

        if dice_value == 6:
            self.six_tracker += 1
        else:
            self.six_tracker = 0

        if coins_inside == 1 and dice_value == 6:
            self.six_list.append("first_move")

        if ((coins_inside == 1 and dice_value == 6) or (coins_inside == 0)) \
                and self.six_tracker < 3:
            allow = 1
            if player_coin == "red":
                crnt_val = self.red_coin_start_pos
            elif player_coin == "green":
                crnt_val = self.green_coin_start_pos
            elif player_coin == "yellow":
                crnt_val = self.yellow_coin_start_pos
            else:
                crnt_val = self.blue_coin_start_pos

            if dice_value < 6:
                if self.turn_after_six == 1:
                    self.clock_counter -= 1
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
                self.clock_counter -= 1
                self.turn_after_six = 0
            self.player_bot_manager()

        if dice_value == 6 and self.six_tracker < 3 and \
                roll_predict_coins[2][0]['state'] == NORMAL:
            self.clock_counter -= 1
        else:
            self.six_tracker = 0

        if self.check_if_bot == 1 and bot_parameter:
            self.bot_operations(bot_parameter)

    # Player Scope controller method
    def player_bot_manager(self, bot_parameter=None):
        if self.clock_counter == -1:
            pass
        else:
            self.roll_predict_coins[self.total_people_play[self.clock_counter]][1]['state'] = DISABLED
        if self.clock_counter == len(self.total_people_play) - 1:
            self.clock_counter = -1

        self.clock_counter += 1
        self.roll_predict_coins[self.total_people_play[self.clock_counter]][1]['state'] = NORMAL

        if self.check_if_bot == 1 and self.clock_counter == 0:
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
                messagebox.showwarning("Woohoo! Coin Reached Home. ")

            elif self.red_player_pos[int(coin_number) - 1] == -1 and self.red_coin_tracker == 6:
                self.initial_position_red(coin_number)
                self.red_coin_start_pos[int(coin_number) - 1] = 1

            elif self.red_player_pos[int(coin_number) - 1] > -1:
                coin_index_coord = self.ludo_game.coords(self.graphical_red_coin[int(coin_number) - 1])
                red_start_label_x = coin_index_coord[0] + 10
                red_start_label_y = coin_index_coord[1] + 5
                self.label_red_coin[int(coin_number) - 1].place(x=red_start_label_x, y=red_start_label_y)

                if self.red_player_pos[int(coin_number) - 1] + self.red_coin_tracker <= 106:
                    self.red_player_pos[int(coin_number) - 1] = self.coin_traversal(
                        self.red_player_pos[int(coin_number) - 1], self.graphical_red_coin[int(coin_number) - 1],
                        self.label_red_coin[int(coin_number) - 1], red_start_label_x, red_start_label_y, "red",
                        self.red_coin_tracker)
                    if self.check_if_bot and self.red_player_pos[
                        int(coin_number) - 1] == 106 and color_coin == "red":
                        self.bot_value_pos.remove(int(coin_number))
                        print("After removing: ", self.bot_value_pos)

                else:
                    if not self.check_if_bot:
                        messagebox.showerror("Not possible", "Sorry, not permitted")
                    self.coin_buttons_manager(self.roll_predict_coins[0][2])

                    if self.check_if_bot:
                        bot_parameter = "give"
                        self.bot_operations(bot_parameter)
                    return
                if self.red_player_pos[int(coin_number) - 1] == 22 or self.red_player_pos[
                    int(coin_number) - 1] == 9 or self.red_player_pos[int(coin_number) - 1] == 48 or \
                        self.red_player_pos[int(coin_number) - 1] == 35 or self.red_player_pos[
                    int(coin_number) - 1] == 14 or self.red_player_pos[int(coin_number) - 1] == 27 or \
                        self.red_player_pos[int(coin_number) - 1] == 40 or self.red_player_pos[
                    int(coin_number) - 1] == 1:
                    pass

                else:
                    if self.red_player_pos[int(coin_number) - 1] < 100:
                        self.player_elimination(self.red_player_pos[int(coin_number) - 1], color_coin,
                                                self.red_coin_tracker)

                self.red_coin_start_pos[int(coin_number) - 1] = self.red_player_pos[int(coin_number) - 1]
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

            elif self.yellow_player_pos[int(coin_number) - 1] == -1 and self.yellow_coin_tracker == 6:
                self.initial_position_yellow(coin_number)
                self.yellow_coin_start_pos[int(coin_number) - 1] = 27

            elif self.yellow_player_pos[int(coin_number) - 1] > -1:
                coin_index_coord = self.ludo_game.coords(self.graphical_yellow_coin[int(coin_number) - 1])
                yellow_start_label_x = coin_index_coord[0] + 10
                yellow_start_label_y = coin_index_coord[1] + 5
                self.label_yellow_coin[int(coin_number) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)

                if self.yellow_player_pos[int(coin_number) - 1] + self.yellow_coin_tracker <= 106:
                    self.yellow_player_pos[int(coin_number) - 1] = self.coin_traversal(
                        self.yellow_player_pos[int(coin_number) - 1],
                        self.graphical_yellow_coin[int(coin_number) - 1], self.label_yellow_coin[int(coin_number) - 1],
                        yellow_start_label_x, yellow_start_label_y, "yellow", self.yellow_coin_tracker)
                else:
                    messagebox.showerror("Coin Already Reached Home or Path not Permitted ")

                    self.coin_buttons_manager(self.roll_predict_coins[2][2])
                    return

                if self.yellow_player_pos[int(coin_number) - 1] == 22 or self.yellow_player_pos[
                    int(coin_number) - 1] == 9 or self.yellow_player_pos[int(coin_number) - 1] == 48 or \
                        self.yellow_player_pos[int(coin_number) - 1] == 35 or self.yellow_player_pos[
                    int(coin_number) - 1] == 1 or self.yellow_player_pos[int(coin_number) - 1] == 14 or \
                        self.yellow_player_pos[int(coin_number) - 1] == 40 or self.yellow_player_pos[
                    int(coin_number) - 1] == 27:
                    pass
                else:
                    if self.yellow_player_pos[int(coin_number) - 1] < 100:
                        self.player_elimination(self.yellow_player_pos[int(coin_number) - 1], color_coin,
                                                self.yellow_coin_tracker)

                self.yellow_coin_start_pos[int(coin_number) - 1] = self.yellow_player_pos[int(coin_number) - 1]

            else:
                messagebox.showerror("Wrong choice", "Sorry, This coin in not permitted to travel now")
                self.coin_buttons_manager(self.roll_predict_coins[2][2])
                return

            self.roll_predict_coins[2][1]['state'] = NORMAL

        elif color_coin == "blue":
            self.coin_buttons_manager(self.roll_predict_coins[1][2], 0)

            if self.red_coin_tracker == 106:
                messagebox.showwarning("Woohoo!!! Coin Reached Home.... ")

            elif self.blue_player_pos[int(coin_number) - 1] == -1 and self.blue_coin_tracker == 6:
                self.initial_position_blue(coin_number)
                self.blue_coin_start_pos[int(coin_number) - 1] = 40

            elif self.blue_player_pos[int(coin_number) - 1] > -1:
                coin_index_coord = self.ludo_game.coords(self.graphical_blue_coin[int(coin_number) - 1])
                print("coin_index_coord:", coin_index_coord)
                blue_start_label_x = coin_index_coord[0] + 10
                blue_start_label_y = coin_index_coord[1] + 5
                self.label_blue_coin[int(coin_number) - 1].place(x=blue_start_label_x,
                                                                 y=blue_start_label_y)

                if self.blue_player_pos[int(coin_number) - 1] + self.blue_coin_tracker <= 106:
                    self.blue_player_pos[int(coin_number) - 1] = self.coin_traversal(
                        self.blue_player_pos[int(coin_number) - 1],
                        self.graphical_blue_coin[int(coin_number) - 1], self.label_blue_coin[int(coin_number) - 1],
                        blue_start_label_x, blue_start_label_y, "blue", self.blue_coin_tracker)
                else:
                    messagebox.showerror("Not possible", "No path available")
                    self.coin_buttons_manager(self.roll_predict_coins[1][2])
                    return

                if self.blue_player_pos[int(coin_number) - 1] == 22 or self.blue_player_pos[
                    int(coin_number) - 1] == 9 or self.blue_player_pos[int(coin_number) - 1] == 48 or \
                        self.blue_player_pos[int(coin_number) - 1] == 35 or self.blue_player_pos[
                    int(coin_number) - 1] == 1 or self.blue_player_pos[int(coin_number) - 1] == 14 or \
                        self.blue_player_pos[int(coin_number) - 1] == 27 or self.blue_player_pos[
                    int(coin_number) - 1] == 40:
                    pass
                else:
                    if self.blue_player_pos[int(coin_number) - 1] < 100:
                        self.player_elimination(self.blue_player_pos[int(coin_number) - 1],
                                                color_coin, self.blue_coin_tracker)

                self.blue_coin_start_pos[int(coin_number) - 1] = self.blue_player_pos[int(coin_number) - 1]

            else:
                messagebox.showerror("Wrong choice", "Sorry, This coin in not permitted to travel now")
                self.coin_buttons_manager(self.roll_predict_coins[1][2])
                return

            self.roll_predict_coins[1][1]['state'] = NORMAL
        elif color_coin == "green":
            self.coin_buttons_manager(self.roll_predict_coins[3][2], 0)

            if self.green_coin_tracker == 106:
                messagebox.showwarning("Destination reached", "Reached at the destination")

            elif self.green_player_pos[int(coin_number) - 1] == -1 and self.green_coin_tracker == 6:
                self.initial_position_green(coin_number)
                self.green_coin_start_pos[int(coin_number) - 1] = 14

            elif self.green_player_pos[int(coin_number) - 1] > -1:
                coin_index_coord = self.ludo_game.coords(self.graphical_green_coin[int(coin_number) - 1])
                green_start_label_x = coin_index_coord[0] + 10
                green_start_label_y = coin_index_coord[1] + 5
                self.label_green_coin[int(coin_number) - 1].place(x=green_start_label_x, y=green_start_label_y)

                if self.green_player_pos[int(coin_number) - 1] + self.green_coin_tracker <= 106:
                    self.green_player_pos[int(coin_number) - 1] = self.coin_traversal(
                        self.green_player_pos[int(coin_number) - 1], self.graphical_green_coin[int(coin_number) - 1],
                        self.label_green_coin[int(coin_number) - 1], green_start_label_x, green_start_label_y,
                        "green", self.green_coin_tracker)
                else:
                    messagebox.showerror("Not possible", "No path available")
                    self.coin_buttons_manager(self.roll_predict_coins[3][2])
                    return

                if self.green_player_pos[int(coin_number) - 1] == 22 or self.green_player_pos[
                    int(coin_number) - 1] == 9 or self.green_player_pos[int(coin_number) - 1] == 48 or \
                        self.green_player_pos[int(coin_number) - 1] == 35 or self.green_player_pos[
                    int(coin_number) - 1] == 1 or self.green_player_pos[int(coin_number) - 1] == 27 or \
                        self.green_player_pos[int(coin_number) - 1] == 40 or self.green_player_pos[
                    int(coin_number) - 1] == 14:
                    print("Safe Positions")
                else:
                    if self.green_player_pos[int(coin_number) - 1] < 100:
                        self.player_elimination(self.green_player_pos[int(coin_number) - 1], color_coin,
                                                self.green_coin_tracker)

                self.green_coin_start_pos[int(coin_number) - 1] = self.green_player_pos[int(coin_number) - 1]

            else:
                messagebox.showerror("Wrong choice", "Sorry, Your coin in not permitted to travel")
                self.coin_buttons_manager(self.roll_predict_coins[3][2])
                return
            self.roll_predict_coins[3][1]['state'] = NORMAL

        print(self.red_coin_start_pos)
        print(self.green_coin_start_pos)
        print(self.yellow_coin_start_pos)
        print(self.blue_coin_start_pos)
        if self.check_if_bot == 1:
            print("bot_coins are placed in: ", self.bot_value_pos)

        allow_next_step = True

        if color_coin == "red" and self.red_player_pos[int(coin_number) - 1] == 106:
            allow_next_step = self.win_state_manager(color_coin)
        elif color_coin == "green" and self.green_player_pos[int(coin_number) - 1] == 106:
            allow_next_step = self.win_state_manager(color_coin)
        elif color_coin == "yellow" and self.yellow_player_pos[int(coin_number) - 1] == 106:
            allow_next_step = self.win_state_manager(color_coin)
        elif color_coin == "blue" and self.blue_player_pos[int(coin_number) - 1] == 106:
            allow_next_step = self.win_state_manager(color_coin)

        if allow_next_step:
            self.player_bot_manager(bot_parameter)

    def initial_position_red(self, coin_number):
        self.ludo_game.delete(self.graphical_red_coin[int(coin_number) - 1])
        self.graphical_red_coin[int(coin_number) - 1] = \
            self.ludo_game.create_oval(100 + 40, 15 + (40 * 6),
                                         100 + 40 + 40,
                                         15 + (40 * 6) + 40, fill="red",
                                         width=3,
                                         outline="black")

        self.label_red_coin[int(coin_number) - 1].place_forget()
        red_start_label_x = 100 + 40 + 10
        red_start_label_y = 15 + (40 * 6) + 5
        self.label_red_coin[int(coin_number) - 1].place(x=red_start_label_x, y=red_start_label_y)

        self.red_player_pos[int(coin_number) - 1] = 1
        self.window.update()
        time.sleep(0.2)

    def initial_position_yellow(self, coin_number):
        self.ludo_game.delete(self.graphical_yellow_coin[int(coin_number) - 1])
        self.graphical_yellow_coin[int(coin_number) - 1] = self.ludo_game.create_oval(
            100 + (40 * 6) + (40 * 3) + (40 * 4),
            15 + (40 * 8),
            100 + (40 * 6) + (40 * 3) + (40 * 5),
            15 + (40 * 9), fill="yellow",
            width=3)

        self.label_yellow_coin[int(coin_number) - 1].place_forget()
        yellow_start_label_x = 100 + (40 * 6) + (40 * 3) + (40 * 4) + 10
        yellow_start_label_y = 15 + (40 * 8) + 5
        self.label_yellow_coin[int(coin_number) - 1].place(x=yellow_start_label_x,
                                                           y=yellow_start_label_y)

        self.yellow_player_pos[int(coin_number) - 1] = 27
        self.window.update()
        time.sleep(0.2)

    def initial_position_green(self, coin_number):
        self.ludo_game.delete(self.graphical_green_coin[int(coin_number) - 1])
        self.graphical_green_coin[int(coin_number) - 1] = self.ludo_game.create_oval(100 + (40 * 8), 15 + 40,
                                                                                       100 + (40 * 9), 15 + 40 + 40,
                                                                                       fill="#00FF00", width=3)

        self.label_green_coin[int(coin_number) - 1].place_forget()
        green_start_label_x = 100 + (40 * 8) + 10
        green_start_label_y = 15 + 40 + 5
        self.label_green_coin[int(coin_number) - 1].place(x=green_start_label_x, y=green_start_label_y)

        self.green_player_pos[int(coin_number) - 1] = 14
        self.window.update()
        time.sleep(0.2)

    def initial_position_blue(self, coin_number):
        print("graphical_blue_coin:", self.graphical_blue_coin)
        self.ludo_game.delete(self.graphical_blue_coin[int(coin_number) - 1])
        self.graphical_blue_coin[int(coin_number) - 1] = self.ludo_game.create_oval(100 + 240, 340 + (40 * 5) - 5,
                                                                                      100 + 240 + 40,
                                                                                      340 + (40 * 6) - 5,
                                                                                      fill="#04d9ff", width=3)

        self.label_blue_coin[int(coin_number) - 1].place_forget()
        blue_start_label_x = 100 + 240 + 10
        blue_start_label_y = 340 + (40 * 5) - 5 + 5
        self.label_blue_coin[int(coin_number) - 1].place(x=blue_start_label_x, y=blue_start_label_y)

        self.blue_player_pos[int(coin_number) - 1] = 40
        self.window.update()
        time.sleep(0.2)

    def coin_traversal(self, coin_position, current_coin, coin_num_label, coin_num_label_x, coin_num_label_y,
                       color_coin,
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

                    coin_position = self.movement_controller(current_coin, coin_num_label,
                                                             coin_num_label_x, coin_num_label_y, dice_value,
                                                             coin_position,
                                                             color_coin)

                    if coin_position == 106:

                        if self.check_if_bot == 1 and color_coin == "red":
                            messagebox.showinfo("Coin is Home",
                                                "Coin is Home")
                        else:
                            messagebox.showinfo("Coin is Home",
                                                "Coin is Home")
                        if dice_value == 6:
                            self.turn_after_six = 1
                        else:
                            self.clock_counter -= 1
                    break

                coin_position += 1
                dice_value -= 1
                coin_num_label.place_forget()

                if coin_position <= 5:
                    self.ludo_game.move(current_coin, 40, 0)
                    coin_num_label_x += 40
                elif coin_position == 6:
                    self.ludo_game.move(current_coin, 40, -40)
                    coin_num_label_x += 40
                    coin_num_label_y -= 40
                elif 6 < coin_position <= 11:
                    self.ludo_game.move(current_coin, 0, -40)
                    coin_num_label_y -= 40
                elif coin_position <= 13:
                    self.ludo_game.move(current_coin, 40, 0)
                    coin_num_label_x += 40
                elif coin_position <= 18:
                    self.ludo_game.move(current_coin, 0, 40)
                    coin_num_label_y += 40
                elif coin_position == 19:
                    self.ludo_game.move(current_coin, 40, 40)
                    coin_num_label_x += 40
                    coin_num_label_y += 40
                elif coin_position <= 24:
                    self.ludo_game.move(current_coin, 40, 0)
                    coin_num_label_x += 40
                elif coin_position <= 26:
                    self.ludo_game.move(current_coin, 0, 40)
                    coin_num_label_y += 40
                elif coin_position <= 31:
                    self.ludo_game.move(current_coin, -40, 0)
                    coin_num_label_x -= 40
                elif coin_position == 32:
                    self.ludo_game.move(current_coin, -40, 40)
                    coin_num_label_x -= 40
                    coin_num_label_y += 40
                elif coin_position <= 37:
                    self.ludo_game.move(current_coin, 0, 40)
                    coin_num_label_y += 40
                elif coin_position <= 39:
                    self.ludo_game.move(current_coin, -40, 0)
                    coin_num_label_x -= 40
                elif coin_position <= 44:
                    self.ludo_game.move(current_coin, 0, -40)
                    coin_num_label_y -= 40
                elif coin_position == 45:
                    self.ludo_game.move(current_coin, -40, -40)
                    coin_num_label_x -= 40
                    coin_num_label_y -= 40
                elif coin_position <= 50:
                    self.ludo_game.move(current_coin, -40, 0)
                    coin_num_label_x -= 40
                elif 50 < coin_position <= 52:
                    self.ludo_game.move(current_coin, 0, -40)
                    coin_num_label_y -= 40
                elif coin_position == 53:
                    self.ludo_game.move(current_coin, 40, 0)
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
            self.ludo_game.move(current_coin, 0, -40)
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
            self.ludo_game.move(current_coin, 0, 40)
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
            self.ludo_game.move(current_coin, 40, 0)
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
            self.ludo_game.move(current_coin, -40, 0)
            coin_num_label_x -= 40
            coin_num_label.place(x=coin_num_label_x, y=coin_num_label_y)
            self.window.update()
            time.sleep(0.2)
        return current_pos

    ### Killing the Opponent player

    def player_elimination(self, coin_position, coin_color, check_twice_six_turn):
        if coin_color != "red":
            for coin_index_coin_number in range(len(self.red_coin_start_pos)):
                if self.red_coin_start_pos[coin_index_coin_number] == coin_position:
                    if check_twice_six_turn == 6:
                        self.turn_after_six = 1
                    else:
                        self.clock_counter -= 1

                    self.ludo_game.delete(self.graphical_red_coin[coin_index_coin_number])
                    self.label_red_coin[coin_index_coin_number].place_forget()
                    self.red_player_pos[coin_index_coin_number] = -1
                    self.red_coin_start_pos[coin_index_coin_number] = -1
                    if self.check_if_bot == 1:
                        self.bot_value_pos.remove(coin_index_coin_number + 1)
                        if self.red_player_pos.count(-1) >= 1:
                            self.calculate_bot_turns = 2

                    if coin_index_coin_number == 0:
                        coin_recreate = self.ludo_game.create_oval(100 + 40, 15 + 40, 100 + 40 + 40, 15 + 40 + 40,
                                                                     width=3, fill="red", outline="black")
                        self.label_red_coin[coin_index_coin_number].place(x=100 + 40 + 10, y=15 + 40 + 5)
                    elif coin_index_coin_number == 1:
                        coin_recreate = self.ludo_game.create_oval(100 + 40 + 60 + 60, 15 + 40,
                                                                     100 + 40 + 60 + 60 + 40,
                                                                     15 + 40 + 40, width=3, fill="red", outline="black")
                        self.label_red_coin[coin_index_coin_number].place(x=100 + 40 + 60 + 60 + 10, y=15 + 40 + 5)
                    elif coin_index_coin_number == 2:
                        coin_recreate = self.ludo_game.create_oval(100 + 40 + 60 + 60, 15 + 40 + 100,
                                                                     100 + 40 + 60 + 60 + 40, 15 + 40 + 40 + 100,
                                                                     width=3,
                                                                     fill="red", outline="black")
                        self.label_red_coin[coin_index_coin_number].place(x=100 + 40 + 60 + 60 + 10,
                                                                          y=15 + 40 + 100 + 5)
                    else:
                        coin_recreate = self.ludo_game.create_oval(100 + 40, 15 + 40 + 100, 100 + 40 + 40,
                                                                     15 + 40 + 40 + 100, width=3, fill="red",
                                                                     outline="black")
                        self.label_red_coin[coin_index_coin_number].place(x=100 + 40 + 10, y=15 + 40 + 100 + 5)

                    self.graphical_red_coin[coin_index_coin_number] = coin_recreate

        if coin_color != "green":
            for coin_index_coin_number in range(len(self.green_coin_start_pos)):
                if self.green_coin_start_pos[coin_index_coin_number] == coin_position:
                    if check_twice_six_turn == 6:
                        self.turn_after_six = 1
                    else:
                        self.clock_counter -= 1

                    self.ludo_game.delete(self.graphical_green_coin[coin_index_coin_number])
                    self.label_green_coin[coin_index_coin_number].place_forget()
                    self.green_player_pos[coin_index_coin_number] = -1
                    self.green_coin_start_pos[coin_index_coin_number] = -1

                    if coin_index_coin_number == 0:
                        coin_recreate = self.ludo_game.create_oval(340 + (40 * 3) + 40, 15 + 40,
                                                                     340 + (40 * 3) + 40 + 40, 15 + 40 + 40, width=3,
                                                                     fill="#00FF00", outline="black")
                        self.label_green_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 5)
                    elif coin_index_coin_number == 1:
                        coin_recreate = self.ludo_game.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40,
                                                                     340 + (40 * 3) + 40 + 60 + 40 + 40 + 20,
                                                                     15 + 40 + 40, width=3, fill="#00FF00",
                                                                     outline="black")
                        self.label_green_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30,
                                                                            y=15 + 40 + 5)
                    elif coin_index_coin_number == 2:
                        coin_recreate = self.ludo_game.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40 + 100,
                                                                     340 + (40 * 3) + 40 + 60 + 40 + 40 + 20,
                                                                     15 + 40 + 40 + 100, width=3, fill="#00FF00",
                                                                     outline="black")
                        self.label_green_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30,
                                                                            y=15 + 40 + 100 + 5)
                    else:
                        coin_recreate = self.ludo_game.create_oval(340 + (40 * 3) + 40, 15 + 40 + 100,
                                                                     340 + (40 * 3) + 40 + 40, 15 + 40 + 40 + 100,
                                                                     width=3, fill="#00FF00", outline="black")
                        self.label_green_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 10,
                                                                            y=15 + 40 + 100 + 5)

                    self.graphical_green_coin[coin_index_coin_number] = coin_recreate

        if coin_color != "yellow":
            for coin_index_coin_number in range(len(self.yellow_coin_start_pos)):
                if self.yellow_coin_start_pos[coin_index_coin_number] == coin_position:
                    if check_twice_six_turn == 6:
                        self.turn_after_six = 1
                    else:
                        self.clock_counter -= 1

                    self.ludo_game.delete(self.graphical_yellow_coin[coin_index_coin_number])
                    self.label_yellow_coin[coin_index_coin_number].place_forget()
                    self.yellow_player_pos[coin_index_coin_number] = -1
                    self.yellow_coin_start_pos[coin_index_coin_number] = -1

                    if coin_index_coin_number == 0:
                        coin_recreate = self.ludo_game.create_oval(340 + (40 * 3) + 40, 340 + 80 + 15,
                                                                     340 + (40 * 3) + 40 + 40, 340 + 80 + 40 + 15,
                                                                     width=3, fill="yellow", outline="black")
                        self.label_yellow_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 10,
                                                                             y=30 + (40 * 6) + (40 * 3) + 40 + 10)
                    elif coin_index_coin_number == 1:
                        coin_recreate = self.ludo_game.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340 + 80 + 15,
                                                                     340 + (40 * 3) + 40 + 60 + 40 + 40 + 20,
                                                                     340 + 80 + 40 + 15, width=3, fill="yellow",
                                                                     outline="black")
                        self.label_yellow_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30,
                                                                             y=30 + (40 * 6) + (40 * 3) + 40 + 10)
                    elif coin_index_coin_number == 2:
                        coin_recreate = self.ludo_game.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20,
                                                                     340 + 80 + 60 + 40 + 15,
                                                                     340 + (40 * 3) + 40 + 60 + 40 + 40 + 20,
                                                                     340 + 80 + 60 + 40 + 40 + 15, width=3,
                                                                     fill="yellow",
                                                                     outline="black")
                        self.label_yellow_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 40 + 60 + 30,
                                                                             y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)
                    else:
                        coin_recreate = self.ludo_game.create_oval(340 + (40 * 3) + 40, 340 + 80 + 60 + 40 + 15,
                                                                     340 + (40 * 3) + 40 + 40,
                                                                     340 + 80 + 60 + 40 + 40 + 15, width=3,
                                                                     fill="yellow",
                                                                     outline="black")
                        self.label_yellow_coin[coin_index_coin_number].place(x=340 + (40 * 3) + 40 + 10,
                                                                             y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)

                    self.graphical_yellow_coin[coin_index_coin_number] = coin_recreate

        if coin_color != "blue":
            for coin_index_coin_number in range(len(self.blue_coin_start_pos)):
                if self.blue_coin_start_pos[coin_index_coin_number] == coin_position:
                    if check_twice_six_turn == 6:
                        self.turn_after_six = 1
                    else:
                        self.clock_counter -= 1

                    self.ludo_game.delete(self.graphical_blue_coin[coin_index_coin_number])
                    self.label_blue_coin[coin_index_coin_number].place_forget()
                    self.blue_player_pos[coin_index_coin_number] = -1
                    self.blue_coin_start_pos[coin_index_coin_number] = -1

                    if coin_index_coin_number == 0:
                        coin_recreate = self.ludo_game.create_oval(100 + 40, 340 + 80 + 15, 100 + 40 + 40,
                                                                     340 + 80 + 40 + 15, width=3, fill="#04d9ff",
                                                                     outline="black")
                        self.label_blue_coin[coin_index_coin_number].place(x=100 + 40 + 10,
                                                                           y=30 + (40 * 6) + (40 * 3) + 40 + 10)
                    elif coin_index_coin_number == 1:
                        coin_recreate = self.ludo_game.create_oval(100 + 40 + 60 + 40 + 20, 340 + 80 + 15,
                                                                     100 + 40 + 60 + 40 + 40 + 20, 340 + 80 + 40 + 15,
                                                                     width=3, fill="#04d9ff", outline="black")
                        self.label_blue_coin[coin_index_coin_number].place(x=100 + 40 + 60 + 60 + 10,
                                                                           y=30 + (40 * 6) + (40 * 3) + 40 + 10)
                    elif coin_index_coin_number == 2:
                        coin_recreate = self.ludo_game.create_oval(100 + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15,
                                                                     100 + 40 + 60 + 40 + 40 + 20,
                                                                     340 + 80 + 60 + 40 + 40 + 15, width=3,
                                                                     fill="#04d9ff", outline="black")
                        self.label_blue_coin[coin_index_coin_number].place(x=100 + 40 + 60 + 60 + 10,
                                                                           y=30 + (40 * 6) + (
                                                                                   40 * 3) + 40 + 60 + 40 + 10)
                    else:
                        coin_recreate = self.ludo_game.create_oval(100 + 40, 340 + 80 + 60 + 40 + 15, 100 + 40 + 40,
                                                                     340 + 80 + 60 + 40 + 40 + 15, width=3,
                                                                     fill="#04d9ff", outline="black")
                        self.label_blue_coin[coin_index_coin_number].place(x=100 + 40 + 10, y=30 + (40 * 6) + (
                                40 * 3) + 40 + 60 + 40 + 10)

                    self.graphical_blue_coin[coin_index_coin_number] = coin_recreate

    def win_state_manager(self, color_coin):
        coins_home = 0  # Check for all specific color coins
        if color_coin == "red":
            coins_list = self.red_coin_start_pos
            index_pos = 0  # Player index
        elif color_coin == "green":
            coins_list = self.green_coin_start_pos
            index_pos = 3  # Player index
        elif color_coin == "yellow":
            coins_list = self.yellow_coin_start_pos
            index_pos = 2  # Player index
        else:
            coins_list = self.blue_coin_start_pos
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
                self.first_winner = [color_coin, "Winner of the Game"]
                if self.check_if_bot == 1 and color_coin == "red":
                    string1 = color_coin + "  Winner of the Game"
                    messagebox.showinfo(string1, string1)
                else:
                    string1 = color_coin + "  Winner of the Game"
                    messagebox.showinfo(string1, string1)
            elif self.destination_coin_tracker == 2:
                string2 = color_coin + "  1st Runner Up of the Game"
                if self.check_if_bot == 1 and color_coin == "red":
                    messagebox.showinfo(string2, string2)
                else:
                    messagebox.showinfo(string2, string2)
            elif self.destination_coin_tracker == 3:
                string3 = color_coin + "  2nd Runner Up of the Game"
                if self.check_if_bot == 1 and color_coin == "red":
                    messagebox.showinfo(string3, string3)
                else:
                    messagebox.showinfo(string3, string3)

            self.roll_predict_coins[index_pos][1]['state'] = DISABLED
            self.total_people_play.remove(index_pos)

            if len(self.total_people_play) == 1:
                string4 = "Better Luck Next Time"
                messagebox.showinfo(string4)
                self.roll_predict_coins[0][1]['state'] = DISABLED
                return False
            else:
                self.clock_counter -= 1
        else:
            print("No Winner")

        return True

    def bot_operations(self, bot_op_value="give"):
        if bot_op_value == "give":
            coins_inside = 1
            for i in range(4):
                if self.red_player_pos[i] == -1:
                    coins_inside = 1
                else:
                    coins_inside = 0
                    break

            if coins_inside == 1:
                if self.red_coin_tracker == 6:
                    guessed_coin = choice([1, 2, 3, 4])
                    self.bot_value_pos.append(guessed_coin)
                    self.game_manager("red", guessed_coin)
                else:
                    pass
            else:
                crnt_val = self.red_player_pos
                coin_index_ref = self.blue_player_pos

                if len(self.bot_value_pos) == 1:
                    if self.red_coin_tracker < 6:
                        if (self.calculate_bot_turns > 3) and (
                                33 <= crnt_val[self.bot_value_pos[0] - 1] <= 38):
                            self.calculate_bot_turns = 2
                        self.game_manager("red", self.bot_value_pos[0])
                    else:
                        enable_fwd = 0
                        for coin in coin_index_ref:
                            if -1 < coin < 101:
                                if (coin != 40 or coin != 35 or coin != 27 or coin != 22 or coin != 14 or coin != 9 or
                                    coin != 1 or coin != 48) \
                                        and 6 <= coin - crnt_val[self.bot_value_pos[0] - 1] <= 12:
                                    enable_fwd = 1
                                    break
                                else:
                                    enable_fwd = 0
                            else:
                                enable_fwd = 0

                        if enable_fwd == 0:
                            bot_coins = [1, 2, 3, 4]
                            bot_coins.remove(self.bot_value_pos[0])
                            guessed_coin = choice(bot_coins)
                            self.bot_value_pos.append(guessed_coin)
                            self.game_manager("red", guessed_coin)
                        else:
                            self.game_manager("red", self.bot_value_pos[0])
                else:
                    def normal_movement_according_condition():

                        normal_movement = 1

                        for coin in self.bot_value_pos:
                            if crnt_val[coin - 1] + self.red_coin_tracker <= 106:
                                print("Game running")
                            else:
                                normal_movement = 0
                                break

                        if normal_movement:
                            bot_values = [coin for coin in self.bot_value_pos]
                        else:
                            bot_values = [coin for coin in self.bot_value_pos if
                                          crnt_val[coin - 1] + self.red_coin_tracker <= 106]

                        for coin in bot_values:
                            if len(bot_values) > 1 and crnt_val[coin - 1] < 101:
                                if (crnt_val[coin - 1] in coin_index_ref) and (
                                        crnt_val[coin - 1] != 1 or crnt_val[coin - 1] != 9 or crnt_val[
                                    coin - 1] != 14 or crnt_val[
                                            coin - 1] != 22 or crnt_val[coin - 1] != 27 or crnt_val[coin - 1] != 35 or
                                        crnt_val[
                                            coin - 1] != 40 or crnt_val[coin - 1] != 48):
                                    bot_values.remove(coin)
                                elif crnt_val[coin - 1] <= 39 and crnt_val[coin - 1] + self.red_coin_tracker > 39:
                                    for loc_coin_other in coin_index_ref:
                                        if (40 <= loc_coin_other <= 46) and (
                                                crnt_val[coin - 1] + self.red_coin_tracker > loc_coin_other):
                                            bot_values.remove(coin)
                                            break

                        fwd_permit = 1
                        for coin in bot_values:
                            if crnt_val[coin - 1] + self.red_coin_tracker in coin_index_ref:
                                fwd_permit = 0
                                self.game_manager("red", coin)
                                break
                        if fwd_permit:
                            coin_index_len = len(bot_values)
                            bot_coins = {}
                            if coin_index_ref:
                                for bot in bot_values:
                                    for coin_other in coin_index_ref:
                                        if coin_other > -1 and coin_other < 100:
                                            if coin_index_len > 1 and (crnt_val[bot - 1] > 38 and coin_other <= 38) or \
                                                    ((crnt_val[bot - 1] == 9 or crnt_val[bot - 1] == 14 or crnt_val[
                                                        bot - 1] == 27 or
                                                      crnt_val[bot - 1] == 35 or crnt_val[bot - 1] == 40 or crnt_val[
                                                          bot - 1] == 48 or
                                                      crnt_val[bot - 1] == 22) and
                                                     (coin_other <= crnt_val[bot - 1] or
                                                      (crnt_val[bot - 1] < coin_other <=
                                                       crnt_val[bot - 1] + 3))):
                                                coin_index_len -= 1
                                            else:
                                                bot_coins[crnt_val[bot - 1] - coin_other] = \
                                                    (bot, coin_index_ref.index(coin_other) + 1)
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
                                bot_postve_position = 0
                                coin_index_len = len(bot_coins_positive_dis)
                                new_positive_index = -1

                                while coin_index_len:
                                    if coin_index_min and coin_index_min[0] <= 6:

                                        bot_postve_position = 1
                                        self.game_manager("red", coin_index_min[1][0])
                                        break
                                    else:
                                        new_positive_index -= 1
                                        try:
                                            coin_index_min = min(
                                                sorted(bot_coins_positive_dis.items())[new_positive_index])
                                        except:
                                            break
                                    coin_index_len -= 1
                                bot_neg_position = 0
                                if not bot_postve_position:
                                    coin_index_len = len(bot_coins_negative_dis)
                                    new_positive_index = len(bot_coins_negative_dis) - 1
                                    while coin_index_len:
                                        if coin_index_max and crnt_val[
                                            coin_index_max[1][0] - 1] + self.red_coin_tracker <= \
                                                coin_index_ref[coin_index_max[1][1] - 1]:
                                            bot_neg_position = 1
                                            self.game_manager("red", coin_index_max[1][0])
                                            break
                                        else:
                                            new_positive_index -= 1
                                            try:
                                                coin_index_max = max(
                                                    sorted(bot_coins_negative_dis.items())[new_positive_index])
                                            except:
                                                break
                                        coin_index_len -= 1
                                if not bot_neg_position and not bot_postve_position:
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

                        for coin in self.bot_value_pos:
                            if crnt_val[coin - 1] + self.red_coin_tracker in self.blue_player_pos:
                                coin_proceed = coin
                                break

                        if not coin_proceed:
                            if -1 in self.red_player_pos:
                                coins_list = [1, 2, 3, 4]
                                for coin in self.bot_value_pos:
                                    coins_list.remove(coin)
                                coin_values_prediction = choice(coins_list)
                                self.bot_value_pos.append(coin_values_prediction)
                                self.game_manager("red", coin_values_prediction)
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
