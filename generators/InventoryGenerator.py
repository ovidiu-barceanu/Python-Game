# ----- Custom Exceptions -----

class ItemNotFoundError(Exception):
    """Raised when trying to access or use an item not in the inventory."""
    pass

# --- Inventory Class ---

class Inventory:

    def __init__(self):
        self.inventory = []  # List to store items

    def __str__(self):
        # return (f"The content of your endless bag consists of  : {self.inventory} \n") # this shows the invent as : ['item1', 'item2']
        if not self.inventory:  # Check if the inventory is empty
            return "Your endless bag is empty.\n"
        # return f"The content of your endless bag consists of: {', '.join(self.inventory)}\n" # this shows the invent as : item1, item2
        return f"The content of your endless bag consists of: {', '.join(item.getItemName() for item in self.inventory)}\n"

    def add_item(self, item):
        print(f"You pick up the {item.getItemName()}")
        self.inventory.append(item)
        return self.inventory

    def removeItem(self, item):
        self.inventory.remove(item)
        print(f"You used {item.getItemName()}")
        return self.inventory

    def useItem(self, item):
        item.decreaseItemUses()
        uses_left = item.getItemUsesLeft()
        print(f"{item.getItemName()} has {uses_left} uses left.")
        if uses_left == 0:
            print(f"Item {item.getItemName()} is expended")
            self.removeItem(item)


    def getInventoryItemStats(self, item):
        if item not in self.inventory:
            return f"Item {item} is not in your inventory."

        stats = (
            f"Name: {item.getItemName()}\n"
            f"Usage Type: {item.getItemUsageType()}\n"
            f"Uses Left: {item.getItemUsesLeft()}\n"
            f"Value: {item.getItemValue()}\n"
        )
        return stats

# ====== NEW METHODS ======
    def getItemByType(self, item_type):
        for item in self.inventory:
            if item.getItemName() == item_type:
                return item
        raise ItemNotFoundError(f"Item '{item_type}' not found in inventory.")

    def hasItemOfType(self, item_type):
        return any(item.getItemName() == item_type for item in self.inventory)



