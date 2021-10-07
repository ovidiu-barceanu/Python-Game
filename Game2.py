
import RoomGenerator
import Actions

### imports assignement
actions = Actions.actionList()
room = RoomGenerator.generateRoom()

###initialize dungeon
dungeon = room.choseDungeonSize()

###initalise counters
dungeonCount = 0
heroLifeCounter = 10
enemyLifeCounter

enemyList = ["Dragon", "Vampire", "Ghoul", "none"]
loot = ["healthPotion", "gold"]


while(dungeonCount < dungeon):
    print("dungeonCount is " + str(dungeonCount))
    actions.moveForward()
    room.generateEnemy(enemyList)
    room.generateLoot(loot)
    dungeonCount += 1
    print(dungeonCount)




