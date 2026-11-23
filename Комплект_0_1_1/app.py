import tkinter as tk
from datetime import datetime
from pathlib import Path

LIMIT = 5
STATUSES = ["Запланировано", "Читаю", "Дочитано"]

count = 0
closed = 0
status_index = 0

root = tk.Tk()
root.title("Читательский дневник 0.1.1")
root.geometry("420x360")
root.resizable(False, False)

logo_path = Path(__file__).with_name("logo.png")
logo_img = tk.PhotoImage(file=str(logo_path))

header_frame = tk.Frame(root, pady=10)
header_frame.pack()
tk.Label(header_frame, image=logo_img).pack(side=tk.LEFT, padx=8)
tk.Label(header_frame, text="Читательский дневник", font=("Arial", 16, "bold")).pack(side=tk.LEFT)

count_label = tk.Label(root, text="Книг в списке: 0", font=("Arial", 13))
count_label.pack(pady=4)

date_label = tk.Label(root, text="Добавлено: —", font=("Arial", 11))
date_label.pack(pady=4)

status_label = tk.Label(root, text="Статус: Запланировано", font=("Arial", 12, "bold"), fg="#1b5e20")
status_label.pack(pady=4)

closed_label = tk.Label(root, text="Дочитано книг: 0", font=("Arial", 11))
closed_label.pack(pady=4)

def add_book():
    global count
    if count >= LIMIT:
        return
    count += 1
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    date_label.config(text=f"Добавлено: {now}")
    if count >= LIMIT:
        count_label.config(text=f"Дневная цель: {LIMIT}")
        btn_add.config(state=tk.DISABLED)
    else:
        count_label.config(text=f"Книг в списке: {count}")

def change_status():
    global status_index, closed
    status_index = (status_index + 1) % len(STATUSES)
    current = STATUSES[status_index]
    status_label.config(text=f"Статус: {current}")
    if current == "Дочитано":
        closed += 1
        closed_label.config(text=f"Дочитано книг: {closed}")

def reset_all():
    global count, closed, status_index
    count = 0
    closed = 0
    status_index = 0
    count_label.config(text="Книг в списке: 0")
    date_label.config(text="Добавлено: —")
    status_label.config(text="Статус: Запланировано")
    closed_label.config(text="Дочитано книг: 0")
    btn_add.config(state=tk.NORMAL)

btn_frame = tk.Frame(root, pady=12)
btn_frame.pack()

btn_add = tk.Button(btn_frame, text="Добавить книгу", width=22, font=("Arial", 11), command=add_book)
btn_add.pack(pady=4)

btn_status = tk.Button(btn_frame, text="Сменить статус", width=22, font=("Arial", 11), command=change_status)
btn_status.pack(pady=4)

btn_reset = tk.Button(btn_frame, text="Сбросить", width=22, font=("Arial", 11), command=reset_all)
btn_reset.pack(pady=4)

tk.Label(root, text="Версия 0.1.1", font=("Arial", 9), fg="gray").pack(side=tk.BOTTOM, pady=6)

root.mainloop()
