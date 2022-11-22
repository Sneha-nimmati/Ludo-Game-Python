from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
from random import randint, choice


class Ludo:
    def __init__(self, root, six_side_block, five_side_block, four_side_block, three_side_block, two_side_block,
                 one_side_block):
        self.window = root
        
        self.make_canvas = Canvas(self.window, bg="#E9C67F", width=800, height=630)
        self.make_canvas.pack(fill=BOTH, expand=1)

       
        self.made_red_coin = []
        self.made_green_coin = []
        self.made_yellow_coin = []
        self.made_sky_blue_coin = []

        self.red_number_label = []
        self.green_number_label = []
        self.yellow_number_label = []
        self.sky_blue_number_label = []

        self.block_value_predict = []
        self.total_people_play = []

        self.block_number_side = [one_side_block, two_side_block, three_side_block, four_side_block, five_side_block,
                                  six_side_block]

        
        self.red_coord_store = [-1, -1, -1, -1]
        self.green_coord_store = [-1, -1, -1, -1]
        self.yellow_coord_store = [-1, -1, -1, -1]
        self.sky_blue_coord_store = [-1, -1, -1, -1]

        self.red_coin_position = [0, 1, 2, 3]
        self.green_coin_position = [0, 1, 2, 3]
        self.yellow_coin_position = [0, 1, 2, 3]
        self.sky_blue_coin_position = [0, 1, 2, 3]

        for index in range(len(self.red_coin_position)): 
            self.red_coin_position[index] = -1
            self.green_coin_position[index] = -1
            self.yellow_coin_position[index] = -1
            self.sky_blue_coin_position[index] = -1

       
        self.move_red_counter = 0
        self.move_green_counter = 0
        self.move_yellow_counter = 0
        self.move_sky_blue_counter = 0

        self.take_permission = 0
        self.six_with_overlap = 0

        self.red_store_active = 0
        self.sky_blue_store_active = 0
        self.yellow_store_active = 0
        self.green_store_active = 0

        self.six_counter = 0
        self.time_for = -1

        self.right_star = None
        self.down_star = None
        self.left_star = None
        self.up_star = None

        
        self.robo_prem = 0
        self.count_robo_stage_from_start = 0
        self.robo_store = []

       
        self.board_set_up()

        self.instruction_btn_red()
        self.instruction_btn_sky_blue()
       

        self.take_initial_control()

    def board_set_up(self):
        
        self.make_canvas.create_rectangle(100, 15, 100 + (40 * 15), 15 + (40 * 15), width=6, fill="white")

       
        self.make_canvas.create_rectangle(100, 15, 100 + 240, 15 + 240, width=3, fill="red")  # left up large square
        self.make_canvas.create_rectangle(100, (15 + 240) + (40 * 3), 100 + 240, (15 + 240) + (40 * 3) + (40 * 6),
                                          width=3, fill="#04d9ff")  # left down large square
        self.make_canvas.create_rectangle(340 + (40 * 3), 15, 340 + (40 * 3) + (40 * 6), 15 + 240, width=3,
                                          fill="#00FF00")  # right up large square
        self.make_canvas.create_rectangle(340 + (40 * 3), (15 + 240) + (40 * 3), 340 + (40 * 3) + (40 * 6),
                                          (15 + 240) + (40 * 3) + (40 * 6), width=3,
                                          fill="yellow")  # right down large square

       
        self.make_canvas.create_rectangle(100, (15 + 240), 100 + 240, (15 + 240) + 40, width=3)
        self.make_canvas.create_rectangle(100 + 40, (15 + 240) + 40, 100 + 240, (15 + 240) + 40 + 40, width=3,
                                          fill="#F00000")
        self.make_canvas.create_rectangle(100, (15 + 240) + 80, 100 + 240, (15 + 240) + 80 + 40, width=3)

       
        self.make_canvas.create_rectangle(100 + 240, 15, 100 + 240 + 40, 15 + (40 * 6), width=3)
        self.make_canvas.create_rectangle(100 + 240 + 40, 15 + 40, 100 + 240 + 80, 15 + (40 * 6), width=3,
                                          fill="#00FF00")
        self.make_canvas.create_rectangle(100 + 240 + 80, 15, 100 + 240 + 80 + 40, 15 + (40 * 6), width=3)

        
        self.make_canvas.create_rectangle(340 + (40 * 3), 15 + 240, 340 + (40 * 3) + (40 * 6), 15 + 240 + 40, width=3)
        self.make_canvas.create_rectangle(340 + (40 * 3), 15 + 240 + 40, 340 + (40 * 3) + (40 * 6) - 40, 15 + 240 + 80,
                                          width=3, fill="yellow")
        self.make_canvas.create_rectangle(340 + (40 * 3), 15 + 240 + 80, 340 + (40 * 3) + (40 * 6), 15 + 240 + 120,
                                          width=3)

        
        self.make_canvas.create_rectangle(100, (15 + 240) + (40 * 3), 100 + 240 + 40, (15 + 240) + (40 * 3) + (40 * 6),
                                          width=3)
        self.make_canvas.create_rectangle(100 + 240 + 40, (15 + 240) + (40 * 3), 100 + 240 + 40 + 40,
                                          (15 + 240) + (40 * 3) + (40 * 6) - 40, width=3, fill="#04d9ff")
        self.make_canvas.create_rectangle(100 + 240 + 40 + 40, (15 + 240) + (40 * 3), 100 + 240 + 40 + 40 + 40,
                                          (15 + 240) + (40 * 3) + (40 * 6), width=3)

        
        start_x = 100 + 40
        start_y = 15 + 240
        end_x = 100 + 40
        end_y = 15 + 240 + (40 * 3)
        for _ in range(5):
            self.make_canvas.create_line(start_x, start_y, end_x, end_y, width=3)
            start_x += 40
            end_x += 40

       
        start_x = 100 + 240 + (40 * 3) + 40
        start_y = 15 + 240
        end_x = 100 + 240 + (40 * 3) + 40
        end_y = 15 + 240 + (40 * 3)
        for _ in range(5):
            self.make_canvas.create_line(start_x, start_y, end_x, end_y, width=3)
            start_x += 40
            end_x += 40

        
        start_x = 100 + 240
        start_y = 15 + 40
        end_x = 100 + 240 + (40 * 3)
        end_y = 15 + 40
        for _ in range(5):
            self.make_canvas.create_line(start_x, start_y, end_x, end_y, width=3)
            start_y += 40
            end_y += 40

        
        start_x = 100 + 240
        start_y = 15 + (40 * 6) + (40 * 3) + 40
        end_x = 100 + 240 + (40 * 3)
        end_y = 15 + (40 * 6) + (40 * 3) + 40
        for _ in range(5):
            self.make_canvas.create_line(start_x, start_y, end_x, end_y, width=3)
            start_y += 40
            end_y += 40

        
        self.make_canvas.create_rectangle(100 + 20, 15 + 40 - 20, 100 + 40 + 60 + 40 + 60 + 20,
                                          15 + 40 + 40 + 40 + 100 - 20, width=3, fill="white")
        self.make_canvas.create_rectangle(340 + (40 * 3) + 40 - 20, 15 + 40 - 20,
                                          340 + (40 * 3) + 40 + 60 + 40 + 40 + 20 + 20, 15 + 40 + 40 + 40 + 100 - 20,
                                          width=3, fill="white")
        self.make_canvas.create_rectangle(100 + 20, 340 + 80 - 20 + 15, 100 + 40 + 60 + 40 + 60 + 20,
                                          340 + 80 + 60 + 40 + 40 + 20 + 15, width=3, fill="white")
        self.make_canvas.create_rectangle(340 + (40 * 3) + 40 - 20, 340 + 80 - 20 + 15,
                                          340 + (40 * 3) + 40 + 60 + 40 + 40 + 20 + 20,
                                          340 + 80 + 60 + 40 + 40 + 20 + 15, width=3, fill="white")

    
        self.make_canvas.create_rectangle(100 + 40, 15 + 40, 100 + 40 + 40, 15 + 40 + 40, width=3, fill="red")
        self.make_canvas.create_rectangle(100 + 40 + 60 + 60, 15 + 40, 100 + 40 + 60 + 40 + 60, 15 + 40 + 40, width=3,
                                          fill="red")
        self.make_canvas.create_rectangle(100 + 40, 15 + 40 + 100, 100 + 40 + 40, 15 + 40 + 40 + 100, width=3,
                                          fill="red")
        self.make_canvas.create_rectangle(100 + 40 + 60 + 60, 15 + 40 + 100, 100 + 40 + 60 + 40 + 60,
                                          15 + 40 + 40 + 100, width=3, fill="red")

        
        self.make_canvas.create_rectangle(340 + (40 * 3) + 40, 15 + 40, 340 + (40 * 3) + 40 + 40, 15 + 40 + 40, width=3,
                                          fill="#00FF00")
        self.make_canvas.create_rectangle(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40,
                                          340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 15 + 40 + 40, width=3,
                                          fill="#00FF00")
        self.make_canvas.create_rectangle(340 + (40 * 3) + 40, 15 + 40 + 100, 340 + (40 * 3) + 40 + 40,
                                          15 + 40 + 40 + 100, width=3, fill="#00FF00")
        self.make_canvas.create_rectangle(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40 + 100,
                                          340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 15 + 40 + 40 + 100, width=3,
                                          fill="#00FF00")

    
        self.make_canvas.create_rectangle(100 + 40, 340 + 80 + 15, 100 + 40 + 40, 340 + 80 + 40 + 15, width=3,
                                          fill="#04d9ff")
        self.make_canvas.create_rectangle(100 + 40 + 60 + 40 + 20, 340 + 80 + 15, 100 + 40 + 60 + 40 + 40 + 20,
                                          340 + 80 + 40 + 15, width=3, fill="#04d9ff")
        self.make_canvas.create_rectangle(100 + 40, 340 + 80 + 60 + 40 + 15, 100 + 40 + 40,
                                          340 + 80 + 60 + 40 + 40 + 15, width=3, fill="#04d9ff")
        self.make_canvas.create_rectangle(100 + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15,
                                          100 + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15, width=3,
                                          fill="#04d9ff")

        
        self.make_canvas.create_rectangle(340 + (40 * 3) + 40, 340 + 80 + 15, 340 + (40 * 3) + 40 + 40,
                                          340 + 80 + 40 + 15, width=3, fill="yellow")
        self.make_canvas.create_rectangle(340 + (40 * 3) + 40 + 60 + 40 + 20, 340 + 80 + 15,
                                          340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 340 + 80 + 40 + 15, width=3,
                                          fill="yellow")
        self.make_canvas.create_rectangle(340 + (40 * 3) + 40, 340 + 80 + 60 + 40 + 15, 340 + (40 * 3) + 40 + 40,
                                          340 + 80 + 60 + 40 + 40 + 15, width=3, fill="yellow")
        self.make_canvas.create_rectangle(340 + (40 * 3) + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15,
                                          340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15,
                                          width=3, fill="yellow")

        
        self.make_canvas.create_rectangle(100 + 240, 340 + (40 * 5) - 5, 100 + 240 + 40, 340 + (40 * 6) - 5,
                                          fill="#04d9ff", width=3)
        
        self.make_canvas.create_rectangle(100 + 40, 15 + (40 * 6), 100 + 40 + 40, 15 + (40 * 6) + 40, fill="red",
                                          width=3)
        
        self.make_canvas.create_rectangle(100 + (40 * 8), 15 + 40, 100 + (40 * 9), 15 + 40 + 40, fill="#00FF00",
                                          width=3)
        
        self.make_canvas.create_rectangle(100 + (40 * 6) + (40 * 3) + (40 * 4), 15 + (40 * 8),
                                          100 + (40 * 6) + (40 * 3) + (40 * 5), 15 + (40 * 9), fill="yellow", width=3)

       
        self.make_canvas.create_polygon(100 + 240, 15 + 240, 100 + 240 + 60, 15 + 240 + 60, 100 + 240,
                                        15 + 240 + (40 * 3), width=3, fill="red", outline="black")
        self.make_canvas.create_polygon(100 + 240 + (40 * 3), 15 + 240, 100 + 240 + 60, 15 + 240 + 60,
                                        100 + 240 + (40 * 3), 15 + 240 + (40 * 3), width=3, fill="yellow",
                                        outline="black")
        self.make_canvas.create_polygon(100 + 240, 15 + 240, 100 + 240 + 60, 15 + 240 + 60, 100 + 240 + (40 * 3),
                                        15 + 240, width=3, fill="#00FF00", outline="black")
        self.make_canvas.create_polygon(100 + 240, 15 + 240 + (40 * 3), 100 + 240 + 60, 15 + 240 + 60,
                                        100 + 240 + (40 * 3), 15 + 240 + (40 * 3), width=3, fill="#04d9ff",
                                        outline="black")

        
        red_1_coin = self.make_canvas.create_oval(100 + 40, 15 + 40, 100 + 40 + 40, 15 + 40 + 40, width=3, fill="red",
                                                  outline="black")
        red_2_coin = self.make_canvas.create_oval(100 + 40 + 60 + 60, 15 + 40, 100 + 40 + 60 + 60 + 40, 15 + 40 + 40,
                                                  width=3, fill="red", outline="black")
        red_3_coin = self.make_canvas.create_oval(100 + 40 + 60 + 60, 15 + 40 + 100, 100 + 40 + 60 + 60 + 40,
                                                  15 + 40 + 40 + 100, width=3, fill="red", outline="black")
        red_4_coin = self.make_canvas.create_oval(100 + 40, 15 + 40 + 100, 100 + 40 + 40, 15 + 40 + 40 + 100, width=3,
                                                  fill="red", outline="black")
        self.made_red_coin.append(red_1_coin)
        self.made_red_coin.append(red_2_coin)
        self.made_red_coin.append(red_3_coin)
        self.made_red_coin.append(red_4_coin)

       
        red_1_label = Label(self.make_canvas, text="1", font=("Arial", 15, "bold"), bg="red", fg="black")
        red_1_label.place(x=100 + 40 + 10, y=15 + 40 + 5)
        red_2_label = Label(self.make_canvas, text="2", font=("Arial", 15, "bold"), bg="red", fg="black")
        red_2_label.place(x=100 + 40 + 60 + 60 + 10, y=15 + 40 + 5)
        red_3_label = Label(self.make_canvas, text="3", font=("Arial", 15, "bold"), bg="red", fg="black")
        red_3_label.place(x=100 + 40 + 60 + 60 + 10, y=15 + 40 + 100 + 5)
        red_4_label = Label(self.make_canvas, text="4", font=("Arial", 15, "bold"), bg="red", fg="black")
        red_4_label.place(x=100 + 40 + 10, y=15 + 40 + 100 + 5)
        self.red_number_label.append(red_1_label)
        self.red_number_label.append(red_2_label)
        self.red_number_label.append(red_3_label)
        self.red_number_label.append(red_4_label)

        
        green_1_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40, 15 + 40, 340 + (40 * 3) + 40 + 40,
                                                    15 + 40 + 40, width=3, fill="#00FF00", outline="black")
        green_2_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40,
                                                    340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 15 + 40 + 40, width=3,
                                                    fill="#00FF00", outline="black")
        green_3_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40 + 100,
                                                    340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 15 + 40 + 40 + 100,
                                                    width=3, fill="#00FF00", outline="black")
        green_4_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40, 15 + 40 + 100, 340 + (40 * 3) + 40 + 40,
                                                    15 + 40 + 40 + 100, width=3, fill="#00FF00", outline="black")
        self.made_green_coin.append(green_1_coin)
        self.made_green_coin.append(green_2_coin)
        self.made_green_coin.append(green_3_coin)
        self.made_green_coin.append(green_4_coin)

     
        green_1_label = Label(self.make_canvas, text="1", font=("Arial", 15, "bold"), bg="#00FF00", fg="black")
        green_1_label.place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 5)
        green_2_label = Label(self.make_canvas, text="2", font=("Arial", 15, "bold"), bg="#00FF00", fg="black")
        green_2_label.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 5)
        green_3_label = Label(self.make_canvas, text="3", font=("Arial", 15, "bold"), bg="#00FF00", fg="black")
        green_3_label.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 100 + 5)
        green_4_label = Label(self.make_canvas, text="4", font=("Arial", 15, "bold"), bg="#00FF00", fg="black")
        green_4_label.place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 100 + 5)
        self.green_number_label.append(green_1_label)
        self.green_number_label.append(green_2_label)
        self.green_number_label.append(green_3_label)
        self.green_number_label.append(green_4_label)

        
        sky_blue_1_coin = self.make_canvas.create_oval(100 + 40, 340 + 80 + 15, 100 + 40 + 40, 340 + 80 + 40 + 15,
                                                       width=3, fill="#04d9ff", outline="black")
        sky_blue_2_coin = self.make_canvas.create_oval(100 + 40 + 60 + 40 + 20, 340 + 80 + 15,
                                                       100 + 40 + 60 + 40 + 40 + 20, 340 + 80 + 40 + 15, width=3,
                                                       fill="#04d9ff", outline="black")
        sky_blue_3_coin = self.make_canvas.create_oval(100 + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15,
                                                       100 + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15,
                                                       width=3, fill="#04d9ff", outline="black")
        sky_blue_4_coin = self.make_canvas.create_oval(100 + 40, 340 + 80 + 60 + 40 + 15, 100 + 40 + 40,
                                                       340 + 80 + 60 + 40 + 40 + 15, width=3, fill="#04d9ff",
                                                       outline="black")
        self.made_sky_blue_coin.append(sky_blue_1_coin)
        self.made_sky_blue_coin.append(sky_blue_2_coin)
        self.made_sky_blue_coin.append(sky_blue_3_coin)
        self.made_sky_blue_coin.append(sky_blue_4_coin)

        
        sky_blue_1_label = Label(self.make_canvas, text="1", font=("Arial", 15, "bold"), bg="#04d9ff", fg="black")
        sky_blue_1_label.place(x=100 + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        sky_blue_2_label = Label(self.make_canvas, text="2", font=("Arial", 15, "bold"), bg="#04d9ff", fg="black")
        sky_blue_2_label.place(x=100 + 40 + 60 + 60 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        sky_blue_3_label = Label(self.make_canvas, text="3", font=("Arial", 15, "bold"), bg="#04d9ff", fg="black")
        sky_blue_3_label.place(x=100 + 40 + 60 + 60 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 60 + 40 + 10)
        sky_blue_4_label = Label(self.make_canvas, text="4", font=("Arial", 15, "bold"), bg="#04d9ff", fg="black")
        sky_blue_4_label.place(x=100 + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 60 + 40 + 10)
        self.sky_blue_number_label.append(sky_blue_1_label)
        self.sky_blue_number_label.append(sky_blue_2_label)
        self.sky_blue_number_label.append(sky_blue_3_label)
        self.sky_blue_number_label.append(sky_blue_4_label)

        
        yellow_1_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40, 340 + 80 + 15, 340 + (40 * 3) + 40 + 40,
                                                     340 + 80 + 40 + 15, width=3, fill="yellow", outline="black")
        yellow_2_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340 + 80 + 15,
                                                     340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 340 + 80 + 40 + 15,
                                                     width=3, fill="yellow", outline="black")
        yellow_3_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15,
                                                     340 + (40 * 3) + 40 + 60 + 40 + 40 + 20,
                                                     340 + 80 + 60 + 40 + 40 + 15, width=3, fill="yellow",
                                                     outline="black")
        yellow_4_coin = self.make_canvas.create_oval(340 + (40 * 3) + 40, 340 + 80 + 60 + 40 + 15,
                                                     340 + (40 * 3) + 40 + 40, 340 + 80 + 60 + 40 + 40 + 15, width=3,
                                                     fill="yellow", outline="black")
        self.made_yellow_coin.append(yellow_1_coin)
        self.made_yellow_coin.append(yellow_2_coin)
        self.made_yellow_coin.append(yellow_3_coin)
        self.made_yellow_coin.append(yellow_4_coin)

        # Make coin under number label for yellow right down block
        yellow_1_label = Label(self.make_canvas, text="1", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        yellow_1_label.place(x=340 + (40 * 3) + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        yellow_2_label = Label(self.make_canvas, text="2", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        yellow_2_label.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        yellow_3_label = Label(self.make_canvas, text="3", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        yellow_3_label.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)
        yellow_4_label = Label(self.make_canvas, text="4", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        yellow_4_label.place(x=340 + (40 * 3) + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)
        self.yellow_number_label.append(yellow_1_label)
        self.yellow_number_label.append(yellow_2_label)
        self.yellow_number_label.append(yellow_3_label)
        self.yellow_number_label.append(yellow_4_label)

      
        
        common_x = 340 + (40 * 6) + 20
        common_y = 15 + 240 + 2
        coord = [common_x, common_y, common_x + 5, common_y + 15, common_x + 15, common_y + 15, common_x + 8,
                 common_y + 20, common_x + 15, common_y + 25, common_x + 5, common_y + 25, common_x, common_y + 25 + 10,
                 common_x - 5, common_y + 25, common_x - 16, common_y + 25, common_x - 8, common_y + 15 + 5,
                 common_x - 15, common_y + 15, common_x - 5, common_y + 15]
        self.make_canvas.create_polygon(coord, width=2, fill="blue")

        
        common_x = 100 + 240 + 2 + 18
        common_y = 15 + (40 * 2) + 2
        coord = [common_x, common_y, common_x + 5, common_y + 15, common_x + 15, common_y + 15, common_x + 8,
                 common_y + 20, common_x + 15, common_y + 25, common_x + 5, common_y + 25, common_x, common_y + 25 + 10,
                 common_x - 5, common_y + 25, common_x - 16, common_y + 25, common_x - 8, common_y + 15 + 5,
                 common_x - 15, common_y + 15, common_x - 5, common_y + 15]
        self.make_canvas.create_polygon(coord, width=2, fill="blue")

        
        common_x = 100 + (40 * 2) + 2 + 18
        common_y = 15 + 240 + (40 * 2) + 2
        coord = [common_x, common_y, common_x + 5, common_y + 15, common_x + 15, common_y + 15, common_x + 8,
                 common_y + 20, common_x + 15, common_y + 25, common_x + 5, common_y + 25, common_x, common_y + 25 + 10,
                 common_x - 5, common_y + 25, common_x - 16, common_y + 25, common_x - 8, common_y + 15 + 5,
                 common_x - 15, common_y + 15, common_x - 5, common_y + 15]
        self.make_canvas.create_polygon(coord, width=2, fill="blue")

        
        common_x = 100 + 240 + (40 * 2) + 2 + 18
        common_y = 15 + (40 * 6) + (40 * 3) + (40 * 3) + 2
        coord = [common_x, common_y, common_x + 5, common_y + 15, common_x + 15, common_y + 15, common_x + 8,
                 common_y + 20, common_x + 15, common_y + 25, common_x + 5, common_y + 25, common_x, common_y + 25 + 10,
                 common_x - 5, common_y + 25, common_x - 16, common_y + 25, common_x - 8, common_y + 15 + 5,
                 common_x - 15, common_y + 15, common_x - 5, common_y + 15]
        self.make_canvas.create_polygon(coord, width=3, fill="blue")

    
    def take_initial_control(self):
        for i in range(2):
            self.block_value_predict[i][1]['state'] = DISABLED

       
        top = Toplevel()
        top.geometry("800x600")
        top.maxsize(800, 600)
        top.minsize(800, 600)
        top.config(bg="white")
        top.iconbitmap("Images/ludo_icon.ico")


        def operate(ind):
            if ind:
                self.robo_prem = 1
                for player_index in range(2):
                    self.total_people_play.append(player_index)
                print(self.total_people_play)

                def delay_with_instrctions(time_is):
                    if place_ins['text'] != "":
                        place_ins.place_forget()
                    if command_play['text'] != "":
                        command_play.place_forget()

                    place_ins['text'] = f"  Your game will start within {time_is} sec"
                    place_ins.place(x=250, y=260)

                    if time_is > 5:
                        command_play['text'] = f"             Machine Play With Red and You Play With Sky Blue"
                    elif time_is >= 2 and time_is < 5:
                        command_play['text'] = f"                       You Will Get the First Chance to play"
                    else:
                        command_play['text'] = f"                                      Enjoy this Game               "
                    command_play.place(x=220, y=300)

                time_is = 10
                place_ins = Label(top, text="", font=("Times New Roman", 18, "italic"), fg="black", bg="#F8F7F9")
                command_play = Label(top, text="", font=("Times New Roman", 12, "italic"), fg="black", bg="#F8F7F9")

                try:
                    while time_is:
                        delay_with_instrctions(time_is)
                        time_is -= 1
                        self.window.update()
                        time.sleep(1)
                    top.destroy()
                except:
                    print("Force Stop Error in Operate")
                self.block_value_predict[1][1]['state'] = NORMAL

        mvc_btn = Button(top, text="Play With Computer", bg="#2B4AF7", fg="#FCFCFD", font=("Times New Roman", 16, "bold"),
                         relief=RAISED, bd=3, command=lambda: operate(1), activebackground="#2B4AF7")
        mvc_btn.place(x=300, y=200

        top.mainloop()


        def make_prediction(self, color_indicator):
        try:
            if color_indicator == "red":
                block_value_predict = self.block_value_predict[0]
                if self.robo_prem and self.count_robo_stage_from_start < 3:
                    self.count_robo_stage_from_start += 1
                if self.robo_prem and self.count_robo_stage_from_start == 3 and self.six_counter < 2:
                    permanent_block_number = self.move_red_counter = 6
                    self.count_robo_stage_from_start += 1
                else:
                    permanent_block_number = self.move_red_counter = randint(1, 6)

            elif color_indicator == "sky_blue":
                block_value_predict = self.block_value_predict[1]
                permanent_block_number = self.move_sky_blue_counter = randint(1, 6)
                if self.robo_prem and permanent_block_number == 6:
                    for coin_loc in self.red_coin_position:
                        if 40 <= coin_loc <= 46:
                            permanent_block_number = self.move_sky_blue_counter = randint(1, 5)
                            break


            temp_counter = 12
            while temp_counter > 0:
                move_temp_counter = randint(1, 6)
                block_value_predict[0]['image'] = self.block_number_side[move_temp_counter - 1]
                self.window.update()
                time.sleep(0.1)
                temp_counter -= 1

             print("Prediction result: ", permanent_block_number)

            # Permanent predicted value containing image set
            block_value_predict[0]['image'] = self.block_number_side[permanent_block_number - 1]
            if self.robo_prem == 1 and color_indicator == "red":
                self.window.update()
                time.sleep(0.4)
            self.instructional_btn_customization_based_on_current_situation(color_indicator, permanent_block_number,
                                                                            block_value_predict)
        except:
            print("Force Stop Error in Prediction")

    def instructional_btn_customization_based_on_current_situation(self, color_indicator, permanent_block_number,
                                                                   block_value_predict):
        robo_operator = None
        if color_indicator == "red":
            temp_coin_position = self.red_coin_position
            temp_coin_position = self.sky_blue_coin_position

        all_in = 1
        for i in range(4):
            if temp_coin_position[i] == -1:
                all_in = 1
            else:
                all_in = 0
                break

        if permanent_block_number == 6:
            self.six_counter += 1
        else:
            self.six_counter = 0

        if ((all_in == 1 and permanent_block_number == 6) or (all_in == 0)) and self.six_counter < 3:
            permission = 1
            if color_indicator == "red":
                temp = self.red_coord_store
            elif color_indicator == "green":
                temp = self.green_coord_store
            elif color_indicator == "yellow":
                temp = self.yellow_coord_store
            else:
                temp = self.sky_blue_coord_store

            if permanent_block_number < 6:
                if self.six_with_overlap == 1:
                    self.time_for -= 1
                    self.six_with_overlap = 0
                for i in range(4):
                    if temp[i] == -1:
                        permission = 0
                    elif temp[i] > 100:
                        if temp[i] + permanent_block_number <= 106:
                            permission = 1
                            break
                        else:
                            permission = 0
                    else:
                        permission = 1
                        break
            else:
                for i in range(4):
                    if temp[i] > 100:
                        if temp[i] + permanent_block_number <= 106:
                            permission = 1
                            break
                        else:
                            permission = 0
                    else:
                        permission = 1
                        break
            if permission == 0:
                self.make_command(None)
            else:
                self.num_btns_state_controller(block_value_predict[2])

                if self.robo_prem == 1 and block_value_predict == self.block_value_predict[0]:
                    robo_operator = "give"
                block_value_predict[1]['state'] = DISABLED  # Predict btn deactivation

        else:
            block_value_predict[1]['state'] = NORMAL  # Predict btn activation
            if self.six_with_overlap == 1:
                self.time_for -= 1
                self.six_with_overlap = 0
            self.make_command()

        if permanent_block_number == 6 and self.six_counter < 3 and block_value_predict[2][0]['state'] == NORMAL:
            self.time_for -= 1
        else:
            self.six_counter = 0

        if self.robo_prem == 1 and robo_operator:
            self.robo_judge(robo_operator)

    # Player Scope controller
    def make_command(self, robo_operator=None):
        if self.time_for == -1:
            pass
        else:
            self.block_value_predict[self.total_people_play[self.time_for]][1]['state'] = DISABLED
        if self.time_for == len(self.total_people_play) - 1:
            self.time_for = -1

        self.time_for += 1
        self.block_value_predict[self.total_people_play[self.time_for]][1]['state'] = NORMAL

        if self.robo_prem == 1 and self.time_for == 0:
            robo_operator = "Roll"
        if robo_operator:
            self.robo_judge(robo_operator)

    def instruction_btn_red(self):
        block_predict_red = Label(self.make_canvas, image=self.block_number_side[0])
        block_predict_red.place(x=34, y=15)
        predict_red = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Roll",
                             font=("Arial", 8, "bold"), command=lambda: self.make_prediction("red"))
        predict_red.place(x=25, y=15 + 50)

        btn_1 = Button(self.make_canvas, bg="#262626", fg="#00eb00", text="1", font=("Arial", 13, "bold", "italic"),
                       relief=RAISED, bd=3, command=lambda: self.main_controller("red", '1'), state=DISABLED,
                       disabledforeground="red")
        btn_1.place(x=20, y=15 + 100)
        btn_2 = Button(self.make_canvas, bg="#262626", fg="#00eb00", text="2", font=("Arial", 13, "bold", "italic"),
                       relief=RAISED, bd=3, command=lambda: self.main_controller("red", '2'), state=DISABLED,
                       disabledforeground="red")
        btn_2.place(x=60, y=15 + 100)
        btn_3 = Button(self.make_canvas, bg="#262626", fg="#00eb00", text="3", font=("Arial", 13, "bold", "italic"),
                       relief=RAISED, bd=3, command=lambda: self.main_controller("red", '3'), state=DISABLED,
                       disabledforeground="red")
        btn_3.place(x=20, y=15 + 100 + 40)
        btn_4 = Button(self.make_canvas, bg="#262626", fg="#00eb00", text="4", font=("Arial", 13, "bold", "italic"),
                       relief=RAISED, bd=3, command=lambda: self.main_controller("red", '4'), state=DISABLED,
                       disabledforeground="red")
        btn_4.place(x=60, y=15 + 100 + 40)

        Label(self.make_canvas, text="Player 1", bg="#141414", fg="gold", font=("Arial", 15, "bold")).place(x=15,
                                                                                                            y=15 + 140 + 50)

    def instruction_btn_sky_blue(self):
        block_predict_sky_blue = Label(self.make_canvas, image=self.block_number_side[0])
        block_predict_sky_blue.place(x=34, y=15 + (40 * 6 + 40 * 3) + 10)
        predict_sky_blue = Button(self.make_canvas, bg="black", fg="#00FF00", relief=RAISED, bd=5, text="Roll",
                                  font=("Arial", 8, "bold"), command=lambda: self.make_prediction("sky_blue"))
        predict_sky_blue.place(x=25, y=15 + (40 * 6 + 40 * 3) + 40 + 20)

        btn_1 = Button(self.make_canvas, bg="#262626", fg="#00eb00", text="1", font=("Arial", 13, "bold", "italic"),
                       relief=RAISED, bd=3, command=lambda: self.main_controller("sky_blue", '1'), state=DISABLED,
                       disabledforeground="red")
        btn_1.place(x=20, y=15 + (40 * 6 + 40 * 3) + 40 + 70)
        btn_2 = Button(self.make_canvas, bg="#262626", fg="#00eb00", text="2", font=("Arial", 13, "bold", "italic"),
                       relief=RAISED, bd=3, command=lambda: self.main_controller("sky_blue", '2'), state=DISABLED,
                       disabledforeground="red")
        btn_2.place(x=60, y=15 + (40 * 6 + 40 * 3) + 40 + 70)
        btn_3 = Button(self.make_canvas, bg="#262626", fg="#00eb00", text="3", font=("Arial", 13, "bold", "italic"),
                       relief=RAISED, bd=3, command=lambda: self.main_controller("sky_blue", '3'), state=DISABLED,
                       disabledforeground="red")
        btn_3.place(x=20, y=15 + (40 * 6 + 40 * 3) + 40 + 70 + 40)
        btn_4 = Button(self.make_canvas, bg="#262626", fg="#00eb00", text="4", font=("Arial", 13, "bold", "italic"),
                       relief=RAISED, bd=3, command=lambda: self.main_controller("sky_blue", '4'), state=DISABLED,
                       disabledforeground="red")
        btn_4.place(x=60, y=15 + (40 * 6 + 40 * 3) + 40 + 70 + 40)

        Label(self.make_canvas, text="Player 2", bg="#141414", fg="gold", font=("Arial", 15, "bold")).place(x=12,
                                                                                                            y=15 + (
                                                                                                                        40 * 6 + 40 * 3) + 40 + 110 + 50)
        self.store_instructional_btn(block_predict_sky_blue, predict_sky_blue, [btn_1, btn_2, btn_3, btn_4])

    def store_instructional_btn(self, block_indicator, predictor, entry_controller):
        temp = []
        temp.append(block_indicator)
        temp.append(predictor)
        temp.append(entry_controller)
        self.block_value_predict.append(temp)
    
     def red_circle_start_position(self, coin_number):
        self.make_canvas.delete(self.made_red_coin[int(coin_number) - 1])
        self.made_red_coin[int(coin_number) - 1] = self.make_canvas.create_oval(100 + 40, 15 + (40 * 6), 100 + 40 + 40,
                                                                                15 + (40 * 6) + 40, fill="red", width=3,
                                                                                outline="black")

        self.red_number_label[int(coin_number) - 1].place_forget()
        red_start_label_x = 100 + 40 + 10
        red_start_label_y = 15 + (40 * 6) + 5
        self.red_number_label[int(coin_number) - 1].place(x=red_start_label_x, y=red_start_label_y)

        self.red_coin_position[int(coin_number) - 1] = 1
        self.window.update()
        time.sleep(0.2)

    def green_circle_start_position(self, coin_number):
        self.make_canvas.delete(self.made_green_coin[int(coin_number) - 1])
        self.made_green_coin[int(coin_number) - 1] = self.make_canvas.create_oval(100 + (40 * 8), 15 + 40,
                                                                                  100 + (40 * 9), 15 + 40 + 40,
                                                                                  fill="#00FF00", width=3)

        self.green_number_label[int(coin_number) - 1].place_forget()
        green_start_label_x = 100 + (40 * 8) + 10
        green_start_label_y = 15 + 40 + 5
        self.green_number_label[int(coin_number) - 1].place(x=green_start_label_x, y=green_start_label_y)

        self.green_coin_position[int(coin_number) - 1] = 14
        self.window.update()
        time.sleep(0.2)

    def yellow_circle_start_position(self, coin_number):
        self.make_canvas.delete(self.made_yellow_coin[int(coin_number) - 1])
        self.made_yellow_coin[int(coin_number) - 1] = self.make_canvas.create_oval(100 + (40 * 6) + (40 * 3) + (40 * 4),
                                                                                   15 + (40 * 8),
                                                                                   100 + (40 * 6) + (40 * 3) + (40 * 5),
                                                                                   15 + (40 * 9), fill="yellow",
                                                                                   width=3)

        self.yellow_number_label[int(coin_number) - 1].place_forget()
        yellow_start_label_x = 100 + (40 * 6) + (40 * 3) + (40 * 4) + 10
        yellow_start_label_y = 15 + (40 * 8) + 5
        self.yellow_number_label[int(coin_number) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)

        self.yellow_coin_position[int(coin_number) - 1] = 27
        self.window.update()
        time.sleep(0.2)

    def sky_blue_circle_start_position(self, coin_number):
        self.make_canvas.delete(self.made_sky_blue_coin[int(coin_number) - 1])
        self.made_sky_blue_coin[int(coin_number) - 1] = self.make_canvas.create_oval(100 + 240, 340 + (40 * 5) - 5,
                                                                                     100 + 240 + 40, 340 + (40 * 6) - 5,
                                                                                     fill="#04d9ff", width=3)

        self.sky_blue_number_label[int(coin_number) - 1].place_forget()
        sky_blue_start_label_x = 100 + 240 + 10
        sky_blue_start_label_y = 340 + (40 * 5) - 5 + 5
        self.sky_blue_number_label[int(coin_number) - 1].place(x=sky_blue_start_label_x, y=sky_blue_start_label_y)

        self.sky_blue_coin_position[int(coin_number) - 1] = 40
        self.window.update()
        time.sleep(0.2)

     def num_btns_state_controller(self, take_nums_btns_list, state_control=1):
        if state_control:
            for num_btn in take_nums_btns_list:
                num_btn['state'] = NORMAL
        else:
            for num_btn in take_nums_btns_list:
                num_btn['state'] = DISABLED

    def main_controller(self, color_coin, coin_number):
        robo_operator = None

        if color_coin == "red":
            self.num_btns_state_controller(self.block_value_predict[0][2], 0)

            if self.move_red_counter == 106:
                messagebox.showwarning("Destination reached", "Reached at the destination")

            elif self.red_coin_position[int(coin_number) - 1] == -1 and self.move_red_counter == 6:
                self.red_circle_start_position(coin_number)
                self.red_coord_store[int(coin_number) - 1] = 1

            elif self.red_coin_position[int(coin_number) - 1] > -1:
                take_coord = self.make_canvas.coords(self.made_red_coin[int(coin_number) - 1])
                red_start_label_x = take_coord[0] + 10
                red_start_label_y = take_coord[1] + 5
                self.red_number_label[int(coin_number) - 1].place(x=red_start_label_x, y=red_start_label_y)

                if self.red_coin_position[int(coin_number) - 1] + self.move_red_counter <= 106:
                    self.red_coin_position[int(coin_number) - 1] = self.motion_of_coin(
                        self.red_coin_position[int(coin_number) - 1], self.made_red_coin[int(coin_number) - 1],
                        self.red_number_label[int(coin_number) - 1], red_start_label_x, red_start_label_y, "red",
                        self.move_red_counter)
                    if self.robo_prem and self.red_coin_position[int(coin_number) - 1] == 106 and color_coin == "red":
                        self.robo_store.remove(int(coin_number))
                        print("After removing: ", self.robo_store)

                    if self.robo_prem:
                        robo_operator = "give"
                        self.robo_judge(robo_operator)
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
                        self.coord_overlap(self.red_coin_position[int(coin_number) - 1], color_coin,
                                           self.move_red_counter)

                self.red_coord_store[int(coin_number) - 1] = self.red_coin_position[int(coin_number) - 1]

        elif color_coin == "sky_blue":
            self.num_btns_state_controller(self.block_value_predict[1][2], 0)

            if self.move_red_counter == 106:
                messagebox.showwarning("Destination reached", "Reached at the destination")

            elif self.sky_blue_coin_position[int(coin_number) - 1] == -1 and self.move_sky_blue_counter == 6:
                self.sky_blue_circle_start_position(coin_number)
                self.sky_blue_coord_store[int(coin_number) - 1] = 40

            elif self.sky_blue_coin_position[int(coin_number) - 1] > -1:
                take_coord = self.make_canvas.coords(self.made_sky_blue_coin[int(coin_number) - 1])
                sky_blue_start_label_x = take_coord[0] + 10
                sky_blue_start_label_y = take_coord[1] + 5
                self.sky_blue_number_label[int(coin_number) - 1].place(x=sky_blue_start_label_x,
                                                                       y=sky_blue_start_label_y)

                if self.sky_blue_coin_position[int(coin_number) - 1] + self.move_sky_blue_counter <= 106:
                    self.sky_blue_coin_position[int(coin_number) - 1] = self.motion_of_coin(
                        self.sky_blue_coin_position[int(coin_number) - 1],
                        self.made_sky_blue_coin[int(coin_number) - 1], self.sky_blue_number_label[int(coin_number) - 1],
                        sky_blue_start_label_x, sky_blue_start_label_y, "sky_blue", self.move_sky_blue_counter)
                else:
                    messagebox.showerror("Not possible", "No path available")

                    self.num_btns_state_controller(self.block_value_predict[1][2])
                    return

                if self.sky_blue_coin_position[int(coin_number) - 1] == 22 or self.sky_blue_coin_position[
                    int(coin_number) - 1] == 9 or self.sky_blue_coin_position[int(coin_number) - 1] == 48 or \
                        self.sky_blue_coin_position[int(coin_number) - 1] == 35 or self.sky_blue_coin_position[
                    int(coin_number) - 1] == 1 or self.sky_blue_coin_position[int(coin_number) - 1] == 14 or \
                        self.sky_blue_coin_position[int(coin_number) - 1] == 27 or self.sky_blue_coin_position[
                    int(coin_number) - 1] == 40:
                    pass
                else:
                    if self.sky_blue_coin_position[int(coin_number) - 1] < 100:
                        self.coord_overlap(self.sky_blue_coin_position[int(coin_number) - 1], color_coin,
                                           self.move_sky_blue_counter)

                self.sky_blue_coord_store[int(coin_number) - 1] = self.sky_blue_coin_position[int(coin_number) - 1]

            else:
                messagebox.showerror("Wrong choice", "Sorry, Your coin in not permitted to travel")
                self.num_btns_state_controller(self.block_value_predict[1][2])
                return

            self.block_value_predict[1][1]['state'] = NORMAL

        print(self.red_coord_store)
        print(self.green_coord_store)
        print(self.yellow_coord_store)
        print(self.sky_blue_coord_store)
        if self.robo_prem == 1:
            print("Robo Store is: ", self.robo_store)

        permission_granted_to_proceed = True

        if color_coin == "red" and self.red_coin_position[int(coin_number) - 1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif color_coin == "green" and self.green_coin_position[int(coin_number) - 1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif color_coin == "yellow" and self.yellow_coin_position[int(coin_number) - 1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)
        elif color_coin == "sky_blue" and self.sky_blue_coin_position[int(coin_number) - 1] == 106:
            permission_granted_to_proceed = self.check_winner_and_runner(color_coin)

        if permission_granted_to_proceed:  
            self.make_command(robo_operator)





if __name__ == '__main__':
    window = Tk()
    window.geometry("800x630")
    window.maxsize(800, 630)
    window.minsize(800, 630)
    window.title("AI Integration With Ludo")
    window.iconbitmap("Images/ludo_icon.ico")
    block_six_side = ImageTk.PhotoImage(Image.open("Images/6_block.png").resize((35, 35), Image.ANTIALIAS))
    block_five_side = ImageTk.PhotoImage(Image.open("Images/5_block.png").resize((35, 35), Image.ANTIALIAS))
    block_four_side = ImageTk.PhotoImage(Image.open("Images/4_block.png").resize((35, 35), Image.ANTIALIAS))
    block_three_side = ImageTk.PhotoImage(Image.open("Images/3_block.png").resize((35, 35), Image.ANTIALIAS))
    block_two_side = ImageTk.PhotoImage(Image.open("Images/2_block.png").resize((35, 35), Image.ANTIALIAS))
    block_one_side = ImageTk.PhotoImage(Image.open("Images/1_block.png").resize((35, 35), Image.ANTIALIAS))
    Ludo(window, block_six_side, block_five_side, block_four_side, block_three_side, block_two_side, block_one_side)
    window.mainloop()