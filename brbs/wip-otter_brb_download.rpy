init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_download",
            category=["be right back"],
            prompt="I'm going to download something.",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_download:
    m "Oh! Is that so?"
    m "I wonder what you'll download..."
    m "Be careful with what you download, [player]!"
    m "But I know you won't do any harm to your machine, ehehehe."
    m "I'll be here waiting for you."
    
    $ mas_idle_mailbox.send_idle_cb("otter_brb_download_callback")
    return "idle"

label otter_brb_download_callback:
    m "Hi again, [player]!"
    m "Did the download go as planned?"
    m "Let's spend more time together~"
    
return
