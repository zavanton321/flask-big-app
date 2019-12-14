from flask import redirect, url_for, request, render_template
from flask_login import login_user, login_required, logout_user

from app import db
from app.main.forms import LoginForm
from app.models import User
from . import main


@main.before_app_first_request
def setup_data():
    db.create_all()
    if User.query.filter_by(username='john').first() is None:
        User.register('john', 'cat')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.verify_password(form.password.data):
            return redirect(url_for('main.login', **request.args))
        login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/protected')
@login_required
def protected():
    return render_template('protected.html')
