# LUDO
 #### <i>LUDO is a popular board game that is played by people of all ages. This version of LUDO has been implemented using the Tkinter,pygame libraries in Python.</i>
<br>
<br>

# About the Game

#### <b>LUDO</b> is a game for 2-4 players. Each player is represented by a different color (red, green, blue, and yellow) and has 4 coins that start at the corresponding home position on the board.

#### The objective of the game is to move all of your coins from your initial position to the final destination (the "finish" area) before the other players do.

#### The game is played by rolling a six-sided dice. The number on the dice determines how many spaces you can move one of your coins. You can choose which coin to move based on the number rolled and the current positions of your coins.

#### Once a coin is on the board, it can be "killed" by another player's coin if that player's coin lands on the same space. In that case, the killed coin must return to its home position and start again.

#### The first player to move all of their coins to the finish area wins the game.

<br/>

 # Requirements
#### To run this game, you will need to have python and certain python Packages. Below are the list of packages that are needed to run this program
    1) Tkinter
    2) pygame
    3) PIL

#### You can install these packages using package managers like pip or conda.

<br>

# Running the game

#### To run the game, download the source code and navigate to the directory where you saved it. Then, run the following command:
<br>

    python ludo-game.py
<br>

#### This will launch a window where you can choose any option between play with friends and play with computer and can play the game.

<br>

# How to Play

### There are two ways to play this game.
        1. Play with Computer
        2.Play with Friends

<br/>

### 1. Play with Computer
<br>
     If User wants to play with computer he can choose play with computer and start the game. As soon as the player selects play with computer option, a message will be displayed which gives information about the color of the coin that is assigned to computer and to the player. The message also contains the information about who to start the game and the window disappears. Then the Ludo board is lanched where computer and player starts the Game.
    

<br/>
### 2. Play With Friends
    The second option User can choose is to play with friends. If a user chooses this option, he has to enter number of players to play the game in the input field and start the game. If a user doesnot enters a value between 2 and 4 it displays a message saying please enter values between 2 and 4. if the user enters the correct value and click on start then the ludo board will be launched where the players can start the game.
<br/>

Once the Game starts in any of the above scenarios players can start the game by rolling a dice. Whenever any player gets 6 in the dice he can move one of his coins from initial position to game starting position and also gets one more chance to roll the dice.Based the on value on the dice player can traverse any one of his coins forward by clicking on the number label available beside his color. Then the next player gets the chance to roll the dice and the game continues till any player moves all of his coins to the final position of the game.While playing the game any player can kill the coin of opponents and moves his coin to the same position,this player also gets one more chance to roll the dice in this scenario. The coin that got killed will move to the initial position of the game. The game ends when n-1 players moves all of their coins to the final position(n is total number of player) and displays a message box syaing "Game over". Everytime  a player traverse his coin to the final postion an alert box appears which contains the message saying "You are at the final position". A congratulatory alert box appears when any player traverses all of his coins to the final positions.

<br/>

# Testing:

We have tested few scenarios using Unittest in python.

    1.Checking if valid number is entered when play with friends is selected.
    2.Checking initial positions of the coins.
<br/>


# Contributors:

<br/>

### This game has been developed by Sneha and Swathi.
### For project activities and code commits a git repo was created.
    Git repo: https://github.com/Sneha-nimmati/Software-Development-group-project









