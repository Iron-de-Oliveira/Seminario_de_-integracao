class produtos:
    def __init__(self, foto, categoria, condicao, documentacao, descricao ):
        self.foto = foto
        self.categoria = categoria,
        self.condicao = condicao,
        self.documentacao = documentacao,
        self.descricao = descricao
   
    def to_dict(self):
        return{
          "foto": self.foto, 
          "categoria": self.categoria,
          "condicao" : self.condicao,
          "documentacao": self.documentacao,
          "descricao": self.descricao  
        }
        

