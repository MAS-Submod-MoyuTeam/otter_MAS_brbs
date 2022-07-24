init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_clothes",
            category=["be right back"],
            prompt="I'm going to change clothes",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_clothes:
    m 1wub "Oh! Getting a fresh look, [player]?"
    m 1hub "That's great! "
    extend 4fub "It makes me happy that you're taking care of your hygiene."
    m 2hubla "Pick something cute! Ehehehe~"
    
    $ mas_idle_mailbox.send_idle_cb("otter_brb_clothes_callback")
    return "idle"

label otter_brb_clothes_callback:
    m 1wub "Back, [player]?"
    m 2hubla "Yay! Now we can hang out together some more~"
    
return
