# Базовый образ Python
FROM python:3.12-slim

# Метаданные
LABEL maintainer="DevSecOps Student"
LABEL description="DevSecOps Demo API"

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY app/ .

# Создаём непривилегированного пользователя (безопасность!)
RUN useradd --create-home appuser
USER appuser

# Открываем порт
EXPOSE 8000

# Команда запуска
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
