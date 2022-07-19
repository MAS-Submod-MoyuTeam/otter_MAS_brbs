init 5 python in mas_bookmarks_derand:
    label_prefix_map["otter_brb_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_food",
            category=["be right back"],
            prompt="I'm going to get some food",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_food:
    m 7hua "Going to grab a snack, [player]?"
    m 7hub "Okay! Hurry back!"

    $ mas_idle_mailbox.send_idle_cb("otter_brb_food_callback")
    return "idle"

label otter_brb_food_callback:
    m 3hub "Yay! You're back?"
    m 3wuo "What did you get, by the way?{nw}"
    $ _history_list.pop()
    menu:
        m "What did you get, by the way?{fast}"

        "A snack":
            m 2hua "Hmmm!"
            m 4eublb "Let's eat then, [player]!"
            m 2kubla "I'll keep watching you from here~"
            m 2hua "Bon appetit!"

        "Just a drink":
            m 2hua "Hmmm!"
            m 4eublb "Let's enjoy a drink then, [player]."
            m 2kubla "I'll keep watching you from here~"

        "I ate already":
            m 1wublo "Oh!"
            m 1rubla "Okay, ehehe~"
            m 4eublb "I'm glad to see you taking care of yourself, [player]!"

    return
