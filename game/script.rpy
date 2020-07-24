# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character (("Joe-Sensei"), color = "#88d8c0")
define y = Character (("Me"), color = "#33eb91")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene dojo

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show joe

    # These display lines of dialogue.

    m "Omae wa mo sindeiru." (what_color="#828")

    hide joe

    show joe2
    
    y "NANI!?!?"

    # This ends the game.

    return
