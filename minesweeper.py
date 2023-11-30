import pygame as pg
import random
import time

CELL_SIZE = 32
ROWS = 9
COLS = 9
NUM_MINES = 10
WIDTH = CELL_SIZE * ROWS
HEIGHT = CELL_SIZE *COLS
FPS = 60
click_time = 0

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
        self.first_click = True

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
        self.board.display_board() #you can delete this
        self.first_click = True

    def run_game(self):
        '''Run the game'''
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()

    def draw(self):
        '''Display the game'''
        self.screen.fill('grey')
        self.board.draw(self.screen)
        pg.display.flip()

    def check_win(self):
        '''Check if the game is won'''
        if len(self.board.opened) + NUM_MINES == ROWS*COLS:
            return True
        else:
            return False

    def events(self):
        '''Events for the game'''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit(0) 
            
            if event.type == pg.MOUSEBUTTONDOWN:
                col, row = pg.mouse.get_pos()
                row //= CELL_SIZE
                col //= CELL_SIZE


                if event.button == 1:
                    global click_time
                    if not self.board.list_of_cells[row][col].flagged and not self.board.list_of_cells[row][col].revealed: 
                        #if clicked on a unrevealed and unflagged cell: 
                        if self.first_click:
                            self.first_click = False

                            if self.board.list_of_cells[row][col].state == 'X':
                                #if the first click is a bomb, move it to the first cell that is not a bomb
                                self.board.list_of_cells[row][col].state = '.'

                                looping = True
                                for each_row in self.board.list_of_cells :
                                    for cell in each_row:
                                        if cell.state != 'X':
                                            cell.state = 'X'
                                            looping = False
                                            break
                                    if looping == False:
                                        break
                                
                                self.board.place_clue()
                                self.board.display_board() #you can delete this
                        
                        if not self.board.open_cell(row, col):
                            #clicked on a mine, reveal every bomb and every wrong flag
                            for each_row in self.board.list_of_cells:
                                for cell in each_row:
                                    if cell.flagged and cell.state != 'X':
                                        #reveal wrong flag
                                        cell.flagged = False
                                        cell.revealed = True
                                        cell.image = image_mineFalse
                                    elif cell.state == 'X':
                                        #reveal all bombs
                                        cell.revealed = True
                            
                            self.playing = False

                    #double click to reveal all cells around a number clue if you have already flagged all mines around (just the code block right above but with a loop and double click)
                    if self.board.list_of_cells[row][col].revealed and self.board.list_of_cells[row][col].state == 'N' and time.time() - click_time < 0.5 and self.board.get_num_nearby_flags(row,col) == self.board.get_num_nearby_mines(row,col):
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                neighbour_x = row + i
                                neighbour_y = col + j
                                if 0 <= neighbour_x < ROWS and 0 <= neighbour_y < COLS and not self.board.list_of_cells[neighbour_x][neighbour_y].flagged and not self.board.list_of_cells[neighbour_x][neighbour_y].revealed:
                                    if not self.board.open_cell(neighbour_x, neighbour_y):
                                        for each_row in self.board.list_of_cells:
                                            for cell in each_row:
                                                if cell.flagged and cell.state != 'X':
                                                    cell.flagged = False
                                                    cell.revealed = True
                                                    cell.image = image_mineFalse
                                                elif cell.state == 'X':
                                                    cell.revealed = True
                    
                    click_time = time.time()


                if event.button == 3:
                    if not self.board.list_of_cells[row][col].revealed:
                        #if not revealed, right click will flag the cell
                        self.board.list_of_cells[row][col].flagged = not self.board.list_of_cells[row][col].flagged

                if self.check_win():
                    self.win = True
                    self.playing = False
                    for each_row in self.board.list_of_cells:
                        for cell in each_row:
                            if not cell.revealed:
                                #flag all mines if win
                                cell.flagged = True

            

# State for a cell:
#     '.': unknown (or empty)
#     'X': mine
#     'N': a number


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
        if not self.flagged and self.revealed:
            board.blit(self.image, (self.x, self.y))
        elif self.flagged and not self.revealed:
            board.blit(image_flag, (self.x, self.y))
        elif not self.revealed:
            board.blit(image_grid, (self.x, self.y))

    def __repr__(self):
        return self.state



class Board:
    '''A board that contains many cells'''

    def __init__(self):
        self.board = pg.Surface((WIDTH, HEIGHT))
        self.list_of_cells = [[Cell(row, col, '.', image_emptyGrid) for row in range(ROWS)] for col in range(COLS)]
        self.place_mines()
        self.place_clue()
        self.opened = []

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
                    if nearby_mines > 0:
                        self.list_of_cells[x][y].image = image_grid_number[nearby_mines]
                        self.list_of_cells[x][y].state = "N"

    def get_num_nearby_flags(self, x : int, y : int) -> int:
        '''Count how many flags are neighbor with this cell
        
        Args:
            x: the row of the cell
            y: the col of the cell

        Returns:
            nearby_flags: the number of nearby flags
        '''
        nearby_flags = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbour_x = x + i
                neighbour_y = y + j
                if 0 <= neighbour_x < ROWS and 0 <= neighbour_y < COLS and self.list_of_cells[neighbour_x][neighbour_y].flagged:
                    nearby_flags += 1
        return nearby_flags

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

    def open_cell(self, x : int, y : int) -> bool:
        self.opened.append((x,y))
        if self.list_of_cells[x][y].state == 'X':
            #clicked on a bomb
            self.list_of_cells[x][y].revealed = True
            self.list_of_cells[x][y].image = image_mineClicked
            return False
        elif self.list_of_cells[x][y].state == 'N':
            #clicked on a clue number
            self.list_of_cells[x][y].revealed = True
            return True
        else:
            #click on an empty cell
            self.list_of_cells[x][y].revealed = True
            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighbour_x = x + i
                    neighbour_y = y + j
                    if 0 <= neighbour_x < ROWS and 0 <= neighbour_y < COLS:
                        if (neighbour_x, neighbour_y) not in self.opened:
                            self.open_cell(neighbour_x, neighbour_y)
            return True
    
    def display_board(self):
        '''Display the board code to the terminal'''
        print("THE BOARD DISPLAY CODE:")
        for row in self.list_of_cells:
            print(row)
            



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
        game.new_game('beginner') 
        game.run_game()