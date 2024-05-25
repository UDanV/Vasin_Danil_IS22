import tkinter as tk
from tkinter import ttk

def submit_form():
    print("Форма отправлена")

def clear_form():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)
    specialization_combobox.set('')
    gender_var.set('')
    for skill in skills_vars:
        skill.set(0)
    additional_info_text.delete('1.0', tk.END)

root = tk.Tk()
root.title("Анкета Web-разработчика")

# Создание меток и полей ввода с бордерами
tk.Label(root, text="Регистрационное имя", background="#BFBFBF", relief="solid", bd=1).grid(row=0, column=0, sticky='w', padx=3, pady=3)
username_entry = tk.Entry(root, relief="solid", bd=1)
username_entry.grid(row=0, column=1, padx=0, pady=0)

tk.Label(root, text="Пароль", background="#BFBFBF", relief="solid", bd=1).grid(row=1, column=0, sticky='w', padx=3, pady=3)
password_entry = tk.Entry(root, show='*', relief="solid", bd=1)
password_entry.grid(row=1, column=1, padx=0, pady=0)

tk.Label(root, text="Подтвердите пароль", background="#D1DAC9", relief="solid", bd=1).grid(row=2, column=2, sticky='w', padx=3, pady=3)
confirm_password_entry = tk.Entry(root, show='*', relief="solid", bd=1)
confirm_password_entry.grid(row=2, column=1, padx=0, pady=0)

tk.Label(root, text="Ваша специализация", background="#BFBFBF", relief="solid", bd=1).grid(row=3, column=0, sticky='w', padx=3, pady=3)
specialization_combobox = ttk.Combobox(root, values=["Web-мастер", "Программист", "Дизайнер"])
specialization_combobox.grid(row=3, column=1, padx=0, pady=0)

tk.Label(root, text="Пол", background="#BFBFBF", relief="solid", bd=1).grid(row=4, column=0, sticky='w', padx=3, pady=3)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="М", variable=gender_var, value="М", relief="solid", bd=1).grid(row=4, column=1, sticky='w', padx=3, pady=3)
tk.Radiobutton(root, text="Ж", variable=gender_var, value="Ж", relief="solid", bd=1).grid(row=4, column=1, padx=3, pady=3)

tk.Label(root, text="Ваши навыки", background="#BFBFBF", relief="solid", bd=1).grid(row=5, column=0, sticky='w', padx=3, pady=3)
skills = ["знание HTML и CSS", "знание Perl", "знание ASP", "знание Adobe Photoshop", "знание JAVA", "знание JavaScript", "знание Flash"]
skills_vars = [tk.IntVar() for _ in skills]
for i, skill in enumerate(skills):
    tk.Checkbutton(root, text=skill, variable=skills_vars[i], relief="solid", bd=1).grid(row=5+i, column=1, sticky='w', padx=3, pady=3)

tk.Label(root, text="Дополнительные сведения о себе", background="#BFBFBF", relief="solid", bd=1).grid(row=5+len(skills), column=0, sticky='w', padx=3, pady=3)
additional_info_text = tk.Text(root, width=40, height=4, relief="solid", bd=1)
additional_info_text.grid(row=5+len(skills), column=1, columnspan=3, padx=3, pady=3)

# Создание фреймов для изменения фона столбцов с бордерами
for i in range(6 + len(skills)):
    red_frame_0 = tk.Frame(root, background="#BFBFBF")
    red_frame_0.grid(row=i, column=0, sticky='nsew')
    green_frame = tk.Frame(root, background="#D1DAC9")
    green_frame.grid(row=i, column=1, sticky='nsew')
    red_frame_2 = tk.Frame(root, background="#D1DAC9")
    red_frame_2.grid(row=i, column=2, sticky='nsew')
    frame_3 = tk.Frame(root, background="#D1DAC9")
    frame_3.grid(row=i, column=3, sticky='nsew')

# Повторное размещение меток и полей ввода
tk.Label(root, text="Регистрационное имя", background="#BFBFBF", relief="solid", bd=1).grid(row=0, column=0, sticky='w', padx=3, pady=3)
username_entry = tk.Entry(root, relief="solid", bd=1)
username_entry.grid(row=0, column=1, padx=0, pady=0)

tk.Label(root, text="Пароль", background="#BFBFBF", relief="solid", bd=1).grid(row=1, column=0, sticky='w')
password_entry = tk.Entry(root, show='*', relief="solid", bd=1)
password_entry.grid(row=1, column=1, padx=0, pady=0)

tk.Label(root, text=":подтвердите пароль", background="#D1DAC9", relief="solid", bd=1).grid(row=2, column=2, sticky='w', padx=3, pady=3)
confirm_password_entry = tk.Entry(root, show='*', relief="solid", bd=1)
confirm_password_entry.grid(row=2, column=1, padx=0, pady=0)

tk.Label(root, text="Ваша специализация", background="#BFBFBF", relief="solid", bd=1).grid(row=3, column=0, sticky='w', padx=3, pady=3)
specialization_combobox = ttk.Combobox(root, values=["Web-мастер", "Программист", "Дизайнер"])
specialization_combobox.grid(row=3, column=1, padx=0, pady=0)

tk.Label(root, text="Пол", background="#BFBFBF", relief="solid", bd=1).grid(row=4, column=0, sticky='w', padx=3, pady=3)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="М", variable=gender_var, value="М", relief="solid", bd=1).grid(row=4, column=1, sticky='w', padx=3, pady=3)
tk.Radiobutton(root, text="Ж", variable=gender_var, value="Ж", relief="solid", bd=1).grid(row=4, column=1, padx=3, pady=3)

tk.Label(root, text="Ваши навыки", background="#BFBFBF", relief="solid", bd=1).grid(row=5, column=0, sticky='w', padx=3, pady=3)
for i, skill in enumerate(skills):
    tk.Checkbutton(root, text=skill, variable=skills_vars[i], relief="solid", bd=1).grid(row=5+i, column=1, sticky='w', padx=3, pady=3)

tk.Label(root, text="Дополнительные сведения о себе", background="#BFBFBF", relief="solid", bd=1).grid(row=5+len(skills), column=0, sticky='w', padx=3, pady=3)
additional_info_text = tk.Text(root, width=40, height=4, relief="solid", bd=1)
additional_info_text.grid(row=5+len(skills), column=1, columnspan=3, padx=3, pady=3)

# Создание фрейма для кнопок с бордером сверху
button_frame = tk.Frame(root, highlightbackground="black", highlightthickness=0)
button_frame.grid(row=6+len(skills), column=0, columnspan=1, sticky='ew')

# Кнопки в отдельном фрейме, расположенные рядом слева
submit_button = tk.Button(button_frame, text="зарегистрировать", command=submit_form)
submit_button.grid(row=1, column=0, sticky='w', padx=5, pady=5)

clear_button = tk.Button(button_frame, text="очистить форму", command=clear_form)
clear_button.grid(row=1, column=1, sticky='w', padx=5, pady=5)

# Настройка столбцов для растяжения
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)
button_frame.grid_columnconfigure(3, weight=1)

root.mainloop()
