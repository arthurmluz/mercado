from app import db


class ItemEstoque(db.Model):
    __tablename__ = "item_estoque"

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=0)

    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    prateleira = db.Column(db.Integer, db.ForeignKey("prateleira.id"), nullable=False)

    _item = db.relationship("Item", back_populates="estoque")
    _prateleira = db.relationship("Prateleira", back_populates="itens")

    def __repr__(self):
        return "id: {0} | qtd: {1} | item_id {2} | prateleira {3}"\
            .format(self.id, self.quantity, self.item_id, self.prateleira)
