class Usuario:
    def __init__(self, nome, email, senha, telefone, localizacao, id_usuario=None, completed=False):
            self.id_usuario = id_usuario
            self.nome = nome
            self.email = email
            self.senha = senha
            self.telefone = telefone
            self.localizacao = localizacao
            self.completed = completed
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
    