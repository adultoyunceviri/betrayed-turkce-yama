label scene_as_scarlett_ivanas_apartment_first_time:
    scene scarlett_s03_ivana_apartment01
    iva "OMG! Scarlett!? Where have you been?"
    p "Hi, Ivana... Eeee... Trip around Europe..."
    play sound 'sounds/effects/punch_sound.ogg'
    scene scarlett_s03_ivana_apartment03 with hpunch
    $ renpy.pause(2.0)
    stop sound
    p "Ouch!"
    scene scarlett_s03_ivana_apartment04
    iva "There you go! That's for spying on me..."
    p "Ouuhmm... But… But that was not me?!! What spying are you talking about?"
    scene scarlett_s03_ivana_apartment02
    iva "Really?! I know everything, from Anders!!!"
    scene scarlett_s03_ivana_apartment04
    p "Aaah... that spying. Now I know... (Fuck!!)"
    play sound 'sounds/effects/punch_sound.ogg'
    scene scarlett_s03_ivana_apartment03 with vpunch
    $ renpy.pause(2.0)
    stop sound
    scene scarlett_s03_ivana_apartment04
    p "And what was that for?!"
    scene scarlett_s03_ivana_apartment05
    iva "Because you didn’t tell me where you were going, and made me worry about you. Now, you have one hour - take your stuff and find another apartment! Most of your things were taken to the police station."
    scene city_map
    p "Damn, she was really pissed off. My face looks like a tomato. I just grabbed some trousers, to not have to walk around the city in panties. Now I must find another apartment. Who else is friends with Scarlett?"
    $ scarlett_kicked_out_of_ivanas_apartment = True
    $ hints_counter += 1
    jump city_map

label scene_as_scarlett_sophia_apartment_first_time:
    scene scarlett_s04_sophia_apartment01
    p "I hope it will go better than with Ivana."
    scene scarlett_s04_sophia_apartment02
    p "Hi, sophia."
    sop "Oh?"
    scene scarlett_s04_sophia_apartment03
    sop "OMG!! Scarlett!! You're back! Where have you been?!"
    scene scarlett_s04_sophia_apartment04
    p "That's a long story. I'll tell you more later. For now, can I come in?"
    sop "Of course! Come in!"
    scene black_screen
    "After 20 minutes full of bullshit about travels over in Europe..."
    scene scarlett_s04_sophia_apartment05
    p "And that’s all. I’m back now."
    sop "Wow, that's really great. I can see now why you left in a hurry."
    scene scarlett_s04_sophia_apartment07
    p "Yes... I have one thing to ask you though."
    scene scarlett_s04_sophia_apartment05
    sop "Sure, what do you need?"
    p "I’m looking for a place to stay and I hear that you are looking for a flatmate."
    scene scarlett_s04_sophia_apartment06
    sop "Yes, I have an empty room here now. [p] had a car accident, and now I’m looking for someone to share the apartment with. Because rent here is not cheap."
    scene scarlett_s04_sophia_apartment05
    p "Aaah... Okay. But, you know, I’m a little short on money now. Big expenditure, with the travelling and all, you see."
    sop "It’s okay. You can give me that money a little later. But please, don’t wait too long. My wallet is almost empty too, because I’ve been living here for three weeks alone already, and paying full rent myself."
    p "Shit, it’s been 3 weeks already?"
    sop "Yes, eeh..?"
    p "Fine. I will collect money as soon as possible. How much?"
    sop "Rent is $200 a week."
    p "(Uuufff!) Okay. So where's my new room?"
    scene scarlett_s04_sophia_apartment08
    sop "Here it is! There are still [p]'s posters on the walls, but you can change them."
    p "(Back to my old room...) I think I like them. Now I'll move my stuff here."
    sop "Great! It will be fun to have you here."
    scene city_map
    p "Great, looks like I have my apartment back. But all of Scarlett’s stuff is at the police station. Hope she has money in her stuff.I also  hope they will believe the story about traveling to Europe."
    $ have_gotten_old_apartment_room_back = True
    $ need_to_get_scarlets_stuff_from_police_station = True
    $ hints_counter += 1
    $ inventory.add(apartment_keys)
    $ time_of_day = Set_Time_of_Day('ÖĞLEN')

    jump city_map

label scene_as_scarlett_police_station_first_time:
    scene scarlett_s05_police_station01
    p "(The Police captain wanted me in his office for a chat. I’m really scared of what will happen. What if in that basement, they find Scarlett’s finger prints or anything else of hers.)"
    cap "So please tell me the whole story. Why did you leave so suddenly without telling anybody."
    p "Sure..."
    "After 20 minutes of the same bullshit I told Sophia..."
    cap "That’s really interesting... And now I'd like to hear the truth..."
    scene scarlett_s05_police_station09
    p "(I fucked up...)"
    p "What truth?"
    scene scarlett_s05_police_station02
    cap "Look, we have the same friend. You see this tattoo? I’m her eyes and ears in the city."
    p "What?"
    cap "I just want to know why you opened all the doors in that basement?"
    p "I.. I… just."
    scene scarlett_s05_police_station06
    d "You just...?"
    scene scarlett_s05_police_station09
    p "OH MY GOD! One day I will really die, from all your games."
    scene scarlett_s05_police_station07
    d "You're not glad to see me?"
    scene scarlett_s05_police_station04
    p "Of course I am. There is no other person I would want to see more, in this moment."
    d "That's nice. Hihi."
    scene scarlett_s05_police_station03
    p "Who was he talking about?"
    scene scarlett_s05_police_station08
    d "Him? About me, of course."
    p "He knows about you? How?"
    d "Same way as you. Did you think, you were the only one?"
    p "Eeehm… Yes?"
    d "Don’t be silly. I work as hard as any other person."
    p "Ah."
    scene scarlett_s05_police_station05
    d "But don’t worry, you are my favorite one. I have a special weakness for you."
    p "Um, that's nice. So, will I have any more problems with the police now?"
    d "Of course not. You don’t need to worry about a thing. Just go back to your apartment. The cops already moved your stuff back."
    d "And he will send a letter to the school about Scarlett’s case and how all is solved. Just visit the Dean later."
    d "I just wanted to see you sweat a little, in that chair, hihi. Sorry about that."
    p "Uh… you are nice and terrible at the same time. But, thank you."
    d "Sure thing. See ya."
    scene black_screen with fade
    $ need_to_get_scarlets_stuff_from_police_station = False
    $ mc_room_window_opened = False
    $ time_of_day = Set_Time_of_Day('AKŞAM')
    $ hints_counter += 1
    scene mc_room_day
    show mc_room_box:
        xpos 750 ypos 650 # TEMP
    p "Finally, I’m back in my apartment. The cops delivered Scarlett's stuff. I'll put on better clothes and then go to sleep. Today was a really long day..."
    jump mc_room

label interaction_scarletts_box_open:
    if not have_changed_clothes_as_scarlett:
        scene mc_room_day
        if not have_opened_scarletts_box:
            show mc_room_box:
                xpos 730 ypos 650 # TEMP
        p "I really want to change out of these clothes before doing anything else."
        jump mc_room
    else:
        scene scarlett_s06_mcroom_box01
        p "What have we here?"
        scene scarlett_s06_mcroom_box02
        p "Oh, my God!! The box is full of sextoys!!!"
        scene scarlett_s06_mcroom_box03
        p "I will put them all here into this bedside cabinet. Maybe I will check them out later."
        $ have_opened_scarletts_box = True
        #$ hints_counter += 1
        $ time_of_day = Set_Time_of_Day('GECE')
        jump interaction_mc_room_bedside_table_scarlett


label scene_wardrobe_scarlett_changing_clothes:
    scene scarlett_s06_mcroom_clothes01
    p "Hmm, what should I pick? There are mostly only dresses, which I don’t want to wear. Hmm, this one looks interesting."
    scene scarlett_s06_mcroom_clothes02
    p "Yes, that looks good."
    scene mc_room_shoes
    p "Which shoes should I wear?"
    $ hints_counter += 1
    jump scarlets_shoes

label scene_wardrobe_scarlett_chosen_shoes:
    scene scarlett_s06_mcroom_clothes03
    p "Yes, they are quite comfortable. Great!"
    p "Now I have comfortable clothes for outdoors and shoes I can walk around in normally, for a change."
    $ have_changed_clothes_as_scarlett = True
    $ hints_counter += 1
    jump mc_room


label scene_as_scarlett_dildo_choices:
    if current_dildo_choice == 1:
        call scene_as_scarlett_dildo_choice_1 from _call_scene_as_scarlett_dildo_choice_1
    elif current_dildo_choice == 2:
        call scene_as_scarlett_dildo_choice_2 from _call_scene_as_scarlett_dildo_choice_2
    elif current_dildo_choice == 3:
        call scene_as_scarlett_dildo_choice_3 from _call_scene_as_scarlett_dildo_choice_3
    elif current_dildo_choice == 4:
        call scene_as_scarlett_dildo_choice_4 from _call_scene_as_scarlett_dildo_choice_4
    elif current_dildo_choice == 5:
        call scene_as_scarlett_dildo_choice_5 from _call_scene_as_scarlett_dildo_choice_5
    elif current_dildo_choice == 6:
        call scene_as_scarlett_dildo_choice_6 from _call_scene_as_scarlett_dildo_choice_6
    scene scarlett_s20_toys01
    p "The toy is back in the drawer. Now it's time for bed."
    $ have_used_sex_toy_that_night_as_scarlett = True
    scene black_screen with fade
    label skip_to_sleep:
    if have_used_sex_toy_that_night_as_scarlett:
        $ have_used_sex_toy_that_night_as_scarlett = False
    else:
        scene mc_room_toys

    if sophia_in_her_room_for_webshow:
        $ sophia_in_her_room_for_webshow = False
        $ had_web_show_with_sophia_that_night = False

    if have_paid_first_rent_to_sophia_as_scarlett and not have_been_woken_up_morning_after_paid_first_rent:
        scene scarlett_s16_sophia_wakeup01
        sop "Hey Scar, wake up! You'll be late for school."
        p "Oh..."
        scene scarlett_s16_sophia_wakeup02
        p "It's already that time?"
        sop "Hah! Yes, you were snoring like an old truck driver."
        p "Haha!"
        if turned_down_strip_club_owner:
            sop "About yesterday's show: Girl, it was a huge success! Your rent is more than paid, by this one show."
            sop "And I must say, it was a lot of fun doing that with you after a long time. I missed you so much."
            p "Yes, it was fun. But you did say we should be getting to school."
        else:
            sop "And thanks again for paying the rent yesterday, so fast. It saves me stressing over it."
            p "No problem. But time to go to school."
        $ time_of_day = Set_Time_of_Day('SABAH')
        scene city_map
        p "On the way to school, I should check the hospital again, just to be sure."
        $ have_been_woken_up_morning_after_paid_first_rent = True
        $ double_check_the_hospital_after_paying_first_rent = True
        $ hints_counter += 1
        jump city_map
    else:

        scene scarlett_sleeping with dissolve
        $ renpy.pause()
        $ time_of_day = Set_Time_of_Day('SABAH')
        if not settled_as_scarlett:
            $ hints_counter += 1
            $ settled_as_scarlett = True
        elif need_to_sleep_after_finding_pill_on_clothes:
            $ need_to_sleep_after_finding_pill_on_clothes = False
            $ have_to_return_found_pill_to_meg = True
            jump scene_sophia_wakes_up_scarlett_for_the_plan
        elif waking_up_in_the_morning_after_threesome:
            scene scarlett_s16_sophia_wakeup01 with fade
            p "Aaaah... (I feel like a new man... Eh, woman? I woke up at a good time. I need to be at school before Megan. I will grab the shrinking pills and head there now.)"
            $ waking_up_in_the_morning_after_threesome = False
            $ mc_scarlett_leaving_apartment_morning_after_threesome = True
            $ hints_counter += 1
            $ inventory.add(shrinking_pills)
        elif time_to_sleep_after_choices_afternoon:
            $ time_to_sleep_after_choices_afternoon = False
            scene scarlett_s16_sophia_wakeup01 with fade
            p "Aaaaahh... (Wake up, lazy-bones. Today is the day to punish Brooke. I'll need the horny pills this time. Let’s head to the gym.)"
            $ inventory.add(horny_pills)
            $ inventory.drop(shrinking_pills)
            $ hints_counter += 1
            $ time_to_punish_beth_n_brooke_in_sports_hall = True

        jump mc_room


label scene_as_scarlett_dildo_choice_1:
    play music "sounds/music/Sexy_music1_monks_topher.ogg" fadein 3.0
    scene scarlett_s20_toys_n1_02
    p "This toy looks really unusual. Why does it have these bunny ears..? Hah!"
    p "Probably these serve some functions down there."
    scene scarlett_s20_toys_n1_01
    p "Let’s see what you can do."
    scene scarlett_s20_toys_n1_07
    $ renpy.movie_cutscene("scenes/Scarlett/20_toys_play/toy_1/scarlett_s20_toy_n1_1.webm", loops=3, delay=-1, stop_music=False)
    scene scarlett_s20_toys_n1_07
    p "Whooow! The bunny is on the move, hah! Let’s try it out."
    scene scarlett_s20_toys_n1_03
    p "Feels promising, so far. Vibrations are really strong, for the toy’s size."
    scene scarlett_s20_toys_n1_04
    p "I’m going to like this more and more. Deeper I go. Pleasure rising up. Girls can have so much fun with all these toys. Now I know why Scarlett has a full drawer of them."
    scene scarlett_s20_toys_n1_05
    p "I’m getting really excited! So, Bunny, show me what you can do."
    $ renpy.movie_cutscene("scenes/Scarlett/20_toys_play/toy_1/scarlett_s20_toy_n1_2.webm", loops=3, delay=-1, stop_music=False)
    scene scarlett_s20_toys_n1_05
    p "Damn… DAMN! My body started shaking."
    scene scarlett_s20_toys_n1_06
    $ renpy.movie_cutscene("scenes/Scarlett/20_toys_play/toy_1/scarlett_s20_toy_n1_3.webm", loops=0, delay=-1, stop_music=False)
    scene scarlett_s20_toys_n1_06
    p "Oohmmm!!! Oohhm!!  Shit… ... That was a really STRONG one."
    scene scarlett_s20_toys_n1_07
    p "This toy looks odd, but... wow does it have good functions."

    return
label scene_as_scarlett_dildo_choice_2:
    play music "sounds/music/Sexy_music1_monks_topher.ogg" fadein 3.0
    scene scarlett_s20_toys_n2_01
    p "Hmmm."
    p "Looks like Scarlett has all kind of toys. Let’s test this now. This plug is definitelly not the smallest one."
    scene scarlett_s20_toys_n2_04
    p "Slowly inside…."
    scene scarlett_s20_toys_n2_03
    p "Oh yes… It’s getting more intense with every inch."
    scene scarlett_s20_toys_n2_06
    p "And my nipples are rock hard already."
    scene scarlett_s20_toys_n2_07
    p "This last part will be tough…."
    scene scarlett_s20_toys_n2_09
    scene scarlett_s20_toys_n2_05
    p "Damn, I don't think I can do it."
    scene scarlett_s20_toys_n2_08
    p "Definitelly not - but it was good fun. This plug feels pretty nice, lubed by my wet pussy."
    scene scarlett_s20_toys_n2_10
    p "But... maybe I can try more than my pussy. It IS a buttplug afterall, right?"
    menu:
        "Should I continue?"
        "NO":
            p "I think that's enough for today."
            #End of scene.
        "YES":

            scene scarlett_s20_toys_n2_13
            $ renpy.pause(2.0)
            scene scarlett_s20_toys_n2_11
            $ renpy.pause(2.0)
            scene scarlett_s20_toys_n2_12
            p "Damn….. I’m surprised just by even considering trying this."
            scene scarlett_s20_toys_n2_14
            p "But it's not that bad at all. Not as much pain as I thought it would be, just a weird feeling."
            scene scarlett_s20_toys_n2_12
            p "Maybe I can try to sit on it. Just a little."
            scene scarlett_s20_toys_n2_18
            $ renpy.pause(2.0)
            scene scarlett_s20_toys_n2_16
            p "Slowly… slowly inside"
            scene scarlett_s20_toys_n2_15
            p "I feel excitement going through my whole body. And Scarlett’s pussy lubed this toy pretty well."
            scene scarlett_s20_toys_n2_16
            p "Slowly... Just a little more…"
            scene scarlett_s20_toys_n2_17
            p "Ohmmmm…."
            scene scarlett_s20_toys_n2_18
            p "Yeah… just a little more movement….."
            #(With dissolve)
            scene scarlett_s20_toys_n2_19 with dissolve
            $ renpy.pause(1.0)

            scene scarlett_s20_toys_n2_20 with dissolve
            $ renpy.pause(1.0)

            scene scarlett_s20_toys_n2_21 with dissolve
            $ renpy.pause(1.0)

            scene scarlett_s20_toys_n2_22 with dissolve
            p "FUCK!!!!"
            #(with dissolve)
            scene scarlett_s20_toys_n2_23 with dissolve
            #$ renpy.pause()

            scene scarlett_s20_toys_n2_24 with dissolve
            #$ renpy.pause()

            scene scarlett_s20_toys_n2_25 with dissolve
            #$ renpy.pause()

            scene scarlett_s20_toys_n2_26 with dissolve
            #$ renpy.pause()

            scene scarlett_s20_toys_n2_27 with dissolve
            p "HOLY FUCK!!!! Aaaaaahh!!"
            scene scarlett_s20_toys_n2_28
            p "It’s fucking huge….. That was a fucking stupid idea!"
            p "I don't think I can push it out!!"
            scene scarlett_s20_toys_n2_34
            p "Hmmmm pffff…."
            scene scarlett_s20_toys_n2_33
            p "It’s too big, and won't come out…."
            scene scarlett_s20_toys_n2_34
            p "Yes…….. I can do it….."
            #(dissolve)
            scene scarlett_s20_toys_n2_29 with dissolve
            $ renpy.pause(0.1)

            scene scarlett_s20_toys_n2_30 with dissolve
            $ renpy.pause(0.1)

            scene scarlett_s20_toys_n2_31 with dissolve
            $ renpy.pause(0.1)

            scene scarlett_s20_toys_n2_32 with dissolve
            $ renpy.pause(0.1)

            scene scarlett_s20_toys_n2_33 with dissolve
            p "It’s done... I peed myself, during all that pushing. Fuck, that was terrible. My ass is on fire. Better go to bed and try to forget about this."

    return
