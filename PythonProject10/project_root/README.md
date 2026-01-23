
# README.md

# Автоматизация тестирования страницы логина

## О проекте

Репозиторий содержит автоматизированные тесты для страницы входа на сайт. Используется Python, Selenium и pytest с применением паттерна Page Object для удобства поддержки и расширения.

## Структура проекта

- **pages/login_page.py** — Page Object с методами для работы со страницей входа  
- **tests/test_login.py** — тестовые сценарии для проверки логина  
- **requirements.txt** — список зависимостей  
- **Dockerfile** — контейнер для запуска тестов с Chrome и Chromedriver  
- **pytest.ini** — настройки для pytest  

## Требования и установка

- Установлен Python 3.10+  
- Локально нужен Google Chrome и Chromedriver подходящей версии  
- Для запуска в контейнере — Docker

### Установка

```bash
git clone <репозиторий>
cd project_root
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
pip install -r requirements.txt
