class Produtos:
    def __init__(self,id_produto, foto, categoria, condicao, documentacao, descricao ):
        self.id_produto = id_produto,
        self.foto = foto
        self.categoria = categoria,
        self.condicao = condicao,
        self.documentacao = documentacao,
        self.descricao = descricao
   
    def to_dict(self):
        return{
          "id_produto": self.id_produto,
          "foto": self.foto, 
          "categoria": self.categoria,
          "condicao" : self.condicao,
          "documentacao": self.documentacao,
          "descricao": self.descricao  
        }
        

