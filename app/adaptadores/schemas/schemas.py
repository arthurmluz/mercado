from flask_restx import fields
from app import root_api as api

item_fields = api.model("ItemModel", {
    'id': fields.Integer(),
    'name': fields.String(),
    'type': fields.String(),
    'weight': fields.Float(),
    'volume': fields.Float()
})

estoque_fields = api.model("EstoqueModel", {
    'id': fields.Integer(),
    'quantity': fields.Integer(),
    'prateleira': fields.Integer(),
    'item': fields.Nested(item_fields, attribute='_item')
})

prateleira_fields = api.model("PrateleiraModel", {
    'id': fields.Integer(),
    'max_weight': fields.Float(),
    'max_volume': fields.Float(),
    'itens': fields.List(
        fields.Nested(estoque_fields)
    )
})

setor_fields = api.model("SetorModel", {
    'id': fields.Integer(),
    'name': fields.String(),
    'prateleiras': fields.List(
        fields.Nested(prateleira_fields)
    )
})

estoque_put_fields = api.model("EstoquePutModel", {
    'id': fields.Integer(),
    'quantity': fields.Integer(),
})

estoque_post_fields = api.model("EstoquePostModel", {
    'item_id':  fields.Integer(),
    'quantity': fields.Integer(),
})


