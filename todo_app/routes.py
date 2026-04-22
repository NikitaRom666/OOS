from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from extensions import db
from forms import LoginForm, RegisterForm, TaskForm
from models import Task, User


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/')
def index():
    return render_template('index.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter((User.username == form.username.data) | (User.email == form.email.data)).first()
        if user:
            flash('Користувач з таким ім\'ям або email вже існує.', 'danger')
            return render_template('register.html', form=form)

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Реєстрація успішна. Тепер увійдіть у систему.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Вхід виконано успішно.', 'success')
            return redirect(url_for('auth.dashboard'))

        flash('Невірний email або пароль.', 'danger')

    return render_template('login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Ви вийшли з акаунта.', 'info')
    return redirect(url_for('auth.index'))


@auth_bp.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.created_at.desc()).all()
    form = TaskForm()
    return render_template('dashboard.html', tasks=tasks, form=form)


@auth_bp.route('/task/add', methods=['POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            user_id=current_user.id
        )
        db.session.add(task)
        db.session.commit()
        flash('Задачу додано.', 'success')
        return redirect(url_for('auth.dashboard'))

    flash('Не вдалося додати задачу. Перевірте форму.', 'danger')
    return redirect(url_for('auth.dashboard'))


@auth_bp.route('/task/done/<int:id>')
@login_required
def done_task(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    task.done = True
    db.session.commit()
    flash('Задачу позначено як виконану.', 'success')
    return redirect(url_for('auth.dashboard'))


@auth_bp.route('/task/delete/<int:id>')
@login_required
def delete_task(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    flash('Задачу видалено.', 'warning')
    return redirect(url_for('auth.dashboard'))
