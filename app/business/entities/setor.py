from app import db


class Setor(db.Model):
    __tablename__ = "setor"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    prateleiras = db.relationship("Prateleira", back_populates="_setor")

    def __repr__(self):
        return "id: {0} | name: {1} |".format(self.id, self.name)
