"""
Простой калькулятор на PySide6
Simple Calculator using PySide6 for CI/CD demonstration
"""

import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, 
                               QPushButton, QLineEdit, QVBoxLayout)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class Calculator(QMainWindow):
    """Главный класс калькулятора"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setFixedSize(350, 450)
        
        # Инициализация переменных
        self.current_value = ""
        self.previous_value = ""
        self.operation = ""
        
        # Создание интерфейса
        self.init_ui()
        
    def init_ui(self):
        """Инициализация пользовательского интерфейса"""
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Основной layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Дисплей для отображения чисел
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(60)
        font = QFont()
        font.setPointSize(18)
        self.display.setFont(font)
        self.display.setText("0")
        layout.addWidget(self.display)
        
        # Сетка кнопок
        button_grid = QGridLayout()
        layout.addLayout(button_grid)
        
        # Определение кнопок
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0), ('CE', 4, 1), ('←', 4, 2), ('±', 4, 3),
        ]
        
        # Создание и размещение кнопок
        for button_text, row, col in buttons:
            button = QPushButton(button_text)
            button.setFixedSize(70, 60)
            button_font = QFont()
            button_font.setPointSize(14)
            button.setFont(button_font)
            button.clicked.connect(lambda checked, text=button_text: self.on_button_click(text))
            button_grid.addWidget(button, row, col)
    
    def on_button_click(self, text):
        """Обработка нажатия кнопок"""
        if text.isdigit() or text == '.':
            self.handle_number(text)
        elif text in ['+', '-', '*', '/']:
            self.handle_operation(text)
        elif text == '=':
            self.calculate_result()
        elif text == 'C':
            self.clear_all()
        elif text == 'CE':
            self.clear_entry()
        elif text == '←':
            self.backspace()
        elif text == '±':
            self.toggle_sign()
    
    def handle_number(self, number):
        """Обработка ввода цифр"""
        if number == '.' and '.' in self.current_value:
            return
        
        if self.current_value == "0" and number != '.':
            self.current_value = number
        else:
            self.current_value += number
        
        self.update_display(self.current_value)
    
    def handle_operation(self, op):
        """Обработка математических операций"""
        if self.current_value:
            if self.previous_value and self.operation:
                self.calculate_result()
            self.previous_value = self.current_value
            self.current_value = ""
            self.operation = op
    
    def calculate_result(self):
        """Вычисление результата"""
        if not self.previous_value or not self.operation:
            return
        
        if not self.current_value:
            self.current_value = self.previous_value
        
        try:
            prev = float(self.previous_value)
            curr = float(self.current_value)
            
            if self.operation == '+':
                result = prev + curr
            elif self.operation == '-':
                result = prev - curr
            elif self.operation == '*':
                result = prev * curr
            elif self.operation == '/':
                if curr == 0:
                    self.update_display("Ошибка")
                    self.clear_all()
                    return
                result = prev / curr
            else:
                return
            
            # Форматирование результата
            if result == int(result):
                result = int(result)
            else:
                result = round(result, 8)
            
            self.current_value = str(result)
            self.update_display(self.current_value)
            self.previous_value = ""
            self.operation = ""
            
        except Exception as e:
            self.update_display("Ошибка")
            self.clear_all()
    
    def clear_all(self):
        """Полная очистка"""
        self.current_value = ""
        self.previous_value = ""
        self.operation = ""
        self.update_display("0")
    
    def clear_entry(self):
        """Очистка текущего ввода"""
        self.current_value = ""
        self.update_display("0")
    
    def backspace(self):
        """Удаление последнего символа"""
        if self.current_value:
            self.current_value = self.current_value[:-1]
            self.update_display(self.current_value if self.current_value else "0")
    
    def toggle_sign(self):
        """Изменение знака числа"""
        if self.current_value and self.current_value != "0":
            if self.current_value.startswith('-'):
                self.current_value = self.current_value[1:]
            else:
                self.current_value = '-' + self.current_value
            self.update_display(self.current_value)
    
    def update_display(self, value):
        """Обновление дисплея"""
        self.display.setText(str(value))


def main():
    """Главная функция запуска приложения"""
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
