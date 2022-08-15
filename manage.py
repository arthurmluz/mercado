from app import create_app
from app.business.entities.item import Item

from app.business.database import database
from app.business.entities.itemEstoque import ItemEstoque
from app.business.entities.prateleira import Prateleira
from app.business.entities.setor import Setor

app = create_app()


@app.route('/')
def start():  # application's code here
    database.getAll(Setor)
#    database.createEntity(Item, {"name": "Balinhas", "type": "COMIDAS", "weight": 1, "volume": 1})
    return "tela inicial"


if __name__ == '__main__':
    app.run()
