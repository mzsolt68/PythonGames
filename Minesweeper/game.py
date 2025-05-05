from tkinter import Tk, messagebox, Menu
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
        game_menu.add_command(label="50x50", command=lambda: self.start_game(50, 50))
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.cleanup)
        menu.add_cascade(label="Game", menu=game_menu)
        self.root.config(menu=menu)
    
    def start_game(self, size: int, mines:int):
        pass

    def cleanup(self):
        try:
            self.root.update_idletasks()
            self.root.quit()
            self.root.destroy()
        except Exception as e:
            print(f"Error during cleanup: {e}")