label scene_as_scarlett_dildo_choice_3:
    play music "sounds/music/Background_music2_Brunno.ogg" fadein 3.0
    scene scarlett_s20_toys_n3_03
    p "This one should be fine, I think. Looks a little unusual maybe, but in this case, everything's unusual though."
    scene scarlett_s20_toys_n3_04
    p "I cannot wait to experience these new feelings..."
    scene black_screen
    $ renpy.movie_cutscene("scenes/Scarlett/20_toys_play/toy_3/scarlett_s20_toy_n3_3.webm", loops=0, delay=-1, stop_music=False)
    scene scarlett_s20_toys_n3_05
    $ renpy.movie_cutscene("scenes/Scarlett/20_toys_play/toy_3/scarlett_s20_toy_n3_2.webm", loops=0, delay=-1, stop_music=False)
    p "That’s incredible... I need more..."
    scene scarlett_s20_toys_n3_06
    $ renpy.movie_cutscene("scenes/Scarlett/20_toys_play/toy_3/scarlett_s20_toy_n3_4.webm", loops=0, delay=-1, stop_music=False)
    p "Ouuhmmm... Does it feel the same, with girls riding it???"
    scene black_screen
    $ renpy.movie_cutscene("scenes/Scarlett/20_toys_play/toy_3/scarlett_s20_toy_n3_1.webm", loops=0, delay=-1, stop_music=False)
    scene scarlett_s20_toys_n3_01
    $ renpy.movie_cutscene("scenes/Scarlett/20_toys_play/toy_3/scarlett_s20_toy_n3_5.webm", loops=0, delay=-1, stop_music=False)
    p "I’m Cumming!!! Ooooh!!!"
    scene scarlett_s20_toys_n3_01
    p "Aaaaaaaahhhh!!!"
    scene scarlett_s20_toys08_2
    p "Damn... That was much better than I expected! Wow..."
    if not have_used_dildo_3_as_scarlett_before:
        $ have_used_dildo_3_as_scarlett_before = True
    return
label scene_as_scarlett_dildo_choice_4:
    scene scarlett_s20_toys_n4_01
    p "This one looks a little boring. But maybe looks are deceiving."
    scene scarlett_s20_toys_n4_02
    p "Oho... The vibrations feel nice on the nipples."
    scene scarlett_s20_toys_n4_03
    p "And down here as well……  This will be really fun."
    scene scarlett_s20_toys_n4_05
    p "Oooh... I’m getting so fucking horny."
    scene scarlett_s20_toys_n4_04
    p "Let’s test it inside."
    scene scarlett_s20_toys_n4_06
    p "Slowly inside… these vibrations are really awesome."
    scene scarlett_s20_toys_n4_08
    p "Hmmmmm….."
    scene scarlett_s20_toys_n4_07
    p "And the size of this toy is pretty awesome too. I feel how it fills the whole pussy."
    scene scarlett_s20_toys_n4_11
    p "Oohmm... I cannot stop... This BODY needs more…. More!!!"
    scene scarlett_s20_toys_n4_12
    p "Mmmmm…"
    scene scarlett_s20_toys_n4_10
    p "Yes! As deep as this pussy can handle…. YES!!!!"
    #(dissolve)
    scene scarlett_s20_toys_n4_09 with dissolve
    p "Aaaaaaa!!!!  I’m cumming hard….. DAMN! What a feeling….. Aaaaahm…."
    p "That was fucking amazing!!!"
    scene scarlett_s20_toys_n4_14
    p "So Scarlett tastes like this... Not bad at all..."

    return
label scene_as_scarlett_dildo_choice_5:
    play music "sounds/music/sexy_music4_Tripst_topher.ogg" fadein 3.0
    scene scarlett_s20_toys_n5_02
    p "Well, this is probably the largest toy I've EVER seen. It’s so big and heavy."
    scene scarlett_s20_toys_n5_01
    p "Phfeh, I think... it can't even fit in my mouth."
    scene scarlett_s20_toys_n5_03
    p "*Mumphf* Nope, it can’t. Just the tip."
    scene scarlett_s20_toys_n5_05
    p "But I’m really curious, what girls feel when something like this goes inside."
    scene scarlett_s20_toys_n5_04
    p "It’s not going inside. And it's starting to hurt a little. Scarlett’s pussy is so small. How the hell can she fit this inside?! Maybe in another possition...?"
    scene scarlett_s20_toys_n5_07
    p "Hmmm... It's so stiff and heavy. I’m barely even able to hold it."
    scene scarlett_s20_toys_n5_06
    p "Stupid toy! It’s too big and stiff and heavy. My hand already hurts more than that hole down there..."
    scene scarlett_s20_toys_n5_08
    d "Maybe I can help you?"
    p "Oooh! You scared me... DAMN! Pretty nice clothes."
    scene scarlett_s20_toys_n5_09
    d "Thank you! So do you want my help?"
    menu:

        "NO":
            p "No, sorry. I don’t want to hurt this body."
            d "As you wish."

        "YES":

            p "Oookay... but please be gentle."
            d "Don’t worry, you're gonna love it."
            scene scarlett_s20_toys_n5_11
            p "MmmmMmmmmm... mmm..."
            d "Oh yes! You're taking that big toy really well. Damn, I’m getting horny just by looking at you."
            p "Keep going! I’m on the edge!"
            scene scarlett_s20_toys_n5_10
            d "Don’t need to ask me twice!"
            scene scarlett_s20_toys_n5_13
            $ renpy.movie_cutscene("scenes/Scarlett/20_toys_play/toy_5/scarlett_toy_n5_1.webm", loops=0, delay=-1, stop_music=False)
            scene scarlett_s20_toys_n5_13
            d "Yes! Yes!!! Take it, you slut!"
            scene scarlett_s20_toys_n5_14
            $ renpy.movie_cutscene("scenes/Scarlett/20_toys_play/toy_5/scarlett_toy_n5_1.webm", loops=0, delay=-1, stop_music=False)
            $ renpy.movie_cutscene("scenes/Scarlett/20_toys_play/toy_5/scarlett_toy_n5_2.webm", loops=0, delay=-1, stop_music=False)
            scene scarlett_s20_toys_n5_14
            d "Aaaaaah!!!"
            scene scarlett_s20_toys_n5_15
            p "Aaaaaaaah!!!!"
            scene scarlett_s20_toys_n5_12
            p "That was the strongest feeling I've ever had in my entire life…..."
    return
label scene_as_scarlett_dildo_choice_6:
    scene scarlett_s20_toys_n6_01
    p "This one looks more like a massage tool, than a sex toy."
    scene scarlett_s20_toys_n6_02
    p "Name on it says magic wand. Maybe it does some “magic”."

    if had_dinner_with_angel_after_no_drug_sell_and_helped_trapped_girl:

        scene scarlett_s20_toys_n6_04
        a "With my help, there will definitelly be some magic."
        scene scarlett_s20_toys_n6_03
        p "Oh.. What are you doing here?"
        scene scarlett_s20_toys_n6_07
        a "What do you think? It's been a while since our last meeting in the restaurant. And now you are a pretty redhead girl. So maybe we can step it up to the next level?"
        scene scarlett_s20_toys_n6_06
        p "Ah?!  Next level…. You mean… you want to have sex with me?"
        scene scarlett_s20_toys_n6_08
        a "Why not? You think that angels cannot have their own “fun moments”?"
        scene scarlett_s20_toys_n6_05
        p "Of course not. But I wasn’t expecting this from you…"
        scene scarlett_s20_toys_n6_08
        a "Expecting... that I’m into girls?"
        scene scarlett_s20_toys_n6_05
        p "Yeaaaah….. Something like that?"
        scene scarlett_s20_toys_n6_08
        a "Look, I’ve been living here for centuries. And I've learned in that time, you have to try everything - to not get bored to death..."
        a "But if you're not comfortable, I can leave."
        menu:
            "Should I tell Angel to leave?"
            "NO":

                p "Nononoooo. It’s fine.  I’d be honoured to spend more time with you."
                scene scarlett_s20_toys_n6_08
                a "Good. You are so cute….. So, let’s start with some magic."
                scene scarlett_s20_toys_n6_09
                p "Oh….. that’s too much!!!"
                scene scarlett_s20_toys_n6_11
                p "The vibrations are too strong. That feels more like a jackhammer, than a toy. My teeth are chattering in my mouth. Switch it to a slightly lower level, please ."
                a "It’s on the lowest level, honey…"
                p "Lowest? ...the fuck? Really?!"
                a "Try to relax, and just accept and enjoy this feeling. You'll see: this will be awesome."
                p "Okay. I'll try…."
                scene scarlett_s20_toys_n6_09
                p "Ooooooo Oooo……"
                a "That’s it…."
                scene scarlett_s20_toys_n6_10
                p "DAMN!!!! This is…… Aaah!!!"
                a "And this is just the beginning…… Undress yourself and show me that hungry pussy."
                scene scarlett_s20_toys_n6_13
                a "That’s it! You nasty girl…"
                scene scarlett_s20_toys_n6_12
                a "Yeeees..! You are doing great!"
                scene scarlett_s20_toys_n6_14
                p "Aaaahhh.. Mhmmmmm… That's… incredible."
                scene scarlett_s20_toys_n6_15
                a "Damn, girl. Your pussy drives me crazy tooo…  I cannot resist. Wait a second..."
                scene scarlett_s20_toys_n6_16
                $ renpy.pause()
                scene scarlett_s20_toys_n6_18
                a "Yes! This feeling, I needed!!!"
                scene scarlett_s20_toys_n6_17
                p "Please… more. You are pushing it towards me. That feels so nice."
                scene scarlett_s20_toys_n6_18
                a "Turn around…."
                scene scarlett_s20_toys_n6_20
                a "Let’s see how much this toy can do, with the vibrations on maximum…"
                scene scarlett_s20_toys_n6_19
                a "Are you enjoying this?"
                scene scarlett_s20_toys_n6_22
                p "I am - but I feel like I’m on the edge already!!!"
                scene scarlett_s20_toys_n6_21
                a "HOLD on! We will cum together! Hold on, and push it towards meee... as hard as you can!!!"
                scene scarlett_s20_toys_n6_23
                p "I’m trying!! GOD!!!! Aaahm……"
                a "Push more!!! Pffhmmm..."
                scene scarlett_s20_toys_n6_26
                a "I’m on the edge too!"
                p "Me too! But it’s feeling so fucking great to hold on to this a moment longer..."
                a "MORE…."
                scene scarlett_s20_toys_n6_25
                p "Aaaahhh... I can't!!!!"
                scene scarlett_s20_toys_n6_24
                a "I’m... cumming!!!!!!"
                #(Dissolve)
                scene scarlett_s20_toys_n6_39 with fade

                scene scarlett_s20_toys_n6_40 with dissolve
                $ renpy.pause(0.7)

                scene scarlett_s20_toys_n6_41 with dissolve
                $ renpy.pause()

                scene scarlett_s20_toys_n6_29 with fade
                a "Mmmmm…"
                scene scarlett_s20_toys_n6_27
                a "How do you feel?"
                scene scarlett_s20_toys_n6_42
                $ renpy.pause()
                p "Great…. That was the best orgasm I have ever had EVER - boy or girl. (Her pussy is still dripping like crazy.)"
                a "I must say: for me, this moment was the best of this century, honey. We absolutely have to do this again soon."
                p "Yes..."
                scene black with fade
                return
            "YES":
                p "I think I'd like to be alone actually."
                a "As you wish..."

    #Cotinues same as version without angel.
    #If not met with Angel in restaurant for a wine before:
    scene scarlett_s20_toys_n6_02
    p "I’m really curious, what this toy can do."
    scene scarlett_s20_toys_n6_30
    p "Wow! These vibrations are really strong - even on the lowest level."
    scene scarlett_s20_toys_n6_31
    p "DAMN! I love it! Let’s try it naked!!!"
    scene scarlett_s20_toys_n6_32
    p "Yes!!! That’s great!"
    scene scarlett_s20_toys_n6_33
    p "Oohmm… Need more of these vibrations."
    scene scarlett_s20_toys_n6_34
    p "Yes! Almost at maximum level... Aaah!"
    scene scarlett_s20_toys_n6_35
    p "Aaaaaah... AAAAAh… Maximum…! YES!!"
    scene scarlett_s20_toys_n6_36
    p "DAMN!! I LOVE this wand!!!"
    scene scarlett_s20_toys_n6_38
    p "I’m CUMMING!!!"
    #(dissolve)
    scene scarlett_s20_toys_n6_35
    $ renpy.pause(1.0)

    scene scarlett_s20_toys_n6_37 with dissolve
    p "AAAAAAAAH!!!"
    p "Awesome feeling…."

    return


label scenes_kitchen_as_scarlett_talk_to_sophia_after_settled_in:
    scene scarlett_s08_sophia_morning01
    sop "Hi, Scarlett, how was your night?"
    p "Oh, I feel really great."
    sop "Are you going to school today? Or do you still have holidays or something?"
    p "Yeah, that's right, I need to talk with the Dean. And after school I will look for some work, to make some money."
    scene scarlett_s08_sophia_morning02
    sop "Cool. You know, I was thinking about that a little. And I have an offer for you."
    p "Offer?"
    sop "It's about my webcam shows. After you left, my earnings took a big dive. What about us doing some shows together again?"
    p "(They were doing webshows? God, I didn't see that in the flashback.)"
    p "I will think about it. Okay?"
    sop "Great! So, let’s go to school together."
    scene black_screen with fade
    $ have_talked_to_sophia_in_kitchen_as_scarlett = True
    $ hints_counter += 1
    jump school

label scene_as_scarlet_go_to_deans_office:
    scene scarlett_s07_dean01
    p "I hear loud voices from the inside. Would be better to wait."
    scene scarlett_s07_dean02
    p "(Somebody is in trouble.)"
    dean "Better hope that will work!! After that fail with the bikini competition, Brooke told me those pills you gave me weren’t working! Instead, that Sophia came to the competition, looking like a bikini goddess, and won! It's all your fault!"
    dean "Now leave my sight and do your job properly!"
    scene scarlett_s07_dean03
    meg "*crying*"
    p "(That’s Megan… Damn, that was me who got her into that situation. I need to help her somehow.)"
    p "(Now it's my turn. I don’t know if I even want to go inside. But, I don’t want to destroy Scarlett's life more than it is.)"
    scene scarlett_s07_dean04
    dean "Who do we have here? Our missing girl."
    p "Hello, Miss Smith."
    dean "You've caused quite a few problems for us, by leaving unannounced. Police officers were looking for you across the state. Next time, just tell somebody. I have here a letter from the police captain. Everything has been explained."
    p "Okay..."
    scene scarlett_s07_dean05
    dean "And we have here, your student records. You've missed many lessons. I may let you continue the year. But there's been a complaint from Mr. Anders. He doesn’t want to let you rejoin his class. If you can convince him to change his mind, you may graduate yet."
    p "(Ohhh, shit…) Fine. Thanks for your kindness, Miss Smith."
    scene school_map
    p "Damn, I need to convince Anders somehow. Looks like he's really angry at Scarlett right now. I need to think how to do that."
    p "But I don't want to be going to school now, because my time is short and I want to have more fun than sitting in some boring classes."
    p "Now I need to talk with Megan, She will probably be at lunch in the school dinning hall."
    p "But damn, I need to pee now. This girl must have a tiny bladder, I just went before I left the apartment."
    $ have_talked_to_dean_as_scarlett_to_reenroll = True
    $ need_to_pee_as_scarlett = True
    $ hints_counter += 1
    jump school


