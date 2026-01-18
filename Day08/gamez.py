import tkinter as tk

CELL_SIZE = 80
COLS = 7

START_POS = 5  # x = 6
GOAL_POS = 4   # x = 5


class ReeborgGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Reeborg's World")

        self.canvas = tk.Canvas(
            root,
            width=COLS * CELL_SIZE,
            height=CELL_SIZE,
            bg="#fdf6e3"
        )
        self.canvas.pack(pady=10)

        self.robot_pos = START_POS
        self.direction = "W"

        self.draw_world()

        btn = tk.Button(root, text="MOVE", command=self.move)
        btn.pack()

    def draw_world(self):
        self.canvas.delete("all")

        for col in range(COLS):
            x1 = col * CELL_SIZE
            x2 = x1 + CELL_SIZE
            self.canvas.create_rectangle(x1, 0, x2, CELL_SIZE, outline="brown", width=3)
            self.canvas.create_text(x1 + CELL_SIZE / 2, CELL_SIZE - 10, text=str(col + 1))

        gx = GOAL_POS * CELL_SIZE + CELL_SIZE / 2
        self.canvas.create_text(gx, CELL_SIZE / 2, text="⭐", font=("Arial", 30))

        rx = self.robot_pos * CELL_SIZE + CELL_SIZE / 2
        self.canvas.create_text(rx, CELL_SIZE / 2, text="🤖", font=("Arial", 30))

    def move(self):
        if self.robot_pos > 0:
            self.robot_pos -= 1
        self.draw_world()


# 🔴 THIS PART IS MANDATORY
if __name__ == "__main__":
    root = tk.Tk()
    game = ReeborgGame(root)
    root.mainloop()
