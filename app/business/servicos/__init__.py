from app.business.servicos.itemService import ItemService
from app.business.servicos.itemEstoqueService import ItemEstoqueService
from app.business.servicos.prateleiraService import PrateleiraService
from app.business.servicos.setorService import SetorService

# dont delete the imports
from app.business.entities.item import Item
from app.business.entities.itemEstoque import ItemEstoque
from app.business.entities.prateleira import Prateleira
from app.business.entities.setor import Setor

ItemEstoqueService = ItemEstoqueService()
ItemService = ItemService()
PrateleiraService = PrateleiraService()
SetorService = SetorService()
