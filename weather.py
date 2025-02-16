from tkinter import *
from tkinter import ttk

def close_window():
    root.destroy()

def minimize_window():
    root.iconify() 

def maximize_window():
    if root.winfo_height() < screen_height and root.winfo_width() < screen_width:
        root.geometry(f"{screen_width}x{screen_height}+0+0")  # Разворачивает на весь экран
    else:
        root.geometry(f"{window_width}x{window_height}+0+0")  # Возвращает к первоначальному размеру

def on_enter_close(event):
    close_button.config(bg="#e81123")  # Изменяем цвет кнопки на красный при наведении

def on_leave_close(event):
    close_button.config(bg='#1f1f1f')  # Возвращаем цвет кнопки на серый при уходе мыши

def on_enter_minimize(event):
    minimize_button.config(bg="#373737")  # Изменяем цвет кнопки на #373737 при наведении

def on_leave_minimize(event):
    minimize_button.config(bg="#1f1f1f")  # Возвращаем цвет кнопки на серый при уходе мыши

def on_enter_maximize(event):
    maximize_button.config(bg="#373737")  # Изменяем цвет кнопки на #373737 при наведении

def on_leave_maximize(event):
    maximize_button.config(bg="#1f1f1f")  # Возвращаем цвет кнопки на серый при уходе мыши


root = Tk()     
root.title("WeatherApp")
root.iconbitmap("img/IconApp.ico")

# Получаем размеры экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Получаем половины размеров экрана
window_width = root.winfo_screenwidth() // 2 
window_height = root.winfo_screenheight() // 2

# Выставляем внешний вид в верхнем левом углу размерами в половину экрана
root.geometry(f"{window_width}x{window_height}+0+0")

# Убираем внешнюю рамку
root.overrideredirect(True)

# Создаем свою рамку с нужным цветом
border_frame = Frame(root, bg="#1f1f1f", height=100)
border_frame.pack(fill=X)

# Заголовок
title_label = Label(border_frame, text="WeatherApp", bg="#1f1f1f", fg="#FFFFFF", font=("Arial", 14))
title_label.pack(side=LEFT, padx=10, pady=4)

# Кнопка закрытия
close_button = Button(border_frame, text="X", command=close_window, bg="#1f1f1f", fg="white", font=("Arial", 14))
close_button.pack(side=RIGHT, padx=0)  # Установка кнопки закрытия

# События кнопки закрытия
close_button.bind("<Enter>", on_enter_close)  # При наведении
close_button.bind("<Leave>", on_leave_close)   # При уходе мыши

# Кнопка минимизации
minimize_button = Button(border_frame, text="_", command=minimize_window, bg="#1f1f1f", fg="white", font=("Arial", 14))
minimize_button.pack(side=RIGHT, padx=0)  # Установка кнопки минимизации

# События кнопки минимизации
minimize_button.bind("<Enter>", on_enter_minimize)  # При наведении
minimize_button.bind("<Leave>", on_leave_minimize)   # При уходе мыши

# Кнопка разворачивания
maximize_button = Button(border_frame, text="[ ]", command=maximize_window, bg="#1f1f1f", fg="white", font=("Arial", 14))
maximize_button.pack(side=RIGHT, padx=0)  # Установка кнопки разворачивания

# События кнопки разворачивания
maximize_button.bind("<Enter>", on_enter_maximize)  # При наведении
maximize_button.bind("<Leave>", on_leave_maximize)   # При уходе мыши

# выставляем внешний цвета экрана 
style = ttk.Style()
style.configure("TFrame", background="#4E4E4E")  

frame = ttk.Frame(root, style="TFrame")
frame.pack(expand=True, fill="both", padx=0, pady=0)

root.mainloop()
