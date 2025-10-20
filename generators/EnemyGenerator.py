import random

# from generators.EnemyStats import enemy


class EnemyGenerator:

    def __init__(self, enemyType, hp, damage):
        self.enemyType = enemyType # Enemy type Goblin, undead etc , string
        self.hp = hp # Enemy hitpoints , int
        self.damage = damage # Enemy damage per hit, int

    # def __del__(self):
    #     print("{} instance has been deleted".format(self.enemyType))


        self.enemies = ["Goblin", "Undead", "Skeleton", "Dragon"]

    def __str__(self):
        return self.enemyType

    def enemyAttack(self, playerhp):
        print ("The {} attacks you for {} points of damage".format(self.enemyType, self.damage))
        newLife = playerhp - self.damage
        print("Your hp drops to {}".format(newLife))
        return newLife

    # def generateEnemy(self, enemy_key, enemies_stats):
    #     """Generate enemy from the enemies_stats dictionary"""
    #     if enemy_key not in enemies_stats:
    #         raise ValueError(f"Enemy '{enemy_key}' not found in stats!")
    #
    #     name, hp, damage = enemies_stats[enemy_key]
    #     self.enemyType = name
    #     self.hp = hp
    #     self.damage = damage
    #     print(f"Generated enemy: {self.enemyType} (HP: {self.hp}, DMG: {self.damage})")
    #     return self

    def generateRandomEnemy(self, ):
        pass


