from app import create_app

from app.business.servicos import ItemService, ItemEstoqueService, PrateleiraService, SetorService

app = create_app()


@app.route('/')
def start():  # application's code here
    a = ItemService.getAll()
#    database.create({"name": "Balinhas", "type": "COMIDAS", "weight": 1, "volume": 1})
    return "{0}".format(a[0].name)


if __name__ == '__main__':
    app.run()
