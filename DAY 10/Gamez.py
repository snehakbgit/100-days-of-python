import tkinter as tk
from tkinter import messagebox

# ---------------- CONFIG ----------------
CELL_SIZE = 80
COLS = 7

START_POS = 5   # x = 6
GOAL_POS = 4    # x = 5
WALLS = [0, 6]  # walls at x = 1 and x = 7
# ---------------------------------------


class ReeborgGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Reeborg's World – Task Driven Learning")

        self.canvas = tk.Canvas(
            root,
            width=COLS * CELL_SIZE,
            height=CELL_SIZE,
            bg="#fdf6e3"
        )
        self.canvas.pack(pady=10)

        self.info = tk.Label(root, text="", font=("Arial", 12))
        self.info.pack()

        self.create_controls()
        self.reset()

    # ---------------- GAME LOGIC ----------------
    def reset(self):
        self.robot_pos = START_POS
        self.direction = "W"
        self.draw_world()
        self.update_info("Facing West")

    def move(self):
        next_pos = self.robot_pos - 1 if self.direction == "W" else self.robot_pos + 1

        if next_pos in WALLS or not (0 <= next_pos < COLS):
            messagebox.showwarning("Blocked!", "Wall ahead!")
            return

        self.robot_pos = next_pos
        self.draw_world()
        self.check_goal()

    def turn_left(self):
        self.direction = "E" if self.direction == "W" else "W"
        self.update_info(f"Facing {'West' if self.direction == 'W' else 'East'}")

    def check_goal(self):
        if self.robot_pos == GOAL_POS:
            messagebox.showinfo("Success 🎉", "Task Completed!")

    # ---------------- UI ----------------
    def draw_world(self):
        self.canvas.delete("all")

        for col in range(COLS):
            x1 = col * CELL_SIZE
            x2 = x1 + CELL_SIZE
            self.canvas.create_rectangle(x1, 0, x2, CELL_SIZE, outline="brown", width=3)
            self.canvas.create_text(x1 + CELL_SIZE / 2, CELL_SIZE - 10, text=str(col + 1))

        for wall in WALLS:
            wx = wall * CELL_SIZE
            self.canvas.create_rectangle(
                wx, 0, wx + CELL_SIZE, CELL_SIZE,
                fill="#8b0000"
            )

        gx = GOAL_POS * CELL_SIZE + CELL_SIZE / 2
        self.canvas.create_text(gx, CELL_SIZE / 2, text="⭐", font=("Arial", 30))

        rx = self.robot_pos * CELL_SIZE + CELL_SIZE / 2
        self.canvas.create_text(rx, CELL_SIZE / 2, text="🤖", font=("Arial", 30))

    def update_info(self, text):
        self.info.config(text=text)

    def create_controls(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="Turn Left", width=12, command=self.turn_left).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Move", width=12, command=self.move).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Reset", width=12, command=self.reset).grid(row=0, column=2, padx=5)

        tk.Button(
            self.root,
            text="▶ Run Student Code",
            width=20,
            command=self.run_student_code
        ).pack(pady=5)

    # ---------------- STUDENT CODE ----------------
    def run_student_code(self):
        self.reset()
        try:
            exec(student_code, {"move": self.move, "turn_left": self.turn_left})
        except Exception as e:
            messagebox.showerror("Error", str(e))


# ---------------- STUDENT AREA ----------------
student_code = """
turn_left()
move()
"""
# ----------------------------------------------


if __name__ == "__main__":
    root = tk.Tk()
    game = ReeborgGame(root)
    root.mainloop()
