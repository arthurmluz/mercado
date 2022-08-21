from app import create_app, root_api, root_blueprint
from flask import jsonify

from app.business.servicos import ItemService, ItemEstoqueService, PrateleiraService, SetorService

app = create_app()

#@root_blueprint.route('/', methods=['GET'])
#def get():  # application's code here
#    res = ItemEstoqueService.getAll()
#    return jsonify(res)


if __name__ == '__main__':
    app.run()
