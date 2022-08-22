import flask_sqlalchemy

from app import db
from app.business.dbInterface import DBInterface
from app.business.entities.setor import Setor


class SetorService(DBInterface):
    """ SetorService: methods related to accessing/modifying the database table 'setor' """

    @staticmethod
    def getAll():
        """ returns all rows from table 'setor' """
        return db.session.query(Setor).all()

    @staticmethod
    def getById(target_id: int):
        """ Receives an ID, and returns a row with that ID from that table"""

        result = (
            db.session.query(Setor)
            .filter(
                Setor.id == target_id
            )
            .first()
        )
        return result

    @staticmethod
    def getByName(target_name: str):
        """Receives a value, returns all rows with that property value on that table"""

        result = (
            db.session.query(Setor)
            .filter(
                Setor.name == target_name
            )
            .all()
        )

        return result

    @staticmethod
    def create(data: dict):
        """Receives a table and a dictionary with data to create a new object to that table"""
        entity = Setor()

        columns = entity.__table__.columns._all_columns

        DBInterface._validateFields(entity, columns, data)

        # adds the entity on the database and commits the transaction
        db.session.add(entity)
        db.session.commit()

        return entity
