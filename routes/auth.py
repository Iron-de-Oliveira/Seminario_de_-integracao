from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_user, logout_user, login_required
from models.user import Usuario

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario.buscar_por_email(email)
        if usuario and usuario.senha == senha:
            login_user(usuario)
            return redirect(url_for('/'))  # ajuste conforme sua rota principal
        return 'Email ou senha inválidos.'
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