label scene_go_into_wrong_toilets_as_scarlett:
    scene scarlett_s09_toilets03
    p "Ehmmm... What the hell was the plan here?"
    scene scarlett_s09_toilets04
    nick "Hey, girl, are you lost in here? I could help you..."
    scene scarlett_s09_toilets05
    p "Hahaha! You are so funny. Hahaha! FUCK off, prick!"
    p "(What an idiot. I don’t know what Megan sees in him?)"
    scene scarlett_s09_toilets01
    p "(I need to remember not to go in the male’s toilets. It's just the force of habit.)"
    "Brrrrrppppppttttt...."
    scene scarlett_s09_toilets02
    p "(Is that the sound of girls farting? Haha!)"
    scene black_screen with fade
    scene school_dining_hall
    show school_dining_hall_secret:
        xpos 535 ypos 460
    p "(There's Megan there.)"
    $ need_to_pee_as_scarlett = False
    $ hints_counter += 1
    jump dining_hall

label scene_go_into_good_toilets_as_scarlett:
    scene scarlett_s09_toilets01
    p "(I still have a strong desire to go into the male's toilets. It's probably just the force of habit.)"
    "Brrrrrppppppttttt...."
    scene scarlett_s09_toilets02
    p "(Is that the sound of girls farting? Haha!)"
    scene black_screen with fade
    scene school_dining_hall
    show school_dining_hall_secret:
        xpos 535 ypos 460
    p "(There's Megan there.)"
    $ need_to_pee_as_scarlett = False
    $ hints_counter += 1
    jump dining_hall

label scene_dining_hall_brooke_and_beth:
    scene scarlett_s11_dining_hall04
    brook "Look who's back, Beth. Scarlett."
    beth "Oh, yes. Welcome back..."
    scene scarlett_s11_dining_hall02
    brook "Where have you been, all this time - in gnome land?"
    beth "Haha, yes, with your fellow gnomes on vacation!"
    p "Eh…."
    beth "Hey gnome, bring us some water!"
    p "Fuck off, you bitches..."
    brook "Haha!"
    jump dining_hall
label scene_dining_hall_megan:
    scene scarlett_s11_dining_hall01
    p "Hi, Megan. May I sit here?"
    meg "Of course."
    p "I heard what the Dean was saying to you in the office. It's not your fault. You are a good girl."
    meg "I'm sorry, but you don’t know anything about that. She's right, it’s my fault."
    p "Look, is there any way I can help you? Maybe another test subject?"
    scene scarlett_s11_dining_hall03
    meg "How did you learn about what I’m doing?"
    p "Eeehm.... From Nick..."
    meg "Aah... Nick... No, sorry. From now on, I will practice all my experiments on my rat, Rocco. Because people are not reliable."
    p "Okay. However you want, Meg. If you change your mind, just call me on this number."
    meg "Fine..."
    scene black_screen with fade
    scene city_map
    p "Aah... So what next? I have no idea how to convince Anders. I will take a look around for some work. Maybe in that coffee shop, see if they're hiring. On the way I will check the hospital to see if Mom’s car is still parked out front."
    $ time_of_day = Set_Time_of_Day('ÖĞLEN')
    $ looking_for_a_job_as_scarlett = True
    $ hints_counter += 1
    jump city_map

label scene_hospital_carpark_no_car:
    scene scarlett_s12_hospital_car01
    p "Looks like Mom’s car isn’t here."
    jump city_map

label scene_coffee_shop_ask_about_job_as_scarlet:
    scene shop_main
    p "Hello. I just want to ask about a job. Are there any available?"
    brst "Yes actually. I’m looking for someone to help out here."
    p "Great! And what is the pay?"
    brst "15 per hour."
    p "Only 15 per hour?"
    scene shop_girl_work
    brst "And what number were you expecting, young girl?"
    p "I don’t know, but maybe at least three times that amount?"
    brst "Haha! You're funny."
    scene shop_girl_work2
    brst "You know where  girls earn big money? In the strip club, just around the corner. You could try your luck at that. It’s nearly 8pm. I think they're just openeing."
    $ time_of_day = Set_Time_of_Day('AKŞAM')
    $ strip_club_location_available = True
    scene city_map
    p "Hmm... Strip club? Maybe that's not such a bad idea? What's there to it? Just throw off your clothes and take the money - easy stuff..."
    $ hints_counter += 1
    jump city_map

label scene_as_scarlett_at_strip_first_time:
    scene scarlett_s10_stripclub01
    bncr "Hello, little lady. What're you looking for?"
    p "I’m looking for work."
    scene scarlett_s10_stripclub02
    bncr "Really? Hmm... well, you are young, but that body... I don’t know. What is it you think you'll be doing here?"
    p "Look, are you the owner? I don’t think so!"
    bncr "Hah, you're right. You'll find the owner in the upper lounge. Good luck."
    p "Thanks."
    scene scarlett_s10_stripclub03
    ownr "Welcome, young lady."
    p "Hello."
    ownr "What's your name?"
    p "Emm... Brooke."
    burt "I’m Burt. My man informed me that you're looking for work."
    p "Yes, I’m thinking about it."
    burt "Are you a good dancer?"
    p "(Great, this is getting more complicated by the minute.) I hope so."
    burt "So, show me what you got."
    p "For free?"
    burt "Pffftt! Hah! Okay, young lady, normally I don't do that. But since you intrigue me, I will pay you $100 to see your young body, naked. No matter how good your dance will be. But if you dance well, I will give you work and good money for it. Deal?"
    $ have_to_pay_first_rent_to_sophia_as_scarlett = True
    menu:
        "What do you want to do?"
        "Dance for Burt":
            jump scene_as_scarlett_dancing_for_burt
        "Decline":
            p "I’m sorry, Burt, but I changed my mind. Can I leave now?"
            scene scarlett_s10_stripclub04
            burt "Of course, you are free to leave whenever you want - but know this: once you walk out that door, I will never give you another chance."
            menu:
                "Do you still want to leave?"
                "No":
                    jump scene_as_scarlett_dancing_for_burt
                "Yes":
                    $ time_of_day = Set_Time_of_Day('GECE')
                    $ turned_down_strip_club_owner = True
                    $ looking_for_a_job_as_scarlett = False
                    $ hints_counter += 1
                    scene city_map_night
                    p "I hope I made the right choice. Fine... I have no other way to get money fast. I will do that webshow with Sophia."
                    jump city_map


label scenes_sophia_room_accept_webshow_offer:
    scene scarlett_s22_webcam01
    sop "Everything is set up. The only thing is: your clothes are not good enough."
    p "Yeah, but I don’t have anything better."
    sop "I have a surprise for you. There are some clothes, on the bed. I bought them before you left on your Europe trip. So finally, I'll be able to see how well they suit you."
    p "Cool. Give me a second."
    scene scarlett_s22_webcam02
    p "How do I look?"
    sop "Great! Irresistible and sweet, all at once."
    p "(Is that a compliment? Hah!)"
    p "Thank you, Sophia."
    scene scarlett_s22_webcam03
    sop "So now we're ready, aren't we?"
    p "I hope so."
    sop "Don’t worry. I know it’s been a while. Maybe you’re feeling like someone in another person’s skin."
    p "(Yeah. Literally...)"
    sop "But I promise you, When this camera goes live, everything will come back to you."
    p "Let’s do it."
    scene scarlett_s22_webcam04
    $ renpy.pause(1.5)
    scene scarlett_s22_webcam05
    "Sly Stallion" "Hey, Sophia!!!"
    sop "Hello, guys. Today I have a big surprise for you."
    "Sly Stallion" "I see your juicy boobs are gone. I’m leaving…."
    scene scarlett_s22_webcam06
    sop "Look who's back! My good friend Scarlett!!!"
    "Sly Stallion" "OMG!!!"
    "J.C. VanDammned" "Scarlett is back!!"
    p "Hi, guys…."
    "Sly Stallion" "She looks stunning…"
    p "Thank you."
    "Arnie Schwarzenegger" "tip 1000 tokens."
    sop "Wow!"
    "Arnie Schwarzenegger" "Stop talking…. We want some action, girls."
    scene scarlett_s22_webcam07
    p "(I was so nervous before, but when she started kissing me just now, it’s like I'm floating to another world. She’s so great at it. I feel like there's nothing else around us.)"
    sop "Hmmmmm….. I missed you so much…."
    scene scarlett_s22_webcam08
    sop "Lie on your back."
    scene scarlett_s22_webcam09
    $ renpy.pause()
    scene scarlett_s22_webcam10
    p "That is soooo intense...."
    scene scarlett_s22_webcam11
    $ renpy.pause()
    scene scarlett_s22_webcam12
    p "Mmmmmm...."
    scene scarlett_s22_webcam14
    p "(Now I know why girls love stuff like this.)"
    scene scarlett_s22_webcam13
    p "Sophieeeee... keep going."
    scene scarlett_s22_webcam15
    "Sly Stallion" "Damn, girls, you’re heating me up!"
    "J.C. VanDammned" "tips 1000 tokens."
    "J.C. VanDammned" "Hey Scar, ride on Sophia’s face…"
    scene scarlett_s22_webcam16
    p "(That was fucking amazing...)"
    p "I need more."
    scene scarlett_s22_webcam18
    p "Mmmmmmm..."
    scene scarlett_s22_webcam17
    sop "*Humpffff*"
    "Leo Dick a Prio" "tips 1000 tokens"
    "Leo Dick a Prio" "Stick your finger in her ass, Sophia."
    scene scarlett_s22_webcam19
    $ renpy.pause()
    scene scarlett_s22_webcam20
    p "Ooooooohh!!"
    scene scarlett_s22_webcam21
    p "(Well, that feels really strange...)"
    scene scarlett_s22_webcam21
    p "What about me satisfying you, hmm?"
    "Arnie Schwarzenegger" "tips 10 000 tokens"
    "Arnie Schwarzenegger" "Hey Sophie, fuck her from behind till she cums."
    scene scarlett_s22_webcam22
    sop "OMG!! THANK you so much!!!"
    scene scarlett_s22_webcam21
    p "(Fucking Arnie!)"
    scene scarlett_s22_webcam23
    sop "Just give me a second, guys...."
    scene scarlett_s22_webcam25
    p "That thing is HUGE!!"
    scene scarlett_s22_webcam24
    sop "Don’t worry, it's just like we used to do it before."
    scene scarlett_s22_webcam27
    $ renpy.pause()
    scene scarlett_s22_webcam26
    "Sly Stallion" "Your pussy's getting soaking wet, Sophia. Looks like you're enjoying it a lot. GIVE HER MORE!!"
    scene scarlett_s22_webcam28
    p "I'm CUMMING...!!!!"
    scene scarlett_s22_webcam29
    "Puck Norris" "I’m done tooo...  Wow, you girls really know how to do it... See you girls next time!"
    sop "That was great. I must say: I really missed doing that with you."
    p "Yes, that was like a new experience. I’m quite sleepy now."
    sop "Good night, my sweet."
    $ have_to_pay_first_rent_to_sophia_as_scarlett = False
    $ have_paid_first_rent_to_sophia_as_scarlett = True
    $ had_first_web_show_with_sophia_as_scarlett = True
    $ had_web_show_with_sophia_that_night = True
    $ hints_counter += 2
    jump mc_room

label scene_as_scarlett_dancing_for_burt:
    scene scarlett_s10_stripclub04
    burt "I'm happy you made the right decision. Just go to the dressing room and pick out the clothes you want. I'll wait here."
    scene scarlett_s10_stripclub05
    p "Damn, so many clothes again. Most of them are dresses that barely hide anything. What am I doing? I’m not even a good dancer - let alone a striper."
    scene scarlett_s10_stripclub06
    d "Maybe you need a helping hand? Hmmm?"
    scene scarlett_s10_stripclub07
    d "What about some damn sexy western style stripdance?"
    p "But…. I cannot dance, 'cause I don’t know how. I’m a poor dancer at best."
    scene scarlett_s10_stripclub08
    a "Don’t worry about it. I can help you dance like a PRO."
    d "Pfeeeh…? You?"
    a "Yes… Me."


    scene scarlett_s10_stripclub10
    d "Ha! You must have fallen on your head. Why the hell would he pick you over me. I’m the nasty lady here with the skills. We need to heat up that owner guy, not bore him to death with amateur swinging."
    scene scarlett_s10_stripclub09
    p "I appreciate both of you trying to help - but how will you do that?"
    scene scarlett_s10_stripclub10
    a "It's easy: just pick one of us and we will help you with the dancing - controlling your body throughout."
    menu:
        p "Hmmm sounds easy enough. So I’m picking…"
        "Angel":
            $ have_chosen_devil_during_striptease = False
        "Devil":
            $ have_chosen_devil_during_striptease = True


    play music "sounds/music/winger_cant_get_enough.ogg" fadein 3.0
    scene scarlett_s21_striptease01
    p "(Ufff. Let's do this)"
    scene scarlett_s21_striptease02
    $ renpy.pause()
    scene scarlett_s21_striptease03
    $ renpy.pause()
    scene scarlett_s21_striptease04
    $ renpy.pause()
    scene scarlett_s21_striptease05
    $ renpy.pause()
    scene scarlett_s21_striptease06
    $ renpy.pause()
    scene scarlett_s21_striptease11
    $ renpy.pause()
    scene scarlett_s21_striptease12
    $ renpy.pause()
    scene scarlett_s21_striptease13
    $ renpy.pause()
    scene scarlett_s21_striptease14
    $ renpy.pause()
    scene scarlett_s21_striptease07
    $ renpy.pause()
    scene scarlett_s21_striptease08
    $ renpy.pause()
    scene scarlett_s21_striptease17
    $ renpy.pause()
    scene scarlett_s21_striptease15
    $ renpy.pause()
    scene scarlett_s21_striptease16
    p "I've got something special for you..."
    scene scarlett_s21_striptease18
    $ renpy.movie_cutscene("scenes/Scarlett/21_striptease/scarlett_s22_gun_move.webm", loops=0, delay=-1, stop_music=False)
    scene scarlett_s21_striptease10
    $ renpy.movie_cutscene("scenes/Scarlett/21_striptease/scarlett_s22_gun_lick.webm", loops=0, delay=-1, stop_music=False)
    p "Pheh… and you're dead now..."
    if not have_chosen_devil_during_striptease:
        scene scarlett_s21_striptease09
        burt "Nicely done, girl. The money is yours - $100 plus a $100 more 'cause I liked it. And I will be really happy to see you again."
    #if reputation_number < 1:TODO devil images
    #else: # TODO angel images
    elif have_chosen_devil_during_striptease:
        play sound 'sounds/effects/gunshot_sound.ogg'
        scene scarlett_s21_striptease19
        $ renpy.pause(1.0)
        scene scarlett_s21_striptease21 with fade
        $ renpy.pause(0.5)
        scene scarlett_s21_striptease20 with dissolve
        p "WHAT the…!!?!?"
        scene scarlett_s21_striptease24
        d "Whoohaaaa!!! That was a hilarious grande finalle. PERFECT!!!!"
        scene scarlett_s21_striptease23
        p "What have you done?!!!"
        scene scarlett_s21_striptease22
        d "Me?! What do you mean?"
        p "What I mean is: you made me kill him!"
        d "Hah! Hey! Yes, I was controlling you. But during the dance only. You pulled the trigger, not me. By the way - “Nice shootin', son.” Haha!"
        scene scarlett_s21_striptease23
        p "That's not funny!"
        scene scarlett_s21_striptease22
        d "Sorry, but it is. Look at you - how you're jumping around and yelling there. What's the problem? He was an old perverted deviant, forcing young girls to dance here for him. He probably didn't even want to pay you for this dance."
        scene scarlett_s21_striptease25
        p "Hmmm... but it's too late find that out, right?"
        d "Heh, most likely. I'm not a doctor, but with that hole in his head, he looks pretty dead to me."
        p "So what now?!"
        d "Just leave that gun there. Here is your money. He won't need it anymore, where he's going. And leave the rest to me."
        p "Leave it to you...? arghh... I’m starting to worry when you say that..., but I guess I don't really have a choice."
        scene scarlett_s21_striptease26 with fade
        "A FEW MOMENTS LATER..."
        bncr "So, that little bitch killed my boss..."

    $ time_of_day = Set_Time_of_Day('GECE')
    $ looking_for_a_job_as_scarlett = False
    $ hints_counter += 3 #MAGIC
    scene city_map_night
    p "I hope I made the right choice. Time to get back to the apartment."
    jump city_map

