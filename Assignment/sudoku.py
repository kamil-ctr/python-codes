import tkinter as tk
from tkinter import messagebox

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")
        self.cells = []
        self.grid = [[0] * 9 for _ in range(9)]

        self.create_grid()
        self.generate_puzzle()
        self.create_buttons()

    def create_grid(self):
        for row in range(9):
            row_cells = []
            for col in range(9):
                entry = tk.Entry(self.root, width=2, font=("Arial", 18), justify="center", fg="black")
                entry.grid(row=row, column=col, padx=1, pady=1)
                
                entry.configure(bg="#e6f7ff" if (row // 3 + col // 3) % 2 == 0 else "#add8e6")
                row_cells.append(entry)
            self.cells.append(row_cells)

    def create_buttons(self):
        tk.Button(self.root, text="Check", command=self.check_solution).grid(row=9, column=0, columnspan=4, sticky="we")
        tk.Button(self.root, text="Reset", command=self.reset_grid).grid(row=9, column=5, columnspan=4, sticky="we")

    def generate_puzzle(self):
        puzzle = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        for row in range(9):
            for col in range(9):
                value = puzzle[row][col]
                if value != 0:
                    self.cells[row][col].insert(0, str(value))
                    self.cells[row][col].configure(state="disabled")
                self.grid[row][col] = value

    def check_solution(self):
        try:
            current_grid = [[int(self.cells[row][col].get() or 0) for col in range(9)] for row in range(9)]

            if self.is_valid_sudoku(current_grid):
                messagebox.showinfo("Success", "You solved it correctly!")
            else:
                messagebox.showerror("Error", "Incorrect solution. Try again.")
        except ValueError:
            messagebox.showerror("Error", "Enter numbers between 1 and 9.")

    def is_valid_sudoku(self, grid):
        for i in range(9):
            if not self.is_unique(grid[i]) or not self.is_unique([grid[row][i] for row in range(9)]):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                subgrid = [grid[row][col] for row in range(box_row, box_row + 3) for col in range(box_col, box_col + 3)]
                if not self.is_unique(subgrid):
                    return False
        return True

    def is_unique(self, values):
        nums = [num for num in values if num != 0]
        return len(nums) == len(set(nums))

    def reset_grid(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col]["state"] != "disabled":
                    self.cells[row][col].delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    SudokuGame(root)
    root.mainloop()
