define m = Character("Mogall_Guy")
## define e = Character("Eliwood", color="#ff632b")
define e = Character("Lorenz", color="#ff632b")
define mc = Character("Casual")

define longfade = Fade(3.0, 0.0, 3.0)

label intro_to_spe:
    scene homepage with longfade
    show mogallguyfieri at right with moveinright
    show lorenz_mogall at left with moveinleft

    e "You're finally awake."
    m "You were trying to cross the border, right?"
    mc "Border? What border? Where am I?"
    m "The border between worlds, of course!"
    e "It's great to meet you, Casual."
    mc "My name is [mcname]!"
    e "There are better places to take a nap than on the ground, Casual."
    e "Give me your hand."

    "I take the mogall's tentacle and rise to my feet."

    mc "What is this place?"
    m "Welcome to the world of SPE."
    m "There are lots of mogalls and furrets. It's a wonderful place."
    e "Thanks for the welcome I will subscribe so we can beat naughty r/FEH"
    m "I want you to do something else besides subscribe..."
    e "Eh?! Kyaa!~~"

    ## Mogall messing around with showing protag over menus
    hide eliwoodbig
    show eliwoodbig onlayer o_screen
    menu:
        "Kiss the wiggly man":
            hide eliwoodbig onlayer o_screen
            show eliwoodbig at left
            jump kissmogall
        "Run away and get a bad end":
            hide eliwoodbig onlayer o_screen
            show eliwoodbig at left
            jump badend1

label kissmogall:
    m "Mmm oh yeah baby pucker up"
    jump ending

label badend1:
    m "Too bad so sad"
    jump ending

label ending:
    hide mogallguyfieri
    e "Free will doesn't exist haha yeah"
    return
