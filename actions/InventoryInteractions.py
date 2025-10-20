from generators.InventoryGenerator import Inventory
from generators.ItemGenerator import ItemGenerator

def addItemToInventory(inventory, item):
    inventory.add_item(item)
    print("adding :", item)

def removeItemFromInventory(inventory, item):
    inventory.removeItem(item)
    print("removing :", item)

def useItem():
    print("Use item")
    # if itemUse == 0 then remove item