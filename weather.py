from tkinter import *
from tkinter import ttk
import requests

API_KEY = "370dbe75b29e4b0ec1414f7ddc566f3c"

API_KEY = "370dbe75b29e4b0ec1414f7ddc566f3c"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, есть ли ошибки в ответе
        data = response.json()
        print(data)  # Выводим ответ API в консоль для отладки
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"Погода: {weather}, Температура: {temperature}°C"
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP ошибка: {http_err}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Ошибка подключения: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Таймаут запроса: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Ошибка запроса: {req_err}"
    except KeyError as key_err:
        return f"Ошибка в данных: {key_err}"

def show_weather():
    city = city_entry.get()
    if city.strip():  # Проверяем, что поле не пустое
        weather_info = get_weather(city)
        weather_label.config(text=weather_info)
    else:
        weather_label.config(text="Введите название города")

def close_window():
    root.destroy()

def minimize_window():
    root.state('withdrawn')  # Скрывает окно, минимизируя его

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

def start_resize(event):
    global resize_start_x, resize_start_y
    resize_start_x = event.x_root
    resize_start_y = event.y_root
    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+{root.winfo_x()}+{root.winfo_y()}")

def resize_window(event):
    global resize_start_x, resize_start_y
    x = root.winfo_x()
    y = root.winfo_y()
    width = root.winfo_width()
    height = root.winfo_height()

    new_width = width + (event.x_root - resize_start_x)
    new_height = height + (event.y_root - resize_start_y)

    if new_width > 100 and new_height > 100:  # Минимальный размер окна
        root.geometry(f"{new_width}x{new_height}+{x}+{y}")
        resize_start_x = event.x_root
        resize_start_y = event.y_root

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
border_frame = Frame(root, bg="#1f1f1f")
border_frame.pack(fill=X)

# Иконка
icon_photo = PhotoImage(file="img/icon1.png")  # Загружаем иконку
image_label = Label(border_frame, image=icon_photo, bg="#1f1f1f")
image_label.pack(side=LEFT, padx=3, pady=4)

# Заголовок
title_label = Label(border_frame, text="WeatherApp", bg="#1f1f1f", fg="#FFFFFF", font=("Arial", 14))
title_label.pack(side=LEFT, padx=5, pady=4)

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

# Создаем рамку для изменения размера окна
resize_frame = Frame(root, bg="#1f1f1f", cursor="sizing")
resize_frame.pack(side=BOTTOM, fill=X, padx=0, pady=0)

# События для изменения размера окна
resize_frame.bind("<ButtonPress-1>", start_resize)
resize_frame.bind("<B1-Motion>", resize_window)

# Создаем поле для ввода города
city_label = Label(root, text="Введите город:", bg="#4E4E4E", fg="#FFFFFF")
city_label.pack(pady=10)

city_entry = Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

# Кнопка для получения погоды
get_weather_button = Button(root, text="Получить погоду", command=show_weather, bg="#1f1f1f", fg="white", font=("Arial", 14))
get_weather_button.pack(pady=10)

# Метка для отображения информации о погоде
weather_label = Label(root, text="", bg="#4E4E4E", fg="#FFFFFF", font=("Arial", 14))
weather_label.pack(pady=10)

# Выставляем внешний цвета экрана 
style = ttk.Style()
style.configure("TFrame", background="#4E4E4E")  

frame = ttk.Frame(root, style="TFrame")
frame.pack(expand=True, fill="both", padx=0, pady=0)

root.mainloop()