class actionList:
    def __init__(self):

        print("initialise acctions")

    def moveForward(self):
        print("Will you move forward?")
        answer = str(input("==>"))
        if (answer == "y"):
            print("Going to the next room")
        elif (answer == "n"):
            print("Time passes by while you struggle to make a simple decision and you starve to death. Game Over")
            return
