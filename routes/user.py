from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from flask_login import login_required
from models.user import Usuario
from flask_cors import cross_origin
from database.cenexao import conectar
import re

user_rotas = Blueprint('user_rotas', __name__)

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao, email))

# NOVO USUÁRIO
@user_rotas.route("/usuario", methods=['POST'])
@cross_origin()  
def novo_usuario():
    try:
        data = request.get_json()
        print("Recebido do front-end:", data)

        conexao = conectar()
        with conexao:
            with conexao.cursor() as cursor:
                 # Verifica se email já existe
                cursor.execute("SELECT * FROM usuario WHERE email = %s", (data['email'],))
                existente = cursor.fetchone()
                if existente:
                    return jsonify({"message": "Email já cadastrado."}), 400
                # id = gerar_id_unico(cursor) # variável recebe id aleatório
                new_usuario = Usuario(idusuario = None, nome=data['nome'], email=data['email'], senha= data['senha'], telefone= data['telefone'], localizacao= data['localizacao'])
                sql = "INSERT INTO usuario (nome, email, senha, telefone, localizacao) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (
                    new_usuario.nome,
                    new_usuario.email,
                    new_usuario.senha,
                    new_usuario.telefone,  
                    new_usuario.localizacao
                    
                ))
            conexao.commit()
    
    except Exception as e:
        print("Erro ao inserir no banco:", e)
        
        return jsonify({"message": "Erro ao salvar no banco de dados"}), 500
    return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201

# exibir usuário
@user_rotas.route("/perfil_usuario", methods=['GET'])
@login_required
def dados_usuario():

    
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT idusuario, nome, email, telefone, localizacao From usuario")
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    usuarios = []
    for row in resultados:
        usuarios.append({
            "id_usuario": row[0],
            "nome": row[1],
            "email": row[2], 
            "telefone": row[4],
            "localizacao": row[5]
        })

    return render_template("perfil_usuario.html", resultado=usuarios)

# Atualizar usuário

@user_rotas.route("/usuario/<int:idusuario>", methods=['PUT'])
@cross_origin()
@login_required
def atualizar_usuario(idusuario):
    try:
        data = request.get_json()
        print("Dados para atualização:", data)

        conexao = conectar()
        with conexao:
            with conexao.cursor() as cursor:
                # Verifica se usuário existe
                cursor.execute("SELECT * FROM usuario WHERE idusuario = %s", (idusuario,))
                existente = cursor.fetchone()
                if not existente:
                    return jsonify({"message": "Usuário não encontrado."}), 404
                
                # Monta a query dinamicamente para atualizar só os campos enviados
                campos = []
                valores = []
                for campo in ['nome', 'email', 'senha', 'telefone', 'localizacao']:
                    if campo in data:
                        campos.append(f"{campo} = %s")
                        valores.append(data[campo])

                if not campos:
                    return jsonify({"message": "Nenhum campo para atualizar."}), 400

                valores.append(idusuario)
                sql = f"UPDATE usuario SET {', '.join(campos)} WHERE idusuario = %s"
                cursor.execute(sql, valores)
            conexao.commit()

    except Exception as e:
        print("Erro ao atualizar no banco:", e)
        return jsonify({"message": "Erro ao atualizar usuário"}), 500
    
    return jsonify({"message": "Usuário atualizado com sucesso!"}), 200
