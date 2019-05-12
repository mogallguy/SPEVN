define pmc = Character("[mcname]")


label start:
    python:
        mcname = renpy.input("Enter your name:")
        mcname = mcname.strip()

        if not mcname:
            mcname = "Zigludo"

    play music "road taken.mp3"
    scene bedroom

    pmc "Another night on my favourite subreddit, r/shitpostemblem."

    "Although, I was pretty tired. Maybe if I closed my eyes for
    just a little while..."

    jump intro_to_spe
