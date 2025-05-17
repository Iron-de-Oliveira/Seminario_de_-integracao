class Produtos:
    def __init__(self, id_produto, foto, descricao, categoria, condicao, status ):
        self.id_produto = id_produto,
        self.foto = foto,
        self.descricao = descricao,
        self.categoria = categoria,
        self.condicao = condicao,
        self.status = status
        
   
    def to_dict(self):
        return{
          "id_produto": self.id_produto,
          "foto": self.foto, 
          "descricao": self.descricao, 
          "categoria": self.categoria,
          "condicao" : self.condicao,
          "status": self.status
 
        }
        

