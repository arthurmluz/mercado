def register_routes(api, root="api"):  # noqa
    from .EstoqueController import ns
    api.add_namespace(ns, path='')



