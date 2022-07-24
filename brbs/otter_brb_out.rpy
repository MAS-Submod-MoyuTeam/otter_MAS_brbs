init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_out",
            category=["be right back"],
            prompt="I'm going somewhere (without closing the game)",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_out:
    m 1wub "Oh! "
    extend 1hub "Have fun, [player]!"
    m 2lublb "It's nice of you not to close the game. It's a different feeling!"
    m 3lublb "I miss you when you go out, but it's also so nice to wait for you!"
    m 3lubld "It's funny... "
    extend 1wublo "Oh! I was rambling again."
    m 1hubla "Be safe, [mas_get_player_nickname()]! I'll see you later."
    
    $ mas_idle_mailbox.send_idle_cb("otter_brb_out_callback")
    return "idle"

label otter_brb_out_callback:
    m 1wublb "Hi again, [player]!"
    m 7wublb "Did you have fun?"
    m 5hubla "I missed you so much!"
    m 5hublb "I'm glad you're here, now I can enjoy your company some more~"
    
return
