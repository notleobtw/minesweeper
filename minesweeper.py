import pygame as pg

CELL_SIZE = 30
ROWS = 10
COLS = 10
NUM_MINES = 5
WIDTH = CELL_SIZE * ROWS
HEIGHT = CELL_SIZE *COLS
FPS = 60

image_emptyGrid = pg.image.load("Sprites/empty.png")
image_flag = pg.image.load("Sprites/flag.png")
image_grid = pg.image.load("Sprites/Grid.png")
image_grid1 = pg.image.load("Sprites/grid1.png")
image_grid2 = pg.image.load("Sprites/grid2.png")
image_grid3 = pg.image.load("Sprites/grid3.png")
image_grid4 = pg.image.load("Sprites/grid4.png")
image_grid5 = pg.image.load("Sprites/grid5.png")
image_grid6 = pg.image.load("Sprites/grid6.png")
image_grid7 = pg.image.load("Sprites/grid7.png")
image_grid8 = pg.image.load("Sprites/grid8.png")
image_grid7 = pg.image.load("Sprites/grid7.png")
image_mine = pg.image.load("Sprites/mine.png")
image_mineClicked = pg.image.load("Sprites/mineClicked.png")
image_mineFalse = pg.image.load("Sprites/mineFalse.png")


class Game:
    '''The main game class'''
    def __init__(self) -> None:
        pass

    def set_difficulty(self, difficulty : str):
        '''Set the game difficulty
        
        Args:
            difficulty: the game difficulty
        '''
        pass

    def new_game(self):
        '''Generate a new game from the start'''
        pass

    def run_game(self):
        '''Run the game'''
        pass

    def draw(self):
        '''Display the game'''
        pass

    def close_game(self):
        '''Closes the game'''
        pass

# State for a cell:
#     '.': unknown
#     'X': mine
#     'N': a number (empty is 0)

class Cell:
    '''One cell in the grid'''
    def __init__(self, pos_X, pos_Y, state, image, revealed=False, flagged=False):
        self.x = pos_X * CELL_SIZE
        self.y = pos_Y * CELL_SIZE
        self.revealed = revealed
        self.flagged = flagged
        self.state = state
        self.image = image

    def draw(self, board):
        '''Display the cell on the board'''
        pass

class Board:
    '''A board that contains many cells'''

    def __init__(self):
        self.board = pg.Surface(WIDTH, HEIGHT)
        self.list_of_cells = [[Cell(row, col, '.', image_grid) for row in range(ROWS)] for col in range(COLS)]