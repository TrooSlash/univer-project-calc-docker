"""
Тесты для калькулятора
Unit tests for Calculator application
"""

import pytest
import sys
from PySide6.QtWidgets import QApplication
from calculator import Calculator


@pytest.fixture
def app(qtbot):
    """Создание экземпляра приложения для тестов"""
    test_app = QApplication.instance()
    if test_app is None:
        test_app = QApplication(sys.argv)
    return test_app


@pytest.fixture
def calculator(qtbot, app):
    """Создание экземпляра калькулятора для тестов"""
    calc = Calculator()
    qtbot.addWidget(calc)
    return calc


class TestCalculator:
    """Класс тестов для калькулятора"""
    
    def test_calculator_initialization(self, calculator):
        """Тест инициализации калькулятора"""
        assert calculator.current_value == ""
        assert calculator.previous_value == ""
        assert calculator.operation == ""
        assert calculator.display.text() == "0"
    
    def test_number_input(self, calculator):
        """Тест ввода чисел"""
        calculator.handle_number("5")
        assert calculator.current_value == "5"
        assert calculator.display.text() == "5"
        
        calculator.handle_number("3")
        assert calculator.current_value == "53"
        assert calculator.display.text() == "53"
    
    def test_decimal_input(self, calculator):
        """Тест ввода десятичных чисел"""
        calculator.handle_number("3")
        calculator.handle_number(".")
        calculator.handle_number("1")
        calculator.handle_number("4")
        assert calculator.current_value == "3.14"
        assert calculator.display.text() == "3.14"
    
    def test_multiple_decimal_points(self, calculator):
        """Тест предотвращения множественных точек"""
        calculator.handle_number("3")
        calculator.handle_number(".")
        calculator.handle_number("1")
        calculator.handle_number(".")  # Вторая точка не должна быть добавлена
        assert calculator.current_value == "3.1"
    
    def test_addition(self, calculator):
        """Тест сложения"""
        calculator.handle_number("5")
        calculator.handle_operation("+")
        calculator.handle_number("3")
        calculator.calculate_result()
        assert calculator.current_value == "8"
        assert calculator.display.text() == "8"
    
    def test_subtraction(self, calculator):
        """Тест вычитания"""
        calculator.handle_number("1")
        calculator.handle_number("0")
        calculator.handle_operation("-")
        calculator.handle_number("3")
        calculator.calculate_result()
        assert calculator.current_value == "7"
        assert calculator.display.text() == "7"
    
    def test_multiplication(self, calculator):
        """Тест умножения"""
        calculator.handle_number("4")
        calculator.handle_operation("*")
        calculator.handle_number("5")
        calculator.calculate_result()
        assert calculator.current_value == "20"
        assert calculator.display.text() == "20"
    
    def test_division(self, calculator):
        """Тест деления"""
        calculator.handle_number("1")
        calculator.handle_number("5")
        calculator.handle_operation("/")
        calculator.handle_number("3")
        calculator.calculate_result()
        result = float(calculator.current_value)
        assert abs(result - 5.0) < 0.001
    
    def test_division_by_zero(self, calculator):
        """Тест деления на ноль"""
        calculator.handle_number("5")
        calculator.handle_operation("/")
        calculator.handle_number("0")
        calculator.calculate_result()
        assert calculator.current_value == ""
        assert calculator.display.text() == "0"
    
    def test_clear_all(self, calculator):
        """Тест полной очистки"""
        calculator.handle_number("5")
        calculator.handle_operation("+")
        calculator.handle_number("3")
        calculator.clear_all()
        assert calculator.current_value == ""
        assert calculator.previous_value == ""
        assert calculator.operation == ""
        assert calculator.display.text() == "0"
    
    def test_clear_entry(self, calculator):
        """Тест очистки текущего ввода"""
        calculator.handle_number("5")
        calculator.handle_number("3")
        calculator.clear_entry()
        assert calculator.current_value == ""
        assert calculator.display.text() == "0"
    
    def test_backspace(self, calculator):
        """Тест удаления последнего символа"""
        calculator.handle_number("1")
        calculator.handle_number("2")
        calculator.handle_number("3")
        calculator.backspace()
        assert calculator.current_value == "12"
        assert calculator.display.text() == "12"
    
    def test_toggle_sign_positive_to_negative(self, calculator):
        """Тест изменения знака с положительного на отрицательный"""
        calculator.handle_number("5")
        calculator.toggle_sign()
        assert calculator.current_value == "-5"
        assert calculator.display.text() == "-5"
    
    def test_toggle_sign_negative_to_positive(self, calculator):
        """Тест изменения знака с отрицательного на положительный"""
        calculator.handle_number("5")
        calculator.toggle_sign()
        calculator.toggle_sign()
        assert calculator.current_value == "5"
        assert calculator.display.text() == "5"
    
    def test_chained_operations(self, calculator):
        """Тест цепочки операций"""
        calculator.handle_number("2")
        calculator.handle_operation("+")
        calculator.handle_number("3")
        calculator.handle_operation("*")  # Должно вычислить 2+3=5
        calculator.handle_number("4")
        calculator.calculate_result()  # 5*4=20
        assert calculator.current_value == "20"
    
    def test_decimal_result(self, calculator):
        """Тест результата с десятичной частью"""
        calculator.handle_number("7")
        calculator.handle_operation("/")
        calculator.handle_number("2")
        calculator.calculate_result()
        assert calculator.current_value == "3.5"
        assert calculator.display.text() == "3.5"
    
    def test_negative_numbers_calculation(self, calculator):
        """Тест вычисления с отрицательными числами"""
        calculator.handle_number("5")
        calculator.toggle_sign()
        calculator.handle_operation("+")
        calculator.handle_number("3")
        calculator.calculate_result()
        assert calculator.current_value == "-2"
        assert calculator.display.text() == "-2"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
