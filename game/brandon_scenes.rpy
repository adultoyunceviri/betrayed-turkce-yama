label scene_try_flash_drive_on_pc:
    scene brandons02_hacking01
    p "Damn! This drive is locked! Aaah! Without the password, I’m fucked!"
    scene brandons02_hacking02
    p "What kind of password could he have?"
    scene brandons02_hacking03
    p "What is that noise outside?"
    scene brandons02_hacking04
    p "SHIT! (This just keeps getting better and better..!)"
    scene brandons02_hacking05
    p "My mom is here with Sophia. Why is Mom here?"
    scene brandons02_hacking06
    mom "I’m so happy that you are here to help me with his stuff."
    sop "It’s okay, Mrs. Donovan."
    scene brandons02_hacking07
    sop "It's fine. I will take them all and you can take another pile."
    mom "Okay."
    scene brandons02_hacking08
    p "(Shit! They are moving my stuff!? SHIT! I forgot that flash drive, in the computer!)"
    scene brandons02_hacking09
    p "Hmm... I have a great idea!"
    scene brandons02_hacking10
    sop "Oh! Hello, Brandon. what are you doing here?"
    p "Hi, Sophia. I’m just passing by. What are you doing with all this? Is someone moving into your flat?"
    mom "No, we are just moving stuff belonging to my son."
    p "Ah... I wouldn’t mind helping you with his stuff?"
    sop "Of course! A pair of strong hands, always comes in handy."
    scene brandons02_hacking11
    p "I will get this heavy computer and the stuff around it."
    mom "Great!"
    scene brandons02_hacking12
    sop "(Damn, he is so cute! And his ass, while he is kneeling under that table: so yummy.)"
    scene brandons02_hacking13
    mom "Really, thank you, Brandon. You helped us a lot."
    scene brandons02_hacking10
    mom "Ah. Finally, that was the last one. What about joining us for dinner after all that hard work? A young man has got to eat."
    p "I don’t know? I should just leave you to it. I have some work to do."
    sop "Oh, Brandon, please, come with us. Work can wait a little."
    mom "And you must, definitely be hungry now."
    p "(I have the flashdrive back; but the only place I could use it is the school computer class, which is now closed.)"
    p "Okay, you make a good point..."
    $ need_to_access_flash_drive_at_home = False
    $ need_to_access_flash_drive_at_school = True
    $ time_of_day = TimeOfDay_Dict[ TimeOfDay_Dict.keys()[TimeOfDay_Dict.values().index('AKŞAM')] ] #TEMP
    $ sophia_roommate_ad_placed = True
    $ ready_for_call_from_dealer = True
    $ classes_have_started = False
    $ has_stuff_been_moved_from_apartment = True
    jump scene_mom_and_sophia_in_restaurant

label scene_brandon_and_security_guard:
    scene security_brandon_entrance
    sec "Hey Brandon. Do you have that new shit I asked for?"
    p "What? What do you mean?"
    sec "Don’t act stupid. I really need that stuff! The crap from other dealers, is just horrible."
    p "Okay... I will do my best."
    p "(Is this Brandon... a drug dealer..?)"

    jump scene_brandon_answering_phone

label scene_try_flash_drive_on_school_computer:
    scene brandons03_computer_class01
    p "Argh... I almost can’t even concentrate on this flash drive because Sophia’s still looking at me."
    scene brandons03_computer_class02
    sop "(Hmmm... He is so fine... I don’t know how Ivana cannot like him: he is like, eye candy.)"
    scene brandons03_computer_class03
    p "(Yes, our Computing teacher: Mrs. Barber. She always has a terrible sense of fashion.)"
    p "(And her computer skills start with one click and end with double clicks.)"
    scene brandons03_computer_class04
    p "(I must concentrate on my own business, if I’m going to crack into this stupid flash drive.)"
    p "(Bethany...)"
    p "(Brandon...)"
    p "(ARGHHH! All denied!)"
    p "(Pills...)"
    scene brandons03_computer_class05
    p "HAHAaaaaa! Finally I’m in luck!"
    scene brandons03_computer_class06
    $ renpy.pause(1.0, hard=True)
    jump brandon_on_class_computer


