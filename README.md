# ApiTestCore

Automated testing framework for REST API with focus on Role-Based Access Control (RBAC).

## Features
- Parametrized tests by user roles
- RBAC matrix loaded from CSV
- Secure API key handling via .env
- Status code and response structure validation
- Pytest fixtures and session-scoped data

## Tech Stack
- pytest
- requests
- python-dotenv


Nest open API for

1. Go to ApiTestCore in Terminal
cd ~/Desktop/ApiTestCore
2. Created the environment in folder 
python3 -m venv .venv
3. Activate it
source .venv/bin/activate
4. Download frameworks pytest - base; 
httpx - library for request (PUT/POST/GET); 
pytest-httpx - for httpx; 
python-dotenv - for save Token/Base_URL/... in .env ????
pip install --upgrade pip  //(upgrade version?)
pip install pytest httpx python-dotenv
5. Save changes
pip freeze > requirements.txt
(if you want to put out it
pip install -r requirements.txt)
(if you want to delite old venv
rm -rf .venv)
6. Чтоб подтянутоль правильное окружение
Cmd + Shift + P
Python: Select Interpreter
Если нет моего пути к окружению то нажать
Enter interpreter path...
~/Desktop/ApiTestCore/.venv/bin/python

+cards.index (смотреть список карт)
+cards.show (смотреть конкретную карту)
cards.store (выпуск карты)
+cards.credentials.show (смотреть креды конкретной карты)
+cards.update (generic permission - used for title/state updates and archival) (изменять название/статус карты)
cards.spending-controls.show