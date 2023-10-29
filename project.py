import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk


# Создание базы данных и таблицы
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees
    (id INTEGER PRIMARY KEY,
     full_name TEXT,
     phone_number TEXT,
     email TEXT,
     salary REAL)
''')
conn.commit()

# Функция для добавления нового сотрудника
def add_employee():
    full_name = entry_name.get()
    phone_number = entry_phone.get()
    email = entry_email.get()
    salary = entry_salary.get()
    cursor.execute('''
        INSERT INTO employees (full_name, phone_number, email, salary)
        VALUES (?, ?, ?, ?)
    ''', (full_name, phone_number, email, salary))
    conn.commit()
    messagebox.showinfo("Успех", "Новый сотрудник добавлен.")
    update_treeview()

# Функция для удаления сотрудника
def delete_employee():
    employee_id = entry_delete_id.get()
    cursor.execute('DELETE FROM employees WHERE id=?', (employee_id,))
    conn.commit()
    messagebox.showinfo("Успех", f"Сотрудник с ID {employee_id} удален.")
    update_treeview()

# Функция для обновления данных сотрудника
def update_employee():
    employee_id = entry_update_id.get()
    full_name = entry_update_name.get()
    phone_number = entry_update_phone.get()
    email = entry_update_email.get()
    salary = entry_update_salary.get()
    cursor.execute('''
        UPDATE employees
        SET full_name=?, phone_number=?, email=?, salary=?
        WHERE id=?
    ''', (full_name, phone_number, email, salary, employee_id))
    conn.commit()
    messagebox.showinfo("Успех", f"Данные сотрудника с ID {employee_id} обновлены.")
    update_treeview()

# Функция для поиска сотрудника по ФИО
def search_employee():
    search_name = entry_search_name.get()
    cursor.execute('SELECT * FROM employees WHERE full_name=?', (search_name,))
    results = cursor.fetchall()
    if results:
        messagebox.showinfo("Результат поиска", f"Найдены сотрудники: {results}")
    else:
        messagebox.showinfo("Результат поиска", "Сотрудник не найден.")
    update_treeview()

# Функция для обновления виджета Treeview
def update_treeview():
    tree.delete(*tree.get_children())
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)

# Создание главного окна
root = tk.Tk()
root.title("Список сотрудников компании")
root.geometry('1050x650')
root.resizable(width = False,height = False)
root.config( bg='#008080')

# Добавление сотрудника
label_name = tk.Label(root, text="ФИО:",bg='#008080')
label_name.place(x=30, y=250)
entry_name = tk.Entry(root)
entry_name.place(x=30, y=270)

label_phone = tk.Label(root, text="Номер телефона:",bg='#008080')
label_phone.place(x=30, y=290)
entry_phone = tk.Entry(root)
entry_phone.place(x=30, y=310)

label_email = tk.Label(root, text="Email:",bg='#008080')
label_email.place(x=30, y=330)
entry_email = tk.Entry(root)
entry_email.place(x=30, y=350)

label_salary = tk.Label(root, text="Заработная плата:",bg='#008080')
label_salary.place(x=30, y=370)
entry_salary = tk.Entry(root)
entry_salary.place(x=30, y=390)

Imgbutton_add = ImageTk.PhotoImage(file='./img/add.png')
button_add = tk.Button(root, text="", image=Imgbutton_add, height=40, compound= "bottom",  command=add_employee)
button_add.place(x=30, y=430)

# Удаление сотрудника
label_delete_id = tk.Label(root, text="ID сотрудника для удаления:",bg='#008080')
label_delete_id.place(x=220, y=250)
entry_delete_id = tk.Entry(root)
entry_delete_id.place(x=230, y=270)

Imgbutton_delete = ImageTk.PhotoImage(file='./img/delete.png')
button_delete = tk.Button(root, text="", image=Imgbutton_delete, height=60, command=delete_employee)
button_delete.place(x=250, y=310)


# Обновление сотрудника
label_update_id = tk.Label(root, text="ID сотрудника для обновления:",bg='#008080')
label_update_id.place(x=420, y=250)
entry_update_id = tk.Entry(root)
entry_update_id.place(x=430, y=270)

label_update_name = tk.Label(root, text="Новое ФИО:",bg='#008080')
label_update_name.place(x=420, y=290)
entry_update_name = tk.Entry(root)
entry_update_name.place(x=430, y=310)

label_update_phone = tk.Label(root, text="Новый номер телефона:",bg='#008080')
label_update_phone.place(x=420, y=330)
entry_update_phone = tk.Entry(root)
entry_update_phone.place(x=430, y=350)

label_update_email = tk.Label(root, text="Новый Email:",bg='#008080')
label_update_email.place(x=420, y=370)
entry_update_email = tk.Entry(root)
entry_update_email.place(x=430, y=390)

label_update_salary = tk.Label(root, text="Новая заработная плата:",bg='#008080')
label_update_salary.place(x=420, y=410)
entry_update_salary = tk.Entry(root)
entry_update_salary.place(x=430, y=430)


Imgbutton_update = ImageTk.PhotoImage(file='./img/change.png')
button_update = tk.Button(root, text="Обновить сотрудника", image=Imgbutton_update, height=55, command=update_employee)
button_update.place(x=430, y=470)

# Поиск сотрудника
label_search_name = tk.Label(root, text="ФИО для поиска:",bg='#008080')
label_search_name.place(x=680, y=250)
entry_search_name = tk.Entry(root)
entry_search_name.place(x=680, y=270)

Imgbutton_search = ImageTk.PhotoImage(file='./img/search.png')
button_search = tk.Button(root, text="Найти сотрудника", image=Imgbutton_search, height=55, command=search_employee)
button_search.place(x=680, y=310)

# Создание Treeview
tree = ttk.Treeview(root, column=("column1", "column2", "column3", "column4", "column5"), show='headings')
tree.heading("#1", text="ID")
tree.heading("#2", text="ФИО")
tree.heading("#3", text="Номер телефона")
tree.heading("#4", text="Email")
tree.heading("#5", text="Заработная плата")
tree.place(x=20, y=20)

label_ogr3 = tk.Label(text='',bg='#008080')
label_ogr3.grid(row=1, column=0)

label_ogr4 = tk.Label(text='',bg='#008080')
label_ogr4.grid(row=2, column=0)

# Заполнение Treeview данными из базы данных
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()
for row in rows:
    tree.insert("", tk.END, values=row)

# Запуск главного цикла событий
root.mainloop()

# Закрытие соединения с базой данных
conn.close()
