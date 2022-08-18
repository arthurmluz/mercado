import flask_sqlalchemy

from app import db
from app.business.dbInterface import DBInterface
from app.business.exceptions import EntityPropertyNotFound, APIBadRequest
from app.business.entities.itemEstoque import ItemEstoque
from app.business.entities.prateleira import Prateleira
from app.business.entities.setor import Setor


class ItemEstoqueService(DBInterface):

    @staticmethod
    def getAll():
        return db.session.query(ItemEstoque).all()

    @staticmethod
    def getById(target_id: int):
        """ Receives an ID, and returns a row with that ID from that table"""

        result = (
            db.session.query(ItemEstoque)
            .filter(
                ItemEstoque.id == target_id
            )
            .first()
        )
        return result

    @staticmethod
    def create(data: dict):
        """Receives a table and a dictionary with data to create a new object to that table"""
        entity = ItemEstoque()

        columns = entity.__table__.columns._all_columns

        DBInterface._validateFields(entity, columns, data)

        # adds the entity on the database and commits the transaction
        db.session.add(entity)
        db.session.commit()

        return entity

    @staticmethod
    def delete(target_id: int):

        entity = (
            db.session.query(ItemEstoque)
            .filter(
                ItemEstoque.id == target_id
            )
            .first()
        )

        db.session.delete(entity)
        db.session.commit()

        return True
