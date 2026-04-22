# Практична робота — Веб-додаток на Flask

## Опис

Даний проєкт являє собою веб-додаток для обліку задач, створений на базі Flask. У ньому реалізовано реєстрацію користувача, вхід у систему, роботу із задачами та захист сторінок для авторизованих користувачів.

Проєкт виконано як навчальну практичну роботу. Для збереження даних використовується SQLite, а інтерфейс побудовано на Jinja2 і Bootstrap 5.

## Технології

- Python 3.10
- Flask
- SQLAlchemy
- Flask-Login
- Flask-WTF
- Bootstrap 5

## Скріншоти зі звіту

<p align="center">
	<img src="images/photo1.jpg" alt="Фото 1" width="100%">
</p>

<p align="center">
	<img src="images/photo2.jpg" alt="Фото 2" width="100%">
</p>

<p align="center">
	<img src="images/photo3.jpg" alt="Фото 3" width="100%">
</p>

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
