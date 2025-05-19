from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from models.produtos import Produtos
from flask_cors import cross_origin
import base64
from database.cenexao import conectar

pdt_rotas = Blueprint('pdt_rotas', __name__)

# cadastrar produto
@pdt_rotas.route("/produto", methods=['POST'])
@cross_origin()
def novo_produto():
    try:
        data = request.get_json()
        print("Recebido do front-end:", data)

        conexao = conectar()
        with conexao:
            with conexao.cursor() as cursor:
                new_produto = Produtos(
                    idprodutos=None,
                    foto=data['foto'],
                    descricao=data['descricao'],
                    categoria=data['categoria'],
                    condicao=data['condicao'],
                    status=data['status'])
                sql = "INSERT INTO produtos (foto, descricao, categoria, condicao, status) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (
                    new_produto.foto,
                    new_produto.descricao,
                    new_produto.categoria,
                    new_produto.condicao,
                    new_produto.status
                ))


            conexao.commit()

        return jsonify({"message": "Produto cadastrado com sucesso!"}), 201

    except Exception as e:
        print("Erro ao inserir no banco:", e)
        return jsonify({"message": "Erro ao salvar no banco de dados"}), 500


# mostrar produtos em home

@pdt_rotas.route("/resultado", methods=['GET'])


def dados_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT foto FROM produtos")
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    Produtos = []

    for row in resultados:
        foto_bytes = row["foto"]

        if foto_bytes:
            foto_base64 = base64.b64encode(foto_bytes).decode('utf-8')
            foto_base64 = f"data:image/png;base64,{foto_base64}"
        else:
            foto_base64 = ''

    return render_template("home.html", resultado=Produtos)

