

# def makeChoice(text):
    # choice = input(text+"> ")
    # return int(choice)

def makeChoice(choices):
    print("What do you want to do?")
    # Display each choice to the player
    for choice in choices:
        print(f"{choice[0]} - {choice[1]}")  # choice[0] is the number, choice[1] is the description

    # Get player input and find the matching choice
    choice = input("> ")

    try:
        choice = int(choice)  # Convert input to an integer
        # Find the action for the selected choice
        for option in choices:
            if option[0] == choice:
                print()
                return option[2]()  # Call the function associated with the choice
        else:
            print("Invalid choice, try again.")
            return makeChoice(choices)  # Recurse if the choice is invalid
    except ValueError:
        print("Invalid input, please enter a number.")
        return makeChoice(choices)  # Recurse if the input is not a valid number


def pickUpObject():
    print("picking up")

def useObject():
    print("using object")

def movePlayer():
    print("moving")

def playerDeath(text):
    print(text)
    print("Game Over")
    return False

def wait_for_space():
    import sys
    import termios
    import tty

    print("Press SPACE to continue...")
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1)
            if ch == " ":
                break
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)