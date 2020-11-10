
label play_intro:
    stop music fadeout (1.0)
    play music "sounds/music/Background_music_Funk_Game_Loop.ogg"
    scene intro_01 with Pause(2)
    jor "This is where the story starts for our protagonist. He just finished another lazy day in college..."
    scene intro_02 with Pause(2)
    jor "No worries - no problems - Just thinking about which hot girl he would try to spend the evening with."
    scene intro_03 with Pause(2)
    p "{i}\“Hmm... maybe Jennifer?\” She always looks like an innocent angel.{/i}"
    scene intro_04 with Pause(2)
    #$ renpy.music.play('sounds/music/Menu_intro_music.ogg', channel="music2", loop=True, fadein = 2)
    jor "- But things can change in a heartbeat."
    stop music
    play sound 'sounds/effects/Car_accident_sound.ogg'
    $ renpy.pause(2.0, hard=True)
    scene intro_05 with hpunch
    $ renpy.pause(1)
    scene intro_06 with hpunch
    jor "- All due to a little lack of attention..."
    scene intro_07 with Pause(2)
    jor "...and everything becomes a different story."
    play sound "<from 1 to 7>sounds/flatline.mp3"
    scene black with dissolve
    $ renpy.pause(3)
    stop sound
    scene intro_08 with Pause(2)
    p "What the hell? What just happened? Why am I seeing myself lying there... and why are my hands transparent?"
    scene intro_09 with Pause(2)
    dr "Oh, my GOD!!! Is he dead?! I couldn't do anything - he just suddenly stepped out in front of my car. Oh, my GOD! HELP!!! ANYBODY!! Please!"
    scene intro_10 with Pause(2)
    play music "sounds/music/Background_music3_Disclo_ultralounge.ogg"
    scene intro_11 with Pause(2)
    a "Hello there."
    p "Who are you!? What happened!?"
    a "Always the same questions, over and over..."
    scene intro_12 with Pause(2)
    a "Here - take a seat! This will take some time - as always. Be calm - there is no more danger to you."
    scene intro_13 with Pause(2)
    a "So, what were you asking..? Ah, yes! Who am I and what happened, right?"
    a "It’s very easy: you didn't look around, before stepping onto the crosswalk - and that reduces your days left in this world... to zero."
    a "And I’m... Well now, I think it is obvious who I am."
    p "An angel? My... guardian angel?"
    a "Great! Your head is still working - after that crash. Nice to meet you."
    p "But that can't be... This must be some kind of a bad dream, or something. I’m still too young and haven't enjoyed my life enough. I have plans for the future - this cannot be the end for me!"
    a "It is not the end, silly... Just the start of another story, in another place."
    p "BUT - I want to stay here, in THIS place!"
    a "Look... I'm here for YOU. And that means you don’t have any other choices now. Your choice was not to look around, 5 minutes ago."
    a "You chose - to stare at your stupid phone, on the crosswalk. What a shame... Sorry - game over, finito, the end."
    p "Is there no other option?"
    stop music # TODO maybe some whooshing sound or something when the devil magically appears.
    play music "sounds/music/Sexy_music1_monks_topher.ogg"
    scene intro_14 with Pause(2)
    p "-hmmm..?"
    scene intro_15 with Pause(2)
    a "Pfeh.. Her, again."
    scene intro_16 with Pause(2)
    d "Hi! Hmm... what a nice boy. I think I can feel a good opportunity coming for you. Forget all that blonde trickster's mumbo-jumbo."
    scene intro_15 with Pause(2)
    a "Pfeh! I don’t want to listen to this..."
    scene intro_16 with Pause(2)
    d "So, what do you think? Do you want to hear my offer?"
    p "Why not...?"
    d "Great!"
    scene intro_17 with Pause(2)
    d "So, welcome to my humble abode. Are you sitting comfortably?"
    scene intro_18 with Pause(2)
    p "Yeah - I’m fine now."
    scene intro_17
    d "Cool! I really like these modern seats. They look fantastic... and sooo very comfy. Not like THIS garbage from medieval times."
    d "But we are here for another reason! So, I have a little deal for you... I was listening to everything she said to you."
    d "Haha! Don’t listen to her - there are always other options.  They are so behind-the-times and strict."
    scene intro_18
    p "Good to hear that there’s another way."
    scene intro_17
    d "So you want more time? How much? What about one month?"
    scene intro_18
    p "Only one month?"
    scene intro_17
    d "This will not be a mere month - as you are used to, babe. I will also give you some special skills, you can use."
    scene intro_18
    p "What skills?"
    scene intro_17
    d "What about invisibility? Just think about it: nobody can see you if you don’t want to..."
    d "How about the power to manipulate others. Doesn't that sound fun? Bending others to your own will?"
    scene intro_18
    p "Hmmm... That does sound interesting."
    p "And why are you doing this for me? What is it that you want in return?"
    scene intro_17
    d "Nothing special really - it is all explained in the contract you need to sign."
    scene intro_18
    p "Great! Can I see that contract?"
    scene intro_19 with Pause(2)
    d "Of course, you clever boy! Of course you can! Here it is! And read it carefully."
    scene intro_20 with Pause(2)
    p "Whaaat?! This is Huge?!"
    scene intro_21 with Pause(2)
    d "Don’t worry... we have time. Like - forever, I think. Haha!"
    scene intro_27
    d "Or you can look at this shorter version."
    scene intro_22 with Pause(2)
    p "That looks much better. Let's see what we have here. [player_name], hereby known as the damned... Whaat?!"
    scene intro_21 with Pause(2)
    d "It is a standard form, honey. It IS Hell - and we must follow some ancient rules. We are trying to be modern, but these things still stay the same. Don’t worry about that. Like I said: it's just a formality."
    scene intro_22 with Pause(2)
    p "Fine, Sign here? How am I supposed to sign this? With my blood?"
    scene intro_23 with Pause(2)
    d "Haha! No, I think with this pen will be good enough."
    scene intro_25 with Pause(2)
    p "Done."
    scene intro_24 with Pause(2)
    d "Great! So, do you have any more questions?"
