# The game starts here.



label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg dojo

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show phonepizza
    show phonetextbox at Position(xpos=0.38,ypos=0.73) with dissolve
    show text "{color=#a54545}{size=46}Hey!{/color}" at Position(xpos=0.38,ypos=0.69) with dissolve
    
   

    # These display lines of dialogue.

    Joe "Omae wa mo sindeiru."

    hide joe

    show joe2
    
    Joe "NANI!?!?"

    menu: 
        "What storyline?"

        "anime":
            jump anime
        "gamer":
            jump gamer
        "overwatch":
            jump overwatch
        "streamer":
            jump streamer

    return