label scenes_brandon_sees_codenames_on_computer:
    scene brandon_in_classroom_test
    p "(So Brandon is a drug mule. well I guess it beats sleeping under a bridge.)"
    play sound 'sounds/effects/sms_sound.ogg'
    scene brandons03_computer_class7
    show phone_beth_sms
    p "(What's this? A text from Beth. She wants me to meet her in the girl's toilets.)"
    $ need_to_access_flash_drive_at_school = False
    $ classes_have_started = True
    $ beth_waiting_in_female_wc = True
    $ time_of_day = TimeOfDay_Dict[ TimeOfDay_Dict.keys()[TimeOfDay_Dict.values().index('AKŞAM')] ]
    $ hints_counter += 1
    hide phone_beth_sms
    jump school

label scene_brandon_answering_phone:
    play sound "sounds/effects/phone_ringing_sound.ogg"
    scene main_hall
    show telephone00
    $ renpy.pause(0.02, hard=True)
    hide telephone00
    show telephone01
    $ renpy.pause(0.02, hard=True)
    hide telephone01
    show telephone02
    $ renpy.pause(0.02, hard=True)
    hide telephone02
    show telephone03
    $ renpy.pause(0.02, hard=True)
    hide telephone03
    show telephone04
    $ renpy.pause(0.02, hard=True)
    hide telephone04
    show telephone05
    $ renpy.pause(0.02, hard=True)
    hide telephone05
    show telephone06
    $ renpy.pause(0.02, hard=True)
    hide telephone06
    show telephone07
    $ renpy.pause(0.02, hard=True)
    hide telephone07
    show telephone08
    $ renpy.pause(0.02, hard=True)
    hide telephone08
    show telephone09
    $ renpy.pause(0.02, hard=True)
    hide telephone09
    show telephone10
    $ renpy.pause(0.02, hard=True)
    hide telephone10
    show telephone11
    $ renpy.pause(0.02, hard=True)
    hide telephone11
    show telephone12
    $ renpy.pause(0.02, hard=True)
    hide telephone12
    show telephone13
    $ renpy.pause(0.02, hard=True)
    hide telephone13
    show telephone14
    $ renpy.pause(0.02, hard=True)
    hide telephone14
    show telephone15
    $ renpy.pause(0.02, hard=True)
    hide telephone15
    show telephone16
    $ renpy.pause(0.02, hard=True)
    hide telephone16
    show telephone17
    $ renpy.pause(0.02, hard=True)
    hide telephone17
    show telephone18
    $ renpy.pause(0.02, hard=True)
    hide telephone18
    show telephone19
    $ renpy.pause(0.02, hard=True)
    hide telephone19
    show telephone20_unknown_call
    $ renpy.pause(0.02, hard=True)
    hide telephone20
    show telephone20_unknown_call
    stop sound
    p "(Hmm... Unknown number.)"
    p "Hello..."
    cllr "The clothes are in the laundry..."
    p "(Huh? That was weird.)"
    $ ready_for_call_from_dealer = False
    jump scene_sophia_sees_brandon_main_hall

label scene_brandon_in_deans_office:
    scene brandons04_deans_office1
    dean "I’m glad that you got here so fast."
    scene brandons04_deans_office2
    dean "So, do you have any news for me?"
    scene brandons04_deans_office4
    p "What do you mean, news?"
    scene brandons04_deans_office5
    dean "Don’t play dumb. I’m talking about the pills. Did they work?"
    p "(Is the Dean also into this drug stuff?)"
    scene brandons04_deans_office6
    p "Aaah! The pills... Yes, I tried them both."
    dean "What do you mean, both? I gave you a whole package for testing."
    p "Y-yes, I know. I mean: I tried, both on myself and on other subjects."
    menu:
        "Tell the Truth":
            jump scene_brandon_in_deans_office_truth
        "Lie":
            jump scene_brandon_in_deans_office_lie
label scene_brandon_in_deans_office_truth:
    $ told_truth_to_dean = True
    scene brandons04_deans_office5
    p "...And they worked - in a few cases - almost instantly. But now I’m out of pills, for more testing."
    scene brandons04_deans_office2
    dean "That is great news! Here, I will give you more."
    jump scene_brandon_in_deans_office_dean_leaves

