class Produtos:
    def __init__(self, idprodutos, foto, descricao, categoria, condicao, status ):
        self.idprodutos = idprodutos
        self.foto = foto
        self.descricao = descricao
        self.categoria = categoria
        self.condicao = condicao
        self.status = status


   
    def to_dict(self):
        return{
          "idproduto": self.idprodutos,
          "foto": self.foto,
          "descricao": self.descricao, 
          "categoria": self.categoria,
          "condicao" : self.condicao,
          "status": self.status
 
        }
        

