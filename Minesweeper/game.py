from tkinter import Tk, Menu, Frame, Canvas
import random

CELL_SIZE = 30  # Size of each cell in pixels

class Minesweeper:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Minesweeper")
        self.root.geometry("400x400")
        self.board_size = None
        self.num_mines = None
        self.board = []

        self.create_menu()

    def create_menu(self):
        menu = Menu(self.root)
        game_menu = Menu(menu, tearoff=0)
        game_menu.add_command(label="10x10", command=lambda: self.start_game(10, 10))
        game_menu.add_command(label="20x20", command=lambda: self.start_game(20, 20))
        game_menu.add_command(label="30x30", command=lambda: self.start_game(30, 30))
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.cleanup)
        menu.add_cascade(label="Game", menu=game_menu)
        self.root.config(menu=menu)
    
    def start_game(self, board_size: int, num_mines:int):
        self.board_size = board_size
        self.num_mines = num_mines

        # Clear the board frame if it exists
        if hasattr(self, 'board_frame') and self.board_frame:
            self.board_frame.destroy()
        
        self.initialize_board()
        self.create_board()

    def cleanup(self):

        try:
            self.root.update_idletasks()
            self.root.quit()
            self.root.destroy()
        except Exception as e:
            print(f"Error during cleanup: {e}")
    
    def initialize_board(self):
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]

        # Place mines randomly
        mine_positions = random.sample(range(self.board_size * self.board_size), self.num_mines)
        for position in mine_positions:
            row, column = divmod(position, self.board_size)
            self.board[row][column] = -1
    
    def create_board(self):
        self.board_frame = Frame(self.root)
        self.board_frame.pack()
        canvas = Canvas(self.board_frame, width=self.board_size * CELL_SIZE, height=self.board_size * CELL_SIZE, bg="white")
        canvas.pack()

        self.cells = {} # Store cell references for later use
        for row in range(self.board_size):
            for column in range(self.board_size):
                x1, y1 = column * CELL_SIZE, row * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray", outline="black")
                self.cells[(row, column)] = rectangle
                canvas.tag_bind(rectangle, "<Button-1>", lambda event, r=row, c=column: self.reveal_cell(r, c))
        
        board_width = self.board_size * CELL_SIZE
        board_height = self.board_size * CELL_SIZE
        self.root.geometry(f"{board_width}x{board_height}")
    
    def reveal_cell(self, row: int, column: int):
        pass
