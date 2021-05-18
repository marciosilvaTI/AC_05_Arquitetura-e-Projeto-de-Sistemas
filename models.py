# models.py


from app import db


class Produto(db.Model):
    __tablename__ = "produto"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo_barras = db.Column(db.String(50), nullable=False, unique=True)
    descricao_produto = db.Column(db.String(40), nullable=False)
    quantidade_produto = db.Column(db.Integer, nullable=False)
    preco_venda = db.Column(db.Float(2, 0), nullable=False)

    def __init__(self, codigo_barras, descricao_produto, quantidade_produto,
                 preco_venda):

        self.codigo_barras = codigo_barras
        self.descricao_produto = descricao_produto
        self.quantidade_produto = quantidade_produto
        self.preco_venda = preco_venda

    def __repr__(self):
        return "<Produto %r>" % self.id
