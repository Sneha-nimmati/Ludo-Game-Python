import unittest
from ludo_game import Ludo
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import pygame
from random import randint, choice
import pytest

class TestLudo(unittest.TestCase):
    '''
        Tests whether user has entered valid number in the input Field
    '''
    async def _start_app(self):
        self.app.mainloop()

    def setUp(self):
        self.app = Ludo()
        self._start_app()

    def test_startup(self):
        robo_play = self.app.robo_prem
        total_people_play = self.app.total_people_play
        robolist = [len(total_people_play), robo_play]
        comp_list = [2, 1]
        if robo_play == 1 and len(total_people_play) == 2:
            self.assertEqual(robolist, comp_list)
        else:
            assert 0 < len(total_people_play) < 5

    def test_startup1(self):
        six_list = self.app.red_six_list
        list6 = ["first_move"]
        self.assertEqual(six_list,list6)