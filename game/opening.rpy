define pmc = Character("[mcname]")

label start:
    python:
        mcname = renpy.input("Enter your name:")
        mcname = mcname.strip()

        if not mcname:
            mcname = "Zigludo"

    play music "road taken.mp3"
    scene bedroom

    "Another night on my favourite subreddit, r/shitpostemblem."

    "I always had fun scrolling through the posts here. A little Sigurd here, a little Shinon there..."

    "These days, though, I'm not so sure."

    pmc "..."

    "Do I miss the 776 jokes that much?"

    pmc "..."

    "Whatever. It's getting pretty late, and I still haven't
    finished my latest meme. I've got to get back to work."

    pmc "...Fates... ...bad."

    pmc "Fire Emblem... Blazing... *yawn*"

    "On second thought, maybe I could close my eyes for just a little while..."

    jump intro_to_spe
