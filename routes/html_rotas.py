from flask import Blueprint, render_template, redirect, url_for, session
from models.user import Usuario

html_rotas = Blueprint('html_rotas', __name__)

# rota da página principal
@html_rotas.route("/")
def home():
    usuario = None
    if 'user_id' in session:
        usuario = Usuario.buscar_por_id(session['user_id'])
    return render_template('home.html', usuario=usuario)

# rota para págna cadastro
@html_rotas.route("/cadastro.html")
def cadastro():
    return render_template('cadastro.html')

# rota para página de perfil do usuário 
@html_rotas.route("/perfil_usuario.html")
def perfil_user():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))

    usuario = Usuario.buscar_por_id(user_id)
    if not usuario:
        return "Usuário não encontrado", 404
    return render_template('perfil_usuario.html', usuario=usuario)

# rota para página de login
@html_rotas.route("/login.html")
def login():
    return render_template ('login.html')

# rota para página de cadastro de item para doação
@html_rotas.route("/cadastrar_item_doacao.html")
def casdastro_doacao():
        return render_template('cadastrar_item_doacao.html')   

# rota para página de cadastro de item para troca
@html_rotas.route("/cadastrar_item_troca.html")
def casdastro_troca():
        return render_template('cadastrar_item_troca.html')  