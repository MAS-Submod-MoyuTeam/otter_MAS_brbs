init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_out",
            category=["be right back"],
            prompt="I'm going somewhere (without closing the game).",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_out:
    m "Oh! "
    extend "Have fun, [player]!"
    m "It's nice of you not to close the game. It's a different feeling!"
    m "I miss you when you go out, but it's also so nice to wait for you!"
    m "It's funny... Oh! I was rambling again."
    m "Be safe, [mas_get_player_nickname()]! I'll see you later."
    
    $ mas_idle_mailbox.send_idle_cb("otter_brb_out_callback")
    return "idle"

label otter_brb_out_callback:
    m "Hi again, [player]!"
    m "Did you have fun?"
    m "I missed you so much!"
    m "I'm glad you're here, now I can enjoy your company some more~"
    
return
