from flask import Blueprint, render_template, request, jsonify
from models.user import Usuario
from database.cenexao import conectar

user_rotas = Blueprint('user_rotas', __name__)

# NOVO USUÁRIO
@user_rotas.route("/usuario", methods=['POST'])
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

# exibir usuário
@user_rotas.route("/perfil_usuario", methods=['GET'])
def dados_usuario():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tabela_do_banco")
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    
    return render_template("perfil_usuario.html", resultado = resultados)