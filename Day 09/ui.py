import tkinter as tk
from tkinter import ttk

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Python Robot Simulator")
root.geometry("1200x650")
root.configure(bg="#eaeaea")

# ---------------- Top Bar ----------------
top_bar = tk.Frame(root, bg="#2b5fad", height=50)
top_bar.pack(fill="x", side="top")

language_var = tk.StringVar(value="Python")
language_menu = ttk.Combobox(
    top_bar,
    textvariable=language_var,
    values=["Python", "JavaScript"],
    width=10,
    state="readonly"
)
language_menu.place(x=80, y=12)

lang_label = tk.Label(top_bar, text="Language:", fg="white", bg="#2b5fad")
lang_label.place(x=10, y=12)

region_menu = ttk.Combobox(
    top_bar,
    values=["English", "Deutsch"],
    width=10,
    state="readonly"
)
region_menu.set("Deutsch")
region_menu.place(x=1050, y=12)

# ---------------- Control Bar ----------------
control_bar = tk.Frame(root, bg="#f4f4f4", height=45)
control_bar.pack(fill="x")

btn_play = tk.Button(control_bar, text="▶", width=4)
btn_pause = tk.Button(control_bar, text="⏸", width=4)
btn_stop = tk.Button(control_bar, text="⏹", width=4)

btn_play.pack(side="left", padx=5, pady=5)
btn_pause.pack(side="left", padx=5)
btn_stop.pack(side="left", padx=5)

progress = ttk.Scale(control_bar, from_=0, to=100, orient="horizontal", length=300)
progress.pack(side="left", padx=20)

step_label = tk.Label(control_bar, text="0 / 0", bg="#f4f4f4")
step_label.pack(side="left")

# ---------------- Main Area ----------------
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# ---------------- Canvas (Left) ----------------
canvas_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid")
canvas_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

canvas = tk.Canvas(canvas_frame, bg="white")
canvas.pack(fill="both", expand=True)

# Thinking bubble
canvas.create_oval(350, 220, 650, 350, outline="#1e4fa1", width=6)
canvas.create_text(500, 285, text="Thinking", font=("Arial", 18, "bold"))

# Robot icon (simple)
canvas.create_rectangle(470, 300, 530, 360, fill="#cfcfcf")
canvas.create_rectangle(485, 270, 515, 300, fill="#b0b0b0")

# ---------------- Code Panel (Right) ----------------
code_panel = tk.Frame(main_frame, width=350, bg="#f9f9f9")
code_panel.pack(side="right", fill="y")

code_label = tk.Label(code_panel, text="Code Editor", bg="#f9f9f9", font=("Arial", 12, "bold"))
code_label.pack(anchor="w", padx=10, pady=5)

code_text = tk.Text(code_panel, height=20, width=40, font=("Consolas", 12))
code_text.pack(padx=10, pady=5)
code_text.insert("1.0", "move()\n")

# ---------------- Run Logic (Demo) ----------------
def run_code():
    canvas.itemconfig(2, text="Running...")

btn_play.config(command=run_code)

# ---------------- Start App ----------------
root.mainloop()
