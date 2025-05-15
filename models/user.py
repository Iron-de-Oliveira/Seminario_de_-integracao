from flask_login import UserMixin
from database.cenexao import conectar

class Usuario(UserMixin):
    def __init__(self, nome, email, senha, telefone, localizacao, id_usuario=None, completed=False):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.localizacao = localizacao
        self.completed = completed

    def get_id(self):
        return str(self.id_usuario)

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "telefone": self.telefone,
            "localizacao": self.localizacao,
            "completed": self.completed
        }

    @staticmethod
    def buscar_por_email(email):
        conn = conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
                dados = cursor.fetchone()
                if dados:
                    return Usuario(
                        id_usuario=dados['id_usuario'],
                        nome=dados['nome'],
                        email=dados['email'],
                        senha=dados['senha'],
                        telefone=dados['telefone'],
                        localizacao=dados['localizacao'],
                        completed=dados['completed']
                    )
        finally:
            conn.close()
        return None

    @staticmethod
    def buscar_por_id(user_id):
        conn = conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (user_id,))
                dados = cursor.fetchone()
                if dados:
                    return Usuario(
                        id_usuario=dados['id_usuario'],
                        nome=dados['nome'],
                        email=dados['email'],
                        senha=dados['senha'],
                        telefone=dados['telefone'],
                        localizacao=dados['localizacao'],
                        completed=dados['completed']
                    )
        finally:
            conn.close()
        return None
