from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from models.produtos import Produtos
from flask_cors import cross_origin
from datetime import date
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
        
         # Cria a pasta se não existir
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        # Salva imagem no servidor
        nome_arquivo = secure_filename(foto.filename)

        caminho = os.path.join(UPLOAD_FOLDER, nome_arquivo)
        foto.save(caminho)

         # Caminho relativo para salvar no banco
        caminho_no_banco = os.path.join("uploads", nome_arquivo)

        conexao = conectar()
        conexao = conectar()
        with conexao:
            with conexao.cursor() as cursor:
                # 1) Criar a transação com produto_idproduto = None
                tipo_transacao = 'Doacao'
                usuario_idusuario = 1
                avaliacao_id = None
                data_transacao = date.today()

                sql_transacao = """
                    INSERT INTO transacoes (tipo_transacao, data_transacao, usuario_idusuario, produto_idproduto, avaliacao_idavaliacoes)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql_transacao, (tipo_transacao, data_transacao, usuario_idusuario, None, avaliacao_id))
                idtransacoes = cursor.lastrowid

                # 2) Inserir o produto com a FK da transação
                sql_produto = """
                    INSERT INTO produtos (foto, descricao, categoria, condicao, status, transacoes_idtransacoes)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql_produto, (caminho_no_banco, descricao, categoria, condicao, status, idtransacoes))
                idprodutos = cursor.lastrowid

                # 3) Atualizar a transação com o id do produto
                sql_update = """
                    UPDATE transacoes SET produto_idproduto = %s WHERE idtransacoes = %s
                """
                cursor.execute(sql_update, (idprodutos, idtransacoes))

            conexao.commit()

        return jsonify({"message": "Produto cadastrado com sucesso!"}), 201

    except Exception as e:
        print("Erro ao salvar no banco:", e)
        return jsonify({"message": "Erro no servidor"}), 500