label scenes_kitchen_as_scarlett_settle_first_rent_with_sophia:
    scene scarlett_s08_sophia_morning01
    if turned_down_strip_club_owner:
        p "(No other choice...)"
        p "Hey Sophia, I was thinking about it, and I think I'll take you up on that webshow offer."
        scene scarlett_s08_sophia_morning02
        sop "Great! Let me go and get it all set up. Come to my room in a little bit."
        scene black_screen with fade
        $ sophia_in_her_room_for_webshow = True
        $ hints_counter += 1
        jump roommate_room
    else:
        if have_chosen_devil_during_striptease:
            p "(It feels weird, giving Sophia this blood money. But she does need it for the rent...)"
        else:
            p "(It was humiliating, but at least I can pay Sophia...)"
        p "Here is your money for the rent, Sophia."
        sop "Wow, that was quick?"
        p "Yeah, new job of sorts."
        sop "That's good. What is it?"
        p "I'd rather not say."
        sop "That bad, huh? Well, at least the money is good. Thanks for this."
        p "No problem."
        $ have_to_pay_first_rent_to_sophia_as_scarlett = False
        $ have_paid_first_rent_to_sophia_as_scarlett = True
        $ hints_counter += 1
        jump kitchen

label scene_hospital_carpark_double_check:
    scene scarlett_s12_hospital_car03
    p "(Hmm, Mom’s car is here again. I'll quickly check inside.)"
    scene scarlett_s12_hospital_inside01
    p "(I'll ask at the reception.)"
    scene scarlett_s12_hospital_inside02
    p "Hello?"
    nrs "Hello. What can I help you with?"
    p "I’m just looking for one person. Can you please tell me where I can find her?"
    nrs "Sure, if she is in a public department."
    scene scarlett_s12_hospital_inside03
    p "Fine. Her name is Julia Levins."
    scene scarlett_s12_hospital_inside04
    play sound "sounds/effects/phone_ringing_sound.ogg"
    $ renpy.pause(2.0, hard=True)
    nrs "Just give me a second."
    p "(That’s Megan calling me.)"
    stop sound
    scene scarlett_s12_hospital_megan_phone
    meg "Hi, Scarlett. Please, I need your help immediatelly."
    p "Sure, Megan. I'll be at school soon. Can you wait a while?"
    meg "I don’t think so. I really need you, now. You are the only one who can help me."
    p "Fine, I’ll be at the lab shortly."
    scene scarlett_s12_hospital_inside05
    nrs "We're having a little problem with the network. This might take a while."
    scene scarlett_s12_hospital_inside03
    p "It's okay, I need to go anyway. I'll be back later. Bye."
    $ double_check_the_hospital_after_paying_first_rent = False
    $ megan_desperately_needs_scarlett_in_lab = True
    $ hints_counter += 1
    jump city_map

label scene_megan_needs_scarlett_in_lab_immediately:
    scene scarlett_s13_megan_lab01
    meg "I’m so glad that you made it so fast."
    p "Of course, Meg. I’m happy to help you. What happened?"
    scene scarlett_s13_megan_lab02
    meg "My rat Rocco, dissapeared… And I don’t have another test rat to analyse the new pills effects. And I must present them to the Dean today."
    p "It’s Okay, Megan. As I said before, I will help you with that. I’ll be your guinea pig, hih."
    scene scarlett_s13_megan_lab03
    meg "You will? That's great! Let’s get to work."
    scene scarlett_s13_megan_lab04
    meg "Just give me a few minutes, and I will make the testing pills."
    scene scarlett_s17_pills_testing01
    meg "There we go. Our samples. Let’s try the first one."
    scene scarlett_s17_pills_testing02
    p "Fine, let’s do it. (I’m really curious to see how girls react to them.)"
    scene scarlett_s17_pills_testing12
    meg "How do you feel?"
    p "Good, so far. Hmm... A little warm here."
    show scarlett_s17_pills_testing_grow1
    $ renpy.pause(1.0)
    show scarlett_s17_pills_testing_grow2 with dissolve
    $ renpy.pause(1.0)
    show scarlett_s17_pills_testing_grow3 with dissolve
    $ renpy.pause(1.0)
    show scarlett_s17_pills_testing_grow4 with dissolve
    $ renpy.pause(1.0)
    scene scarlett_s17_pills_testing04
    p "Wow... That was a really strange feeling. But pretty cool."
    meg "So this one's effect is growing. Now try another one."
    scene scarlett_s17_pills_testing05
    p "Okay."
    scene scarlett_s17_pills_testing03
    p "Whoops..."
    p "It fell somewhere on the floor. Don't worry, I will find it."
    scene scarlett_s17_pills_testing06
    play sound "sounds/effects/ripping_sound.ogg"
    $ renpy.pause(2.0, hard=True)
    p "Shit!"
    scene scarlett_s17_pills_testing07
    p "Damn! I just ruined my favorite trousers."
    meg "Heheh... That's the side effect of growing pills. It’s okay, forget about it. I will find that one later."
    meg "Here is another one. Try it."
    scene scarlett_s17_pills_testing05
    p "Fine."
    scene scarlett_s17_pills_testing13
    meg "So, feeling anything?"
    p "Hmmm... nothing. I still feel the same."
    meg "Okay, so this one's not working."
    meg "Now for the last one."
    scene scarlett_s17_pills_testing_small1
    meg "Feel anything?"
    p "Yes, a little cold."
    show scarlett_s17_pills_testing_small2 with dissolve
    $ renpy.pause(1.0)
    show scarlett_s17_pills_testing_small3 with dissolve
    $ renpy.pause(1.0)
    show scarlett_s17_pills_testing_small4 with dissolve
    $ renpy.pause(1.0)
    p "Oh God, I'm even smaller than normal."
    meg "That means, what we have here, is a pill with a strong reduction effect."
    scene scarlett_s17_pills_testing08
    p "That's nice, but what about me?!"
    meg "Don’t worry. I have a,... let's call it a size neutralizer. It should reverse all size related effects of these pills. Just stay calm..."
    scene scarlett_s17_pills_testing11
    $ renpy.pause(1.5)
    scene scarlett_s17_pills_testing09 with dissolve
    $ renpy.pause(1.5)
    scene scarlett_s17_pills_testing10
    $ renpy.pause()
    meg "And that’s everything, for now. You've helped me a lot. Tomorrow, can you please come back. And I will have a few more tests, and then we're done."
    p "No problem, Meg."
    scene school_map
    p "That was really cool. But I'm feeling a little strange now. Better find a safe space, so nobody sees me. Maybe the toilets. Girls toilets, I must remember."
    $ megan_desperately_needs_scarlett_in_lab = False
    $ as_scarlett_feeling_weird_after_first_lab_tests = True
    $ hints_counter += 1
    jump school

label scene_as_scarlett_female_wc_stall_feeling_weird:
    scene scarlett_s18_horny_wc01
    p "What the hell is happening to me?"
    p "I’m feeling a strong heat under my belly."
    scene scarlett_s18_horny_wc02
    p "And it’s getting stronger."
    scene scarlett_s18_horny_wc04
    p "And my nipples, are so stiff and sensitive."
    scene scarlett_s18_horny_wc03
    p "Hmmm... I think I’m going to like this, touching myself."
    scene scarlett_s18_horny_wc05
    p "Aaaah... They are rock hard."
    scene scarlett_s18_horny_wc06
    p "I must do it... I cannot resist this strong feeling."
    scene scarlett_s18_horny_wc07
    p "DAMN! My panties are absolutely wet, and this pussy is heating up like an oven."
    scene scarlett_s18_horny_wc09
    p "Hmmm... yes, that is soo... Goooood!!!"
    scene scarlett_s18_horny_wc08
    p "I think it’s comming! MmmmmMm..."
    scene scarlett_s18_horny_wc10
    p "MmmmmmmMm..."
    p "That was absolutely amazing! My first female orgasm. Such a strong feeling."
    scene scarlett_s18_horny_wc10
    play sound 'sounds/effects/door_open_sound.ogg'
    $ renpy.pause(1.0, hard=True)
    scene scarlett_s18_horny_wc12
    p "Uh. Somebody came into the toilets."
    scene scarlett_s18_horny_wc13
    p "That’s Brooke and Bethany..."
    beth "So you will have them tomorrow?"
    brook "Yes. I will."
    scene scarlett_s18_horny_wc14
    brook "And with those pills, we'll be unbeatable in the tournament."
    scene scarlett_s18_horny_wc11
    p "Are they talking about pills? And what tournament?"
    scene scarlett_s18_horny_wc15
    beth "Hah! We'll show Sophia, how things are done."
    brook "Yeah. But don't tell anybody about it."
    beth "Of course! I’m not an idiot."
    scene scarlett_s18_horny_wc16
    p "I need to tell Sophia about this."
    scene city_map
    p "Before going home, I'll stop by the hospital again."
    $ time_of_day = Set_Time_of_Day('ÖĞLEN')
    $ as_scarlett_feeling_weird_after_first_lab_tests = False
    $ checking_hospital_again_after_first_lab_tests = True
    $ hints_counter += 1
    jump city_map

label scene_devil_at_hospital_when_looking_for_mom:
    scene scarlett_s12_hospital_car02
    p "Hmm... Mom’s car is not here anymore."
    scene scarlett_s12_hospital_devil01
    d "Hey. Are you sick?"
    p "Oh, no, I’m not. Why do you say that?"
    scene scarlett_s12_hospital_devil03
    d "Because you are coming here, again and again… So, I just wanted to ask why?"
    p "Aaah, I just saw my mom’s car here earlier. I just wanted to see her and I was curious what she's still doing in the city."
    scene scarlett_s12_hospital_devil02
    d "Are you sure that was her car?"
    p "I think... Yes... 90\%."
    d "Maybe she just needed some papers for your case. You know there’s always lots of paperwork when an accident happens."
    p "Hmmmm. Yes. That seems like a good reason."
    d "Didn’t you want to tell Sophia something ? 'Cause she's home now."
    scene scarlett_s12_hospital_devil04
    p "Yes, you are right. Better to catch her..."
    $ checking_hospital_again_after_first_lab_tests = False
    $ have_to_tell_sophia_about_beth_brooke_talk = True
    $ hints_counter += 1
    jump city_map

label scene_go_to_apartment_to_tell_sophia_about_beth_brook_talk:
    scene scarlett_s13_volleyball01
    p "(There she is. The Devil was right, looks like she’s going somewhere.)"
    p "Hi, Sophia."
    scene scarlett_s13_volleyball02
    sop "Hi, Scarlett. How are you?"
    p "Good. Where you off to?"
    sop "Ah, just volleyball training with Ivana."
    sop "Do you want to come with us?"
    p "I don’t know. You know Ivana is still a little upset with me…"
    scene scarlett_s13_volleyball03
    sop "Yeah, I know, but you need to see this. Last time we beat Bethany and Brooke. And I feel we can do it again."
    sop "Please come with me and support us. It's our last training before the tournament."
    p "(Aaah, about that tournament... the way the other girls talked, I don’t know, Sophia, if you'll be able to beat them now...)"
    p "Fine. I’m in..."
    sop "Great… Let’s go!"
    scene black_screen with fade
    scene scarlett_s13_volleyball04
    brook "What’s up, Sophia? I bet you thought you could beat us again, right?"
    beth "Haha! So silly."
    brook "If you don’t have those pills, you're not that good, huh?"
    scene scarlett_s13_volleyball05
    iva "Pills? What pills?"
    sop "Oooh."
    scene scarlett_s13_volleyball06
    sop "I'll tell you about them later."
    scene scarlett_s13_volleyball04
    beth "Haha! Bye, girls. We'll see you at the tournament. Haha!"
    scene black_screen with fade
    scene scarlett_s13_volleyball09
    p "I think I have an idea."
    scene scarlett_s13_volleyball07
    iva "Yeah? Keep your ideas to yourself. We have no interest in them."
    p "Fine. But I just want to tell you, they will both have those growing pills for the tournament. And with them, they'll beat all other teams like nothing."
    scene scarlett_s13_volleyball07
    iva "Growing pills?"
    p "Yes. There are these growing pills, that can make you a little taller, or your boobs bigger, and much more."
    iva "Haha! Good one..."
    scene scarlett_s13_volleyball09
    p "Sophia, can you say somehing?"
    scene scarlett_s13_volleyball08
    sop "Eeehm... She's right. I was using them that day during the bikini competition. Do you remember how my boobs looked? That was not the Wonderbra, but these miracle pills."
    scene scarlett_s13_volleyball10
    iva "Fiiiiiine! What is this plan of yours?"
    scene scarlett_s13_volleyball09
    p "Just leave it to me. I'll take care of the rest."
    $ time_of_day = Set_Time_of_Day('GECE')
    scene city_map_night
    p "(In the morning I will go to school and ask Megan for those pills. But now, I’m already tired and ready for bed."
    $ have_to_tell_sophia_about_beth_brooke_talk = False
    $ time_to_find_growing_pill_on_clothes = True
    $ hints_counter += 1
    jump city_map

label scene_find_lost_pill_on_clothes:
    scene scarlett_s13_pill_found01
    p "Aaah... Hmmm, I have something... in my clothes..."
    scene scarlett_s13_pill_found02
    p "?????"
    scene scarlett_s13_pill_found03
    p "Hah, it is that pill. I thought I dropped it somewhere in the lab. Probably that “horny” pill. Not what I need."
    scene scarlett_s13_pill_found04
    p "I will return it to Meg tomorrow. But now, time to sleep."
    $ time_to_find_growing_pill_on_clothes = False
    $ need_to_sleep_after_finding_pill_on_clothes = True
    jump mc_room

label scene_sophia_wakes_up_scarlett_for_the_plan:
    scene scarlett_s16_sophia_wakeup01
    sop " Wake up, sleepy."
    p "Aaaah... Am I late?"
    sop "No. How is your plan looking ?"
    p "Hey, calm down. Give me some time. Later today I will have those pills."
    sop "Great! Okay, I’m going to school with Ivana, so see you there."
    p "Fine."
    scene mc_room_day # TEMP TODO change to scarlett room pic
    p "First thing is to go to the school lab. I need to ask Megan for more pills and give her back the one I found yesterday."
    $ need_to_sleep_after_finding_pill_on_clothes = False
    $ have_to_return_found_pill_to_meg = True
    $ hints_counter += 1
    jump city_map

label scene_as_scarlett_returning_lost_pill_to_meg_in_lab:
    scene scarlett_s19_horny_megan14
    p "Hey, Megan. How are you?"
    meg "Hi, Scarlett! Good. My research is moving forward. You've helped me a lot."
    p "Ah, yes... Can you help me tooo?"
    meg "Of course! What do you need?"
    p "You know, I really need those growing pills. They were really great. And I want..."
    scene scarlett_s19_horny_megan15
    meg "No! Never! I cannot do that. Because I already made that mistake once, and the Dean will go crazy when she finds out."
    p "Aah."
    scene scarlett_s19_horny_megan16
    meg "I’m sorry. I didn't mean to be so angry. I’m just a little tired because of my research."
    p "It’s okay, Meg. How about a big coffee to wake you up?"
    scene scarlett_s13_megan_lab03
    meg "Uuuh... Coffee would be great. But I cannot go out right now. I must have these pills ready today for the Dean."
    p "It’s okay, I'm going for coffee anyway. I can bring you one."
    meg "You are great... Here is some money. Get me a capuccino, please."
    p "No problem. I'll be back shortly."
    $ have_to_return_found_pill_to_meg = False
    $ have_to_get_meg_coffee_from_shop = True
    $ hints_counter += 1
    jump city_map

label scene_return_to_lab_after_buying_coffee_for_meg:
    $ have_to_get_meg_coffee_from_shop = False
    $ have_a_bunch_of_pills_to_test_on_ivana_and_sophia = True
    scene shop_main
    p "One large capuccino, please."
    brst "Here it is. Enjoy your coffee."
    p "Thank you. (This one is going to be fun...)"
    scene scarlett_s13_megan_lab06
    p "(Sorry Megan, but I don't have time to waste.)"
    scene scarlett_s13_megan_lab05
    meg "Wow, that's a big one."
    p "Here you go, Megan."
    meg "Great! That was nice of you."
    p "No problem. Is there anything more I can do for you?"
    scene scarlett_s19_horny_megan01
    meg "Yeah, sure. You can clean out those bottles for the pills."
    meg "(Oh... hmm... mmm... What is happening??)"
    scene scarlett_s19_horny_megan04
    meg "(She has such a beautiful butt...)"
    scene scarlett_s19_horny_megan02
    meg "(Damn, she's heating me up. I cannot resist her anymore.)"
    scene scarlett_s19_horny_megan03
    meg "Hey, let me help you a little."
    scene scarlett_s19_horny_megan05
    p "(It’s working really fast on her.)"
    p "Of course..."
    meg "Your smell is soo nice, Scarlett."
    p "Thank y..."
    scene scarlett_s19_horny_megan06
    meg "*kissing*"
    scene scarlett_s19_horny_megan07
    p "(Damn, her tongue is really nimble. I love her kisses.)"
    scene scarlett_s19_horny_megan08 with dissolve
    p "Yes. Please don’t stop, Megan."
    scene scarlett_s19_horny_megan09
    meg "Aaaaahh!! What am I doing?!!!"
    scene scarlett_s19_horny_megan10
    p "I don’t know, but please keep going."
    scene scarlett_s19_horny_megan12
    meg "I CAN’T!!!!"
    scene scarlett_s19_horny_megan11
    p "Hah, that went way different than I was expecting, but... mission accomplished."
    scene scarlett_s19_horny_megan13
    p "Megan already has hundreds of pills. I'll just take a few pills and hope that she won't notice."
    p "Each container has a different colour lid. Unfortunately, they are not labeled. I can't tell which ones are growing, and which are horny and reducing pills."
    p "I'll need to test them on Ivana and Sophia, to be sure..."
    #jump vote_next_content#TEMP
    $ are_hints_available = True
    $ hints_counter += 1
    $ inventory.add(unlabeled_pills)
    scene school_map
    p "(I'll need to find Ivana and Sophia. They must still be here.)"
    jump school
    #stop music fadeout 1.0
    #play music "sounds/music/Menu_intro_music.ogg" fadein 3.0
    #scene outro
    #$ renpy.pause(15.0, hard=True)
    #$ renpy.quit()

