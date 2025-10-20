from random import randint


class Actions:

    def __init__(self, player, enemy):
        # self.character = character
        self.player = player
        self.enemy = enemy

#Private method
    def __diceRoll(self, character):
        print("{}'s turn to roll the dice".format(character))
        roll = randint(1, 6)
        print("{} rolled a {}".format(character, roll))
        return roll

    def strikeOrder(self):
        # global enemy_dice, player_dice
        enemy_dice = self.__diceRoll(self.enemy)
        player_dice = self.__diceRoll(self.player)

        while enemy_dice == player_dice:  # Keep rerolling until there's no tie
            print("It's a tie! Rerolling...")
            # enemy_dice = diceRoll(self.enemy)
            # player_dice = diceRoll(self.player)

        if enemy_dice > player_dice:
            print("The enemy was faster and strikes first")
            return 'enemy'
        else:
            print("You were faster and strike first")
            return "player"