label scene_brandon_in_deans_office_lie:
    scene brandons04_deans_office5
    p "...And they didn’t work. But I wanted to try more. Unfortunately I’m out of pills for more testing."
    scene brandons04_deans_office2
    dean "Ahm... That is not good news. Here, I will give you more and we will maybe have better results next time."
    dean "Try to combine them, with maybe alcohol, or other things. In the future, I want better results from you!"
    jump scene_brandon_in_deans_office_dean_leaves

label scene_brandon_in_deans_office_dean_leaves:
    scene brandons04_deans_office3
    dean "Damn! I have none left. Stay here. I'll go see my lab technician. I will be back in a moment with them."
    scene brandons04_deans_office7
    p "(Now's my chance to get on her computer and find out Brandon's address and also about these drugs for Bethany.)"
    scene brandons04_deans_office7_denied
    p "SHIT! Denied! I need to answer security questions since I don't know her password. There must be some clues around the office somewhere. I need to hurry."
    $ hints_counter += 1
    jump scene_brandon_in_deans_office_try_password

label scene_brandon_in_deans_office_try_password:
    scene brandons04_deans_office7
    menu:
        p "Do I know enough about the Dean to answer her security questions?"
        "Try Password":
            jump scene_brandon_in_deans_office_password_attempt
        "Give Up and Wait for the Dean":
            jump scene_brandon_in_deans_office_dean_returns
        "Keep Searching Office":
            jump deans_office

label scene_brandon_in_deans_office_password_attempt:
    scene brandons04_deans_office7
    p "Three security questions to answer:"
    $ renpy.pause(1.0)
    if deans_password_count == 0:
        p "First question: What is your favourite team?"
        p "It doesn't say which sport. I could try all of the city's home teams."
    menu:
        "What is your favourite team?"
        "Sabres":
            pass
        "Coyotes":
            pass
        "Panthers":
            pass
        "Stars":
            pass
        "Highlanders"if deans_password_guess_highlanders == 1:
            #$ deans_password_guess_highlanders = 2
            $ deans_password_count += 1

    p "Second question: What is your favourite place?"
    p "It could be anything. I can try to guess obvious places or try to find something more specific."

    menu:
        "What is your favourite place?"

        "London":
            pass
        "Prague":
            pass
        "Rome":
            pass
        "Madrid":
            pass
        "Paris":
            pass
        "Salou"if deans_password_guess_salou == 1:
            #$ deans_password_guess_salou = 2
            $ deans_password_count += 1
    p "Third and final question: Who is your favourite person?"
    p "Hmmm... Who does the Dean actually like? Brandon?"
    p "Who is that lab girl making the pills?"
    menu:
        "Who is your favourite person?"
        "Brandon":
            pass
        "Lab technician":
            pass

        "Brooke"if deans_password_guess_brooke == 1:
            #$ deans_password_guess_brooke = 2
            $ deans_password_count += 1
        "Dean Smith"if deans_password_guess_certificates == 1:
            #$ deans_password_guess_certificates = 2
            pass
        "Faith"if deans_password_guess_best_teacher == 1:
            #$ deans_password_guess_best_teacher = 2
            pass
        #"Mirapill"if deans_password_guess_mirapill == 1:
        #    $ deans_password_guess_mirapill = 2
        "Mary"if deans_password_guess_highlanders == 1:
            #$ deans_password_guess_highlanders = 2
            pass


        #"Guess a Password":
        #    pass


    if deans_password_count != 3:
        scene brandons04_deans_office7_denied
        p "Fuck! Number of correct answers: [deans_password_count]"
        $ deans_password_failed_attempts += 1
        if deans_password_failed_attempts == 3:
            # failed and dean back
            jump scene_brandon_in_deans_office_dean_outside_door
        $ deans_password_count = 0
        jump scene_brandon_in_deans_office_try_password
    else:
        scene brandons04_deans_office7_granted
        p "Yes! Awesome!"
        $ deans_office_have_got_on_computer = True
        scene brandons04_deans_office7_inside
        p "(Whooa!? Is that young Mrs. Smith? I never imagined the Dean was ever young.)"
        scene brandons04_deans_office7_fullscreen
        p "(Damn, what a screen wallpaper. She was pretty hot! No time to lose, though. I must find Brandon's address.)"
        scene brandons04_deans_office7_adres
        p "Oh noooo! (This address is in another state! He used his prior address during registration. It can't be his address during study here. I’m fucked!)"
        scene brandons04_deans_office7_media
        p "(Aaah... what have we here? Camera recording?)"
        scene megans03_01
        p "(Hmm... this looks promising. Why does the Dean have this? Isn't this the girl in the blue dress I saw in the toilets?)"
        scene black_screen
        # TODO play animation
        $ renpy.movie_cutscene("scenes/Megan/S03_Camera_record_lab/meganS03_camerarecord_cam1.webm", loops=5, stop_music=False)
        scene brandons04_deans_office7_media
        $ renpy.movie_cutscene("scenes/Megan/S03_Camera_record_lab/meganS03_camerarecord_cam2.webm", loops=5, stop_music=False)
        p "(Haha! What a lucky guy. But is he dead, or what?. I think I need to show that beauty, how long I can go for. Haha!)"
        jump scene_brandon_in_deans_office_dean_outside_door
            # correct


