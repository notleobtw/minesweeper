import pygame as pg
import random

CELL_SIZE = 32
ROWS = 9
COLS = 9
NUM_MINES = 10
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
image_mine = pg.image.load("Sprites/mine.png")

image_grid_number = [image_emptyGrid, image_grid1, image_grid2, image_grid3, image_grid4, image_grid5, image_grid6, image_grid7, image_grid8]
image_mineClicked = pg.image.load("Sprites/mineClicked.png")
image_mineFalse = pg.image.load("Sprites/mineFalse.png")


class Game:
    '''The main game class'''

    def __init__(self) -> None:
        pg.display.set_caption("Leo's Minesweeper")
        self.clock = pg.time.Clock()

    def set_difficulty(self, difficulty : str):
        '''Set the game difficulty
        
        Args:
            difficulty: the game difficulty
        '''
        global ROWS, COLS, NUM_MINES, WIDTH, HEIGHT
        if difficulty == 'beginner':
            ROWS = 9
            COLS = 9
            NUM_MINES = 10
            WIDTH = CELL_SIZE * ROWS
            HEIGHT = CELL_SIZE *COLS
            
        elif difficulty == 'intermediate':
            ROWS = 16
            COLS = 16
            NUM_MINES = 40
            WIDTH = CELL_SIZE * ROWS
            HEIGHT = CELL_SIZE *COLS
        elif difficulty == 'expert':
            ROWS = 30
            COLS = 16
            NUM_MINES = 99
            WIDTH = CELL_SIZE * ROWS
            HEIGHT = CELL_SIZE *COLS

    def new_game(self, difficulty : str = 'beginner'):
        '''Generate a new game from the start'''
        self.set_difficulty(difficulty)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.board = Board()

    def run_game(self):
        '''Run the game'''
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.close_game()
            self.draw()

    def draw(self):
        '''Display the game'''
        self.screen.fill('grey')
        self.board.draw(self.screen)
        pg.display.flip()

    def close_game(self):
        '''Closes the game'''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit(0) 

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
        '''Display the cell on the board
        
        Args:
            board: the game's board
        '''
        # # Revealed cell
        # if self.revealed:
        #     board.blit(self.image, (self.x, self.y))
        # # Flagged cell
        # elif self.flagged and not self.revealed:
        #     board.blit(image_flag, (self.x, self.y))
        # # Unrevealed cell
        # elif not self.revealed:
        #     board.blit(self.image, (self.x, self.y))
        if not self.flagged and self.revealed:
            board.blit(self.image, (self.x, self.y))
        elif self.flagged and not self.revealed:
            board.blit(image_flag, (self.x, self.y))
        elif not self.revealed:
            board.blit(image_grid, (self.x, self.y))



class Board:
    '''A board that contains many cells'''

    def __init__(self):
        self.board = pg.Surface((WIDTH, HEIGHT))
        self.list_of_cells = [[Cell(row, col, '.', image_grid) for row in range(ROWS)] for col in range(COLS)]
        self.place_mines()
        self.place_clue()

    def place_mines(self):
        '''Place mines in the board'''
        for i in range(NUM_MINES):
            while True:
                x = random.randint(0, ROWS-1)
                y = random.randint(0, COLS-1)
                if self.list_of_cells[x][y].state == ".":
                    self.list_of_cells[x][y].image = image_mine
                    self.list_of_cells[x][y].state = "X"
                    break

    def place_clue(self):
        '''Place clues or the number surrounding mines in the board'''
        for x in range(ROWS):
            for y in range(COLS):
                if self.list_of_cells[x][y].state != "X":
                    nearby_mines = self.get_num_nearby_mines(x, y)
                    self.list_of_cells[x][y].image = image_grid_number[nearby_mines]
                    self.list_of_cells[x][y].state = "N"


    def get_num_nearby_mines(self, x : int, y : int) -> int:
        '''Count how many mines are neighbor with this cell
        
        Args:
            x: the row of the cell
            y: the col of the cell

        Returns:
            nearby_mines: the number of nearby mines
        '''
        nearby_mines = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbour_x = x + i
                neighbour_y = y + j
                if 0 <= neighbour_x < ROWS and 0 <= neighbour_y < COLS and self.list_of_cells[neighbour_x][neighbour_y].state == 'X':
                    nearby_mines += 1
        return nearby_mines

    def draw(self, window):
        '''Display the board to the game's window
        
        Args:
            window: the game's window
        '''
        for row in self.list_of_cells:
            for cell in row:
                cell.draw(self.board)
        window.blit(self.board, (0, 0))


if __name__ == '__main__':
    game = Game()
    game.set_difficulty('beginner')
    if (ROWS == 9) and (COLS == 9) and (NUM_MINES == 10):
        print("PASSED!")
    else:
        print("FAILED!")

    game.set_difficulty('intermediate')
    if (ROWS == 16) and (COLS == 16) and (NUM_MINES == 40):
        print("PASSED!")
    else:
        print("FAILED!")

    game.set_difficulty('expert')
    if (ROWS == 30) and (COLS == 16) and (NUM_MINES == 99):
        print("PASSED!")
    else:
        print("FAILED!")
    
    while True:
        #Change this to see the board size changing
        game.new_game('intermediate') 
        game.run_game()