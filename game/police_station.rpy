
screen police_station_interrogation_room:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:

        ground "scenes/Policeman/31_interrogation/interrogation_main.webp"#TODO put image into a destinations folder
        hover "scenes/Policeman/31_interrogation/interrogation_main_glow.png"#TODO put image into a destinations folder

        hotspot (700, 235, 333, 620) action Jump("interaction_brandon_informant")#brandon

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "police_station_interrogation_room"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "police_station_interrogation_room"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "police_station_interrogation_room"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "police_station_interrogation_room"), Jump("joraell_message_no_phone")
            hotspot (0, 130, 70, 65):
                hovered SetVariable("menu_can_show_inventory_hover", True)
                unhovered SetVariable("menu_can_show_inventory_hover", False)
                action Show("inventory_screen")
            imagebutton:
                if menu_can_show_inventory_hover == False and menu_can_show_phone_hover == False and menu_can_show_hint_hover == False:
                    idle "game_menu"
                elif menu_can_show_hint_hover == True:
                    idle "game_menu_hint_glow"
                elif menu_can_show_phone_hover == True:
                    idle "game_menu_phone_glow"
                elif menu_can_show_inventory_hover == True:
                    idle "game_menu_inventory_glow"


label police_station_interrogation_room:
    if as_cop_ready_to_interrogate_brandon:
        scene interrogation_main
        p "(Wow! What a surprise to see him here.)"
        $ hints_counter += 1
    call screen police_station_interrogation_room

label interaction_brandon_informant:
    scene interrogation_main
    scene black_screen with fade
    scene policeman_s31_interrgoration01
    p "Hello. I’m Detective Matrix… John Matrix."
    bran "Hi."
    p "So, dealing drugs? Hmmm? That's a really big crime, kid."
    scene policeman_s31_interrgoration02
    bran "But..."
    p "But what? You want to try and explain yourself somehow?"
    scene policeman_s31_interrgoration03
    bran "Not exactly... I’m here on this case as an informant."
    p "Informant?"
    bran "Yes. Take a look at my papers."
    p "Oh... My apologies. So, do you have something for us, relating to this case?"
    p "(I hope he doesn’t know anything...)"
    if chose_to_sell_drugs_to_brandon:
        p "Who is that guy..?"
        bran "That's the dealer, but I don’t know who he really is.. I was to bring him to you guys - that was my task."
        p "(This little piece of shit. He was playing me the whole time!)"
        p "Yes, I know. But unfortunately, he managed to escape, didn’t he?."
        scene policeman_s31_interrgoration02
        bran "He escaped?! Fuck! He’s going to kill me! I’m fucked!"
        p "(Hah! If only you knew how fucked you really are. You don’t even know, the cop already tried to blow you away the last time.)"

    elif not chose_to_sell_drugs_to_brandon:
        bran "I tried to persuade him to go for another deal, but he didn’t want to. I don’t know what else to do."
        p "(This little piece of shit. He was playing me the whole time! Good thing I didn’t take the bait.)"
        bran "And by now he probably knows about me working with the cops, so I’m fucked now!"
        p "(Hah! If only you knew how fucked you really are. You’re lucky I answered the call, and not the cop.) "
    p "Don’t worry, you are safe in here..."
    scene policeman_s31_interrgoration01
    bran "No! I’m not! This guy is crazy, man! I’ve heard rumors that he killed many people, and that one of his victims, he’s keeping as a slave."
    p "(Ohhhh..? That is interesting.) Tell me more about these rumors."
    bran "It's just rumors. He's now climbing higher and higher on the underground ladder and many people are scared of him. I heard that he has his hands in many criminal activities. Like drugs, gun dealing and prostitution."
    p "Hmmm... (Sounds like this cop is a real gangster, and Brandon looks really scared.)"
    bran "What are you going to do to protect me?"
    p "(He betrayed me, but not actually me... I’m not this cop - this is not my war. But when my time runs out or if I swap to another body, he'll probably kill him. I must figure out how to save him.)"
    p "For the next few days you will stay here, until things return to normal."
    bran "Thanks."
    p "No problem, and thank you for your cooperation."
    scene black_screen with fade
    scene city_map
    if reputation_number > 0:
        p "Ufff... that was really strange. Now that I know this cop is a real gangster, it's not a good feeling."
    else:
        p "Ufff... that was really strange. Now that I know this cop is a real gangster -like from a gangster movie- people are scared of me. Hah! A really weird feeling."
    if accepted_devils_offer_for_anders_soul:
        p "Now, I need to go to school. I have those papers for the Dean, about Anders. And I want to check out Scarlett’s usb drive."
    else:
        p "I need to go to the school and look into Scarlett’s usb drive."
    $ time_to_look_at_scarletts_flash_drive = True
    $ as_cop_ready_to_interrogate_brandon = False
    $ hints_counter += 1
    jump city_map
