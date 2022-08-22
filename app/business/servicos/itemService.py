import flask_sqlalchemy

from app import db
from app.business.dbInterface import DBInterface
from app.business.entities.item import Item


class ItemService(DBInterface):
    """ ItemService: methods related to accessing/modifying the database table 'item' """

    @staticmethod
    def getAll():
        """ returns all rows from table 'item' """
        return db.session.query(Item).all()

    @staticmethod
    def getById(target_id: int):
        """ Receives an ID, and returns a row with that ID from that table"""

        result = (
            db.session.query(Item)
            .filter(
                Item.id == target_id
            )
            .first()
        )
        return result

    @staticmethod
    def getByName(target_name: str):
        """Receives a value, returns all rows with that property value on that table"""

        result = (
            db.session.query(Item)
            .filter(
                Item.name == target_name
            )
            .all()
        )

        return result

    @staticmethod
    def getByType(target_type: str):
        """Receives a value, returns all rows with that property value on that table"""

        result = (
            db.session.query(Item)
            .filter(
                Item.type == target_type
            )
            .all()
        )

        return result

    @staticmethod
    def create(data: dict):
        """Receives a table and a dictionary with data to create a new object to that table"""
        entity = Item()

        columns = entity.__table__.columns._all_columns

        DBInterface._validateFields(entity, columns, data)

        # adds the entity on the database and commits the transaction
        db.session.add(entity)
        db.session.commit()

        return entity

    @staticmethod
    def delete(target_id: int):

        entity = (
            db.session.query(Item)
            .filter(
                Item.id == target_id
            )
            .first()
        )

        db.session.delete(entity)
        db.session.commit()

        return True
