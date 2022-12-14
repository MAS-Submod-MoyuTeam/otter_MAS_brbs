init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_download",
            category=["be right back"],
            prompt="I'm going to download something",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_download:
    m 1wub "Oh! Is that so?"
    m 1lub "I wonder what you'll download..."
    m 7wud "Be careful with what you download, [player]!"
    m 2kua "But I know you won't do any harm to your machine, ehehehe."
    m 2hubla "I'll be here waiting for you."
    
    $ mas_idle_mailbox.send_idle_cb("otter_brb_download_callback")
    return "idle"

label otter_brb_download_callback:
    m 2fua "Hi again, [player]!"
    m 2wub "Did the download go as planned?"
    m 2hubla "Let's spend more time together~"
    
return
