from abc import ABC, abstractmethod

from app.business.exceptions import DatabaseEntityNotFound


# Database Interface
# Contains methods to be used on future databases
class DBInterface(ABC):
    """Table model is the type of the class that implements the tables"""
    tableModel = None

    # verifies if entity is part of the database model being used
    @staticmethod
    def checkEntity(table):
        """Checks if given object is really a table from the current db"""
        if type(table) != DBInterface.tableModel:
            raise DatabaseEntityNotFound(table.__name__)

    @staticmethod
    @abstractmethod
    def getAll(table):
        """ Receives a table and returns all rows from it"""
        pass

    @staticmethod
    @abstractmethod
    def getById(table, target_id):
        """ Receives a table (entity) and ID, and returns a row with that ID from that table"""
        pass

    @staticmethod
    @abstractmethod
    def getByProperty(table, target_property, target_value):
        """Receives a table (entity) a property and a value, returns all rows with that property value on that table"""
        pass

    @staticmethod
    @abstractmethod
    def createEntity(table, data):
        """Receives a table and a dictionary with data to create a new object to that table"""
        pass
