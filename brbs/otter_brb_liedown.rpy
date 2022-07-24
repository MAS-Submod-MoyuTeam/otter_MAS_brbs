init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_liedown",
            category=["be right back"],
            prompt="I'm going to lie down",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_liedown:
    m 1wuo "You're gonna rest for a bit, [player]?"
    m 7hub "That's great!"
    m 7eud "You know for how long you'll be gone?{nw}"

    $ _history_list.pop()
    menu:
        m "You know for how long you'll be gone?{fast}"

        "Only resting my eyes and body":
            jump otter_brb_quickliedown

        "Just a quick nap":
            jump otter_brb_quickliedown

        "I'm very tired...":
            m 2dkc "[player]..."
            m 4wud "Indeed, go rest!"
            m 2ekd "I'll close the game for you so you can rest even more."
            m 2eka "Don't worry, I'll be right here waiting for you to come back!"
            m 2hka "I love you, okay?"
            m 2hkb "Good rest, [mas_get_player_nickname()]~"

            return "quit"

label otter_brb_quickliedown:
    m 2dua "I see, [mas_get_player_nickname()]."
    m 4eub "Go rest, okay?"
    m 4wub "I'll be right here waiting for you."
    m 2hsb "I love you!"

    $ mas_idle_mailbox.send_idle_cb("otter_brb_liedown_callback")
    return "idle"

label otter_brb_liedown_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=300), "otter_brb_liedown"):
        m 2rkd "You were gone for a long time, [player]..."
        m 7rksdla "Did you accidentally fall asleep?"
        m 2hksdlb "Ahahaha~"
        m 2fka "It's no problem, [mas_get_player_nickname()]."
        m 7hsa "I'm just glad you had a good time resting!"
        m 2kua "Let's spend more time together now that you're back~"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=60), "otter_brb_liedown"):
        m 4wub "Welcome back, [player]!"
        m 4wua "I hope you feel rested now!"
        m 2kua "Let's spend more time together~"

    else:
        m 4wub "That was quick, [player]!"
        m 7lsa "But I know, sometimes just lying down for a few minutes can help."
        m 7hsa "And I hope it did!"
        m 2kua "Let's spend more time together, [mas_get_player_nickname()]~"

    return
