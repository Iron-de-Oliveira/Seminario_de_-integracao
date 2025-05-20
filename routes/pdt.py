from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from models.produtos import Produtos
from flask_cors import cross_origin
from database.cenexao import conectar

pdt_rotas = Blueprint('pdt_rotas', __name__)

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'

# cadastrar produto
@pdt_rotas.route("/produto", methods=['POST'])
@cross_origin()
def novo_produto():
    try:
        print("Recebendo dados do formulário...")

        foto = request.files.get("foto")
        categoria = request.form.get("categoria")
        condicao = request.form.get("condicao")
        descricao = request.form.get("descricao")
        status = request.form.get("status")

        if not foto:
            return jsonify({"message": "Imagem não enviada"}), 400

        # Salva imagem no servidor
        nome_arquivo = foto.filename
        caminho = os.path.join("static", "uploads", nome_arquivo)
        foto.save(caminho)

        caminho_no_banco = os.path.join("uploads", nome_arquivo)

        conexao = conectar()
        with conexao:
            with conexao.cursor() as cursor:
                sql = "INSERT INTO produtos (foto, descricao, categoria, condicao, status) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (
                    caminho_no_banco,
                    descricao,
                    categoria,
                    condicao,
                    status
                ))
            conexao.commit()

        return jsonify({"message": "Produto cadastrado com sucesso!"}), 201

    except Exception as e:
        print("Erro ao salvar no banco:", e)
        return jsonify({"message": "Erro no servidor"}), 500
