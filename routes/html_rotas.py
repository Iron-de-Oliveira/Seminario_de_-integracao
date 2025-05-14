from flask import Blueprint, render_template

html_rotas = Blueprint('html_rotas', __name__)

# rota da página principal
@html_rotas.route("/")
def home():
    return render_template("home.html")

# rota para págna cadastro
@html_rotas.route("/cadastro.html")
def cadastro():
    return render_template('cadastro.html')

# rota para página de perfil do usuário 
@html_rotas.route("/perfil_usuario.html")
def perfil_user():
    return render_template('perfil_usuario.html')

# rota para página de login
@html_rotas.route("/login_cadastro.html")
def login():
    return render_template ('login_cadastro.html')

# rota para página de cadastro de item para doação
@html_rotas.route("/cadastrar_item_doacao.html")
def casdastro_doacao():
        return render_template('cadastrar_item_doacao.html')   

# rota para página de cadastro de item para troca
@html_rotas.route("/cadastrar_item_troca.html")
def casdastro_troca():
        return render_template('cadastrar_item_troca.html')  