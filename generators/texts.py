

from art import text2art


# welcome_text = text2art("Game Start", font="block")
# welcome_text = text2art("Game Start", font="doh")
welcome_text = text2art("Game Start", font="tarty1") # this is ok for welcome screen
# welcome_text = text2art("Game Start", font="tarty2")
# welcome_text = text2art("Game Start", font="tarty3")
# welcome_text = text2art("Game Start", font="tarty4")
# welcome_text = text2art("Game Start", font="tarty5")
# welcome_text = text2art("Game Start", font="tarty7")
# welcome_text = text2art("Game Start", font="tarty8")
# welcome_text = text2art("Game Start", font="tarty9")

def printStarWars(textToPrint):
    ascii_art_starwars = text2art(textToPrint, font="starwars")  # Change "block" to other available fonts
    print(ascii_art_starwars)

def printTarty1(textToPrint):
    print (text2art(textToPrint, font="tarty2"))
# GateHouse Texts

gtText01 = """
On your way to StormHave to sell your goods you make camp near a forest for the night.
While gathering woods for the fire you stumble across a derelict castle.
The GateHouse is is quite decrepit, the walls are falling apart and wood chunks everywhere,
but it looks like the gate is locked.
You wonder if you should explore the castle a little, since there is still some daylight.
"""

# gtText01 = text2art("""
# On your way to StormHave to sell your goods you make camp near a forest for the night.
# While gathering woods for the fire you stumble across a derelict castle.
# The GateHouse is is quite decrepit, the walls are falling apart and wood chunks everywhere,
# but it looks like the gate is locked.
# You wonder if you should explore the castle a little, since there is still some daylight.
# """, font="black_bubble")

gtChoice02 = """
Do you:    
1 - force the gate
2 - try to squeeze through the crack in the wall
3 - for open the door
"""

gtChoice = """
Do you :
1 - Go in the gatehouse
2 - Leave
"""

# The choices are stored in a list of tuples, where the number is the option and the value is the function or action.
# gtChoicesTest = [
#     (1, "Go in the gatehouse", gateHouseScene01),  # If choice is 1, go to gateHouseScene01
#     (2, "Leave", lambda: stopGame)  # If choice is 2, end the game
# ]

gtDeath = """
You try to squeeze through the crack but a boulder shits and the whole pylon crashes onto you and kills you
# """

# gtDeath = text2art("""
# You try to squeeze through the crack but a boulder shits and the whole pylon crashes onto you and kills you
# """, font="black_bubble")

# gtDeath = text2art("""
# You try to squeeze through the crack but a boulder shits and the whole pylon crashes onto you and kills you
# """, font="black_square")
#
# gtDeath = text2art("""
# You try to squeeze through the crack but a boulder shits and the whole pylon crashes onto you and kills you
# """, font="fancy142")
#
# gtDeath = text2art("""
# You try to squeeze through the crack but a boulder shits and the whole pylon crashes onto you and kills you
# """, font="fancy143")
#
# gtDeath = text2art("""
# You try to squeeze through the crack but a boulder shits and the whole pylon crashes onto you and kills you
# """, font="fancy144")
#
# gtDeath = text2art("""
# You try to squeeze through the crack but a boulder shits and the whole pylon crashes onto you and kills you
# """, font="fancy145")



# ForestScene


forestSceneDescription = """
Heading to StormHaven to sell your goods, you make one stop before reaching the city.
The forest next to which you made your camp is old and dense. You can feel old magic and creatures dwelling inside it.
You start gathering wood to keep the fire going for tonight, thinking that you should definitely not go too deep inside the woods, 
which, like often happens, isn't working with you.
You realize that you've wandered too deep into the woods and now stand in front of the gatehouse of an old, decrepit castle.
"""

forestSceneOptions="""
Do you :
1 - Go in the gatehouse
2 - Leave
"""
