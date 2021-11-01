import random

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

    def randomMiss(self):
        miss = random.choice([True, False])
        return miss

    def enemyAttack(self, hitPoints):
        print("The " + self.name + " makes his attack")
        if (self.randomMiss() == True):
            print("You are lucky. The " + self.name + " missed")
            return hitPoints
        else:
            hitPoints = hitPoints - self.damage
            print("Your hp drops to " + str(hitPoints))
            print("##############")
            print()
            return hitPoints


    def heroAttack(self, enemyLife,heroDamage):
        print("You take a deep breath and measure your enemy, then make your attack")
        if (self.randomMiss() == True):
            print("Tough luck, you just missed")
            return enemyLife
        else:
            enemyLife = enemyLife - heroDamage
            print("The " + self.name + " HitPoints drops to " + str(enemyLife))
            print("##############")
            print()
            return enemyLife

    def checkWinner(self, hitPoints, enemyLife, round):
        if (hitPoints <= 0):
            print("you lost")
            print("you lasted " + str(round) + " rounds")
            print("##############")
            print()

        elif (enemyLife <= 0):
            print("You succeded in defeating your enemy")
            print("The enemy lasted " + str(round) + " rounds")
            print("##############")
            print()

    def fightSequence(self, heroLife, heroDamage):
        #Counters
        round = 0
        hitPoints = heroLife
        print(hitPoints)
        enemyLife = self.hp
        print(enemyLife)
#TODO find a whay to separate the fight
        while(hitPoints >= 1 or enemyLife >= 1):
            #while (enemyLife >= 0):
            round += 1
            print("Current round is " + str(round))
            print("##############")
            print()
            hitPoints = self.enemyAttack(hitPoints)
            input("Enemy atack round ended. Hit enter to continue. (press enter)")
            print(hitPoints)
            print()
            enemyLife = self.heroAttack(enemyLife, heroDamage)
            input("Your attack round ended. Hit enter to continue. (press enter)")
            print(enemyLife)
            print()

        self.checkWinner(hitPoints, enemyLife, round)


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=2, damage=1)


class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)

class Vampire(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)


class Ghoul(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)