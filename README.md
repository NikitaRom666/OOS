# Практична робота — Веб-додаток на Flask

## Опис

Це простий веб-додаток для задач на Flask. У ньому є реєстрація, вхід в акаунт, додавання задач і їх видалення.

Я зробив його як навчальний проєкт, щоб показати роботу з формами, базою даних і шаблонами. Додаток працює на SQLite і має простий інтерфейс.

## Технології

- Python 3.10
- Flask
- SQLAlchemy
- Flask-Login
- Flask-WTF
- Bootstrap 5

## Як запустити

1. Створіть та активуйте віртуальне середовище.
2. Встановіть залежності:

```bash
pip install -r todo_app/requirements.txt
```

3. Запустіть додаток:

```bash
python todo_app/app.py
```

Після першого запуску база даних SQLite створиться автоматично через `db.create_all()`.

## Скріншоти зі звіту

![Фото 1](images/photo1.jpg)
![Фото 2](images/photo2.jpg)
![Фото 3](images/photo3.jpg)

## Структура проєкту

```text
brud/
├── REPORT.md
├── README.md
├── images/
│   ├── photo1.jpg
│   ├── photo2.jpg
│   └── photo3.jpg
└── todo_app/
	├── app.py
	├── config.py
	├── extensions.py
	├── forms.py
	├── models.py
	├── routes.py
	├── requirements.txt
	├── static/
	│   └── style.css
	└── templates/
		├── base.html
		├── dashboard.html
		├── index.html
		├── login.html
		└── register.html
```
