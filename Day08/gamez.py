import tkinter as tk

# ---------------- CONFIG ----------------
CELL_SIZE = 80
ROWS = 1
COLS = 7

START_POS = 5   # index starts from 0 → x=6
GOAL_POS = 4    # x=5
# ----------------------------------------


class ReeborgGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Reeborg's World - Task Driven Learning")

        self.canvas = tk.Canvas(
            root,
            width=COLS * CELL_SIZE,
            height=ROWS * CELL_SIZE,
            bg="#fdf6e3"
        )
