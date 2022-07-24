init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_vc",
            category=["be right back"],
            prompt="I'm going to voice chat with someone",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_vc:
    m 3wub "Going to hang out with a friend, [player]?"
    m 3hua "That's amazing!"
    m 1hub "Tell them I said hi! Ahahaha!"
    m 5rua "Have a great time with them, I'll be waiting for you~"

    $ mas_idle_mailbox.send_idle_cb("otter_brb_vc_callback")
    return "idle"

label otter_brb_vc_callback:
    m 1htb "Welcome back, [mas_get_player_nickname()]!"
    m 3htb "Did you have a good time?"
    m 3ttb "Were they nice with my precious [player]?"
    m 3tfa "They better be! "
    extend 3htb "Ehehehe~"
    m 5fua "Let's spend more time together~"

    return
