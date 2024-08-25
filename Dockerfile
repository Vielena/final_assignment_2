# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы requirements и приложения
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY wait-for-it.sh .

# Указываем команду для ожидания и выполнения
CMD ["./wait-for-it.sh", "db", "--", "python", "app.py"]
