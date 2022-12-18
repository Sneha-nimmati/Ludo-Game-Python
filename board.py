from tkinter import *
class Board:
    def __init__(self,make_canvas):
        self.graphical_red_coin = []
        self.graphical_blue_coin = []
        self.graphical_green_coin = []
        self.graphical_yellow_coin = []
        self.label_red_coin = []
        self.label_blue_coin = []
        self.label_green_coin = []
        self.label_yellow_coin = []
        self.make_canvas = make_canvas
    def board_set_up(self):
        '''
        In this method we create the Ludo board

        First we create the rectangle boxes of all colors,then create all the border lines of play area and square boxes
        then fill with respective colors wherever necessary

        variable: variable initialised in the __init__ method are used to create the board

        output: A ludo board gets created with 4 different coins, initial positions, safe places,and number labels,
         play area and final destination area in it.

        '''

        self.make_canvas.create_rectangle(100, 15, 100 + (40 * 15), 15 + (40 * 15), width=6, fill="white")
        print("created initial rectangle")
        # initial place for all coins
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

        # creating border lines
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

        # creating play area
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

        # Destination position for all coins
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
    def coins(self,x0,y0,x1,y1,width,color,outline="black"):

        # creating coins and number labels
        coin_creation = self.make_canvas.create_oval(x0, y0, x1, y1, width=width, fill=color,
                                                  outline=outline)
        if color == "red":
            self.graphical_red_coin.append(coin_creation)
        elif color == "#04d9ff":
            self.graphical_blue_coin.append(coin_creation)
        elif color == "#00FF00":
            self.graphical_green_coin.append(coin_creation)
        elif color == "yellow":
            self.graphical_yellow_coin.append(coin_creation)
        else:
            pass
        print("coin_creation:",self.graphical_blue_coin)
        print("yellow_coin_creation:", self.graphical_yellow_coin)

    def label_coin(self,number,color,xcoord,ycoord):
        coin_label = Label(self.make_canvas, text=str(number), font=("Arial", 15, "bold"), bg=color, fg="black")
        coin_label.place(x=xcoord, y=ycoord)
        if color == "red":
            self.label_red_coin.append(coin_label)
        elif color == "#04d9ff":
            self.label_blue_coin.append(coin_label)
        elif color == "#00FF00":
            self.label_green_coin.append(coin_label)
        elif color == "yellow":
            self.label_yellow_coin.append(coin_label)

    def safe_place(self):
        # safe places at 4 sides
        common_x = 340 + (40 * 6) + 20
        common_y = 15 + 240 + 2
        coord = [common_x, common_y, common_x + 5, common_y + 15, common_x + 15, common_y + 15, common_x + 8,
                 common_y + 20, common_x + 15, common_y + 25, common_x + 5, common_y + 25, common_x, common_y + 25 + 10,
                 common_x - 5, common_y + 25, common_x - 16, common_y + 25, common_x - 8, common_y + 15 + 5,
                 common_x - 15, common_y + 15, common_x - 5, common_y + 15]
        self.make_canvas.create_polygon(coord, width=2, fill="black")

        common_x = 100 + 240 + 2 + 18
        common_y = 15 + (40 * 2) + 2
        coord = [common_x, common_y, common_x + 5, common_y + 15, common_x + 15, common_y + 15, common_x + 8,
                 common_y + 20, common_x + 15, common_y + 25, common_x + 5, common_y + 25, common_x, common_y + 25 + 10,
                 common_x - 5, common_y + 25, common_x - 16, common_y + 25, common_x - 8, common_y + 15 + 5,
                 common_x - 15, common_y + 15, common_x - 5, common_y + 15]
        self.make_canvas.create_polygon(coord, width=2, fill="black")

        common_x = 100 + (40 * 2) + 2 + 18
        common_y = 15 + 240 + (40 * 2) + 2
        coord = [common_x, common_y, common_x + 5, common_y + 15, common_x + 15, common_y + 15, common_x + 8,
                 common_y + 20, common_x + 15, common_y + 25, common_x + 5, common_y + 25, common_x, common_y + 25 + 10,
                 common_x - 5, common_y + 25, common_x - 16, common_y + 25, common_x - 8, common_y + 15 + 5,
                 common_x - 15, common_y + 15, common_x - 5, common_y + 15]
        self.make_canvas.create_polygon(coord, width=2, fill="black")

        common_x = 100 + 240 + (40 * 2) + 2 + 18
        common_y = 15 + (40 * 6) + (40 * 3) + (40 * 3) + 2
        coord = [common_x, common_y, common_x + 5, common_y + 15, common_x + 15, common_y + 15, common_x + 8,
                 common_y + 20, common_x + 15, common_y + 25, common_x + 5, common_y + 25, common_x, common_y + 25 + 10,
                 common_x - 5, common_y + 25, common_x - 16, common_y + 25, common_x - 8, common_y + 15 + 5,
                 common_x - 15, common_y + 15, common_x - 5, common_y + 15]
        self.make_canvas.create_polygon(coord, width=3, fill="black")
