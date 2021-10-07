import inventory as inv







"""
mystuff = {'apple': "I am apples!"}
print mystuff['apple']

import mystuff
mystuff.apple()

print mystuff.tangerine
"""

class Inventory(object):
    bag = []
    #global.item???

    def addToBag(self):

        self.bag.append(item)

    def CheckBag(self):
        print "you have %d items " %len(self.bag)
        print self.bag

class BackPack(Inventory):

    def checkType(self):
        print "This is a BackPack. It has few slots available"

item = "test"

invent1 = Inventory()
invent1.addToBag()
invent1.CheckBag()


print "############################"


invent2 = BackPack()
invent2.addToBag()
invent2.CheckBag()
invent2.checkType()





