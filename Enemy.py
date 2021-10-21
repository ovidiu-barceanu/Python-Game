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
        print("The enemy makes his attack")
        if (self.randomMiss() == True):
            print("You are lucky. The enemy missed")
        else:
            hitPoints = hitPoints - self.damage
            print("Your hp drops to " + str(hitPoints))
            print("##############")
            print()
            return int(hitPoints)


    def heroAttack(self, enemyLife,heroDamage):
        print("you stare in the eye of your enemy and you make your attack")
        if (self.randomMiss() == True):
            print("Tough luck, you just missed")
        else:
            enemyLife = enemyLife - heroDamage
            print("Enemy hp drops to " + str(enemyLife))
            print("##############")
            print()
            return int(enemyLife)


    def fight(self, heroLife, heroDamage):
        #Counters
        round = 0
        hitPoints = heroLife
        enemyLife = self.hp

        while(hitPoints >= 0):
            while (enemyLife >= 0 ):
                round += 1
                print("Current round is " + str(round))
                print("##############")
                print()

                hitPoints = self.enemyAttack(hitPoints)
                input("Enemy atack end. Hit enter to continue. (press enter)")
                print()
                enemyLife = self.heroAttack(enemyLife, heroDamage)
                input("Your atack end. Hit enter to continue. (press enter)")
                print()

                """
                # Enemy attack round
                print("The enemy makes his attack")
                if(missEnemy == True):
                    print("You are lucky. The enemy missed")
                else:
                    hitPoints = hitPoints - self.damage
                    print("Your hp drops to " + str(hitPoints))
                    print("##############")
                    print()
                
                """
                """
                input("Enemy atack end. Hit enter to continue. (press enter)")
                print()

                # Hero attack round
                print("you stare in the eye of your enemy and you make your attack")
                if (missHero == True):
                    print("Tough luck, you just missed")
                else:
                    enemyLife = enemyLife - heroDamage
                    print("Enemy hp drops to " + str(enemyLife))
                    print("##############")
                    print()


                input("Your atack end. Hit enter to continue. (press enter)")
                print()
                """


                if(hitPoints <= 0):
                    print("you lost")
                    print("you lasted " + str(round) + " rounds")
                    print("##############")
                    print()
                    break
                elif(enemyLife <= 0):
                    print("You succeded in defeating your enemy")
                    print("The enemy lasted " + str(round) + " rounds")
                    print("##############")
                    print()
                    break
            break


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=15, damage=1)


class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)

class Vampire(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)


class Ghoul(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)