label intro_questions_menu:
    scene intro_24
    menu:
        "How exactly does this invisibility work?"if have_asked_intro_invisibility_question == False:
            p "How exactly does this invisibility work?"
            d "It is not actually invisibility, but you will become a spirit and you can go with people, wherever you want and hear their thoughts and conversations."
            p "That sounds good."
            d "Yes it does."
            d "Any other questions?"
            $ have_asked_intro_invisibility_question = True
            jump intro_questions_menu
        "How can I control a person's will?"if have_asked_intro_control_will_question == False:
            d "You can’t. I cannot do it either. But you can - as a spirit - transfer into another person and use their skills as your own strengths."
            d "And of course, nobody will realise that it is you."
            p "Hmm... Sounds useful."
            d "You will enjoy this."
            d "Any other questions?"
            $ have_asked_intro_control_will_question = True
            jump intro_questions_menu
        "Why are there all these rules for everybody?"if have_asked_intro_why_rules_question == False:
            scene intro_22 with Pause(2)
            p "Yes - about this reincarnation thing. Why are there all these rules for everybody?"
            scene intro_24
            d "Yeah... That's easy. From the start, your skills will be - not that strong. This will affect your ability to control everybody."
            d "Each person is different, some are more resistant - others not so much."
            scene intro_26 with Pause(2)
            d "And because, in the past, we have had some problems with... really creative people with these powers."
            scene intro_28 with Pause(2)
            p "Haha! Now I get it. Funny to think about it from this point of view."
            $ have_asked_intro_why_rules_question = True
            jump intro_questions_menu
        "No, I don’t have anymore questions right now.":
            pass
    scene intro_27 with Pause(2)
    d "So, everything seems to be in order."
    d "Are you ready now?"
    scene intro_28
    p "Yes, I am."
    scene intro_29 with Pause(2)
    d "Good! So, hold your breath now. And let the magic happen!"
    stop music fadeout 2.0
    scene black_screen
    with fade
    $ renpy.pause(1.0, hard=True)
    jump mc_room