### Voting screen
screen vote_next_content:
    on "show" action Play('music', "sounds/music/Menu_intro_music.ogg", fadein=3.0, if_changed=True)
    imagemap:
        ground "votescreen.png"
        hover "votescreen_glow.png"


        hotspot (600, 450, 400, 200) action OpenURL('https://www.patreon.com/posts/40586950'), Jump("interaction_voted_pressed")#vote


label vote_next_content:
    call screen vote_next_content

label interaction_voted_pressed:
    scene outro
    stop music fadeout 1.0
    play music "sounds/music/Menu_intro_music.ogg" fadein 3.0
    $ renpy.pause(15.0, hard=True)
    $ renpy.quit()

## 0.5 #############################################################################################
label scene_female_wc_megan_jacking_in_stall:
    scene female_wc
    scene black with fade
    $ have_a_bunch_of_pills_to_test_on_ivana_and_sophia = False

    #TODO moaning sound
    scene scarlett_s25_megan_wc01
    p "(Hoho! Looks like those sounds are coming from this closed stall."
    scene scarlett_s25_megan_wc02
    p "(Hehe... silently……)"
    stop music fadeout 1.0
    scene scarlett_s25_megan_wc03 with fade
    play music "sounds/music/Sexy_music1_monks_topher.ogg" fadein 3.0
    p "(Looks like someone's having a happy moment.)"
    menu:
        "Should I take a look?"
        "NO":
            p "(I’m not a freak. I'll just leave her to enjoy the pleasure alone.)"
            #Jump to school map female WC disabled for this moment.

        "YES":
            scene scarlett_s25_megan_wc10 with fade
            p "(Just a little look...)"
            scene black with fade
            scene scarlett_s25_megan_wc05 with dissolve
            p "(That’s… That’s Megan! Wow! I've never seen her naked.)"
            scene scarlett_s25_megan_wc06 with fade
            $ renpy.pause(1.5)

            p "(Wow! Her legs look stunning, and that tiny pussy.)"
            scene scarlett_s25_megan_wc07
            $ renpy.pause(2.0,hard=True)
            scene scarlett_s25_megan_wc08
            $ renpy.pause(2.0)
            scene scarlett_s25_megan_wc09
            $ renpy.pause(1.0)

            p "She's definitely enjoying this moment."
            scene scarlett_s25_megan_wc12
            p "Damn... Maybe I can go inside? She might not run away this time?"
            scene scarlett_s25_megan_wc11 with fade
            $ renpy.pause(0.5)
            p "(That slippery little freak...)"
            scene scarlett_s25_megan_wc13 with dissolve
            a "Ehm… HEY!"
            scene scarlett_s25_megan_wc23 with hpunch#( image of scarlett hit’s her head)#TODO dec
            play sound 'sounds/effects/punch_sound.ogg'
            $ renpy.pause(2.0)

            scene scarlett_s25_megan_wc22 #(ouch image)#TODO dec
            p "Ouch… What are you DOING HERE? I almost went though this door with my head!"
            scene scarlett_s25_megan_wc13
            a "You got what you deserved. Be happy that she didn't hear that."
            p "So, what do you want?"
            a "You've been watching too many porn movies…"
            p "What?"
            scene scarlett_s25_megan_wc14
            a "If you ever want to be with her, don’t try to trick her. Just some good old advice from me."
            p "Ah... Okay."
            a "And it's better to leave her alone for now. I think you have far more to offer than lying here on your belly and sneaking a peek at a good looking scientist masturbating."
            p "Eeeeeh? Really? You think?"
            hide window
            scene scarlett_s25_megan_wc17 with dissolve
            a "Heeh. I hope so. And you still need to find Sophia and Ivana right now."
            p "Yeah..."
            menu:
                "Should I stay and watch Megan?"
                #reputation -1
                "YES":
                    $ rep_choice_mc_scarlett_watched_meg_jacking_in_stall = True
                    $ reputation_number -= 1
                    p "But I want to see her cumming. So please, leave me alone here."
                    hide window
                    scene scarlett_s25_megan_wc13 with dissolve
                    $ renpy.pause(1.0)
                    a "As you like...."
                    scene black with fade
                    scene scarlett_s25_megan_wc08 with fade
                    $ renpy.pause(1.5, hard=True)
                    meg "Mmmmmmm…. Aaah.."
                    scene scarlett_s25_megan_wc16
                    $ renpy.pause(1.0)
                    meg "Yes…. Please……!!!"
                    p "(Damn, she is so fucking HOT!)"
                    scene scarlett_s25_megan_wc19
                    p "(Those lovely perky titties.)"
                    scene scarlett_s25_megan_wc21
                    meg "Hmmmmpfff!!!!!"
                    hide window
                    scene scarlett_s25_megan_wc18 with dissolve
                    scene scarlett_s25_megan_wc18 with vpunch
                    $ renpy.pause(1.0)
                    meg "AAAAAAhh! I’m cumming!!! FUCK! YES!"
                    scene scarlett_s25_megan_wc15 with dissolve
                    $ renpy.pause(3.0,hard=True)

                    meg "YES! FUCK ME! I need mooore! FUCK ME YOU PIG!"
                    p "(Damn! She’s going really crazy.)"
                    scene scarlett_s25_megan_wc20 with dissolve
                    $ renpy.pause(1.0)
                    p "(Her pussy's dripping like crazy too. What an orgasm!  Damn, I hope one day I can make her do that too.)"

                "NO":
                    scene scarlett_s25_megan_wc17
                    p "You are right- time to go. I have seen enough."
    stop music fadeout 3.0
    scene school_map with fade
    p "(I'm not seeing Ivana and Sophia anywhere. They wouldn't be upstairs, would they?)"
    $ mc_scarlett_upstairs_when_looking_for_ivana_n_sophia_available = True
    $ hints_counter += 1
    jump school

label scene_mc_scarlett_upstairs_looking_for_ivana_n_sophia_run_into_anders:
    scene black
    $ mc_scarlett_upstairs_when_looking_for_ivana_n_sophia_available = False
    scene scarlett_s23_onstairs_anders01 with fade
    andr "Who have we here?"
    scene scarlett_s23_onstairs_anders05
    p "Ah. Hello, Mr. Anders. I don’t suppose you know where I can find Sophia?"
    scene scarlett_s23_onstairs_anders06
    andr "Yes, she's with Ivana in the school cafeteria for lunch."
    p "Aah, yes it’s lunch time. I forgot it's that time already."
    scene scarlett_s23_onstairs_anders04
    andr "What will we do about your Biology grade?"
    p "(Aaaah! That’s a topic I didn’t want to talk about.)"
    scene scarlett_s23_onstairs_anders02
    p "Yes... Biology. Hehe... Eeeh..."
    p "What if I apologise for all the things I did to you?"
    scene scarlett_s23_onstairs_anders03
    andr "Hmm... And do you think that will be enough?"
    p "I’m hoping it is..."
    p "I’m really sorry for all those things... Really, from the bottom of my heart. It was a really big mistake and I’m sorry."
    scene scarlett_s23_onstairs_anders06
    andr "Okay, we won't talk about it here. Meet me any day after school in my office, and we can talk about how... deep... your apology is."
    p "(He wants to fuck me?!?!?)"
    scene scarlett_s23_onstairs_anders05
    p "Hih. Okay. See you later, Mr. Anders. Now I must run to the cafeteria to catch the girls."

    scene scarlett_s24_lunch01 with fade
    sop "Finally! You are here! So?"
    iva "Take a seat."
    p "Argh... It’s fish again today?"
    iva "It’s healthy."
    scene scarlett_s24_lunch02
    sop "So how did it go with Megan?"
    p "It went different than I thought."
    scene scarlett_s24_lunch07
    iva "So you don’t have it?"
    scene scarlett_s24_lunch04
    p "Of course I have it, girls!"
    scene scarlett_s24_lunch03
    iva "You sneaky... You had us going, there."
    scene scarlett_s24_lunch06
    sop "Damn, girl, I love you… So we can test them right now?"
    scene scarlett_s24_lunch04
    p "No, it's not a good place. And we have a little problem: Megan has three types of pills and they are all the same color, because she hasn’t colorcoded them yet. And I don’t know which one is which. So we need to test them in a safe place."
    scene scarlett_s24_lunch03
    iva "So, where and when?"
    scene scarlett_s24_lunch08
    p "How about this evening? At our apartment? What do you think, Sophia?"
    scene scarlett_s24_lunch05
    sop "I think it’s a great idea."
    scene scarlett_s24_lunch04
    p "Good."
    iva "And why is that death sticker on them?"
    p "It’s okay, it’s just a vial from another product. But it’s clean, don’t worry."
    p "So, this evening, girls..."

    scene school_map
    p "Better go to the apartment to hide the pills in a safe place. And then I can visit Anders in his office."
    $ need_to_hide_unlabebeled_pills_in_apartment = True
    $ hints_counter += 1
    jump school
    #interaction on go out.
    #Disable interaction on female WC with Megan


label scene_beth_and_brooke_bullying_megan_outside_school:
    $ need_to_hide_unlabebeled_pills_in_apartment = False
    scene black
    scene scarlett_s26_bullying01 with fade
    p "(I think that's Megan, talking with Brooke and Bethany. What do they have to talk about?)"

    beth "You know, that tournament is in two days, and we still don’t have the pills from you?!"
    meg "But I have them almost ready now, don’t worry, girls, I will give them to the Dean tomorrow morning."
    scene scarlett_s26_bullying03
    brook "Hmmmm..."
    scene scarlett_s26_bullying02
    beth "Better hope you're right. Or..."
    scene scarlett_s26_bullying07
    p "Or what, you bitches?"
    meg "Oh…"
    scene scarlett_s26_bullying04
    brook "Arrrrgh! The gnome strikes back! What the hell are you doing here?"
    scene scarlett_s26_bullying06
    beth "Hahaha!! It’s a bad time to be looking for Snow White, haha."
    scene scarlett_s26_bullying07
    p "Fuck off, both of you. Maybe I’m smaller, but..."
    scene scarlett_s26_bullying05
    brook "Eerrr... Megan, do your JOB! Hey Beth, we're leaving before this gnome tries to bite us."
    scene scarlett_s26_bullying08
    meg "Thank you, but you didn’t need to do that."
    p "It’s okay. I just don’t like them."
    p "(To be honest, I just want to fuck their brains out of their heads.)"
    meg "How about some coffee? I’m paying."
    p "(Anders will have to wait for another day.)"
    p "Of course."
    $ have_to_meet_megan_at_coffee_shop = True
    $ time_of_day = "ÖĞLEN"
    $ hints_counter += 1
    jump city_map

label scene_mc_scarlett_coffee_shop_with_megan:
    $ have_to_meet_megan_at_coffee_shop = False
    scene black
    scene scarlett_s27_coffee01 with fade
    meg "I really like this coffee shop. It’s a nice place and the coffee is the best in the whole city."
    p "I have to agree with you there."
    scene scarlett_s27_coffee04
    p "I just want to say, about this morning... I just want to say, I’m..."
    scene scarlett_s27_coffee02
    meg "Stop."
    meg "I don’t want to talk about it. I don’t know what happened with me. Let's change the topic."
    p "Oh, okay. So what did those two want from you?"
    meg "That’s a long story, but, in short: in two days is the big volleyball tournament and those girls want to win. And they want to use my growing pills. You saw what they can do."
    scene scarlett_s27_coffee04
    p "(Hell yeah! And what “horny pills” do, as well.)"
    p "Yes, so they want bigger boobs?"
    scene scarlett_s27_coffee03
    meg "Haha! I think not. With bigger boobs, I cannot imagine how they'll even jump."
    meg "My new version of growing pills are now working a little differently. You can grow the parts you want - you just need to focus your mind on that."
    scene scarlett_s27_coffee04
    p "Woww! That’s a great improvement."
    meg "Yes... The old ones worked really weird. They had a longer effect than new ones though, because the new ones seem to work only for a few hours."
    p "So, were those the new ones, that we tested? Or were they the old ones?"
    meg "Nooo, these were the new ones - it's just that you thought about your boobs, hence the result."
    p "Yes... Well I was thinking about this. It’s true."
    p "And the reducing ones?"
    meg "They're still just reducing all body parts."
    p "Hmm...Interesting."
    scene scarlett_s27_coffee03
    meg "Yeah, tomorrow I will finally show my results to the Dean."
    p "And why are you doing all this? For her?"
    meg "It’s easy: for my career, of course. If these experiments are successful, she can give me a good recommendation for some big pharmaceutical company."
    p "Yes, that makes sense."
    scene scarlett_s27_coffee04
    p "So, good luck tomorow, Megan. It was nice talking with you. But I need to go. I already have something planned with Ivana and Sophia."
    scene scarlett_s27_coffee03
    meg "Of course. It was great to chat over coffee with you. Have a nice day!"
    scene city_map with fade
    p "Megan is so fine. Unfortunately Ivana and Sophia are probably already waiting for me at home."
    $ time_to_test_unlabelled_pills_on_ivana_n_sophia = True
    $ time_of_day = "AKŞAM"
    $ hints_counter += 1
    jump city_map

