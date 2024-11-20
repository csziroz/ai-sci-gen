# ai-sci-gen
**AI-sci-gen** – это приложение, которое генерирует биографию и портрет учёного будущего, используя OpenAI GPT и DALL-E.

---

## Основные возможности

1. Генерация краткой биографии учёного на основе заданных параметров.
2. Генерация изображения портрета учёного.
3. Сохранение и получение результатов через API.

---

## Требования

- Python 3.9+
- OpenAI API ключ
- Docker (опционально)

---

## Установка и запуск

### Вариант 1: Запуск через Docker

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/csziroz/ai-sci-gen.git
   cd ai-sci-gen
   
2. Создайте файл .env на основе .env.example и добавьте свой OpenAI API ключ:
   ```bash
    cp .env.example .env
    nano .env

3. Соберите и запустите контейнер:
    ```bash
    docker-compose up --build -d

4. Приложение будет доступно по адресу:
    - Локально: http://localhost:8000
    - Документация API: http://localhost:8000/docs


### Вариант 2: Запуск вручную

1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/csziroz/ai-sci-gen.git
    cd ai-sci-gen

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt

4. Создайте файл .env на основе .env.example и добавьте свой OpenAI API ключ.

5. Запустите приложение:
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000

6.Приложение будет доступно по адресу:
    - Локально: http://localhost:8000
    - Документация API: http://localhost:8000/docs
