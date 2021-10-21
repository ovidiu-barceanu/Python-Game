
import RoomGenerator
import Actions
import Enemy

### imports assignement
actions = Actions.actionList()
room = RoomGenerator.generateRoom()
ogre = Enemy.Ogre()

###initialize dungeon
dungeon = room.choseDungeonSize()

###initalise counters
dungeonCount = 0
heroLifeCounter = 20
heroDamage = 1
enemyLifeCounter = 10

enemyList = ["Dragon", "Vampire", "Ghoul", "GiantSpider", "Ogre", "none"]
loot = ["healthPotion", "gold"]


while(dungeonCount < dungeon):
    print("dungeonCount is " + str(dungeonCount))
    actions.moveForward()
    #room.generateEnemy(enemyList)
    ogre.fight(heroLifeCounter, heroDamage)
    ogre.is_alive()
    room.generateLoot(loot)
    dungeonCount += 1
    print(dungeonCount)