label scene_mc_scarlett_with_ivana_n_sophia_threesome:
    $ time_to_test_unlabelled_pills_on_ivana_n_sophia = False
    scene scarlett_s27_lesbian_threesome00
    p "Sorry. I’m a little late."
    sop "I think we can forgive you."
    scene scarlett_s27_lesbian_threesome01
    p "Thanks. So how will we do this?"
    scene scarlett_s27_lesbian_threesome02
    p "Here are all the pills that Megan made."
    sop "And one of them is my growing one?"
    iva "And why do they have different color lids?"
    p "To know which one is which, after we test them. When I was stealing them from the lab they were only marked as numbers like 00541054 and shit… "
    iva "Aah, okay, so?"
    p "I think the best thing we can do is each take a different pill and test that one, for accurate results."
    sop "Fine: I’m taking blue."
    iva "I want the red one."
    p "Cool, then mine is green."
    scene scarlett_s27_lesbian_threesome03
    p "Good luck, girls. Megan mentioned to me about the new growing pills, that after swallowing them, you just need to focus your mind on the part you want to make grow. Let’s do this all at once. 3... 2... 1..."
    scene scarlett_s27_lesbian_threesome04
    iva "I’m really curious about the effects..."
    sop "I think it’s working for me already. YES!"
    scene scarlett_s27_lesbian_threesome05
    sop "YES! I’m feeling it."
    scene scarlett_s27_lesbian_threesome06
    iva "That’s not fair, she always picks the right one!"
    scene scarlett_s27_lesbian_threesome07
    sop "Don’t be jealous and find those growing boobs ones. Yes, c'mon. I want them BIGGER again! Yes! BIGGER!"
    window hide
    #TODO dec need video transition image
    scene scarlett_s27_trans01 with dissolve
    scene scarlett_s27_trans02
    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_sophia_shrink.webm", loops=0, delay=-1, stop_music=False)
    #animation:scarlett_s28_sophia_shrink
    scene scarlett_s27_trans02
    $  renpy.pause(1.0)
    scene scarlett_s27_lesbian_threesome08 with fade
    iva "HAAAAAAHAAHAHAAAaaa!! OMG!!! HAHAHAAAA!!!!"
    scene scarlett_s27_lesbian_threesome09
    sop "Hey!!!! I may be smaller, but I can still punch you!!!"
    scene scarlett_s27_lesbian_threesome08
    iva "I’m so sorry, but … I can’t help it. HAhahaha!!! YES BIGGER!! Hahahaa!"
    sop "GRRRRR!!!"
    p "C'mon, girls, we still have two more pills to test."
    scene scarlett_s27_lesbian_threesome10
    p "And I’m feeling the heat here."
    iva "Just don’t go yelling bigger and bigger, please. 'Cause I can't handle it again. HAHA!"
    scene scarlett_s27_lesbian_threesome11
    p "Let’s see…."
    scene scarlett_s27_lesbian_threesome12
    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_scarlett_grow.webm", loops=0, delay=-1, stop_music=False)
    #animation scarlett_s28_scarlett_grow
    iva "Wooow! That was some crazy shit... Damn...! They are huge!"
    sop "Grrr…."
    iva "Do you think… I can touch them? You know, just to weigh them?"
    p "Of course, why not… Go ahead."
    scene scarlett_s27_lesbian_threesome13
    iva "OMG! They are really big and heavy!"
    scene scarlett_s27_lesbian_threesome14
    iva "It’s so cool touching them."
    sop "Hih. What is happening here?"
    iva "Do you think I ca…?"
    p "(Looks like that horny pill already started working.)"
    p "Of course. Do what you want…"
    scene scarlett_s27_lesbian_threesome15
    iva "Damn... I can't take my eyes off of them."
    scene scarlett_s27_lesbian_threesome16
    p "Wooow..."
    iva "I can't resist. I have to try these rock hard nipples."
    #TODO dec need video transition images
    scene scarlett_s27_trans03
    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_boobs_lick1.webm", loops=2, delay=-1, stop_music=False)
    #$ renpy.pause(2.0)

    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_boobs_lick2.webm", loops=-1, delay=2.05, stop_music=False)
    #animation scarlett_s28_boobs_lick1
    #animation scarlett_s28_boobs_lick2
    scene scarlett_s27_lesbian_threesome17
    p "Ooooufff... That’s a cool feeling. Keep going, Ivana."
    p "(Looks like Sophia has her own plan.)"
    scene black
    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_skirt1.webm", loops=0, delay=2.005, stop_music=False)
    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_skirt2.webm", loops=0, delay=2.005, stop_music=False)
    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_skirt3.webm", loops=0, delay=2.005, stop_music=False)
    scene scarlett_s27_lesbian_threesome18 with fade
    #animation scarlett_s28_skirt1
    #animation scarlett_s28_skirt2
    #animation scarlett_s28_skirt3

    sop "Hmm. What a nice tight pair of holes we have here."
    hide window
    scene scarlett_s27_lesbian_threesome20 with dissolve
    $ renpy.pause(1.0)

    sop "Damn, so soft…."
    scene scarlett_s27_lesbian_threesome19
    $ renpy.pause(1.0)
    sop "And nice spreading."
    scene scarlett_s27_lesbian_threesome21
    $ renpy.pause(1.0)

    iva "Hey Sophia, what are you waiting for?"
    scene scarlett_s27_lesbian_threesome22
    p "Looks like Ivana wants her fun, Sophia."
    scene scarlett_s27_lesbian_threesome23
    sop "Haha, let’s do this. Mmmmmpha..!"
    scene black
    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_fingering1_loop.webm", loops=3, delay=-1, stop_music=False)
    #animation: scarlett_s28_fingering1_loop
    scene scarlett_s27_lesbian_threesome21 with fade
    $ renpy.pause(1.5)

    iva "YES! Gimme more!"
    scene black
    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_fingering2_loop.webm", loops=2, delay=-1, stop_music=False)
    #animation scarlett_s28_fingering2_loop
    scene scarlett_s27_lesbian_threesome21
    iva "Awesome! Please use more fingers. Make me cum, Sophia!"
    scene black
    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_fingering_2finger.webm", loops=0, delay=-1, stop_music=False)
    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_fingering_2finger_loop.webm", loops=2, delay=-1, stop_music=False)
    #animation: scarlett_s28_fingering_2finger
    #animation: scarlett_s28_fingering_2finger_loop
    scene scarlett_s27_lesbian_threesome24 with fade
    $ renpy.pause(1.5)

    sop "Mmmm.. Your pussy tastes sooo good, Ivana."
    iva "Yeahhh? But now I want to taste yours."
    scene scarlett_s27_lesbian_threesome25
    sop "Really?"
    p "(Haha, Sophia cannot believe that Ivana said that. That horny pill is really powerful.)"
    scene scarlett_s27_lesbian_threesome26 with fade
    $ renpy.pause(1.5)

    sop "Damn!"
    iva "Mmmmmmm."
    scene scarlett_s27_lesbian_threesome27
    $ renpy.pause(1.0)

    sop "YES. I love what you're doing. AAaargh!!! LICK Meeeee!!"
    scene scarlett_s27_lesbian_threesome28 with dissolve
    $ renpy.pause(1.5)

    p "Ivana is really into this. She's doing it like a real lesbian. And it’s HOT as hell. It feels like Sophia's started shaking already."
    scene scarlett_s27_lesbian_threesome29 with dissolve
    $ renpy.pause(1.5)

    p "And she's shaking more and more."
    scene scarlett_s27_lesbian_threesome33
    $ renpy.pause(1.0)

    sop "AAAAAAAARGH!!!!!"
    scene scarlett_s27_lesbian_threesome32 with dissolve
    $ renpy.pause(1.5)
    sop "FUUUUCK!!!! YOU FUCKING BITCH!!! YEEES!"
    p "Keep going, Ivana! Shes cumming hard!"
    scene scarlett_s27_lesbian_threesome31 with dissolve
    $ renpy.pause(1.5)

    sop "MY GOOOOODDD!!! AAAAAAH!"
    p "Damn, I almost can't hold her, the way she's shaking."
    hide window
    scene scarlett_s27_lesbian_threesome30 with dissolve
    $ renpy.pause(1.5)

    iva "Mmmmaaaaaah!"
    sop "AAAaaaaa!"
    window hide
    scene scarlett_s27_lesbian_threesome35 with dissolve
    $ renpy.pause(1.0)
    iva "Hahah... That was really fun. Damn! I LOVE IT!"
    hide window
    $ renpy.pause(0.5)

    scene scarlett_s27_lesbian_threesome34 with dissolve
    $ renpy.pause(1.0)

    iva "And your cum is delicious, Sophia.  Mmmmm… I can't get enough of it."
    sop "Aaaaah….."
    p "She looks like she's almost dead now, haha."
    sop "Now it's your turn, girls. Let me show you my skills."
    scene scarlett_s27_lesbian_threesome36 with fade
    $ renpy.pause(1.5)

    sop "And poke those asses as high up as you can!"
    scene scarlett_s27_lesbian_threesome38
    $ renpy.pause(0.5)

    iva "Scarlett, that’s awesome. I love you both..."
    scene scarlett_s27_lesbian_threesome37
    $ renpy.pause(1.0)

    p "(She is absolutely out of her mind.)"
    p "I love you too, honey!"
    scene scarlett_s27_lesbian_threesome39
    sop "Stop talking, girls... Fun is coming."
    scene scarlett_s27_lesbian_threesome40 with fade
    $ renpy.pause(1.5)

    sop "Aaah, my pussy's still dripping like crazy. Damn you, Ivana. You made me feel, like no one else. Now I will return the favor."
    scene scarlett_s27_lesbian_threesome41 with dissolve
    $ renpy.pause(1.0)

    p "Mmmm."
    scene scarlett_s27_lesbian_threesome49 with dissolve
    $ renpy.pause(1.0)

    p "(Sophia is really skilled at fingering, but what do I know - I’ve only been a female for just a few days now.)"
    scene scarlett_s27_lesbian_threesome42
    $ renpy.pause(0.5)

    p "(Ivana looks really surprised.)"
    iva "Ouuuuh, that’s so good."
    scene scarlett_s27_lesbian_threesome45
    $ renpy.pause(0.5)
    sop "Can you handle more fingers, Ivana?"
    scene scarlett_s27_lesbian_threesome38
    iva "Yeees, please give me more. More fingers!"
    hide window
    scene scarlett_s27_lesbian_threesome49
    with fade
    scene scarlett_s27_lesbian_threesome45
    with dissolve
    scene scarlett_s27_lesbian_threesome47
    with dissolve
    scene scarlett_s27_lesbian_threesome46
    with dissolve
    scene scarlett_s27_lesbian_threesome43
    with dissolve
    $ renpy.pause(1.0)
    scene scarlett_s27_lesbian_threesome48
    $ renpy.pause(0.5)

    iva "OMG!!!!!"
    sop "Haha! She took my whole hand like it's nothing! What a hungry SLUT you are, Ivana."
    p "DAMN?! The whole hand?! "
    iva "FUCK ME, FOR GOD'S SAKE!!! HARD!!!"
    scene scarlett_s27_lesbian_threesome44 with fade
    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_fisting.webm", loops=2, delay=-1, stop_music=False)
    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_fisting_face.webm", loops=0, delay=-1, stop_music=False)
    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_fisting.webm", loops=1, delay=-1, stop_music=False)
    $ renpy.movie_cutscene("scenes/Scarlett/28_pills_test_threesome/WEBM/scarlett_s28_fisting_face.webm", loops=0, delay=-1, stop_music=False)
    #animation: scarlett_s28_fisting
    #animation: scarlett_s28_fisting_face
    scene scarlett_s27_lesbian_threesome44
    with dissolve
    iva "AAAAAH....!!! AAAAAAAAAAHH!"
    sop "Here she comes!!!"
    window hide
    scene scarlett_s27_lesbian_threesome50 with vpunch
    scene scarlett_s27_lesbian_threesome51
    with dissolve
    $ renpy.pause(2.0)
    sop "FUUUCK, That’s one huge fucking SQUIRT!"
    iva "AAaaaiiiii !!!!"
    p "DAMN!!"
    iva "AAaaAAaa  Hhhh AAAA !!!"
    scene scarlett_s27_lesbian_threesome52
    iva "Aaarghhhhh.."
    p "Damn, she's shaking like a drilling machine. And her pussy is dripping all over the floor, staying wide open."
    scene scarlett_s27_lesbian_threesome53
    iva "Vrrrrrr... mmmmmmm…."
    scene scarlett_s27_lesbian_threesome54 with fade
    iva "OMG… My best orgasm ever. I love you girls! I LOVE YOU!"
    scene scarlett_s27_lesbian_threesome55 with fade
    $ renpy.pause(1.5)

    sop "That was some great fun."
    iva "I must agree."
    sop "So now we know which pills are which... What will we do next?"
    iva "We can change Brooke's pills for the shrinking ones, and then beat them easily. And maybe after the game, punish them hard, like fuck them or something… Mmmmmm."
    p "(Haha! Ivana is still under the effect of that pill.)"
    p "Haha, that sounds like a plan! So, I'll meet with Megan tomorrow morning, before she gives the growing pills to the Dean. And I will swap them with the shrinking ones."
    sop "That would be great."
    iva "Haha! I cannot wait to fuck them. By the way, how about another round..?"
    p "Oooh..!"
    sop "Sorry, you slutty lady, but I’m done."
    p "I'll go take a shower."
    iva "Aaah, what a waste..."
    $ time_of_day = "GECE"
    $ mc_scarlett_needs_shower_after_threesome = True
    $ hints_counter += 1
    jump apartment_map

label scene_mc_scarlett_taking_shower_in_apartment_after_threesome:
    $ mc_scarlett_needs_shower_after_threesome = False
    scene black
    scene scarlett_s29_shower01 with fade
    $ renpy.pause(0.0)
    p "A shower is always great."
    scene scarlett_s29_shower02 with dissolve
    $ renpy.pause(0.0)
    p "and refreshing..."
    scene scarlett_s29_shower03 with fade
    $ renpy.pause(0.0)

    p "Mmmm... With boobs like these, I could play with them all day long."
    scene scarlett_s29_shower04 with dissolve
    $ renpy.pause(0.0)
    p "So big and firm."
    scene scarlett_s29_shower05 with dissolve
    $ renpy.pause()
    scene scarlett_s29_shower06 with dissolve
    $ renpy.pause()
    scene scarlett_s29_shower07 with dissolve
    $ renpy.pause()
    scene scarlett_s29_shower08 with dissolve
    $ renpy.pause()

    p "I really can't stop touching them, but I’m getting exhausted already. The whole testing thing really wore me out."
    $ hints_counter += 1
    $ need_to_hide_pills_after_threesome = True
    jump mc_room

label scene_mc_scarlett_hiding_pills_behind_bedside_cabinet:
    $ need_to_hide_pills_after_threesome = False
    scene scarlett_s29_shower09
    p "The pills should be in a safe place, behind this cabinet."
    $ waking_up_in_the_morning_after_threesome = True
    $ have_used_sex_toy_that_night_as_scarlett = True
    jump skip_to_sleep


label scene_leaving_apartment_morning_after_threesome:
    $ mc_scarlett_leaving_apartment_morning_after_threesome = False
    scene apartment
    scene scarlett_s30_meet_megan_at_deans00 with fade
    sop "Hey, Scar... Good luck."
    p "Hehe, don’t worry."
    scene city_map with fade
    p "Megan has a meeting today, to show the Dean her results. That's probably where I'll find her."
    $ need_to_meet_meg_in_deans_office_after_threesome = True
    jump city_map

label scene_mc_scarlett_meet_megan_in_deans_after_threesome:
    $ need_to_meet_meg_in_deans_office_after_threesome = False
    scene school_map
    scene scarlett_s30_meet_megan_at_deans01 with fade
    p "Hello, Megan."
    scene scarlett_s30_meet_megan_at_deans04
    $ renpy.pause(0.5)

    meg "Oh. Hi, Scarlett, what are you doing here?"
    scene scarlett_s30_meet_megan_at_deans01
    p "Just wanted to see you."
    meg "Hmm. We are just friends, right?"
    p "Of course. I’m just here to tell you: good luck with your presentation."
    scene black
    scene scarlett_s30_meet_megan_at_deans03 with dissolve
    $ renpy.pause(1.5)

    meg "Ah, yes, that’s nice of you. Look at them. All these months of work, in this little jar."
    p "Aaaaahhh... Yes!"
    scene scarlett_s30_meet_megan_at_deans02
    p "(FUCK me in the ass! They are another color!)"
    scene scarlett_s30_meet_megan_at_deans03
    p "Weren’t they blue before?"
    meg "Yes, but I colorized them during the night. Looks better than the blue color, doesn't it ?"
    p "Aaaah... yeah, definitelly."
    meg "Sorry, I must go. The Dean is always upset if someone arrives late."
    p "Sure! GOOD LUCK, Meg!"
    scene scarlett_s30_meet_megan_at_deans06 with fade
    $ renpy.pause(1.0)

    p "(FUCK! What will we do now?)"
    p "(I need to find Sophia and tell her about it. She should have computer class, right about now, if I recall.)"
    $ need_to_tell_sophia_about_pills_colour_change = True
    $ hints_counter += 1
    jump school

label scene_finding_sophia_and_telling_her_about_pills_colour_change:
    $ need_to_tell_sophia_about_pills_colour_change = False
    scene black
    scene scarlett_s31_computer_sophia01 with fade
    sop "Damn, how is this stupid program supposed to work..."
    p "Hey.. Sophia."
    scene scarlett_s31_computer_sophia02
    sop "Scarlett, what are you doing here?"
    p "We have a problem with the pills."
    sop "What problem?"
    p "Megan changed the color of the pills last night. Now they are pink... So, I cannot switch them anymore..."
    sop "Shit. That sounds like a big problem. "
    p "What will we do?"
    scene scarlett_s31_computer_sophia03
    sop "What are you doing after school? How about some shopping?"
    p "What?? We have a serious problem, here!"
    sop "I know. But everytime I have a problem I have to go shopping. It helps me. And after I clear my head, sometimes I get a good idea."
    p "Eeeh... okay. Why don’t you go with Ivana?"
    sop "Because she is going to the beach today. And after yesterday... I don’t know why, but she is a little upset."
    p "Aah..."
    p "(Looks like Ivana is a little disoriented -same as Megan- after using the horny pills. She definitely liked it, but she must know something was wrong.)"
    scene scarlett_s31_computer_sophia04
    bab "Ehm, girls, this is a classroom, not a union discussion."
    sop "Oh... shit."
    bab "I don’t remember you being in any of my classes..."
    p "Of course I am, Mrs. Baber. I’m just helping out Sophia with this problem."
    bab "Really? So what is the problem we are having right now?"
    sop "Sshhh..."
    p "Right now..? We are working with layers and transitions in photoshop. I know it pretty well. For this scene we have to …….  …… . … "
    scene black with fade
    "3 minutes later..."
    scene scarlett_s31_computer_sophia06
    bab "Wow. I’m really surprised - in a good way. I didn’t expect that. Looks like you really know your stuff. So, continue, but just a little more quietly."
    scene scarlett_s31_computer_sophia03
    sop "Damn... You handled that well."
    p "So..?"
    sop "So after school, at the shopping centre?"
    p "Okay."

    scene school_map
    p "(Hah, shopping! I don’t even have any money for shopping!)"
    p "(I think that's Ivana heading out of the school. I will try and talk with her.)"
    $ time_to_see_ivana_after_threesome_outside_school = True
    $ hints_counter += 1
    jump school


