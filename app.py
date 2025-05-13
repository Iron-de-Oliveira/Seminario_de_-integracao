from flask import Flask, render_template, request, jsonify
from models.user import Usuario
from models.produtos import Produtos
from database.cenexao import conectar

app = Flask (__name__)

# rotas templates
# @app.route("/")
# def home1():
#     return "<h1>Bem-vindo ao Projeto Integrador!</h1><p>Acesse <a href='/cadastro'>/cadastro</a></p>"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cadastro.html")
def cadastro():
    return render_template('cadastro.html')

@app.route("/perfil_usuario.html")
def perfil_user():
    return render_template('perfil_usuario.html')

@app.route("/login_cadastro.html")
def login():
    return render_template ('login_cadastro.html')

@app.route("/cadastrar_item_doacao.html")
def casdastro_doacao():
        return render_template('cadastrar_item_doacao.html')   

@app.route("/cadastrar_item_troca.html")
def casdastro_troca():
        return render_template('cadastrar_item_troca.html')  

# rotas APIs
# NOVO USUÁRIO
@app.route("/usuario", methods=['POST'])
def novo_usuario():
    data = request.get_json()
    print("Recebido do front-end:", data)
    try:
        conexao = conectar()
        with conexao:
            with conexao.cursor() as cursor:
                # id = gerar_id_unico(cursor) # variável recebe id aleatório
                new_usuario = Usuario(id_usuario = id, nome=data['nome'], email=data['email'], senha= data['senha'], numero= data['numero'], locatizacao= data['localizacao'])
                sql = "INSERT INTO (id_aluno, nome, email, senha, numero, localizacao) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (
                    new_usuario.id_usuario,
                    new_usuario.nome,
                    new_usuario.email,
                    new_usuario.senha
                ))
            conexao.commit()
    except Exception as e:
        print("Erro ao inserir no banco:", e)
        return jsonify({"message": "Erro ao salvar no banco de dados"}), 500
    return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201


@app.route("/produto", methods=['POST'])
def novo_produto():
    data = request.get_json()
    print("Recebido do front-end:", data)
    try:
        conexao = conectar()
        with conexao:
            with conexao.cursor() as cursor:
                new_produto = Produtos(id_produto = id, foto=data['foto'], categoria=data['categoria'], condicao=data['condicao'],documentacao= data['documentacao'], descricao= data['descricao'])
                sql = "INSERT INTO (id_aluno, nome, email, senha, numero, localizacao) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (
                    new_produto.id_produto,
                    new_produto.foto,
                    new_produto.categoria,
                    new_produto.condicao,
                    new_produto.documentacao,
                    new_produto.descricao 
                ))
            conexao.commit()
    except Exception as e:
        print("Erro ao inserir no banco:", e)
        return jsonify({"message": "Erro ao salvar no banco de dados"}), 500
    return jsonify({"message": "produto cadastrado com sucesso!"}), 201    

# exibir usuário
@app.route("/perfil_usuario", methods=['GET'])
def dados_usuario():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tabela_do_banco")
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    
    return render_template("perfil_usuario.html", resultado = resultados)
    
if __name__ == '__main__':
   app.run(debug = True)