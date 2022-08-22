from app import db


class Prateleira(db.Model):
    __tablename__ = "prateleira"

    id = db.Column(db.Integer, primary_key=True)
    max_weight = db.Column(db.Float, nullable=False)
    max_volume = db.Column(db.Float, nullable=False)

    setor = db.Column(db.Integer, db.ForeignKey("setor.id"), nullable=False)
    _setor = db.relationship("Setor", back_populates="prateleiras")

    itens = db.relationship("ItemEstoque", back_populates="_prateleira")

    def __repr__(self):
        return "id: {0} | setor: {1} | max_weight: {2} | max_vol: {3} | ".\
            format(self.id, self.setor, self.max_weight, self.max_volume)


