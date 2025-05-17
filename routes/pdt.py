from flask import Blueprint, request, jsonify
from models.produtos import Produtos
from database.cenexao import conectar
import os, uuid

pdt_rotas = Blueprint('pdt_rotas', __name__)

# Pasta onde os arquivos serão salvos
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@pdt_rotas.route("/produto", methods=['POST'])
def novo_produto():
    try:
        categoria = request.form.get('categoria')
        condicao = request.form.get('condicao')
        descricao = request.form.get('descricao')

        foto = request.files.get('foto')
     # Salva arquivos com nome único para evitar sobrescrever
        foto_filename = None
        if foto:
            foto_filename = f"{uuid.uuid4().hex}_{foto.filename}"
            foto.save(os.path.join(UPLOAD_FOLDER, foto_filename))


        conexao = conectar()
        with conexao:
            with conexao.cursor() as cursor:
                # Note que id_produto pode ser auto-increment no DB
                new_produto = Produtos(
                    id_produto=None,
                    foto=foto_filename,
                    descricao=descricao,
                    categoria=categoria,
                    condicao=condicao,
                    status='ativo' # status padrao
        
                )
                sql = """
                    INSERT INTO produtos (foto, descricao, categoria, condicao, status) 
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (
                    new_produto.foto,
                    new_produto.descricao,
                    new_produto.categoria,
                    new_produto.condicao,
                    'ativo' # status padrão
                    
                ))
            conexao.commit()

        return jsonify({"message": "Produto cadastrado com sucesso!"}), 201

    except Exception as e:
         print("Erro ao inserir no banco:", e)
         return jsonify({"message": "Erro ao salvar no banco de dados"}), 500