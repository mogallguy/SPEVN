define e = Character("Mogall_Guy")
define l = Character("Eliwood")


label start:
    play music "road taken.mp3"
    scene homepage
    show mogallguyfieri at right
    show eliwoodbig at left

    e "Welcome to the world of SPE."
    e "There are lots of mogalls and furrets. It's a wonderful place."
    l "Thanks for the welcome I will subscribe so we can beat naughty r/FEH"

    menu:
        "Kiss the wiggly man":
            jump kissmogall
        "Run away and get a bad end":
            jump badend1

label kissmogall:
    e "Mmm oh yeah baby pucker up"
    return

label badend1:
    e "Too bad so sad"
    return
