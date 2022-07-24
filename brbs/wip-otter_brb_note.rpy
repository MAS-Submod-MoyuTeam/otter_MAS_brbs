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
    m "Need to remember something later, [player]?"
    m "Well, hurry up and write it down!"
    m "Just make sure to write somewhere you won't forget, okay?"
    
    $ mas_idle_mailbox.send_idle_cb("otter_brb_note_callback")
    return "idle"

label otter_brb_note_callback:
    m "All done, [player]?"
    m "Let's be together some more then~"
    
return
