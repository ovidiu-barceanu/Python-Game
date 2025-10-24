def stopGame():
    global gameIsOn
    gameIsOn = False
    print("Game Stopped")
    quit()

def GameOver():
    global gameIsOn
    gameIsOn = False
    print("GameOver")

def pause():
    input("Press Enter to continue... ")

def choose(prompt: str, *options: str):
    """
    Displays a numbered list of options and returns the chosen option string.
    Example call: choose("Pick a potion?", "yes", "no")
    """
    while True:
        # print(prompt)
        game_log(prompt)
        for i, opt in enumerate(options, start=1):
            print(f"{i} - {opt}")

        choice = input("--> ").strip()

        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return options[idx]

        # print("Invalid choice — choose again.\n")
        game_log("Invalid choice — choose again.\n")

def game_log(msg: str):
    # --- log texts instead of printing in main ---
    print("======" + msg + "======")