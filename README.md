# 🧮 Calculator Application with CI/CD Pipeline# Калькулятор с CI/CD | Calculator with CI/CD



[![CI/CD Pipeline](https://github.com/TrooSlash/univer-project-calc-docker/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/TrooSlash/univer-project-calc-docker/actions)![CI/CD Pipeline](https://github.com/TrooSlash/univer-project-calc-docker/workflows/CI/CD%20Pipeline/badge.svg)

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)Простое приложение-калькулятор на Python с использованием PySide6 для демонстрации CI/CD процессов с GitHub Actions и Docker.

[![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)](https://hub.docker.com/r/coofol/calculator-app)

A simple calculator application built with Python and PySide6 to demonstrate CI/CD processes using GitHub Actions and Docker.

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



## ✨ Features## 🎮 Использование | Usage



### Core Functionality### Запуск приложения | Running the Application

- ✅ **Basic Arithmetic Operations**: Addition, subtraction, multiplication, division

- ✅ **Decimal Numbers**: Full floating-point calculation support```bash

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

```bash
pytest -v
```

### Test Structure

- `test_calculator.py` - Comprehensive unit tests for calculator logic
- Tests cover all arithmetic operations and edge cases
- GUI interaction testing with pytest-qt
- Division by zero and error handling validation
- Clear operations and backspace functionality tests

**Test Coverage: High** ✅

---

## 🔄 CI/CD Pipeline

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

```
univer-project-calc-docker/
│
├── .github/
│   └── workflows/
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
```

---

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
   ```bash
   pytest
   ```

3. **Run linters to check code quality:**
   ```bash
   flake8 calculator.py
   pylint calculator.py
   ```

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
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**TrooSlash**

- GitHub: [@TrooSlash](https://github.com/TrooSlash)
- Project: [univer-project-calc-docker](https://github.com/TrooSlash/univer-project-calc-docker)
- Docker Hub: [coofol/calculator-app](https://hub.docker.com/r/coofol/calculator-app)

---

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

---

<div align="center">

**⭐ If you found this project helpful, please consider giving it a star!**

Made with ❤️ for educational purposes

</div>