label scene_brandon_in_deans_office_dean_outside_door:
    scene brandons04_deans_office8
    p "(Fuck! She's right outside! I need to put everything back the way it was!)"

label scene_brandon_in_deans_office_dean_returns:
    $ called_to_deans_office = False
    scene brandons04_deans_office9
    $ renpy.pause()
    scene brandons04_deans_office10
    dean "I’m back. But unfortunately, I couldn't find the girl that makes the pills."
    dean "If you stop by tomorrow, I should have some new ones then. That is all, for now."
    #$ inventory.add(pills)
    #if deans_office_have_got_on_computer == False:
    p "Damn, I couldn't find the information. I guess I have no choice, but to call her."#TODO
    jump scene_brandon_calling_devil


label scene_brandon_calling_devil:
    scene main_hall
    p "(I guess I have no choice...)"
    show phone_gui
    p "Let's see? 666..."
    hide phone_gui
    show phone_devil_call
    play sound "sounds/effects/phone_ringing_sound.ogg"
    $ renpy.pause(2.0, hard=True)
    stop sound
    stop music
    play music "sounds/music/Sexy_music1_monks_topher.ogg"
    scene devils01_after_call01
    d "I'm glad you called!"
    p "Yes. I wanted to see you, and of course, I need your help, a little."
    d "I like to hear that!"
    scene devils01_after_call02
    d "So, what do you need?"
    p "I need to know where Brandon lives. I’d like to visit his house."
    scene devils01_after_call03
    d "That is not all that difficult. But as I said before: my powers are not for free. So, are you ready to make a deal?"
    p "Of course I am!"
    d "Great! I need more souls to add to my collection. How about that bum living under the bridge? What do you think?"
    scene devils01_after_call04
    p "What do you mean - soul. I can't do that!"
    scene devils01_after_call05
    d "Don’t be stupid. I don’t need you to kill him. I just want you do this little task for me."
    p "Okay, I’m listening."
    d "I need you to deliver him this $100 bill. The rest will work out just fine."
    scene devils01_after_call06
    p "I still don’t know. You..."
    d "Still not convinced? How about I sweeten the deal."
    scene devils01_after_call07
    d "The more souls you bring me, the more I will show you what centuries of pleasing men looks like."
    scene devils01_after_call08
    d "If you catch my drift..."
    scene devils01_after_call09
    d "Mmmm..."
    $ have_cursed_dollar_for_hobo = True
    $ inventory.add(cursed_dollar)
    $ time_of_day = TimeOfDay_Dict[ TimeOfDay_Dict.keys()[TimeOfDay_Dict.values().index('GECE')] ]#TEMP
    stop music
    $ hints_counter += 1
    jump city_map

