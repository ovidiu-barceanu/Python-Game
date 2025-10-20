class PlayerGenerator:

    def __init__(self,name, playerHp, playerDamage):
        self.name = name
        self.playerHp = playerHp
        self.playerDamage = playerDamage

    def __str__(self):
        return self.name

    def playerAttacks(self, enemyhp):
        print ("You attack the enemy for {} damage points".format(self.playerDamage))
        newLife = enemyhp - self.playerDamage
        print("The enemy hp drops to {}".format(newLife))
        return newLife


