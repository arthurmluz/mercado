import flask_sqlalchemy

from app import db
from app.business.dbInterface import DBInterface
from app.business.exceptions import EntityPropertyNotFound, APIBadRequest
from app.business.entities.itemEstoque import ItemEstoque
from app.business.entities.prateleira import Prateleira
from app.business.entities.setor import Setor


class ItemEstoqueService(DBInterface):
    """ ItemEstoqueService: methods related to accessing/modifying the database table 'itemEstoque' """

    @staticmethod
    def getAll():
        """ returns all rows from table 'item' """
        return db.session.query(ItemEstoque).order_by(ItemEstoque.id).all()

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
        """Receives a dictionary with data to create a new object to that table"""
        entity = ItemEstoque()

        columns = entity.__table__.columns._all_columns

        DBInterface._validateFields(entity, columns, data)

        # adds the entity on the database and commits the transaction
        db.session.add(entity)
        db.session.commit()

        return entity

    @staticmethod
    def update(data: dict):

        item_id = data['id']

        item_estoque = (
            db.session.query(ItemEstoque)
            .filter(
                ItemEstoque.id == item_id
            ).first()
        )

        item_estoque.quantity = data['quantity']

        db.session.add(item_estoque)
        db.session.commit()

        return {}

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
