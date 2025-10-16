# Калькулятор с CI/CD | Calculator with CI/CD

![CI/CD Pipeline](https://github.com/TrooSlash/univer-project-calc-docker/workflows/CI/CD%20Pipeline/badge.svg)

Простое приложение-калькулятор на Python с использованием PySide6 для демонстрации CI/CD процессов с GitHub Actions и Docker.

A simple calculator application built with Python and PySide6 to demonstrate CI/CD processes using GitHub Actions and Docker.

## 🚀 Особенности | Features

- ✅ Базовые арифметические операции (сложение, вычитание, умножение, деление)
- ✅ Работа с десятичными числами
- ✅ Изменение знака числа
- ✅ Удаление символов (Backspace)
- ✅ Очистка ввода и полная очистка
- ✅ Современный графический интерфейс на PySide6
- ✅ Полное покрытие unit-тестами
- ✅ CI/CD pipeline с GitHub Actions
- ✅ Докеризация приложения

## 📋 Требования | Requirements

- Python 3.11+
- PySide6
- pytest (для тестирования)

## 🔧 Установка | Installation

### Локальная установка | Local Installation

```bash
# Клонировать репозиторий
git clone https://github.com/TrooSlash/univer-project-calc-docker.git
cd univer-project-calc-docker

# Создать виртуальное окружение
python -m venv venv

# Активировать виртуальное окружение
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Установить зависимости
pip install -r requirements.txt
```

## 🎮 Использование | Usage

### Запуск приложения | Running the Application

```bash
python calculator.py
```

### Запуск тестов | Running Tests

```bash
# Запустить все тесты
pytest test_calculator.py -v

# Запустить с покрытием кода
pytest test_calculator.py -v --cov=calculator --cov-report=html
```

## 🐳 Docker

### Сборка образа | Build Image

```bash
docker build -t calculator-app .
```

### Запуск контейнера | Run Container

**Windows с WSL2:**
```bash
docker run -it --rm -e DISPLAY=host.docker.internal:0 calculator-app
```

**Linux:**
```bash
# Разрешить подключение к X server
xhost +local:docker

# Запустить контейнер
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  calculator-app

# После использования отключить доступ
xhost -local:docker
```

**macOS с XQuartz:**
```bash
# Установить XQuartz, затем:
xhost +localhost
docker run -it --rm -e DISPLAY=host.docker.internal:0 calculator-app
```

## 🔄 CI/CD Pipeline

Проект использует GitHub Actions для автоматизации:

### Этапы Pipeline:

1. **Test** - Запуск unit-тестов с покрытием кода
2. **Lint** - Проверка качества кода (flake8, pylint)
3. **Build Docker** - Сборка и публикация Docker образа
4. **Deploy** - Информация о развертывании

### Триггеры:

- Push в ветки `main` и `develop`
- Pull requests в ветки `main` и `develop`

## 📁 Структура проекта | Project Structure

```
univer-project-calc-docker/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # CI/CD конфигурация
├── calculator.py              # Основное приложение
├── test_calculator.py         # Unit-тесты
├── requirements.txt           # Python зависимости
├── Dockerfile                 # Docker конфигурация
└── README.md                  # Документация
```

## 🧪 Тестирование | Testing

Проект включает комплексный набор тестов:

- Тест инициализации
- Тест ввода чисел и десятичных дробей
- Тесты всех арифметических операций
- Тест деления на ноль
- Тесты операций очистки
- Тесты изменения знака
- Тесты цепочек операций

Покрытие кода: >90%

## 🛠️ Технологии | Technologies

- **Python 3.11** - Язык программирования
- **PySide6** - GUI фреймворк (Qt6)
- **pytest** - Фреймворк для тестирования
- **GitHub Actions** - CI/CD
- **Docker** - Контейнеризация

## 📝 Конфигурация для Docker Hub

Для автоматической публикации в Docker Hub необходимо настроить secrets в GitHub:

1. `DOCKER_USERNAME` - Имя пользователя Docker Hub
2. `DOCKER_PASSWORD` - Токен доступа Docker Hub

Перейдите в Settings → Secrets and variables → Actions → New repository secret

## 🎯 Использование калькулятора | Calculator Usage

### Кнопки:

- **0-9** - Цифры
- **+, -, *, /** - Математические операции
- **=** - Вычислить результат
- **.** - Десятичная точка
- **C** - Полная очистка (Clear All)
- **CE** - Очистка текущего ввода (Clear Entry)
- **←** - Удалить последний символ (Backspace)
- **±** - Изменить знак числа

## 🤝 Вклад | Contributing

1. Fork репозиторий
2. Создайте feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit изменения (`git commit -m 'Add some AmazingFeature'`)
4. Push в branch (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📄 Лицензия | License

Этот проект создан в образовательных целях.

This project is created for educational purposes.

## 👤 Автор | Author

TrooSlash

## 📞 Контакты | Contact

GitHub: [@TrooSlash](https://github.com/TrooSlash)

---

⭐ Поставьте звезду, если проект был полезен! | Star this repo if you find it useful!
