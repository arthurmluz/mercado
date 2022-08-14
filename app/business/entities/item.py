from app import db


class Item(db.Model):
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)

    estoque = db.relationship("ItemEstoque", back_populates="_item")

    def __repr__(self):
        return "id: {0} | name: {1} | type {2} |".format(self.id, self.name, self.type)