label scene_brandon_at_home_first_time:
    $ need_to_take_taxi_to_brandons_house = False
    $ inventory.money -= 10
    $ money -= 10
    scene brandons06_house1
    p "Hmmm... This must be his house. Looks nice and posh. And is this his second car here?"
    scene brandons06_house2
    p "Oh shit! I don't have his house keys! Huh? His door is one of those that opens with a code..?"
    play sound 'sounds/effects/keyboard_sound.ogg'
    $ renpy.pause(5.0)
    stop sound
    p "I don't know the code! But maybe I can try some-"
    # TODO door opening sound
    scene brandons06_house3
    trcy "What are you trying there?"
    p "Eeeh... I can’t remember the damn code. Hah! Funny!"
    trcy "Did you hit your head or something? You are here so late and you don’t even remember your date of birth?"
    p "Aaah... Yes. I‘m a dumbass. Haha!"
    trcy "You should think about changing it. I just got here, and even I figured it out. I got tired of waiting for you."
    p "Can we go in?"
    trcy "Of course! It's your house. Hih."
    scene brandons06_house4
    trcy "I'm a little hungry? What about you?"
    p "Yeah. Me to."
    trcy "So, come to the kitchen."
    jump scene_tracy_in_brandon_house

label scene_brandon_wake_up_after_hijack:
    scene policemans02_park01
    p "Arghh..! My head's spinning like hell. What happened?"
    scene policemans02_park02
    p "Oh damn! Hey man, what are you doing? I have no money on me."
    scene policemans02_park03
    kdnppr "Shut the fuck up, you stupid idiot! You were supposed to drop the money at the location I gave you."
    kdnppr "Where is the money?"
    scene policemans02_park04
    p "I’m really sorry, but I had some issues with my card and and have been busy with things."
    scene policemans02_park03
    kdnppr "Hah! They all warned me: telling me that I’m just wasting time, cooperating with you. But I was a fool. So, last chance: where is my money?"
    scene policemans02_park04
    p "Wait, please! I can fix all of this, and maybe I can give you more. I HAVE money. I just need more time."
    scene policemans02_park02
    kdnppr "Time is what you don’t have..."
    if given_hobo_cursed_dollar:
        jump scene_park_hijack_hobo_gets_shot
    elif not given_hobo_cursed_dollar:
        jump scene_park_hijack_hobo_saves_brandon


label scene_park_hijack_hobo_saves_brandon:
    scene policemans02_park05
    $ renpy.pause(1.0)
    play sound 'sounds/effects/punch_sound.ogg'
    $ renpy.pause(0.5, hard=True)
    scene policemans02_park06
    $ renpy.pause(2.0)
    scene policemans02_park09
    stop sound
    p "Damn, man, that was close... Really - thank you."
    scene policemans02_park07
    hobo "Do you think he is dead? What happened here?"
    scene policemans02_park08
    p "I don’t think so. Let’s see who he is?"
    p "Oh, he's a cop!"
    scene policemans02_park07
    hobo "Ohm... Fine. I don’t want to have any more problems than I already have. Bye."
    scene policemans02_park08
    p "I think I should transfer to him. Because Brandon is in danger. And as long as I’m this cop, I can protect him."
    jump scene_brandon_transfers_to_cop

label scene_brandon_transfers_to_cop:
    scene black_screen
    $ renpy.movie_cutscene("scenes/policeman/02_in_park/webm/policeman_transformation.webm", delay=-1, stop_music=False)
    scene policemans02_park19
    $ renpy.pause(1.0)
    p "Aargh..! My head... Why must I always have a broken head. Aaach..."
    scene policemans02_park10
    p "Let’s see what I can do as a cop. Hah!"
    python:
        cop_phone = Item("Phone", element="PuzzleItem14", image="cop_phone_inventory", cost=0)
        cop_car_key = Item("Cop Car Key", element="PuzzleItem15", image="cop_car_key_inventory", cost=0)
        panties = Item("Panties", element="PuzzleItem16", image="panties_inventory", cost=0)
        cop_apartment_keys = Item("Cop's Apartment Keys", element="PuzzleItem19", image="copapartmentkeys_inventory", cost=0)
        gun = Item("Gun", element="PuzzleItem17", image="gun_inventory", cost=0)
        photo = Item("Photo", element="PuzzleItem18", image="photo_inventory", cost=0)
    $ inventory.drop(car_key)
    $ inventory.drop(phone)
    $ inventory.drop(credit_card)
    $ inventory.drop(locker_key_125)
    $ inventory.drop(condoms)
    $ inventory.drop(flash_drive)
    $ inventory.drop(devil_card)
    $ inventory.add(cop_car_key)
    $ inventory.add(cop_phone)
    $ inventory.add(panties)
    $ inventory.add(gun)
    $ inventory.add(cop_apartment_keys)
    $ return_label = "scene_first_steps_as_cop"
    $ special_inventory_display = True
    $ currently_possessed_brandon = False
    $ currently_possessed_cop = True
    call screen inventory_screen
    #play music "sounds/music/Background_music_Funk_Game_Loop.ogg"
    #scene outro
    #jor "Thanks for playing version 0.2.5 And here is your BONUS SCENE!!!"
    #jump phone_bonus1_gallery
    #$ renpy.quit()


