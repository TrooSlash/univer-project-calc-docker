# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем метаданные
LABEL maintainer="your-email@example.com"
LABEL description="Simple Calculator Application with PySide6"

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости для PySide6
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libxcb-xinerama0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-xfixes0 \
    libxkbcommon-x11-0 \
    libdbus-1-3 \
    libegl1 \
    libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY calculator.py .

# Создаем непривилегированного пользователя
RUN useradd -m -u 1000 calculator && \
    chown -R calculator:calculator /app

USER calculator

# Устанавливаем переменные окружения для X11
ENV DISPLAY=:0
ENV QT_QPA_PLATFORM=xcb

# Команда запуска
CMD ["python", "calculator.py"]
