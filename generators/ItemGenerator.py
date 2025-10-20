class ItemGenerator:

    def __init__(self, item_dict):
        self.itemName = item_dict["name"]
        self.itemUsageType = item_dict["consumableType"]
        self.itemUsesLeft = item_dict["usesLeft"]
        self.itemValue = item_dict["value"]



        # if len(item_tuple) != 4:
        #     raise ValueError("Item must have 4 values")
        #
        # self.itemName, self.itemUsageType, self.itemUsesLeft, self.itemValue = item_tuple

    # def __str__(self):
    #     return self.itemName
    # def __str__(self):
    #     # return"Test item testsssssssss"
    #     return f"{self.itemName}\n"
    def __repr__(self):
        # This is what you’ll see inside lists or debugging
        return f"Item({self.itemName}, usesLeft={self.itemUsesLeft}, value={self.itemValue})"

    def decreaseItemUses(self):
        self.itemUsesLeft = self.itemUsesLeft - 1

    def getItemName(self):
        # print(self.itemName)
        return self.itemName

    def getItemUsageType(self):
        return self.itemUsageType

    def getItemUsesLeft(self):
        return self.itemUsesLeft

    def getItemValue(self):
        return self.itemValue

    def getItemUsageType(self):
        return self.itemUsageType