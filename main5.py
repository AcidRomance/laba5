import tkinter as tk
from tkinter import messagebox
import requests

# Функция для получения курсов валют
def get_exchange_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'  # Замените на ваш API адрес
    try:
        response = requests.get(url)
        data = response.json()
        return data['rates']
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось получить курсы валют: {str(e)}")
        return {}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        if from_currency == to_currency:
            result = amount
        else:
            exchange_rate = rates[to_currency] / rates[from_currency]
            result = amount * exchange_rate

        result_label.config(text=f"Результат: {result:.2f} {to_currency}")

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректную сумму.")

def update_amount(value):
    amount_entry.delete(0, tk.END)  # Очистить поле ввода
    amount_entry.insert(0, value)    # Вставить новое значение

# Основное окно
root = tk.Tk()
root.title("Конвертер валюты")

# Получение курсов валют
rates = get_exchange_rates()

# Переменные для хранения состояния чекбоксов
from_currency_var = tk.StringVar(value='USD')
to_currency_var = tk.StringVar(value='EUR')

# Создание интерфейса
tk.Label(root, text="Сумма:").pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

# Ползунок для выбора суммы валюты
amount_slider = tk.Scale(root, from_=1, to=1000, orient=tk.HORIZONTAL, command=update_amount)  # Максимум 1000
amount_slider.pack()

tk.Label(root, text="Из какой валюты:").pack()
from_currency_menu = tk.OptionMenu(root, from_currency_var, *rates.keys())
from_currency_menu.pack()

tk.Label(root, text="В какую валюту:").pack()
to_currency_menu = tk.OptionMenu(root, to_currency_var, *rates.keys())
to_currency_menu.pack()

tk.Button(root, text="Конвертировать", command=convert_currency).pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Запуск главного цикла приложения
root.mainloop()