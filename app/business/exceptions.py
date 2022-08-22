from werkzeug.exceptions import NotFound, BadRequest

""" Contains exceptions to be raised when a problem occurs """


class DatabaseEntityNotFound(Exception):
    """ 404, DataBase Entity Not Found Exception"""
    def __init__(self, entity_name=None):
        raise NotFound(description="Entity Not Found on Database '{0}'".format(entity_name))


class EntityPropertyNotFound(Exception):
    """Entity Property Not Found Exception"""
    def __init__(self, entity_name=None, entity_prop=None):
        raise NotFound(description="Entity Property '{0}' Not Found on '{1}'".format(entity_prop, entity_name))


class APIBadRequest(Exception):
    """*400* BadRequest"""
    def __init__(self, description="Bad Request"):
        raise BadRequest(description=description)