label scene_mc_scarlett_leaving_school_after_seeing_meg_in_deans_office:
    $ time_to_see_ivana_after_threesome_outside_school = False
    scene scarlett_s32_leaving_school01
    p "Hey Ivana! Got a minute?"
    scene scarlett_s32_leaving_school02
    $ renpy.pause(0.5)

    iva "Hi, Scarlett? What do you need?"
    p "I just want to talk with you for a bit."
    hide window
    scene scarlett_s32_leaving_school03 with dissolve
    $ renpy.pause(1.0)
    iva "You don't want to talk about yesterday, right?"
    p "Eeeh?? No..?"
    iva "So?"
    p "I need to talk about the problem we have with the pills now."
    scene scarlett_s32_leaving_school02 with dissolve
    $ renpy.pause(1.0)

    iva "What problem?"
    p "It’s a long story. We need to think about another plan."
    p "Sophia told me that she wants to go shopping. Do you want to come with us? We can talk about this issue."
    hide window
    show black
    scene scarlett_s32_leaving_school04 with dissolve
    iva "Hah! Sophia and her “shopping”. You know, looking at and testing many clothes and boots is not shopping. She never buys anything."
    p "(Cool, so I don’t need any money.)"
    show black
    scene scarlett_s32_leaving_school02 with dissolve
    iva "Sorry. I'm going to the beach. I have a new swimsuit I want to test out today. "
    iva "But, you can come with me. And we can discuss a new plan this evening."
    p "Cool, just like yesterday."
    scene scarlett_s32_leaving_school03 with dissolve
    $ renpy.pause(1.0)

    iva "No! Not like yesterday. Just a normal discussion."
    p "Of course. Sorry."
    scene scarlett_s32_leaving_school02 with dissolve
    $ renpy.pause(1.0)

    iva "I should go now. If you want, come find me on the beach. I know a good place where almost nobody goes."
    p "Okay."

    scene city_map
    p "Aaah, so now I have three options: I can go with Ivana to the beach or with Sophia to the shopping centre or to Anders' office to fix Scarlett’s problems - but I’m really scared of what he wants to do."
    p "Maybe I could convince Ivana to fix this problem, instead?"
    $ time_for_afternoon_choices_after_pills_colouring = True
    $ time_of_day = "ÖĞLEN"
    $ hints_counter += 1
    jump city_map

label scene_one_of_three_coffee_shop:
    $ toggle_mc_scarlett_chose_sophia = True
    scene black
    scene scarlett_s34_shopping_with_sophia01 with fade
    sop "Did you go shopping during your travels in Europe?"
    p "(Oh, which place in Europe is famous for good fashion?)"
    p "Yes, of course. Especially in Paris."
    scene scarlett_s34_shopping_with_sophia02
    sop "Damn. Paris. That's my dream. I found this little shop here. It’s smaller, but they have some of the most recent trends in fashion."
    p "Great."
    scene scarlett_s34_shopping_with_sophia03
    sop "We're here. What do you think?"
    scene scarlett_s34_shopping_with_sophia04
    p "(It’s like a man's worst nightmare, but maybe in a female skin, I can enjoy this too?)"
    p "I must say, damn there are some pretty interesting clothes."
    sop "Cool. So take one you like and go to the changing room. I’m excited to see you in one of these."
    p "Okay."
    scene black with fade
    "5 minutes later..."
    scene scarlett_s34_shopping_with_sophia05
    p "So, what do you think?"
    sop "I think it suits you quite well."
    p "Yeah. It’s really comfortable."
    scene scarlett_s34_shopping_with_sophia07
    $ renpy.pause()

    scene scarlett_s34_shopping_with_sophia08
    sop "Now it's my turn."
    scene scarlett_s34_shopping_with_sophia09
    p "Hmmm."
    scene scarlett_s34_shopping_with_sophia10
    sop "Tadaaaa."
    p "Hah, kitty."
    p "(She looks really fuckable in that teenage costume.)"
    scene scarlett_s34_shopping_with_sophia11
    $ renpy.pause()

    scene scarlett_s34_shopping_with_sophia13
    $ renpy.pause()

    scene scarlett_s34_shopping_with_sophia12
    sop "Sexy enough?"
    p "Hmm, yes, but I think you can do better."
    sop "You can bet your ass on it."
    scene scarlett_s34_shopping_with_sophia14
    $ renpy.pause()

    scene scarlett_s34_shopping_with_sophia15
    $ renpy.pause()

    scene scarlett_s34_shopping_with_sophia19
    $ renpy.pause()

    p "(That short skirt is driving me crazy.)"
    scene scarlett_s34_shopping_with_sophia16
    $ renpy.pause()

    scene scarlett_s34_shopping_with_sophia17
    sop "Bleeh. This you cannot beat."
    p "Do you really think so?"
    scene scarlett_s34_shopping_with_sophia18
    sop "Miaauw. Show me, honey."
    scene scarlett_s34_shopping_with_sophia20
    p "I can't beat you?!"
    scene scarlett_s34_shopping_with_sophia21
    sop "HEY!"
    scene scarlett_s34_shopping_with_sophia22
    sop "That’s not fair! You used a pill."
    scene scarlett_s34_shopping_with_sophia23
    p "Yes. Haha, but only half of one. I have the second half here for you."
    scene scarlett_s34_shopping_with_sophia24
    sop "Good girl."
    p "Does this mean I am the winner?"
    sop "We will see."
    scene scarlett_s34_shopping_with_sophia25
    sop "Hmm. Now we can compare who's sexier."
    scene scarlett_s34_shopping_with_sophia26
    $ renpy.pause()

    scene scarlett_s34_shopping_with_sophia27
    sop "Come here. I want to kiss you again."
    brst "Girls, please, can you stop hogging the stalls. There are other customers waiting."
    scene scarlett_s34_shopping_with_sophia29
    p "Oooh."
    scene scarlett_s34_shopping_with_sophia28
    sop "Of course. We're sorry. Just a moment."
    sop "Let’s go home. We need to talk to Ivana about our plan."

    scene city_map
    p "(That was not a bad way to spend the afternoon, with Sophia. Shopping was good fun actually.)"
    #interaction to apartment and living room
    #and to girls
    $ time_for_afternoon_choices_after_pills_colouring = False
    $ time_to_meet_up_with_ivana_n_sophia_after_choices_afternoon = True
    $ time_of_day = "AKŞAM"
    $ hints_counter += 1
    jump city_map



label scene_one_of_three_beach:
    $ toggle_mc_scarlett_chose_ivana = True
    scene black
    scene scarlett_s33_beach02 with fade
    p "Hmm, looks like nobody's here?"
    scene scarlett_s33_beach01
    iva "Hey, Scarlett! Over here!"
    scene scarlett_s33_beach03
    iva "So you decided to join me at the beach..."
    p "Haha, yes. I just wanted to see that new swimsuit you have. Pretty damn nice."
    iva "Thank you!"
    iva "Do you want to put some sunscreen lotion on my back?"
    scene scarlett_s33_beach04
    p "Do you think I can?"
    iva "Stop joking around. Of course you can."
    p "Okay."
    scene scarlett_s33_beach05
    iva "You know, I’m not upset, like Sophia thinks…"
    p "Just lost, right?"
    iva "Yes, that's the right word. You know it was damn great, but I know that it wasn’t me. On the other hand, maybe I will want to try it again. And that thought scares me a little."
    scene scarlett_s33_beach06
    p "(Heh, I know the feeling. I’m a guy in a female body. This is all new to me.)"
    p "Don’t worry, I know what you're feeling."
    scene scarlett_s33_beach08
    p "(I think that right now is a good time to ask her.)"
    p "Can I ask you what you think about Mr. Anders?"
    scene scarlett_s33_beach09
    iva "What I think? I don’t want to talk about what you've done to me and him."
    scene scarlett_s33_beach08
    p "No no, just wanted to know if you like him or not."
    scene scarlett_s33_beach07
    iva "Hmm... To be honest, I like him a lot. He looks so manly and strong. But after buying my photos from you..."
    scene scarlett_s33_beach10
    p "Sorry, Ivana. I know it was a bad thing I did. All of that was my fault..."
    iva "Apology accepted."
    p "I’m just asking because he doesn’t want to pass me this year, in Biology."
    scene scarlett_s33_beach09
    iva "Hah! And you wanted me to go fuck him, right?"
    p "Of course not. But... maybe you can just, talk to him?"
    iva "I'll think about it, okay?"
    scene scarlett_s33_beach07
    p "Cool. You are the greatest!"
    iva "I know. Now, let me work on ma tan, haha."
    scene scarlett_s33_beach11
    $ renpy.pause()

    scene scarlett_s33_beach12
    $ renpy.pause()

    scene scarlett_s33_beach13
    $ renpy.pause()

    scene scarlett_s33_beach14
    $ renpy.pause()


    scene city_map
    p "That was a nice day on the beach, with Ivana. Looking at her body, covered in lotion, was hotter than the Sun itself."
    p "Now we have a meeting in our living room."
    $ time_for_afternoon_choices_after_pills_colouring = False
    $ time_to_meet_up_with_ivana_n_sophia_after_choices_afternoon = True
    $ hints_counter += 1
    $ time_of_day = "AKŞAM"
    jump city_map
    #interaction on apartment and living room

label scene_one_of_three_anders_office:
    scene black
    scene scarlett_s37_used_by_anders01 with fade
    andr "Hi, Scarlett. What a surprise!"
    p "(I’m surprised too, that I’m actually here...)"
    scene scarlett_s37_used_by_anders02
    p "I’m here to have a talk about my grade, to pass to next year."
    andr "Of course. I know why you're here."
    scene scarlett_s37_used_by_anders04
    andr "I told you, we will talk 'deeply' about your problem."
    scene scarlett_s37_used_by_anders03
    p "Ah, yes... deeply. Heh. I think It would be better if I just go."
    scene scarlett_s37_used_by_anders05
    andr "I think the better choice, would be to stay here. You know you have a big problem. And I really want to help you. But you need to LET me help you."
    scene scarlett_s37_used_by_anders06
    andr "So tell me: do you need my help or not?"
    menu:
        "NO":
            p "I think I will find some way to get help myself."
            andr "As you wish. But, you know, this deal ends here. Now get your ass out of my office."
            scene school_map
            p "(OMG, what a freak.)"
            p "(Argghh. I was really scared of him.)"
            p "(Aaah. I need to start thinking about other things. I could still see Ivana at the beach or catch Sophia at the shops.)"
            $ mc_scarlett_refused_anders_offer_for_scarlett_help = True
            jump school
        "YES":
            $ have_accepted_anders_offer_for_scarlett_help = True
            p "*GULP* Yes. I need your help."
            andr "Great! Just give me a second..."
            scene scarlett_s37_used_by_anders08
            $ renpy.pause(2.0)

            scene scarlett_s37_used_by_anders07
            andr "Now the fun starts."
            scene black with fade
            "After 5 minutes..."
            scene scarlett_s37_used_by_anders09
            andr "Perfection! What do you say to this? Is it comfortable?"
            scene scarlett_s37_used_by_anders10
            p "Mmmhhm! Hmhhh! Mm!!!"
            andr "Sorry for the mouth tape, but I wouldn't want anyone to hear you screaming in here. Except me, just a little, haha."
            scene scarlett_s37_used_by_anders11
            andr "Now, let's begin, shall we?"
            scene scarlett_s37_used_by_anders12
            andr "Hold your breath."
            scene scarlett_s37_used_by_anders13
            andr "After this, you'll never think about blackmailing anybody again."
            scene black with fade
            play sound sound_whipping
            scene scarlett_s37_used_by_anders14
            $ renpy.pause(2.0)

            #(scream sound)#TODO dec
            scene scarlett_s37_used_by_anders15 with dissolve
            p "(SHIIIITT!!!!!!)"
            scene scarlett_s37_used_by_anders12
            andr "Now it’s absolute perfection."
            scene scarlett_s37_used_by_anders16
            d "Haha. I see you are both having fun."
            scene scarlett_s37_used_by_anders18
            p "Fun?!"
            scene scarlett_s37_used_by_anders17
            d "You're not enjoing this? Haha."
            scene scarlett_s37_used_by_anders18
            p "WHAT?!! Are you kidding?! Look at me!"
            scene scarlett_s37_used_by_anders19
            d "Yes, I see. Damn, that is some pretty damn good work with that whip. That guy is a real master."
            scene scarlett_s37_used_by_anders20
            p "HEY! I thought you were here to help me. Not adoring this whip art he created on my ASS!"
            scene scarlett_s37_used_by_anders19
            d "Just take it easy. Of course, I’m here to help you."
            d "But you know what I can do? You are doing this of your own free will, and I cannot change his mind. Maybe you just liked it and wanted more, hmm?"
            scene scarlett_s37_used_by_anders21
            d "Were it me in this situation, just looking at this piece of art on your ass, I would definitely be into it. If I were in your shoes, I would want to be his nasty little schoolgirl every day. Damn, he is so great. He can punish me like he wants, anytime."
            scene scarlett_s37_used_by_anders20
            p "Are you serious?!"
            menu:
                "What do I want to do?"
                "Let the Devil give you a litle help.":
                    $ mc_scarlett_accepted_devils_help_with_anders = True
                    scene scarlett_s37_used_by_anders25
                    d "Shs hs hs s hs shshsssshhshs."
                    scene scarlett_s37_used_by_anders22
                    d "And that’s that. Have a good time. Hihi."
                    scene scarlett_s37_used_by_anders23
                    andr "For today, the lesson has ended. Next time we''ll maybe step it up to another level."
                    scene scarlett_s37_used_by_anders24
                    p "What?! Next lesson? I will never meet you here again!"
                    andr "Oh, really? I think you will, If you want to pass my class."
                    p "But..."
                    andr "But what? The fun hasn’t ended yet. Now take your clothes and get your ass out of my office."
                    scene city_map
                    p "(That fucking pervert! He used me and is still continuing with blackmailing me!)"
                    p "(Arrrgh…  Fine, it’s time to go home. I need to talk with the girls about our plan.)"
                    $ time_for_afternoon_choices_after_pills_colouring = False
                    $ time_to_meet_up_with_ivana_n_sophia_after_choices_afternoon = True
                    $ hints_counter += 1
                    $ time_of_day = "AKŞAM"
                    jump city_map

                "Let Anders continue.":
                    scene scarlett_s37_used_by_anders25
                    d "Shs hs hs s hs shshsssshhshs"
                    scene scarlett_s37_used_by_anders12
                    andr "I have a surprise for you. Just give me a moment."
                    scene scarlett_s37_used_by_anders26
                    p "Oh, FUCK!"
                    scene scarlett_s37_used_by_anders29
                    andr "Haha! Wow, these pills are a miracle. My hands are huge now.  Haha, everything on me, is huge now."
                    scene scarlett_s37_used_by_anders26
                    p "(I’m in deep shit right now!)"
                    scene scarlett_s37_used_by_anders27
                    andr "Haha. I’m curious how this will fit into you, you little slut!"
                    scene scarlett_s37_used_by_anders28
                    p "*GULP*"
                    scene scarlett_s37_used_by_anders30
                    andr "You can say goodbye to your small tight pussy. Just wait 'til I spread you wide with this rod."
                    scene scarlett_s37_used_by_anders31
                    p "Aaaaaahh!! Ahhhh!!!  FUCK! It’s too big!"
                    scene scarlett_s37_used_by_anders32
                    andr "Yeeees! Aah! Sooo tight! I love it!"
                    scene scarlett_s37_used_by_anders33
                    andr "Yes! Deeper and deeeper."
                    scene scarlett_s37_used_by_anders34
                    andr "Mmmmmm..."
                    scene scarlett_s37_used_by_anders31
                    p "Ohhh…. It’s too deep. My God, it’s like a whole hand!"
                    scene scarlett_s37_used_by_anders35
                    andr "This, we'll not need anymore."
                    scene scarlett_s37_used_by_anders36
                    andr "Haha, looks like you are starting to enjoy this huge cock, you little SLUT!"
                    andr "I will give you every last inch of it, don’t worry."
                    scene scarlett_s37_used_by_anders37
                    andr "Yeaah, that’s it!"
                    scene scarlett_s37_used_by_anders38
                    p "(OMG, I cannot even think about anything. He's literally tearing this pussy apart.)"
                    p "Aaaaah..."
                    scene scarlett_s37_used_by_anders39
                    p "(Damn, I think I'm actually starting to like it….)"
                    andr "Mmmmmmm. That’s your real punishment!"
                    scene scarlett_s37_used_by_anders40
                    andr "I think I will cum sooon... YES!"

                    menu:
                        "Please cum on my whipped ass.":
                            p "Please cum on my whipped ass."
                            scene scarlett_s37_used_by_anders47 with fade
                            $ renpy.pause(0.5)

                            scene scarlett_s37_used_by_anders48
                            andr "Hah, that was a nice lesson. Next time we'll try other things."
                            p "But..?"
                            andr "Haha, did you think that I would let you pass, just because of one meeting? Nonono, you are so naive. Now take your clothes and get your ass out my office!"

                        "Please, not yet, I have one hole left.":
                            scene scarlett_s37_used_by_anders42 with fade
                            andr "FUCK you are SUCH a SLUT! Now your ass is mine..."
                            p "AArghh… It’s like jumping on a pole. I’m cumming!!!"
                            scene scarlett_s37_used_by_anders42
                            p "AAAAaaaaah!!!"
                            scene scarlett_s37_used_by_anders41 with dissolve
                            $ renpy.pause(1.0)
                            scene scarlett_s37_used_by_anders43 with dissolve
                            andr "I’m cumming toooooo."

                            menu:
                                "Yes, cum inside!":

                                    p "Yes, cum inside!"
                                    scene scarlett_s37_used_by_anders46 with fade
                                    andr "Aaaargh…."
                                    p "Oh God, it’s like a big flood inside of me."
                                    scene scarlett_s37_used_by_anders50 with fade
                                    p "So I will pass now?"
                                    andr "Haha. No way! For one good fuck? Haha, you are such a naive bitch. Now take your clothes and get your ass out my door."
                                "Please show me that giant cock.":
                                    p "Please show me that giant cock."
                                    scene scarlett_s37_used_by_anders44
                                    $ renpy.pause(2.0, hard=True)
                                    andr "Take it! Every last drop, you bitch!"
                                    scene scarlett_s37_used_by_anders45
                                    $ renpy.pause(1.0, hard=True)
                                    p "So I will pass now?"
                                    hide window
                                    scene scarlett_s37_used_by_anders49 with dissolve
                                    andr "Haha! No way! For one good fuck? Haha you are such a naive bitch. Now take your clothes and get your ass out my door."

                    scene city_map with fade
                    p "(What a bastard. I gave him everything and he just used me like a slut. That’s unfair!)"
                    p "(Argghhh!!)"
                    p "(I’m so angry right now… But I must go home. I need to talk to the girls about our plan.)"
                    $ time_for_afternoon_choices_after_pills_colouring = False
                    $ time_to_meet_up_with_ivana_n_sophia_after_choices_afternoon = True
                    $ hints_counter += 1
                    $ time_of_day = "AKŞAM"
                    jump city_map

