from flask import Blueprint, request, jsonify
from models.produtos import Produtos
from database.cenexao import conectar

pdt_rotas = Blueprint('pdt_rotas', __name__)

@pdt_rotas.route("/produto", methods=['POST'])
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