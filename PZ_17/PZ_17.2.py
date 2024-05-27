"""
Разработать программу с применением пакета tk, взяв в качестве условия одну
любую задачу из ПЗ №№ 2 – 9.
"""
import tkinter as tk
from tkinter import messagebox

def check_even_odd():
    try:
        A = int(entry.get())
        if A % 2 == 0:
            result = f"Число {A} является чётным"
        else:
            result = f"Число {A} является нечётным"
        messagebox.showinfo("Результат", result)
    except ValueError:
        messagebox.showerror("Ошибка", "Ошибка ввода. Введите целое число")

root = tk.Tk()
root.title("Проверка чётности числа")

label = tk.Label(root, text="Введите целое число:")
label.pack(pady=10, padx=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Проверить", command=check_even_odd)
button.pack(pady=20)

root.mainloop()
