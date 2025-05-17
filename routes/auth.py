from flask import Blueprint, request, redirect, url_for, render_template,session
from flask_login import login_user, logout_user, login_required
from models.user import Usuario

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = Usuario.buscar_por_email(request.form['email'])

        if usuario and usuario.senha and usuario.senha == senha:
            login_user(usuario)
            session['user_id'] = usuario.idusuario  # salva id do usuário na sessão

            return redirect(url_for('html_rotas.home'))  # ajuste conforme sua rota principal
        return 'Email ou senha inválidos.'
    return render_template('login.html')

@auth_bp.route('/logout')

def logout():
  session.clear()  # Remove todos os dados da sessão
  return redirect(url_for('html_rotas.home'))  # Redireciona para a home