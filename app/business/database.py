import flask_sqlalchemy

from app import db
from app.business.dbInterface import DBInterface
from app.business.exceptions import EntityPropertyNotFound, APIBadRequest


class Database(DBInterface):

    DBInterface.tableModel = flask_sqlalchemy.model.DefaultMeta

    @staticmethod
    def getAll(table):
        DBInterface.checkEntity(table)

        return db.session.query(table).all()

    @staticmethod
    def getById(table, target_id: int):
        """ Receives a table (entity) and ID, and returns a row with that ID from that table"""
        DBInterface.checkEntity(table)

        result = (
            db.session.query(table)
            .filter(
                table.id == target_id
            )
            .first()
        )
        return result

    @staticmethod
    def getByProperty(table: db.Model, target_property: str, target_value):
        """Receives a table (entity) a property and a value, returns all rows with that property value on that table"""
        DBInterface.checkEntity(table)

        if hasattr(table, target_property) is False:
            return EntityPropertyNotFound(entity_name=table.__name__, entity_prop=target_property)

        result = (
            db.session.query(table)
            .filter(
                getattr(table, target_property) == target_value
            )
            .all()
        )

        return result

    @staticmethod
    def createEntity(table: db.Model, data: dict):
        """Receives a table and a dictionary with data to create a new object to that table"""
        DBInterface.checkEntity(table)
        entity = table()

        # gets all columns from the table entity
        columns = entity.__table__.columns._all_columns

        # for each column attribute on selected table
        for column in columns:
            col_name = column.description
            # id is autogenerated, ignore it
            if col_name == "id":
                continue

            # check if data payload has the column
            if col_name in data:
                setattr(entity, col_name, data[col_name])  # set the column attribute with received value
            elif column.nullable:
                # if it's not on the received data, but is nullable, set as default value
                setattr(entity, col_name, column.default)
            else:
                # if it's not on the data nor is a nullable column
                # throw bad request
                raise APIBadRequest(description="BadRequest creating new entity: '{0}' must be on the payload"
                                    .format(col_name))

        print(entity)
        # adds the entity on the database and commits the transaction
        db.session.add(entity)
        db.session.commit()

        return entity


database = Database()
