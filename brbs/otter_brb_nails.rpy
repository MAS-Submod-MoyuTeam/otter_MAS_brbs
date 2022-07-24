init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_nails",
            category=["be right back"],
            prompt="I'm going to do my nails",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_nails:
    m 2sub "Awww, good luck, [player]!"
    m 2kua "Make them as pretty as you always do!"
    m 2hub "And have fun~"

    $ mas_idle_mailbox.send_idle_cb("otter_brb_nails_callback")
    return "idle"

label otter_brb_nails_callback:
    m 2wub "You're back, [player]?"
    m 2sub "Do they look good?"
    m 5rta "I wonder what color of nail polish you used..."
    m 5hsa "Ehehehe~"
    m 5wso "Careful not to smudge it while using the computer, okay?"

    return
