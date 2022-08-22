from flask import request
from flask_restx import Namespace, Resource, marshal_with
from app.adaptadores.schemas.schemas import estoque_fields, estoque_put_fields, setor_fields, prateleira_fields
from app.business.servicos import ItemService, ItemEstoqueService, PrateleiraService, SetorService

ns = Namespace(name="estoque", description="Funções relativas ao Estoque")


@ns.route("", methods=['GET', 'POST', 'PUT'])
class EstoqueController(Resource):

    @ns.response(200, "Estoque successfully read")
    @marshal_with(estoque_fields)
    def get(self):
        """Gets all estoque"""
        return ItemEstoqueService.getAll()

    @ns.response(200, "Estoque updated")
    @ns.expect(estoque_put_fields)
    def put(self):
        """Edits itemEstoque"""
        return ItemEstoqueService.update(data=request.json)


@ns.route("/setor/<string:setor>", methods=['GET'])
class EstoqueSetorController(Resource):

    @ns.response(200, "Setores successfully read")
    @marshal_with(setor_fields)
    def get(self, setor):
        """Returns all itens on determined setor"""
        return SetorService.getByName(setor)


@ns.route("/prateleira/<int:prateleira>")
class EstoquePrateleiraController(Resource):

    @ns.response(200, "Prateleiras successfully read")
    @marshal_with(prateleira_fields)
    def get(self, prateleira):
        """Returns all itens on detetermined prateleira"""
        return PrateleiraService.getById(prateleira)
