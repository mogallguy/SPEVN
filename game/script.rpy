define m = Character("Mogall_Guy")
define e = Character("Eliwood", color="#ff632b")
define mc = Character("Casual")


label intro_to_spe:
    scene homepage
    show mogallguyfieri at right
    show eliwoodbig at left

    e "You're finally awake."
    m "You were trying to cross the border, right?"
    mc "Border? What border? Where am I?"
    m "The border between worlds, of course!"
    e "It's great to meet you, Casual."
    mc "My name is [mcname]!"
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
