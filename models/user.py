class Usuario:
    def __init__(self, id_usuario, nome, email, senha, numero, locatizacao, completed=False) -> None:
            self.id_usuario = id_usuario
            self.nome = nome
            self.email = email
            self.senha = senha
            self.numero = numero
            self.localizacao = locatizacao
            self.completed = completed
    def to_dict(self):
        return {
            "id_Aluno": self.id_usuario,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "numero": self.numero,
            "localizacao": self.localizacao,
            "completed": self.completed
        } 
    