label scene_meet_up_with_ivana_n_sophia_after_choices_afternoon:
    scene livingroom_main
    show livingroom_button_girls

    if time_to_sleep_after_choices_afternoon:
        p "I'll leave them to it. I need to get some sleep."
        jump living_room
    elif mc_scarlett_needs_shower_after_threesome:
        p "I'll leave them to it. I need to shower."
        jump living_room
    $ time_to_meet_up_with_ivana_n_sophia_after_choices_afternoon = False

    scene scarlett_s35_plan_talking05
    p "I’m here. We can start now."
    sop "Sure. Why don't you sit here."
    if have_accepted_anders_offer_for_scarlett_help:
        scene scarlett_s35_plan_talking06
        p "Ahh... it’s okay, I will stand for a while."
        scene scarlett_s35_plan_talking05 with fade
        #iva "How will we do it?"
        #sop "I was thinking about it, but if the pills have another color, we can't change them anymore."
        #iva "That’s a pity, just think about it. Those two small sluts being punished. Aaah."
        #JUMP TO CONTINUES
    elif not have_accepted_anders_offer_for_scarlett_help:
        scene scarlett_s35_plan_talking01 with fade
    iva "How will we do it?"
    sop "I was thinking about that, but if the pills have another colour, we can't switch them anymore."
    iva "That’s a pity. Just thinking about those two little sluts and punishing them... Aaah..."
        #CONTINUES
    scene black with dissolve
    $ renpy.pause(0.1, hard=True)
    scene scarlett_s36_dreaming05 with dissolve
    p "Deeper!"
    scene scarlett_s36_dreaming04
    p "I said deeper! To this purple bit. You are useless."
    scene scarlett_s36_dreaming06
    p "Brooke, get your ass over here. She is incompetent. I want to see you taking it up to this purple part."
    scene scarlett_s36_dreaming02
    p "C'mon you bitch - just a few more inches. You have such a big mouth when you're talking shit around campus. So, show it to me, right now!"
    scene scarlett_s36_dreaming01
    p "I said to the purple!"
    scene scarlett_s36_dreaming03
    p "Looks like you are both useless. So we need to go for some real punishment. Beth, on your knees. And you, spread her ass wide!"
    scene scarlett_s36_dreaming08
    p "Yeeees! That’s what you deserve!"
    scene scarlett_s36_dreaming09
    p "Yeah, that’s damn good fun. Keep her ass cheeks spread."
    scene scarlett_s36_dreaming07
    beth "Aaaahhh……"
    p "Now's your turn, Brooke."
    scene scarlett_s36_dreaming10
    p "Yeah, take it, balls-deep, you slut."
    scene scarlett_s36_dreaming11
    brook "Aaah, it’s too much!!"
    p "SHUT UP and take it DEEPER!"
    scene scarlett_s36_dreaming12
    brook "AaaaaH!"
    sop "Hey Scarlett! What do you think?"
    p "Deeper!"
    iva "What?"
    sop "Hey Scarlett!"
    scene scarlett_s35_plan_talking02 with dissolve
    p "Uh…"
    p "(DAMN... that was one awesome dream...)"
    scene scarlett_s35_plan_talking03
    sop "So what do you think? Is it a good idea?"
    scene scarlett_s35_plan_talking01
    p "Eeh, can you please explain it to me once again?"
    scene scarlett_s35_plan_talking04
    iva "It’s easy. There aren't that many competitive teams, so we should be playing against Brooke in the final anyway. And before the final, there's always a little breather break ..."
    iva "So, if you find her locker room and maybe throw some reducing pills in their drinks, they will get smaller by the time the final starts."
    scene scarlett_s35_plan_talking02
    p "Hmm, that sounds good, but we will not be using reducing pills."
    iva "Then which ones will we use?"
    p "Because if we use shrinking ones, Megan will still have a problem with those girls. But if we use horny pills, they'll still be bigger and taller, but their minds will be on other things, rather than the game. So, easy win. And Megan will be safe."
    scene scarlett_s35_plan_talking04
    iva "Haha, you are so clever!"
    scene scarlett_s35_plan_talking03
    sop "Hihi, I’m so excited. I don't think I can wait 'till morning."
    scene scarlett_s35_plan_talking01
    p "Ok, then. I will do it during the break before the finals. Now I’m really ready for bed. Good night, girls."
    $ time_to_sleep_after_choices_afternoon = True
    $ time_of_day = "GECE"
    $ hints_counter += 1
    jump living_room


label scene_girls_playing_volleyball_at_gym_again:
    scene scarlett_s38_volleyball_game01
    p "Tournament is in full swing now."
    scene scarlett_s38_volleyball_game02
    p "I was never really into volleyball."
    scene scarlett_s38_volleyball_game03
    p "But I must admit, some of the chicks playing here are hot stuff."
    scene scarlett_s38_volleyball_game04
    $ renpy.pause(2.0)

    scene scarlett_s38_volleyball_game05
    p "Sometimes winning."
    scene scarlett_s38_volleyball_game06
    p "Other times losing."
    scene scarlett_s38_volleyball_game08
    $ renpy.pause(1.0)

    p "There's Beth. Inspecting the other players. “Bad girls”? Hah, yes they are."
    p "I see Sophia was right. Brooke and Bethany have about the same point count as Ivana and Sophia. Both teams will be in the final. So, time to find Beth and Brooke’s locker room."
    scene sportshall_background with fade
    p "Okay. I need to find out which locker room is Beth and Brooke's."
    $ hints_counter += 1
    $ time_to_punish_beth_n_brooke_in_sports_hall = False
    jump gym_map


label scene_sneak_into_bad_girls_locker_room:
    scene scarlett_s39_change01
    p "Okay. Quickly and quietly sneak inside..."
    scene scarlett_s39_change02
    andr "Ehem. What are you doing here, Scarlett?"
    p "(FUCK!!)"
    scene scarlett_s39_change03
    p "Eeeh, hello, Mr. Anders… I’m just looking for the toilets?"
    andr "Yeah? And where did you get those master keys?"
    andr "What’s going on here?"
    scene scarlett_s39_change04
    p "Eeeh…"
    p "(I have only one chance.)"
    scene scarlett_s39_change10
    p "MmmmmMmmm."
    scene scarlett_s39_change10
    $ renpy.pause(1.0)

    scene scarlett_s39_change11  with dissolve
    $ renpy.pause(2.0)
    scene scarlett_s39_change12 with dissolve
    $ renpy.pause(2.0)
    scene scarlett_s39_change11 with dissolve
    $ renpy.pause(0.3)
    scene scarlett_s39_change10 with dissolve
    $ renpy.pause(0.3)
    scene scarlett_s39_change13 with dissolve
    $ renpy.pause(0.3)
    scene scarlett_s39_change14 with dissolve
    $ renpy.pause(0.3)
    scene scarlett_s39_change15 with dissolve
    p "BLAH... Pffff... OMG. I was kissing him. Eeeew. I mean me right now. Blah…."
    scene scarlett_s39_change16
    p "But it’s good to be a man again. I feel much better now."
    scene scarlett_s39_change17
    p "Hmmm. What should I do with her?"
    scene scarlett_s39_change18
    p "Looks like she hit her head a little, but she should be okay. I just need to hide her in a safe place."
    $ currently_possessed_scarlett = False
    $ currently_possessed_anders = True
    scene sportshall_background
    p "So where could I hide her 'till after the tournament."
    $ mc_anders_need_to_hide_scarlett_somewhere = True
    $ inventory.empty()
    $ inventory.add(anders_phone)
    $ inventory.add(anders_keys)
    $ inventory.add(horny_pills)
    jump gym_map

label scene_mc_anders_hiding_scarlett_in_janitors_closet:
    $ mc_anders_need_to_hide_scarlett_somewhere = False
    scene scarlett_s39_change05
    p "Good place. And it will look like she hit her head here. So she won't remember anything from before. She'll think it was just a dream. Sleep well, Scarlett. It was fun being you."
    scene sportshall_background with fade
    p "Fine, now I must do what I started."
    $ hints_counter += 1
    $ mc_anders_needs_to_finish_what_mc_scarlett_started = True
    jump gym_map


label scene_girls_drinks_spiked_fun_begins:
    $ mc_anders_spiked_drinks_fun_begins = False
    scene sportshall_background
    p "Just in time. The semi-finals ended right now. The girls will be here any moment."
    scene scarlett_s39_change07 #bez nahrdelniku a nausnic
    p "There they are."
    scene scarlett_s39_change08
    brook "Hello... Professor."
    beth "Hello, Mr. Anders."
    hide window
    scene scarlett_s39_change09
    $ renpy.pause(2.0, hard=True)
    p "(It will be fun in this body...)"
    $ mc_anders_needs_to_finish_what_mc_scarlett_started = False
    scene anders_s02_volleyball_entering01
    p "(I'd better get back to the sportshall and let... Oh, there's Ivana and Sophia there.)"
    iva "I don’t know where she is. I hope she didn’t double-cross us."
    sop "No, I trust her. Maybe they caught her or something."
    iva "Aaargh… Hopefully she did her job. If not, we're fucked."
    p "(Don’t worry, girls. The job is done. Unfortunately, I will not get a reward for this.)"
    scene anders_s02_volleyball_entering02 with dissolve
    iva "Oh. Hello, Professor."
    p "Hello, girls. How are you? How's the tournament going?"
    sop "Great. We are neck in neck with Bethany and Brooke."
    p "That’s great. I’m expecting a great battle in the finals."
    iva "Yes. Us too. Wish us luck."
    p "Best of luck, girls!"
    sop "Thanks."
    iva "Thanks, Professor. Enjoy the game."
    p "I will, Ivana."
    stop music fadeout 1.0
    play music "sounds/music/Background_music.ogg" fadein 3.0
    scene anders_s02_volleyball_entering03
    p "The whole hall is anticipating the arrival of the final teams. I’m really curious to see how Beth and Brooke will react to the pills."
    scene anders_s02_volleyball_entering04
    $ renpy.pause(1.5, hard=True)

    p "(And there they are. Just a little taller - but nobody could think to notice this small change.)"
    scene anders_s02_volleyball_entering05
    $ renpy.pause(1.5, hard=True)
    p "(Thumbs up to you too, girls. I hope it all goes well.)"

    scene black with fade
    scene anders_s03_tornament01
    brook "Today you will feel defeat again, girls. Are you ready for this?"
    scene anders_s03_tornament02
    beth "Hopefully you won't go and cry afterwards. Haha"
    scene anders_s03_tornament03
    sop "You are much too trusting in your talent, Brooke."#skills talent
    iva "We will see who will cry at the end of this match."
    scene anders_s03_tornament04
    p "Alright, the match is underway."
    scene anders_s03_tornament05
    $ renpy.pause(0.5, hard=True)
    p "The girls are playing really well…"
    scene anders_s03_tornament06
    $ renpy.pause(0.5, hard=True)
    p "Fully focused on the game and getting the win."
    scene anders_s03_tornament07
    $ renpy.pause(0.5, hard=True)
    p "But against Bethany and Brooke when they are augmented with the growing pills, they are losing big time."
    scene anders_s03_tornament08
    p "They seem to be trying different tactics."
    show anders_s03_tornament09 with dissolve
    scene anders_s03_tornament09
    $ renpy.pause(0.5, hard=True)
    show anders_s03_tornament10 with dissolve
    scene anders_s03_tornament10
    $ renpy.pause(0.5, hard=True)
    scene anders_s03_tornament12 with fade
    $ renpy.pause(0.5, hard=True)
    p "But no luck there. First set, “Bad Girls” won easily."
    beth "Haha. Easy win, girls. You have to try harder than that."
    brook "Pfff... They can try as hard as they want, they still won't have a chance."
    scene anders_s03_tornament11
    sop "DAMN! Looks like Scarlett didn’t manage to do it."
    iva "Or maybe the horny pills don't work in combination with the growing ones."
    sop "Yeah, maybe... DAMN, what a shame. I really wanted to beat them, badly."
    iva "Yes, me too. It was a great opportunity. But still, this doesn't mean it's the end."
    sop "You're right. We still have to try to make it. It’s not over yet."
    scene anders_s03_tornament13
    beth "Haha! That was an easy win."
    brook "Yes. These pills are so awesome."
    beth "Yes they are. Megan did her job right."
    brook "Hah, even without the pills we would have beaten them anyway. But now they don’t even stand a chance. Haha!"
    beth "Yes. Let’s go. We must destroy them."
    scene anders_s03_tornament14
    p "Second set's started. Ivana and Sophia have to win this one to have a fighting chance."
    scene anders_s03_tornament15
    p "They lost some points on the first few serves. But the game has slowly started changing."
    scene anders_s03_tornament16
    $ renpy.pause(0.5, hard=True)
    brook "Beth, you have such a nice firm butt. I haven't noticed that before."
    beth "Thank you. I like how you're gently squeezing it, every time we win a point."
    scene anders_s03_tornament17
    p "Looks like the horny pills are starting to kick in. Haha."
    scene anders_s03_tornament20
    p "And they have. Ivana and Sophia win this set. Just barely, with a 2 point difference - but a win."
    scene anders_s03_tornament22
    beth "Aaaaahhhh! They won this one. We almost had them."
    brook "Don’t worry, we will beat them in the third set. Damn, there's so much heat."
    beth "Did I ever tell you, you have nice tits?"
    brook "Oh, no, never... But thanks. I think we can play with them a little, after we win this match. What do you think?"
    beth "I’m definitely into that. But first, let's beat them."
    scene anders_s03_tornament19
    p "In the third set, the girls are doing a really great job."
    scene anders_s03_tornament18
    p "They are not letting any ball through, trying to win it."
    scene anders_s03_tornament21
    p "And they've done it. Two out of three sets win."
    iva "YEAAAH!!!!"
    sop "WE did it!"
    iva "Finally, we won this tournament!"
    scene anders_s03_tornament23
    $ renpy.pause(0.5, hard=True)
    beth "I don't get it. How could they beat us?"
    brook "I have no idea. But I'm still thinking about you girl..."
    beth "How about we forget about this bullshit match and do what we both wanted to do, the whole game?"
    brook "Yes. Let's go..."
    scene anders_s03_tornament21
    p "Hmm... I think I will leave the winners to celebrate... and look into what the losers are doing, hehe."
    show black with fade
    $ bad_girls_lose_volleyball_horny = True
    $ hints_counter +=1
    jump gym_map
    #hide window
    #$ renpy.pause(1.0)
    #scene black with fade
    #jump vote_next_content
