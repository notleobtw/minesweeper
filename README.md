# Project: Simple Minesweeper

# Overview
Simple Minesweeper is a classic Minesweeper game inspired by the original Minesweeper game on Windows. The aim of this project is to create a basic version of the game that replicates the traditional Minesweeper experience with a simple, user-friendly interface. It will also include most of the features in the original game.

# Prerequisites and installation instructions
Please use python 3 or higher. Some fucntion might not work with lower version of Python. 
I only used pygame, pygame_menu and random modules.
Install by pip:
    pip install pygame -U
    pip install pygame-menu -U

Random should come with Python.

# Instructions
## How to run
Run the minesweeper.py file as a script (by running from your code editor or running "python minesweeper.py" from your terminal.
## How to play
Hidden mines are scattered throughout a board, which is divided into cells or tiles. All tile is hidden initially.

Each tile can be:
 - A mine: you lose if you click on it
 - A clue: number 1-8 indicating the number of mines diagonally or adjacent to it
 - Blank: no mine around, all adjacent tiles will automatically be opened if you click on it

You can:
 - Left-click to open a tile. Use the clue to open every tile except for the mines to win
 - Right-click to flag a tile to denote that you believe a mine to be in that place. A flagged tile is consider unopened and may be unflag by right-clicking again

Left-click once after you win or lose to go to the end screen!

# Future directions
Adding user custom option for the map size and number of mines.
Improve user interface to be more appealing.
Maybe allow the game to work on different devices and OS.

# Proposed Features

Traditional Gameplay: Simple Minesweeper will replicate the classic Minesweeper gameplay, including the grid of tiles, numbers, and randomized mines.

Friendly UI: The game will be designed to be easy to play and interact with.

Win/Loss State: Implementing a system to determine when the game is won or lost, with appropriate feedback.

Timer: Adding a timer to keep track of the time it takes the player to complete the game.

Flagging Mines: Allowing players to flag tiles they suspect contain mines for strategic play.

Choosing Difficulty: Allowing players to choose number of mines and size of grid.

# Stakeholders and Intended Users:
## Intended Users:
Simple Minesweeper is intended for individuals interested in playing a straightforward and nostalgic version of the classic Minesweeper game. It is designed for class project purposes and for anyone who wants to enjoy a simplified Minesweeper experience.

## Expected Pre-requisites/Background:
No specific prerequisites or prior gaming experience are required to enjoy Simple Minesweeper. It is designed to be accessible to players of all skill levels.

## Stakeholders:

Developer: Leo Ha, the primary stakeholder is myself developing the project as part of COMP333 assignment.

Class Instructor and TA: Sonia Roberts and Tim Goggin, the instructor of the class and the TA are stakeholders, providing guidance, grading, and evaluation of the project.

Peers and Classmates: Other students in the class may have an interest in playing and testing the game.

Anyone else who interested in playing the game might also be a stakeholder
