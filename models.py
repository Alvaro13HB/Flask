from database import db

class Produto(db.Model):
    __tablename__ = "tb_produto"
    id_produto = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    preco = db.Column(db.Float(2, 10))
    quantidade_estoque = db.Column(db.Integer)


    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    
    def __repr__(self):
        return "<Produto {}>".format(self.nome)
