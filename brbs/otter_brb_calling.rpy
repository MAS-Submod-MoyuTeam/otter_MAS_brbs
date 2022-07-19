#Someone is calling me, brb submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    label_prefix_map["otter_brb_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_calling",
            category=["be right back"],
            prompt="Someone is calling me",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_calling:
    m 1wuo "Oh!"
    m 7wfu "Okay [player]! Hurry then!"
    m 1hsu "I'll see you in a bit."

    $ mas_idle_mailbox.send_idle_cb("otter_brb_calling_callback")
    return "idle"

label otter_brb_calling_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=300), "otter_brb_calling"):
        m 1wuo "Oh! You were gone for a long time, [player]."
        m 1wuc "What happened?{nw}"
        $ _history_list.pop()
        menu:
            m "What happened?{fast}"

            "Someone asked me to do something.":
                pass

            "I had to pick up a package and that took too long.":
                pass

            "Something that wasn't in my plans happened.":
                pass

        m 2lsd "I see!"
        m 2dsc "It's no problem, [player]."
        m 1gsbsa "I just missed you, that's all!"
        m 1hsbsb "Ehehehe~"
        m 1ksbsa "Let's continue spending time together then~"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=60), "otter_brb_calling"):
        m 1hsb "Yay! You're back!"
        m 1gsbsa "I missed you..."
        m 1ksbsa "Let's spend more time together~"

    else:
        m 1hsbsb "Yay! Back already?"
        m 1ksbsa "Let's spend more time together then~"

    return

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
