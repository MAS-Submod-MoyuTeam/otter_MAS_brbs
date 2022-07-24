init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_note",
            category=["be right back"],
            prompt="I'm going to take a note.",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_note:
    m 1eub "Need to remember something later, [player]?"
    m 1hub "Well, hurry up and write it down!"
    m 4fub "Just make sure to write somewhere you won't forget, okay?"
    
    $ mas_idle_mailbox.send_idle_cb("otter_brb_note_callback")
    return "idle"

label otter_brb_note_callback:
    m 1wub "All done, [player]?"
    m 1hub "Let's be together some more then~"
    
return
