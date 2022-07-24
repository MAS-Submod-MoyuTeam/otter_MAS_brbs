init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_socials",
            category=["be right back"],
            prompt="I'm going to check my social media",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_socials:
    m 2wuo "Oh! Okay, [player]!"
    m 3rusdld "Careful not to doomscroll, okay?"
    m 1rusdlb "Ehehe..."
    m 1hua "See you in a bit~"

    $ mas_idle_mailbox.send_idle_cb("otter_brb_socials_callback")
    return "idle"

label otter_brb_socials_callback:
    m 2sub "You're back, [player]?"
    m 4hsa "Anything good on your socials?"
    m 2hsb "Ehehehe!"
    m 5fsbsa "If I had a social profile, I would like all your posts~"

    return
