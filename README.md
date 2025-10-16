<<<<<<< HEAD
# 🧮 Калькулятор с CI/CD Pipeline

[![CI/CD Pipeline](https://github.com/TrooSlash/univer-project-calc-docker/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/TrooSlash/univer-project-calc-docker/actions)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)](https://hub.docker.com/r/coofol/calculator-app)

Современное десктопное приложение-калькулятор на Python с PySide6, демонстрирующее профессиональные практики разработки ПО, включая автоматизированное тестирование, непрерывную интеграцию/развертывание и контейнеризацию.
=======
# 🧮 Calculator Application with CI/CD Pipeline# Калькулятор с CI/CD | Calculator with CI/CD



[![CI/CD Pipeline](https://github.com/TrooSlash/univer-project-calc-docker/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/TrooSlash/univer-project-calc-docker/actions)![CI/CD Pipeline](https://github.com/TrooSlash/univer-project-calc-docker/workflows/CI/CD%20Pipeline/badge.svg)

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)Простое приложение-калькулятор на Python с использованием PySide6 для демонстрации CI/CD процессов с GitHub Actions и Docker.

[![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)](https://hub.docker.com/r/coofol/calculator-app)
>>>>>>> 9ec807b91df1f4639ace84c3a62c7a80d217e527

> 📚 **Университетский проект**: Разработан в рамках курсовой работы для демонстрации современных DevOps практик и принципов разработки программного обеспечения.

<<<<<<< HEAD
---

## 📖 Содержание

- [О проекте](#о-проекте)
- [Возможности](#возможности)
- [Технологический стек](#технологический-стек)
- [Быстрый старт](#быстрый-старт)
  - [Требования](#требования)
  - [Установка](#установка)
  - [Локальный запуск](#локальный-запуск)
  - [Запуск в Docker](#запуск-в-docker)
- [Тестирование](#тестирование)
- [CI/CD Pipeline](#cicd-pipeline)
- [Структура проекта](#структура-проекта)
- [Разработка](#разработка)
- [Вклад в проект](#вклад-в-проект)
- [Лицензия](#лицензия)
- [Контакты](#контакты)

---

## 📝 О проекте

Данный проект демонстрирует полный цикл разработки программного обеспечения - от написания кода до развертывания. Он служит практическим примером реализации:

- **Чистой архитектуры кода**: Хорошо структурированный, поддерживаемый код на Python
- **Test-Driven Development**: Комплексное модульное тестирование с высоким покрытием
- **Непрерывной интеграции**: Автоматизированное тестирование и проверка качества кода
- **Непрерывного развертывания**: Автоматическая сборка и публикация Docker образов
- **Контейнеризации**: Полная поддержка Docker с мультиплатформенной совместимостью
- **Кроссплатформенного GUI**: Современный десктопный интерфейс на Qt (PySide6)

Калькулятор предоставляет базовые арифметические операции и служит надежным примером профессиональных рабочих процессов разработки ПО.

---

## ✨ Возможности

### Основной функционал
- ✅ **Базовые арифметические операции**: Сложение, вычитание, умножение, деление
- ✅ **Десятичные числа**: Полная поддержка вычислений с плавающей точкой
- ✅ **Смена знака**: Изменение знака числа кнопкой ±
- ✅ **Backspace**: Удаление последней введенной цифры
- ✅ **Функции очистки**: CE (очистка ввода) и C (полная очистка)
- ✅ **Обработка ошибок**: Корректная обработка деления на ноль и некорректных операций

### Технические возможности
- 🧪 **Комплексное тестирование**: Полное покрытие модульными тестами с pytest
- 🔄 **CI/CD Pipeline**: Автоматизированное тестирование, линтинг, сборка и развертывание
- 🐳 **Поддержка Docker**: Контейнеризованное приложение с поддержкой GUI через WSLg/X11
- 🎨 **Современный интерфейс**: Чистый, интуитивный UI на PySide6 (Qt 6.x)
- 📊 **Качество кода**: Автоматический линтинг с Flake8 и Pylint
- 🚀 **Кроссплатформенность**: Совместимость с Windows, Linux и macOS

---

## 🛠️ Технологический стек

| Компонент | Технология |
|-----------|-----------|
| **Язык программирования** | Python 3.11+ |
| **GUI Framework** | PySide6 (Qt 6.x) |
| **Тестирование** | pytest, pytest-qt |
| **Качество кода** | Flake8, Pylint |
| **CI/CD** | GitHub Actions |
| **Контейнеризация** | Docker, Docker Compose |
| **Система контроля версий** | Git, GitHub |

---

## 🚀 Быстрый старт

### Требования

Перед началом убедитесь, что у вас установлено:

- **Python 3.11 или выше** - [Скачать Python](https://www.python.org/downloads/)
- **Git** - [Скачать Git](https://git-scm.com/downloads)
- **Docker** (опционально, для контейнерного развертывания) - [Скачать Docker](https://www.docker.com/get-started)

Для поддержки GUI в Windows с Docker необходимо:
- **Windows 11** с WSLg (рекомендуется) - встроенная поддержка X11
- ИЛИ **VcXsrv** / **X410** для X11 forwarding на Windows 10

### Установка

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/TrooSlash/univer-project-calc-docker.git
   cd univer-project-calc-docker
   ```

2. **Создайте виртуальное окружение**
   ```bash
   python -m venv .venv
   ```

3. **Активируйте виртуальное окружение**
   
   **Windows (PowerShell):**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   
   **Windows (CMD):**
   ```cmd
   .venv\Scripts\activate.bat
   ```
   
   **Linux/macOS:**
   ```bash
   source .venv/bin/activate
   ```

4. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
   ```

### Локальный запуск

Просто запустите скрипт калькулятора:
=======
A modern desktop calculator application built with Python and PySide6, demonstrating professional software development practices including automated testing, continuous integration/deployment, and containerization.

## 🚀 Особенности | Features

> 📚 **University Project**: This project was developed as part of university coursework to demonstrate modern DevOps practices and software engineering principles.

- ✅ Базовые арифметические операции (сложение, вычитание, умножение, деление)

---- ✅ Работа с десятичными числами

- ✅ Изменение знака числа

## 📖 Table of Contents- ✅ Удаление символов (Backspace)

- ✅ Очистка ввода и полная очистка

- [About](#about)- ✅ Современный графический интерфейс на PySide6

- [Features](#features)- ✅ Полное покрытие unit-тестами

- [Technology Stack](#technology-stack)- ✅ CI/CD pipeline с GitHub Actions

- [Getting Started](#getting-started)- ✅ Докеризация приложения

  - [Prerequisites](#prerequisites)

  - [Installation](#installation)## 📋 Требования | Requirements

  - [Running Locally](#running-locally)

  - [Running with Docker](#running-with-docker)- Python 3.11+

- [Testing](#testing)- PySide6

- [CI/CD Pipeline](#cicd-pipeline)- pytest (для тестирования)

- [Project Structure](#project-structure)

- [Development](#development)## 🔧 Установка | Installation

- [Contributing](#contributing)

- [License](#license)### Локальная установка | Local Installation

- [Contact](#contact)

```bash

---# Клонировать репозиторий

git clone https://github.com/TrooSlash/univer-project-calc-docker.git

## 📝 Aboutcd univer-project-calc-docker



This project showcases a complete software development lifecycle implementation, from code to deployment. It serves as a practical demonstration of:# Создать виртуальное окружение

python -m venv venv

- **Clean Code Architecture**: Well-structured, maintainable Python code following best practices

- **Test-Driven Development**: Comprehensive unit testing achieving high code coverage# Активировать виртуальное окружение

- **Continuous Integration**: Automated testing and code quality checks on every commit# Windows:

- **Continuous Deployment**: Automated Docker image building and publishing to registryvenv\Scripts\activate

- **Containerization**: Full Docker support with multi-platform compatibility# Linux/Mac:

- **Cross-Platform GUI**: Modern desktop interface using Qt framework (PySide6)source venv/bin/activate



The calculator provides essential arithmetic operations while serving as a robust example of professional software development workflows suitable for production environments.# Установить зависимости

pip install -r requirements.txt

---```

>>>>>>> 9ec807b91df1f4639ace84c3a62c7a80d217e527


<<<<<<< HEAD
Откроется окно калькулятора с интуитивно понятным интерфейсом.

### Запуск в Docker

#### Вариант 1: Загрузка с Docker Hub

```bash
docker pull coofol/calculator-app:latest
```

#### Вариант 2: Локальная сборка
=======
## ✨ Features## 🎮 Использование | Usage



### Core Functionality### Запуск приложения | Running the Application

- ✅ **Basic Arithmetic Operations**: Addition, subtraction, multiplication, division
>>>>>>> 9ec807b91df1f4639ace84c3a62c7a80d217e527

- ✅ **Decimal Numbers**: Full floating-point calculation support```bash

<<<<<<< HEAD
#### Запуск контейнера

**На Windows 11 с WSLg (рекомендуется):**
```powershell
.\run-gui-wslg.ps1
```

**На Linux:**
```bash
# Разрешить подключения к X server
xhost +local:docker

# Запустить контейнер
docker run --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  coofol/calculator-app:latest

# После использования отозвать доступ
xhost -local:docker
```

**С Docker Compose:**
```bash
docker-compose up
```

> 📖 Подробные инструкции по настройке GUI на разных платформах см. в [GUI-LAUNCH.md](GUI-LAUNCH.md)

---

## 🧪 Тестирование

Проект поддерживает высокое качество кода благодаря комплексному автоматизированному тестированию.

### Запуск всех тестов

```bash
pytest
```

### Запуск тестов с отчетом о покрытии

```bash
pytest --cov=calculator --cov-report=term --cov-report=html
```

### Подробный вывод тестов
=======
- ✅ **Sign Toggle**: Change number sign with ±/+/- buttonpython calculator.py

- ✅ **Backspace**: Delete last entered digit```

- ✅ **Clear Functions**: CE (Clear Entry) and C (Clear All)

- ✅ **Error Handling**: Graceful handling of division by zero and invalid operations### Запуск тестов | Running Tests



### Technical Features```bash

- 🧪 **Comprehensive Testing**: Full unit test coverage with pytest# Запустить все тесты

- 🔄 **CI/CD Pipeline**: Automated testing, linting, building, and deploymentpytest test_calculator.py -v

- 🐳 **Docker Support**: Containerized application with GUI support via WSLg/X11

- 🎨 **Modern UI**: Clean, intuitive interface built with PySide6 (Qt 6.x)# Запустить с покрытием кода

- 📊 **Code Quality**: Automated linting with Flake8 and Pylintpytest test_calculator.py -v --cov=calculator --cov-report=html

- 🚀 **Cross-Platform**: Compatible with Windows, Linux, and macOS```



---## 🐳 Docker



## 🛠️ Technology Stack### Сборка образа | Build Image



| Component | Technology |```bash

|-----------|-----------|docker build -t calculator-app .

| **Language** | Python 3.11+ |```

| **GUI Framework** | PySide6 (Qt 6.x) |

| **Testing** | pytest, pytest-qt |### Запуск контейнера | Run Container

| **Code Quality** | Flake8, Pylint |

| **CI/CD** | GitHub Actions |**Windows с WSL2:**

| **Containerization** | Docker, Docker Compose |```bash

| **Version Control** | Git, GitHub |docker run -it --rm -e DISPLAY=host.docker.internal:0 calculator-app

```

---

**Linux:**

## 🚀 Getting Started```bash

# Разрешить подключение к X server

### Prerequisitesxhost +local:docker



Before you begin, ensure you have the following installed:# Запустить контейнер

docker run -it --rm \

- **Python 3.11 or higher** - [Download Python](https://www.python.org/downloads/)  -e DISPLAY=$DISPLAY \

- **Git** - [Download Git](https://git-scm.com/downloads)  -v /tmp/.X11-unix:/tmp/.X11-unix \

- **Docker** (optional, for containerized deployment) - [Download Docker](https://www.docker.com/get-started)  calculator-app



For GUI support on Windows with Docker, you'll need:# После использования отключить доступ

- **Windows 11** with WSLg (recommended) - built-in X11 supportxhost -local:docker

- OR **VcXsrv** / **X410** for X11 forwarding on Windows 10```



### Installation**macOS с XQuartz:**

```bash

1. **Clone the repository**# Установить XQuartz, затем:

   ```bashxhost +localhost

   git clone https://github.com/TrooSlash/univer-project-calc-docker.gitdocker run -it --rm -e DISPLAY=host.docker.internal:0 calculator-app

   cd univer-project-calc-docker```

   ```

## 🔄 CI/CD Pipeline

2. **Create a virtual environment**

   ```bashПроект использует GitHub Actions для автоматизации:

   python -m venv .venv

   ```### Этапы Pipeline:



3. **Activate the virtual environment**1. **Test** - Запуск unit-тестов с покрытием кода

   2. **Lint** - Проверка качества кода (flake8, pylint)

   **Windows (PowerShell):**3. **Build Docker** - Сборка и публикация Docker образа

   ```powershell4. **Deploy** - Информация о развертывании

   .\.venv\Scripts\Activate.ps1

   ```### Триггеры:

   

   **Windows (CMD):**- Push в ветки `main` и `develop`

   ```cmd- Pull requests в ветки `main` и `develop`

   .venv\Scripts\activate.bat

   ```## 📁 Структура проекта | Project Structure

   

   **Linux/macOS:**```

   ```bashuniver-project-calc-docker/

   source .venv/bin/activate├── .github/

   ```│   └── workflows/

│       └── ci-cd.yml          # CI/CD конфигурация

4. **Install dependencies**├── calculator.py              # Основное приложение

   ```bash├── test_calculator.py         # Unit-тесты

   pip install -r requirements.txt├── requirements.txt           # Python зависимости

   ```├── Dockerfile                 # Docker конфигурация

└── README.md                  # Документация

### Running Locally```



Simply execute the calculator script:## 🧪 Тестирование | Testing



```bashПроект включает комплексный набор тестов:

python calculator.py

```- Тест инициализации

- Тест ввода чисел и десятичных дробей

The calculator window will open with a clean, intuitive interface.- Тесты всех арифметических операций

- Тест деления на ноль

### Running with Docker- Тесты операций очистки

- Тесты изменения знака

#### Option 1: Pull from Docker Hub- Тесты цепочек операций



```bashПокрытие кода: >90%

docker pull coofol/calculator-app:latest

```## 🛠️ Технологии | Technologies



#### Option 2: Build Locally- **Python 3.11** - Язык программирования

- **PySide6** - GUI фреймворк (Qt6)

```bash- **pytest** - Фреймворк для тестирования

docker build -t calculator-app .- **GitHub Actions** - CI/CD

```- **Docker** - Контейнеризация



#### Running the Container## 📝 Конфигурация для Docker Hub



**On Windows 11 with WSLg (Recommended):**Для автоматической публикации в Docker Hub необходимо настроить secrets в GitHub:

```powershell

.\run-gui-wslg.ps11. `DOCKER_USERNAME` - Имя пользователя Docker Hub

```2. `DOCKER_PASSWORD` - Токен доступа Docker Hub



**On Linux:**Перейдите в Settings → Secrets and variables → Actions → New repository secret

```bash

# Allow X server connections## 🎯 Использование калькулятора | Calculator Usage

xhost +local:docker

### Кнопки:

# Run container

docker run --rm \- **0-9** - Цифры

  -e DISPLAY=$DISPLAY \- **+, -, *, /** - Математические операции

  -v /tmp/.X11-unix:/tmp/.X11-unix \- **=** - Вычислить результат

  coofol/calculator-app:latest- **.** - Десятичная точка

- **C** - Полная очистка (Clear All)

# Revoke access after use- **CE** - Очистка текущего ввода (Clear Entry)

xhost -local:docker- **←** - Удалить последний символ (Backspace)

```- **±** - Изменить знак числа



**With Docker Compose:**## 🤝 Вклад | Contributing

```bash

docker-compose up1. Fork репозиторий

```2. Создайте feature branch (`git checkout -b feature/AmazingFeature`)

3. Commit изменения (`git commit -m 'Add some AmazingFeature'`)

> 📖 For detailed GUI setup instructions on different platforms, see [GUI-LAUNCH.md](GUI-LAUNCH.md)4. Push в branch (`git push origin feature/AmazingFeature`)

5. Откройте Pull Request

---

## 📄 Лицензия | License

## 🧪 Testing

Этот проект создан в образовательных целях.

This project maintains high code quality with comprehensive automated testing.

This project is created for educational purposes.

### Run All Tests

## 👤 Автор | Author

```bash

pytestTrooSlash

```

## 📞 Контакты | Contact

### Run Tests with Coverage Report

GitHub: [@TrooSlash](https://github.com/TrooSlash)

```bash

pytest --cov=calculator --cov-report=term --cov-report=html---

```

⭐ Поставьте звезду, если проект был полезен! | Star this repo if you find it useful!

### Run Tests Verbosely
>>>>>>> 9ec807b91df1f4639ace84c3a62c7a80d217e527

```bash
pytest -v
```

<<<<<<< HEAD
### Структура тестов

- `test_calculator.py` - Комплексные модульные тесты для логики калькулятора
- Тесты покрывают все арифметические операции и граничные случаи
- Тестирование GUI взаимодействий с pytest-qt
- Проверка деления на ноль и обработки ошибок
- Тесты операций очистки и функции backspace

**Покрытие кода: Высокое** ✅
=======
### Test Structure

- `test_calculator.py` - Comprehensive unit tests for calculator logic
- Tests cover all arithmetic operations and edge cases
- GUI interaction testing with pytest-qt
- Division by zero and error handling validation
- Clear operations and backspace functionality tests

**Test Coverage: High** ✅
>>>>>>> 9ec807b91df1f4639ace84c3a62c7a80d217e527

---

## 🔄 CI/CD Pipeline

<<<<<<< HEAD
Проект реализует полный CI/CD pipeline с использованием GitHub Actions, автоматически запускаемый при изменении кода.

### Архитектура Pipeline

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Тестирование│────▶│  Линтинг    │────▶│   Сборка    │────▶│Развертывание│
│  (pytest)   │     │(flake8/pyl) │     │   Docker    │     │  (Hub Push) │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

### Детали workflow

**Триггеры:**
- Push в ветки `main` или `develop`
- Pull requests в ветки `main` или `develop`

**Задачи Pipeline:**

1. **Запуск тестов**
   - Выполнение pytest с отчетом о покрытии
   - Установка системных зависимостей для PySide6
   - Генерация отчетов о покрытии

2. **Проверка качества кода**
   - Запуск Flake8 для проверки стиля кода
   - Запуск Pylint для анализа кода
   - Продолжение работы при некритичных предупреждениях

3. **Сборка Docker образа**
   - Сборка мультиплатформенного Docker образа
   - Тегирование по commit SHA и имени ветки
   - Кеширование слоев для ускорения сборки

4. **Развертывание в реестр**
   - Аутентификация в Docker Hub
   - Push тегированных образов в реестр
   - Только для ветки main (не для PR)

Посмотреть полную конфигурацию workflow: [`.github/workflows/main.yml`](.github/workflows/main.yml)

### Настройка CI/CD

Для активации автоматического развертывания в Docker Hub:

1. Создайте токен доступа Docker Hub на https://hub.docker.com/settings/security
2. Добавьте секреты репозитория в GitHub Settings → Secrets and variables → Actions:
   - `DOCKER_USERNAME`: Ваше имя пользователя Docker Hub
   - `DOCKER_PASSWORD`: Ваш токен доступа Docker Hub (не пароль!)

---

## 📁 Структура проекта
=======
This project implements a complete CI/CD pipeline using GitHub Actions, automatically triggered on code changes.

### Pipeline Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Testing   │────▶│   Linting   │────▶│   Docker    │────▶│   Deploy    │
│   (pytest)  │     │ (flake8/py) │     │    Build    │     │  (Hub Push) │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

### Workflow Details

**Triggered on:**
- Push to `main` or `develop` branches
- Pull requests targeting `main` or `develop`

**Pipeline Jobs:**

1. **Run Tests**
   - Execute pytest with coverage reporting
   - Install system dependencies for PySide6
   - Generate coverage reports

2. **Code Quality Check**
   - Run Flake8 for style guide enforcement
   - Run Pylint for code analysis
   - Continue on non-critical warnings

3. **Build Docker Image**
   - Build multi-platform Docker image
   - Tag with commit SHA and branch name
   - Cache layers for faster builds

4. **Deploy to Registry**
   - Authenticate with Docker Hub
   - Push tagged images to registry
   - Only on main branch (not on PRs)

View the complete workflow configuration: [`.github/workflows/main.yml`](.github/workflows/main.yml)

### Setting Up CI/CD

To enable automatic deployment to Docker Hub:

1. Create Docker Hub access token at https://hub.docker.com/settings/security
2. Add repository secrets in GitHub Settings → Secrets and variables → Actions:
   - `DOCKER_USERNAME`: Your Docker Hub username
   - `DOCKER_PASSWORD`: Your Docker Hub access token (not password!)

---

## 📁 Project Structure
>>>>>>> 9ec807b91df1f4639ace84c3a62c7a80d217e527

```
univer-project-calc-docker/
│
├── .github/
│   └── workflows/
<<<<<<< HEAD
│       └── main.yml              # Конфигурация CI/CD pipeline
│
├── calculator.py                 # Основной код приложения
├── test_calculator.py            # Модульные тесты
├── requirements.txt              # Зависимости Python
│
├── Dockerfile                    # Определение Docker образа
├── docker-compose.yml            # Конфигурация Docker Compose
├── .gitignore                    # Правила игнорирования Git
│
├── run-gui-wslg.ps1             # Скрипт запуска GUI для Windows
├── GUI-LAUNCH.md                # Документация по настройке GUI
│
├── LICENSE                       # Лицензия MIT
└── README.md                     # Документация проекта
=======
│       └── main.yml              # CI/CD pipeline configuration
│
├── calculator.py                 # Main application code
├── test_calculator.py            # Unit tests
├── requirements.txt              # Python dependencies
│
├── Dockerfile                    # Docker image definition
├── docker-compose.yml            # Docker Compose configuration
├── .gitignore                    # Git ignore rules
│
├── run-gui-wslg.ps1             # Windows GUI launcher script
├── GUI-LAUNCH.md                # GUI setup documentation
│
└── README.md                     # Project documentation
>>>>>>> 9ec807b91df1f4639ace84c3a62c7a80d217e527
```

---

<<<<<<< HEAD
## 💻 Разработка

### Стандарты стиля кода

Проект следует руководству по стилю PEP 8 с автоматической проверкой:

- **Flake8** - Проверка соответствия стилю (макс. длина строки: 100)
- **Pylint** - Комплексный анализ кода и проверка качества

### Запуск проверки качества кода

```bash
# Запуск Flake8
flake8 calculator.py --max-line-length=100

# Запуск Pylint
pylint calculator.py --disable=C0111,C0103
```

### Процесс разработки

1. **Создайте ветку для фичи:**
   ```bash
   git checkout -b feature/название-фичи
   ```

2. **Внесите изменения и убедитесь, что тесты проходят:**
=======
## 💻 Development

### Code Style Guidelines

This project adheres to PEP 8 Python style guide with automated enforcement:

- **Flake8** - Style guide enforcement (max line length: 100)
- **Pylint** - Comprehensive code analysis and quality checks

### Running Code Quality Checks

```bash
# Run Flake8
flake8 calculator.py --max-line-length=100

# Run Pylint
pylint calculator.py --disable=C0111,C0103
```

### Development Workflow

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make changes and ensure tests pass:**
>>>>>>> 9ec807b91df1f4639ace84c3a62c7a80d217e527
   ```bash
   pytest
   ```

<<<<<<< HEAD
3. **Запустите линтеры для проверки качества кода:**
=======
3. **Run linters to check code quality:**
>>>>>>> 9ec807b91df1f4639ace84c3a62c7a80d217e527
   ```bash
   flake8 calculator.py
   pylint calculator.py
   ```

<<<<<<< HEAD
4. **Закоммитьте изменения:**
   ```bash
   git add .
   git commit -m "Add: описательное сообщение коммита"
   ```

5. **Отправьте в свой fork:**
   ```bash
   git push origin feature/название-фичи
   ```

6. **Создайте Pull Request** на GitHub

### Соглашение о сообщениях коммитов

Следуйте семантическим сообщениям коммитов:
- `Add:` - Новая функция или функциональность
- `Fix:` - Исправление ошибки
- `Update:` - Обновление существующей функциональности
- `Refactor:` - Рефакторинг кода
- `Docs:` - Изменения в документации
- `Test:` - Добавление или обновление тестов

---

## 🤝 Вклад в проект

Вклад приветствуется! Чтобы внести вклад в проект:

1. **Сделайте Fork** репозитория
2. **Создайте** ветку для фичи (`git checkout -b feature/AmazingFeature`)
3. **Закоммитьте** изменения (`git commit -m 'Add some AmazingFeature'`)
4. **Отправьте** в ветку (`git push origin feature/AmazingFeature`)
5. **Откройте** Pull Request

Пожалуйста, убедитесь:
- Все тесты проходят (`pytest`)
- Код соответствует стандартам стиля (`flake8`, `pylint`)
- Сообщения коммитов понятны и описательны
- Документация обновлена при необходимости

---

## 🎮 Руководство пользователя

### Операции калькулятора

| Кнопка | Функция |
|--------|---------|
| **0-9** | Ввод цифр |
| **+, -, ×, ÷** | Арифметические операции |
| **=** | Вычислить результат |
| **.** | Десятичная точка |
| **C** | Очистить всё (сброс калькулятора) |
| **CE** | Очистить ввод (очистка текущего ввода) |
| **←** | Backspace (удалить последнюю цифру) |
| **±** | Переключить знак (положительное/отрицательное) |

### Примеры операций

```
Базовые вычисления:    5 + 3 = 8
Десятичные числа:      3.14 × 2 = 6.28
Отрицательные числа:   5 - 8 = -3
Смена знака:           5 [±] = -5
Цепочки операций:      2 + 3 × 4 = 20
=======
4. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Add: descriptive commit message"
   ```

5. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** on GitHub

### Commit Message Convention

Follow semantic commit messages:
- `Add:` - New feature or functionality
- `Fix:` - Bug fix
- `Update:` - Update existing feature
- `Refactor:` - Code refactoring
- `Docs:` - Documentation changes
- `Test:` - Adding or updating tests

---

## 🤝 Contributing

Contributions are welcome! To contribute to this project:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

Please ensure:
- All tests pass (`pytest`)
- Code follows style guidelines (`flake8`, `pylint`)
- Commit messages are clear and descriptive
- Documentation is updated if needed

---

## 🎮 Usage Guide

### Calculator Operations

| Button | Function |
|--------|----------|
| **0-9** | Number input |
| **+, -, ×, ÷** | Arithmetic operations |
| **=** | Calculate result |
| **.** | Decimal point |
| **C** | Clear all (reset calculator) |
| **CE** | Clear entry (clear current input) |
| **←** | Backspace (delete last digit) |
| **±** | Toggle sign (positive/negative) |

### Example Operations

```
Basic calculation:     5 + 3 = 8
Decimal numbers:       3.14 × 2 = 6.28
Negative numbers:      5 - 8 = -3
Sign toggle:           5 [±] = -5
Chain operations:      2 + 3 × 4 = 20
>>>>>>> 9ec807b91df1f4639ace84c3a62c7a80d217e527
```

---

<<<<<<< HEAD
## 📄 Лицензия

Проект распространяется под лицензией MIT - см. файл [LICENSE](LICENSE) для деталей.

---

## 👤 Автор
=======
## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author
>>>>>>> 9ec807b91df1f4639ace84c3a62c7a80d217e527

**TrooSlash**

- GitHub: [@TrooSlash](https://github.com/TrooSlash)
<<<<<<< HEAD
- Проект: [univer-project-calc-docker](https://github.com/TrooSlash/univer-project-calc-docker)
=======
- Project: [univer-project-calc-docker](https://github.com/TrooSlash/univer-project-calc-docker)
>>>>>>> 9ec807b91df1f4639ace84c3a62c7a80d217e527
- Docker Hub: [coofol/calculator-app](https://hub.docker.com/r/coofol/calculator-app)

---

<<<<<<< HEAD
## 🙏 Благодарности

Проект стал возможен благодаря:

- **Команде PySide6** - За отличные привязки Qt 6 для Python
- **GitHub** - За платформу CI/CD Actions
- **Docker** - За технологию контейнеризации
- **Сообществу pytest** - За комплексный фреймворк тестирования
- **Python Software Foundation** - За язык программирования Python

Особая благодарность open-source сообществу за предоставление инструментов и фреймворков, делающих современную разработку ПО эффективной и удобной.

---

## 📚 Дополнительные ресурсы

- [Документация PySide6](https://doc.qt.io/qtforpython/)
- [Документация pytest](https://docs.pytest.org/)
- [Документация Docker](https://docs.docker.com/)
- [Документация GitHub Actions](https://docs.github.com/actions)
=======
## 🙏 Acknowledgments

This project was made possible by:

- **PySide6 Team** - For excellent Qt 6 Python bindings
- **GitHub** - For Actions CI/CD platform
- **Docker** - For containerization technology
- **pytest Community** - For comprehensive testing framework
- **Python Software Foundation** - For the Python language

Special thanks to the open-source community for providing the tools and frameworks that make modern software development efficient and enjoyable.

---

## 📚 Additional Resources

- [PySide6 Documentation](https://doc.qt.io/qtforpython/)
- [pytest Documentation](https://docs.pytest.org/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/actions)
>>>>>>> 9ec807b91df1f4639ace84c3a62c7a80d217e527

---

<div align="center">

<<<<<<< HEAD
**⭐ Если проект оказался полезным, пожалуйста, поставьте звезду!**

Сделано с ❤️ для образовательных целей
=======
**⭐ If you found this project helpful, please consider giving it a star!**

Made with ❤️ for educational purposes
>>>>>>> 9ec807b91df1f4639ace84c3a62c7a80d217e527

</div>
