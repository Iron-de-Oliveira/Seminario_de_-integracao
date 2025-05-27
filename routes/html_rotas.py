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

    cursor.execute("SELECT idprodutos, foto, categoria, condicao, status FROM produtos")
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    produtos = []

    for row in resultados:
        idprodutos = row["idprodutos"]
        foto_path = row["foto"]  
        categoria = row["categoria"]
        condicao = row["condicao"]
        status = row["status"]

        if foto_path:
            caminho_completo = f"/static/{foto_path}"
        else:
            caminho_completo = ""

        produtos.append({
            "idprodutos": idprodutos,
            "foto": caminho_completo,
            "categoria": categoria,
            "condicao": condicao,
            "status": status,
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
        return render_template('login.html')
    return render_template('perfil_usuario.html', usuario=usuario)

# rota para página de login
@html_rotas.route("/login.html")
def login():
    return render_template ('login.html')

# rota para página de cadastro de item para doação
@html_rotas.route("/cadastrar_item_doacao.html")
def casdastro_doacao():
        return render_template('cadastrar_item_doacao.html')   

# exibição do produto escolhido
@html_rotas.route("/produto/<int:idprodutos>")
def exibir_produto(idprodutos):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = """
            SELECT idprodutos, foto, categoria, condicao, status, descricao 
            FROM produtos 
            WHERE idprodutos = %s
        """
        cursor.execute(sql, (idprodutos,))
        produto = cursor.fetchone()

        if not produto:
            return "Produto não encontrado", 404

        # Converte caminho da foto
        if produto["foto"]:
            produto["foto"] = f"/static/{produto['foto']}"

        return render_template("exibicao_pdt.html", produto=produto)

    except Exception as e:
        print("Erro ao carregar produto:", e)
        return "Erro no servidor", 500

    finally:
        cursor.close()
        conexao.close()


