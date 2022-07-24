init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_housework",
            category=["be right back"],
            prompt="I'm going to do some housework.",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_housework:
    m "Aww, that's so responsible of you, [player]!"
    m "Guess I'll see you in a bit, take your time on those chores!"
    m "Maybe put on some music to have fun while you do them."
    m "I'll be right here waiting for you."
    
    $ mas_idle_mailbox.send_idle_cb("otter_brb_housework_callback")
    return "idle"

label otter_brb_housework_callback:
    m "Yay, you're back!"
    m "I hope you're not too tired, [player]!"
    m "Nevertheless, take your deserved rest."
    m "With me! Ehehehe~"
    
return
