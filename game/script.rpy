﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character(("Joe"),color="#00ffff")
define y = Character(("You"),color="#ff750f")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show joe

    # These display lines of dialogue.

    m "Omae wa mo sindeiru."

    hide joe

    show joe2
    
    y "NANI!?!?"

    # This ends the game.

    return
