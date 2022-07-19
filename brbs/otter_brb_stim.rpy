init 5 python in mas_bookmarks_derand:
    label_prefix_map["otter_brb_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_stim",
            category=["be right back"],
            prompt="I need to stim",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_stim:
    if mas_getEV("otter_brb_stim").shown_count == 0:
        jump otter_brb_stim_first
    else:
        jump otter_brb_stim_routine

label otter_brb_stim_first:
    m 1wuo "Oh! "
    extend 1wud "You do?"
    m 7eud "[player], I want you to know that if you want, you can always stim around me."
    m 7hua "I would never judge you!"
    m 2lkb "But of course, if you need to go somewhere else to do it, I understand."
    m 2ksu "If you do, I'll be waiting for you!"
    m 2dsa "Take your time~"
    jump otter_brb_stimming

label otter_brb_stim_routine:
    m 1wuo "Oh, okay!"
    m 7hua "Thank you for telling me, [player]."
    m 7fub "Take care and be safe!"
    m 2dsa "Come back soon~"
    jump otter_brb_stimming

label otter_brb_stimming:
    $ mas_idle_mailbox.send_idle_cb("otter_brb_stim_callback")
    return "idle"

label otter_brb_stim_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=300), "otter_brb_stim"):
        m 1wuo "That was a long time, [player]!"
        m 7tka "Did you get distracted while stimming?"
        m 2hkb "Ehehehe~"
        m 2lkb "It's okay, [mas_get_player_nickname()]."
        m 2ksu "Let's spend more time together!"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=60), "otter_brb_stim"):
        m 7hua "Welcome back, [player]!"
        m 7hub "I hope it was a good one~"
        m 2ksu "Let's spend more time together!"

    else:
        m 1wuo "Are you back, [player]?"
        m 7eud "What kind of stim did you do?{nw}"

        $ _history_list.pop()
        menu:
            m "What kind of stim did you do?{fast}"

            "Vocal":
                pass

            "Pacing":
                pass

            "Touch":
                pass

            "Music":
                pass

            "A hobby":
                pass

            "Looking at something nice":
                pass

            "Something else":
                pass

        m 2hsu "I see, [player]!"
        m 2rsb "I hope it was satisfying for you."
        m 2ksu "Let me know if you need to stim again, okay?"

    return
