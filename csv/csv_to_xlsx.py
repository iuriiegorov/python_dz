import pandas as pd
import tkinter as tk
from tkinter import filedialog

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Анализ CSV-файла")
        self.master.geometry("400x200")
        
        # Создаем кнопку для выбора CSV-файла
        self.choose_button = tk.Button(self.master, text="Выбрать CSV-файл", command=self.choose_file)
        self.choose_button.pack(pady=10)
        
        # Создаем кнопку для запуска анализа данных и создания отчета
        self.analyze_button = tk.Button(self.master, text="Анализировать данные", command=self.analyze_data)
        self.analyze_button.pack(pady=10)
        
        # Создаем метку для отображения статуса программы
        self.status_label = tk.Label(self.master, text="Выберите CSV-файл для анализа")
        self.status_label.pack(pady=10)
        
    def choose_file(self):
        # Открываем диалоговое окно для выбора CSV-файла
        self.filename = filedialog.askopenfilename(initialdir="/", title="Выберите CSV-файл", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        self.status_label.config(text=f"Выбран файл: {self.filename}")
        
    def analyze_data(self):
        try:
            # Читаем CSV-файл
            df = pd.read_csv(self.filename)
            column_min = df.min()

# Создание нового CSV-файла и запись результатов
            column_min.to_csv('summary.csv')

            self.status_label.config(text=f"Отчет успешно создан")
        except:
            # Если произошла ошибка, обновляем метку статуса
            self.status_label.config(text="Ошибка при создании отчета")

root = tk.Tk()
app = App(root)
root.mainloop()