label scene_park_hijack_hobo_gets_shot:
    scene policemans02_park11
    hobo "Ouuh... Hey guys! What’s up? Hmmm... pffff..."
    scene policemans02_park13
    $ renpy.pause(0.5, hard=True)
    play sound 'sounds/effects/gunshot_sound.ogg'
    $ renpy.pause(0.5, hard=True)
    scene policemans02_park14
    $ renpy.pause(1.0, hard=True)
    hobo "Urahhhh!!"
    scene policemans02_park12
    $ renpy.pause(2.0)
    kdnppr "Ooops... Looks like, the bum ruined his wine. Hahah! So, back to you..."
    scene policemans02_park15
    p "Aaaarrrg!!!"
    play sound 'sounds/effects/punch_sound.ogg'
    $ renpy.pause(2.0, hard=True)
    scene policemans02_park20
    d "Wow, that was close."
    scene policemans02_park16
    p "What? What the hell just happened? Was this all part of your plan, or what?"
    scene policemans02_park17
    d "Heeey! Calm down. Why are you so angry with ME? Is it my fault? Are you alive or not?"
    scene policemans02_park16
    p "Yes, I’m alive. But you knew that! You said to give that hobo 100 bucks and everything will take care of itself. And why did you want so much to kill him?!"
    scene policemans02_park18
    $ renpy.pause()
    d "Calm down. You still don’t understand how these things work. So don’t worry yourself about that."
    d "I just wanted that hobo’s soul, and you did pretty well, in this case. And by the way, he looks like a Dante."
    d "Hih.  Now you can transform into this masked guy and you can have more opportunities to have fun with your time. Just take a look in his pocket."
    d "Also, you saved Brandon’s life. Good for you!"
    d "So enjoy the rest of your day. I have work to do now. Byeee, sweetie!"
    scene policemans02_park08
    p "Let’s see who he is. A cop? Oh God! Okay... Maybe the devil’s right, and  it will be fun to be a cop. Let’s do this."
    jump scene_brandon_transfers_to_cop


label city_map_brandon_calling_taxi:
    scene city_map_night
    if not given_hobo_cursed_dollar:
        p "Great... I have another bulge on my head from that bath brush. A few more times and I'll have horns growing from my head. What should I do now?"
        play sound "sounds/effects/phone_ringing_sound.ogg"
        show phone_tracy_call
        $ renpy.pause(2.0, hard=True)
        stop sound
        trcy "Hey, where have you been? I’ve been waiting at your apartment, all day, and you were nowhere to be seen?!"
        trcy "I took the taxi from the airport because I wanted to surprise you."
        p "Are you sure you’re at the right address?"
        trcy "Of course I am! Karter Str. 11, 1010 Sedona."
        p "Aah! Yes, I was just testing you. I’m on the way."
        p "(Hah! Luck has finally struck!)"
        p "Now, I can take the taxi and go. I won’t take my chances with the car right now."
    else:
        p "What happens now?"
        play sound "sounds/effects/sms_sound.ogg"
        $ renpy.pause(1.0, hard=True)
        show phone_devil_sms
        $ renpy.pause()
        p "Ah! SMS from the devil."

    p "So now I know Brandon's address. It's pretty far to walk there. I should take a taxi. I hope I have enough for the fare."
    p "I really need to find info about Brandon's card. Maybe I'll find clues in his house."
    $ is_taxi_stand_available = True
    $ need_to_take_taxi_to_brandons_house = True
    $ hints_counter += 1
    jump city_map#scene_brandon_at_home_first_time
