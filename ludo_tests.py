import pytest
from ludo_game import Ludo
from tkinter import Tk

@pytest.fixture
def game():
    # Create a new tkinter window
    window = Tk()

    # Create a new Ludo game using the tkinter window
    game = Ludo(window)
    return game

def test_init_game_board(game):
    # Check that the game board has been initialized correctly
    robo_play = game.check_if_bot
    total_people_play = game.total_people_play
    robolist = [len(total_people_play), robo_play]
    comp_list = [2, 1]
    if robo_play == 1 and len(total_people_play) == 2:
        assert robolist == comp_list
    else:
        assert 0 < len(total_people_play) < 5

def test_coin_positions(game):
    test_coin_position = [game.red_coin_position, game.green_coin_position,
                          game.blue_coin_position, game.yellow_coin_position]
    coin_pos = [-1,-1,-1,-1]
    for each_coin_pos in test_coin_position:
        assert each_coin_pos == coin_pos

def test_initial_move(game):
    # Render the game board
    six_list = game.six_list
    list6 = ["first_move"]
    assert six_list == list6

def test_final_destination(game):
    # testing the winner of game feature
    winner = game.first_winner
    if len(winner)>0:
        if winner[0] == "red":
            test_winner = ["red","Winner of the Game"]
            assert winner == test_winner
        elif winner[0] == "blue":
            test_winner = ["blue","Winner of the Game"]
            assert winner == test_winner
        elif winner[0] == "green":
            test_winner = ["green", "Winner of the Game"]
            assert winner == test_winner
        elif winner[0] == "yellow":
            test_winner = ["yellow", "Winner of the Game"]
            assert winner == test_winner
    else:
        assert winner == []