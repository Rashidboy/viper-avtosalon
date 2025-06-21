import tkinter as tk
from tkinter import messagebox
import mysql.connector
from dotenv import load_dotenv
import os

# .env faylidan parolni o'qish
load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")

# MySQL ulanish funksiyasi
def get_data(query):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=DB_PASSWORD,
            database="avtosalon"
        )
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        messagebox.showerror("MySQL xatosi", f"Xato: {err}")
        return []
    finally:
        if connection and connection.is_connected():
            connection.close()

# Mashinalar jadvalini olish funksiyasi
def load_mashinalar():
    listbox.delete(0, tk.END)
    query = "SELECT id, model, narx, yil FROM mashinalar"
    result = get_data(query)
    if result:
        for row in result:
            listbox.insert(tk.END, f"ID: {row[0]}, Model: {row[1]}, Narx: {row[2]} USD, Yil: {row[3]}")
    else:
        listbox.insert(tk.END, "Hech qanday ma'lumot topilmadi.")

# Mijozlar jadvalini olish funksiyasi
def load_mijozlar():
    listbox.delete(0, tk.END)
    query = "SELECT id, ism, telefon FROM mijozlar"
    result = get_data(query)
    if result:
        for row in result:
            listbox.insert(tk.END, f"ID: {row[0]}, Ism: {row[1]}, Telefon: {row[2]}")
    else:
        listbox.insert(tk.END, "Hech qanday ma'lumot topilmadi.")

# Xodimlar jadvalini olish funksiyasi
def load_xodimlar():
    listbox.delete(0, tk.END)
    query = "SELECT id, ism, lavozim FROM xodimlar"
    result = get_data(query)
    if result:
        for row in result:
            listbox.insert(tk.END, f"ID: {row[0]}, Ism: {row[1]}, Lavozim: {row[2]}")
    else:
        listbox.insert(tk.END, "Hech qanday ma'lumot topilmadi.")

# Savdo jadvalini olish funksiyasi
def load_savdo():
    listbox.delete(0, tk.END)
    query = "SELECT id, mashina_id, mijoz_id, sana FROM savdo"
    result = get_data(query)
    if result:
        for row in result:
            listbox.insert(tk.END, f"ID: {row[0]}, Mashina ID: {row[1]}, Mijoz ID: {row[2]}, Sana: {row[3]}")
    else:
        listbox.insert(tk.END, "Hech qanday ma'lumot topilmadi.")

# To'lovlar jadvalini olish funksiyasi
def load_tolovlar():
    listbox.delete(0, tk.END)
    query = "SELECT id, savdo_id, summa, sana FROM tolovlar"
    result = get_data(query)
    if result:
        for row in result:
            listbox.insert(tk.END, f"ID: {row[0]}, Savdo ID: {row[1]}, Summa: {row[2]} USD, Sana: {row[3]}")
    else:
        listbox.insert(tk.END, "Hech qanday ma'lumot topilmadi.")

# Servislar jadvalini olish funksiyasi
def load_servislar():
    listbox.delete(0, tk.END)
    query = "SELECT id, mashina_id, xizmat_turi, narx FROM servislar"
    result = get_data(query)
    if result:
        for row in result:
            listbox.insert(tk.END, f"ID: {row[0]}, Mashina ID: {row[1]}, Xizmat: {row[2]}, Narx: {row[3]} USD")
    else:
        listbox.insert(tk.END, "Hech qanday ma'lumot topilmadi.")

# Oynani markazlash funksiyasi
def center_window(width=600, height=400):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x}+{y}')

# Ilova oynasini yaratish
window = tk.Tk()
window.title("Avtosalon Ilovasi")
window.geometry("800x600")
window.configure(bg="#262626")

# Oynani markazda chiqaramiz
center_window(600, 400)

# Ranglar va shriftlar qo'shamiz
window.configure(bg='#262626')
window.option_add('*Font', 'Helvetica 12')

# Menyu paneli
menubar = tk.Menu(window)
window.config(menu=menubar)

# "Bo'limlar" menusi
sections_menu = tk.Menu(menubar, tearoff=0, bg="#444444", fg="#ffffff")
menubar.add_cascade(label="Bo'limlar", menu=sections_menu)
sections_menu.add_command(label="Mashinalar", command=load_mashinalar)
sections_menu.add_command(label="Mijozlar", command=load_mijozlar)
sections_menu.add_command(label="Xodimlar", command=load_xodimlar)
sections_menu.add_command(label="Savdo", command=load_savdo)
sections_menu.add_command(label="To'lovlar", command=load_tolovlar)
sections_menu.add_command(label="Servislar", command=load_servislar)

# Oyna elementi (listbox)
listbox = tk.Listbox(window, width=80, height=20, font=('Helvetica', 10), bg='#333333', fg='#ffffff', bd=2, relief=tk.GROOVE)
listbox.pack(pady=20)

# Tugmalar uchun effektlar qo'shish
def on_enter(e):
    e.widget.config(bg='#555555')

def on_leave(e):
    e.widget.config(bg='#444444')

for item in sections_menu.winfo_children():
    item.bind("<Enter>", on_enter)
    item.bind("<Leave>", on_leave)

# Dasturni ishga tushirish
window.mainloop()