from flask import Blueprint, render_template, redirect, url_for, session
from models.user import Usuario
from database.cenexao import conectar

html_rotas = Blueprint('html_rotas', __name__)


# rota da página principal
@html_rotas.route("/")
def home():
    usuario = None
    if 'user_id' in session:
        usuario = Usuario.buscar_por_id(session['user_id'])

    # Buscar produtos do banco
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT foto FROM produtos")
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    produtos = []

    for row in resultados:
        foto_path = row["foto"]  

        if foto_path:
            caminho_completo = f"/static/{foto_path}"
        else:
            caminho_completo = ""

        produtos.append({
            "foto": caminho_completo,
        })    

    # Renderizar o template passando as duas variáveis
    return render_template("home.html", usuario=usuario, resultado=produtos)

    

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