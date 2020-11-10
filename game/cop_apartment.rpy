screen cop_apartment_main:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/08_policeman_flat/policeman_main.webp"
        hover "destinations/08_policeman_flat/policeman_main_glow.png"

        hotspot (1220, 260, 110, 360):#lockeddoor
            if not need_cops_gun and gun in inventory.items:
                action Jump("exit_block_cop_apartment_main_offload_gun")
            else:
                if cop_apartment_closet_door_unlocked:
                    action Jump("cop_apartment_closet")
                else:
                    action Jump("interaction_cop_apartment_locked_door")

        hotspot (1440, 215, 160, 550):#frontdoor
            if ready_to_sleep_first_time_as_cop:
                action Jump("exit_block_ready_to_sleep_as_cop")
            elif drug_sell_choice_consequence_time:
                if chose_to_sell_drugs_to_brandon:
                    if drugs not in inventory.items:
                        action Jump("exit_block_cop_needs_to_collect_drugs_for_deal")
                    else:
                        action Jump("city_map")
                elif not chose_to_sell_drugs_to_brandon:
                    action Jump("exit_block_angel_waiting_in_cop_apartment")
            elif morning_after_drug_sell_choice_consequenses:
                if chose_to_sell_drugs_to_brandon and devil_or_angel_explained_the_secret_of_the_pills == False:
                    action Jump("exit_block_devil_waiting_in_cop_apartment")
                elif helped_trapped_girl:
                    action Jump("scene_see_trapped_girl_after_note_left")
                else:
                    action Jump("time_to_check_on_sophias_progess_with_pills")

            elif not need_cops_gun and gun in inventory.items:
                action Jump("exit_block_cop_apartment_main_offload_gun")
            else:
                action Jump("city_map")

        if not devil_broke_cop_computer:
            hotspot (745, 410, 300, 375) action Jump("cop_apartment_desk")#table

        if night_before_interrogation_consequence_time and accepted_devils_offer_for_anders_soul:
            hotspot (745, 410, 300, 375) action Jump("scene_put_anders_papers_together_for_dean")#table

        hotspot (545, 450, 150, 135):#drawers
            if drug_sell_choice_consequence_time and chose_to_sell_drugs_to_brandon:
                action Jump("scene_cop_get_drugs_and_gun_for_deal")
            elif done_anders_sting_operation_at_ivanas and not devil_or_angel_explained_the_secret_of_the_pills and not chose_to_sell_drugs_to_brandon and gun in inventory.items:
                action Jump("scene_cop_in_apartment_angry")
            else:
                action Jump("interaction_cop_apartment_drawers")

        hotspot (0, 120, 220, 493):#bedroom_doorway
            if not need_cops_gun and gun in inventory.items:
                action Jump("exit_block_cop_apartment_main_offload_gun")
            else:
                action Jump("cop_apartment_bedroom")


        if drug_sell_choice_consequence_time and not chose_to_sell_drugs_to_brandon:
            imagebutton:
                idle "policeman_main_angel"
                hover "policeman_main_angel_glow"
                xpos 210 ypos 415
                action Jump("scene_not_sell_drugs_consequence_angel_visit")

        if morning_after_drug_sell_choice_consequenses and chose_to_sell_drugs_to_brandon and devil_or_angel_explained_the_secret_of_the_pills == False:
            imagebutton:
                idle "policeman_main_devil"
                hover "policeman_main_devil_glow"
                xpos 270 ypos 395
                action Jump("scene_sell_drugs_consequence_devil_visit")


        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "cop_apartment_main"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "cop_apartment_main"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "cop_apartment_main"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "cop_apartment_main"), Jump("joraell_message_no_phone")
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

label cop_apartment_main:
    if drug_sell_choice_consequence_time and not chose_to_sell_drugs_to_brandon:
        $ hints_counter = 48 #MAGIC
    call screen cop_apartment_main

screen cop_apartment_bedroom:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        if have_left_panties_in_cops_bedroom:
            ground "destinations/08_policeman_flat/policeman_bedroom_panties.webp"
            hover "destinations/08_policeman_flat/policeman_bedroom_glow_panties.png"
        else:
            ground "destinations/08_policeman_flat/policeman_bedroom.webp"
            hover "destinations/08_policeman_flat/policeman_bedroom_glow.png"

        hotspot (1020, 0, 210, 830) action Jump("cop_apartment_bedroom_wardrobe")#wardrobe

        hotspot (150, 15, 300, 370) action Jump("interaction_cop_apartment_bedroom_display_case")#display_case

        hotspot (0, 330, 150, 310):#pillow
            if ready_to_sleep_first_time_as_cop:
                action Jump("scene_cop_sleep_in_bed_first_time")
            elif ready_for_cop_asian_night_scene:
                action Jump("scene_asian_visits_cop_at_night")
            elif cop_ready_to_request_pills_from_megan and time_of_day != 'SABAH':
                if ready_for_cop_angel_night_scene:
                    action Jump("scene_angel_visits_cop_at_night")
                else:
                    action Jump("city_map_cop_ready_to_find_something_on_anders")
            elif cop_ready_for_night_sophia_dream:
                action Jump("scene_cop_sophia_dream")
            elif time_for_bed_after_drug_selling_choice_consequences:
                action Jump("scene_day_after_drug_sell_choice_consequences")
            elif time_for_bed_before_interrogation:
                action Jump("scene_bed_before_interrogation")
            elif time_for_bed_after_bikini_competition:
                action Jump("scene_bed_after_bikini_contest")
            else:
                action Jump("cop_apartment_bedroom_pillow")

        hotspot (470, 760, 530, 140) action Jump("interaction_cop_apartment_bedroom_under_bed")#under_bed

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "cop_apartment_bedroom"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "cop_apartment_bedroom"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "cop_apartment_bedroom"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "cop_apartment_bedroom"), Jump("joraell_message_no_phone")
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
        imagebutton:
            idle "back_button_idle"
            hover "back_button_hover"
            xpos 1405 ypos 820
            if have_left_panties_in_cops_bedroom and have_changed_clothes_as_cop:
                action Jump("cop_apartment_main")
            elif have_left_panties_in_cops_bedroom:
                action Jump("exit_block_cop_apartment_bedroom_clothes_itchy")
            else:
                action Jump("exit_block_cop_apartment_bedroom_find_out_more")


label cop_apartment_bedroom:
    call screen cop_apartment_bedroom


screen cop_apartment_desk:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/08_policeman_flat/policeman_desk.webp"
        hover "destinations/08_policeman_flat/policeman_desk_glow.png"

        hotspot (852, 440, 295, 275) action Jump("scene_cop_apartment_found_password")#note

        hotspot (380, 230, 470, 505) action Jump("interaction_cop_apartment_desk_computer_no_password")#computer

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "cop_apartment_desk"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "cop_apartment_desk"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "cop_apartment_desk"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "cop_apartment_desk"), Jump("joraell_message_no_phone")
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
        imagebutton:
            idle "back_button_idle"
            hover "back_button_hover"
            xpos 1405 ypos 820
            action Jump("cop_apartment_main")

label cop_apartment_desk:
    call screen cop_apartment_desk


screen cop_apartment_closet:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/08_policeman_flat/locked door/cop_stuff_main.png"
        hover "destinations/08_policeman_flat/locked door/cop_stuff_main_glow.png"

        hotspot (661, 483, 35, 45) action Jump("interaction_cop_apartment_closet_detective_badge")#detective_badge

        hotspot (675, 303, 500, 160) action Jump("interaction_cop_apartment_closet_guns")#guns

        hotspot (930, 488, 260, 410) action Jump("interaction_cop_apartment_closet_bulletproof_vest")#bulletproof_vest

        hotspot (539, 548, 265, 160) action Jump("cop_apartment_closet_closeup")#key_closeup

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "cop_apartment_closet"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "cop_apartment_closet"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "cop_apartment_closet"), Show("phone_screen")

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
        #if den_location_available:
        #    imagebutton:
        #        idle "back_button_idle"
        #        hover "back_button_hover"
        #        xpos 1405 ypos 820
        #        action Jump("cop_apartment_main")

label cop_apartment_closet:
    call screen cop_apartment_closet


screen cop_apartment_closet_closeup:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/08_policeman_flat/locked door/cop_stuff_key.png"#TODO
        hover "destinations/08_policeman_flat/locked door/cop_stuff_key_glow.png" #TODO



        hotspot (1049, 42, 140, 540) action Jump("interaction_cop_apartment_closet_lamp")#lamp

        hotspot (560, 252, 100, 120) action Jump("interaction_cop_apartment_closet_key")#key


        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "cop_apartment_closet_closeup"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "cop_apartment_closet_closeup"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "cop_apartment_closet_closeup"), Show("phone_screen")

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

        imagebutton:
            idle "back_button_idle"
            hover "back_button_hover"
            xpos 1405 ypos 820
            action Jump("cop_apartment_closet")

label cop_apartment_closet_closeup:
    call screen cop_apartment_closet_closeup

label interaction_cop_apartment_desk_computer_no_password:
    scene policeman_desk
    p "I don't know the password."
    jump cop_apartment_desk

label interaction_cop_apartment_bedroom_display_case:
    if not have_left_panties_in_cops_bedroom:
        scene policeman_bedroom
        p "I should leave his trophy panties here. It's not really my style."
        $ inventory.drop(panties)
        $ have_left_panties_in_cops_bedroom = True
        if have_changed_clothes_as_cop:
            $ hints_counter += 1#split increment
    scene policeman_bedroom_closer_look
    $ renpy.pause()
    jump cop_apartment_bedroom

label interaction_cop_apartment_bedroom_under_bed:
    if have_left_panties_in_cops_bedroom:
        scene policeman_bedroom_panties
    else:
        scene policeman_bedroom
    jor "Are you scared of a monster under the bed. or what?"
    jump cop_apartment_bedroom

label interaction_cop_apartment_drawers:
    if need_cops_gun:
        if gun in inventory.items:
            scene policeman_main
            p "I still need the gun."
            jump cop_apartment_main
        else:
            jump finding_cops_gun

    else:
        if gun in inventory.items:
            $ inventory.drop(gun)
            scene policeman_s17_gun
            p "I'll leave the gun in here for now."
        else:
            scene policeman_main

            if drug_sell_choice_consequence_time and not chose_to_sell_drugs_to_brandon:
                show policeman_main_angel:
                    xpos 210 ypos 415
            elif morning_after_drug_sell_choice_consequenses and chose_to_sell_drugs_to_brandon and devil_or_angel_explained_the_secret_of_the_pills == False:
                show policeman_main_devil:
                    xpos 270 ypos 395

            p "I don't need the gun right now."
        jump cop_apartment_main

label interaction_cop_apartment_locked_door:
    scene policeman_main
    p "It's locked. And I don't know where the key is."
    jump cop_apartment_main

label exit_block_cop_apartment_bedroom_find_out_more:
    scene policeman_bedroom
    p "I should find out more about the cop before I leave."
    jump cop_apartment_bedroom

label exit_block_cop_apartment_bedroom_clothes_itchy:
    scene policeman_bedroom
    p "I should change out of these clothes. They're really itchy."
    jump cop_apartment_bedroom

label exit_block_cop_apartment_main_offload_gun:
    scene policeman_main
    p "I should offload the gun if I don't need it."
    jump cop_apartment_main

label exit_block_cop_needs_to_collect_drugs_for_deal:
    scene policeman_main
    p "I need to grab the drugs and get over to the warehouse."
    jump cop_apartment_main

label exit_block_angel_waiting_in_cop_apartment:
    scene policeman_main
    show policeman_main_angel:
        xpos 210 ypos 415
    p "I shouldn't leave. It seems I have a visitor."
    jump cop_apartment_main

label exit_block_devil_waiting_in_cop_apartment:
    scene policeman_main
    show policeman_main_devil:
        xpos 270 ypos 395 # TEMP
    p "I should see what she wants before I go anywhere."
    jump cop_apartment_main

label scene_cops_apartment_night_before_interrogation_consequence_time:
    scene policeman_main
    play sound "<from 2 to 5>sounds/effects/phone_ringing_sound.ogg"
    $ renpy.pause(3.0)
    scene policeman_s36_phoning_with_asia with dissolve
    $ asian_called_to_offer_work = True
    asn "Hello, John."
    p "Ee..? Hi. Who's calling?"
    if chose_to_sell_drugs_to_brandon and not accepted_devils_offer_for_anders_soul:
        asn "Your rescuer, from a bad situation..."
        p "Ah, I got it now. Nice to hear from you."
        asn "I’m looking for a reliable guy for some work."
    else:
        asn "A girl that needs reliable guys for work."
        p "(Aaah... that footjob-master girl!)"

    p "Of course. What can I do for you?"
    asn "Nothing special... just a little robbery, as usual. More information will be sent to you later. And as always, not a word in front of my father about it."
    p "Of course."
    play sound "sounds/effects/sms_sound.ogg"
    $ renpy.pause(1.0, hard=True)
    scene asiangirl_s01_sexy_photo01
    asn "And to sweeten the deal, I’m sending you these."
    scene asiangirl_s01_sexy_photo02
    asn "This is what I will be wearing for you if you do the job well."
    scene asiangirl_s01_sexy_photo03
    asn "Just a little incentive. So, wait for more information later."
    p "Sure thing."
    scene policeman_s36_phoning_with_asia
    if chose_to_sell_drugs_to_brandon and accepted_devils_offer_for_anders_soul:
        p "Devil wanted me to put the Anders evidence together for the Dean. I'll work on it at the desk."
        $ hints_counter += 1
        jump cop_apartment_main
    else:
        $ hints_counter += 2
        jump scene_time_for_bed_before_interrogation

label scene_time_for_bed_before_interrogation:
    p "I’m really tired. That sex with Sophia, at the start of the day, wore me out."
    if chose_to_sell_drugs_to_brandon and accepted_devils_offer_for_anders_soul:
        p "And these papers finished me off."
    p "Time for bed."
    $ night_before_interrogation_consequence_time = False
    $ time_for_bed_before_interrogation = True
    jump cop_apartment_main

label scene_put_anders_papers_together_for_dean:
    scene policeman_s36_clues02 #TEMP
    p "Aaafff..! Doing paperwork is always so demanding."
    scene policeman_s36_clues03 #TEMP
    p "Hopefully I got all the facts inside. The devil saved me, so I don’t want to disappoint her."
    python:#TEMP
        anders_evidence = Item("Anders Evidence", element="PuzzleItem22", image="anders_evidence_inventory", cost=0)
    $ inventory.add(anders_evidence)
    $ hints_counter += 1
    jump scene_time_for_bed_before_interrogation


label scene_bed_before_interrogation:
    scene policeman_bedroom_panties
    scene black_screen with fade
    scene policeman_04_go_sleep with fade # TODO joraell need better wake up image
    p "I’m really excited today. I will take part in my first interrogation. I almost didn’t sleep till morning, thinking about this. I wonder if it will be like in the NCIS shows, haha. Let’s head to the local police station."
    $ time_for_bed_before_interrogation = False
    $ police_station_location_available = True
    $ as_cop_ready_to_interrogate_brandon = True
    $ time_of_day = Set_Time_of_Day('SABAH')
    $ hints_counter += 1
    jump cop_apartment_bedroom

label scene_bed_after_bikini_contest:
    scene policeman_bedroom_panties
    scene black_screen with fade
    scene policeman_s39_overgrow_dream01
    p "What is that noise??"
    p "Huh... Bethany? What the…?"
    scene policeman_s39_overgrow_dream02
    beth "Oh, hello! How was your sleep?"
    scene policeman_s39_overgrow_dream03
    p "What are you doing here? How did you find my apartment?"
    scene policeman_s39_overgrow_dream02
    beth "I just followed you - it was easy, I just waited for the right opportunity."
    beth "You thought that I would play by your rules, right? Haha!"
    beth "And look what I found... and swallowed."
    scene policeman_s39_overgrow_dream09
    p "How many of them have you used?"
    scene policeman_s39_overgrow_dream04
    beth "Not many. Just a few…."
    scene policeman_s39_overgrow_dream05
    p "OH MY GOD!"
    scene policeman_s39_overgrow_dream06
    p "You used them all?! That bottle had about fifteen pills left..!"
    scene policeman_s39_overgrow_dream04
    beth "Seventeen, to be exact. Haha!"
    p "That could be dangerous! You need to go to the hospital!"
    scene policeman_s39_overgrow_dream07
    beth "Haha, you silly! I feel great! Like never before!"
    scene policeman_s39_overgrow_dream08
    beth "I’m feeling all that strange and pleasant, warm and tingly sensation, all over my whole body. It is soooo goood!"
    scene policeman_s39_overgrow_dream10
    beth "Haha! I think it’s taking effect right now!"
    scene policeman_s39_overgrow_dream11
    beth "Hmmmmm….."
    scene black_screen
    $ renpy.movie_cutscene("scenes/Policeman/39_bethany_overgrow_dream/webm/BethanyS39_boobscam2.webm", loops=0,delay=-1, stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/39_bethany_overgrow_dream/webm/BethanyS39_boobscam1.webm", loops=0,delay=-1, stop_music=False)
    scene policeman_s39_overgrow_dream14
    beth "Yes! It’s commming..!"
    scene black_screen
    $ renpy.movie_cutscene("scenes/Policeman/39_bethany_overgrow_dream/webm/BethanyS39_asscam2.webm", loops=0,delay=-1, stop_music=False)
    scene policeman_s39_overgrow_dream19
    beth "Hah! My pants didn’t want to hold my size. What a shame..."
    scene policeman_s39_overgrow_dream17
    beth "What do you think about my butt now, hmmm?"
    p "I think you look stunning now."
    beth "That was just the beginning. I’m still feeling such power in my whole body."
    scene policeman_s39_overgrow_dream18
    beth "Ohmmm... It is a little overwhelming. I’m starting to feel really weird..."
    scene black_screen
    $ renpy.movie_cutscene("scenes/Policeman/39_bethany_overgrow_dream/webm/bethany_s39_monstergrow3.webm", loops=0,delay=-1, stop_music=False)
    scene policeman_s39_overgrow_dream20
    beth "What the..? My feet are growing tooo! My shoes are ruined..."
    scene black_screen
    $ renpy.movie_cutscene("scenes/Policeman/39_bethany_overgrow_dream/webm/bethany_s39_monstergrow2.webm", loops=0,delay=-1, stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/39_bethany_overgrow_dream/webm/bethany_s39_monstergrow1.webm", loops=0,delay=-1, stop_music=False)
    scene policeman_s39_overgrow_dream22
    beth "Oh nooo..! I don’t want this!"
    scene policeman_s39_overgrow_dream21
    beth "Do something! STOP it!"
    scene policeman_s39_overgrow_dream23
    p "I don’t know how to help you!"
    scene policeman_s39_overgrow_dream24
    p "(She is still growing, more and more...)"
    scene policeman_s39_overgrow_dream25
    beth "Where are you hiding?"
    scene policeman_s39_overgrow_dream26
    beth "Ahah!!"
    p "What are you going to do to me?!"
    scene policeman_s39_overgrow_dream27
    beth "What do you think? I’m so fucking horny right now. We will have some fun together. That was what you wanted, isn’t it?  Don’t worry..."
    scene policeman_s39_overgrow_dream28
    beth "You will be a nice toy for my big growing pussy."
    p "A-Aaaaaaaaaaaaaaaaah!!!"
    scene black_screen with dissolve
    $ time_for_bed_after_bikini_competition = False
    $ time_of_day = Set_Time_of_Day('SABAH')
    $ hints_counter += 1
    jump scene_cop_bedroom_massage_by_either_devil_or_angel


label scene_cop_bedroom_massage_by_either_devil_or_angel:
    $ time_for_coffee_and_researching_scarlett_case = True
    if reputation_number>0:#had_dinner_with_angel_after_no_drug_sell_and_helped_trapped_girl:
        jump scene_angel_massage_for_cop
    elif reputation_number < 1:#accepted_devils_offer_for_anders_soul:
        jump scene_devil_massage_for_cop
    #else:
    #    scene policeman_bedroom_panties with fade
    #    p "Oh man, I'm even more exhausted than before. I think I'll go buy a coffee and work a little on Scarlett’s case."
    #    jump cop_apartment_bedroom

label scene_angel_massage_for_cop:
    scene policeman_s41_angelmassage01
    a "Heeey... bad dreams?"
    p "Of course! That was the worst dream I’ve ever had, after the accident. Does that dream mean something?"
    scene policeman_s41_angelmassage02
    a "I don’t think so. It’s fine, it was just a dream. This will make you feel better..."
    scene policeman_s41_angelmassage03
    p "Hmmm, you have some nice skills..."
    scene policeman_s41_angelmassage04
    a "It’s due to centuries of practice."
    scene policeman_s41_angelmassage05
    p "I feel really great now. I think I will go buy a coffee and work a little on Scarlett’s case."
    a "Sound’s good. Good luck."
    jump cop_apartment_bedroom

label scene_devil_massage_for_cop:
    scene policeman_s41_devilmassage01
    d "Heeey... bad dreams?"
    p "Of course! That was the worst dream I’ve ever had, after the accident. Does that dream mean something?"
    scene policeman_s41_devilmassage02
    d "I don’t think so. It’s fine, it was just a dream. This will make you feel better..."
    scene policeman_s41_devilmassage03
    p "Hmmm, you have some nice skills..."
    scene policeman_s41_devilmassage04
    d "It’s due to centuries of practice."
    scene policeman_s41_devilmassage05
    p "I feel really great now. I think I will go buy a coffee and work a little on Scarlett’s case."
    d "Sound’s good. Good luck."
    jump cop_apartment_bedroom


label interaction_cop_apartment_closet_detective_badge:
    scene cop_stuff_detective
    p "For all the people I’ve met while being the cop, it was enough telling them I’m a detective. Nobody wanted to see a badge."
    jump cop_apartment_closet

label interaction_cop_apartment_closet_guns:
    scene cop_stuff_guns
    p "Damn, pretty nice guns... But in my case, I don’t even know how to un-safety them for firing. "
    jump cop_apartment_closet

label interaction_cop_apartment_closet_lamp:
    scene cop_stuff_key
    p "I don’t need it, now."
    jump cop_apartment_closet_closeup

label interaction_cop_apartment_closet_bulletproof_vest:
    scene cop_stuff_otherstuff
    p "Bulletproof vest... Good protection, but that weight..."
    jump cop_apartment_closet

label interaction_cop_apartment_closet_key:
    scene cop_stuff_key
    p "Hmm... another key, and with an address. Maybe I could check this out. I still have enough time before the girls come. "
    p "Fine, I will go check out the door for this key. I have a couple of hours."
    python:#TEMP
        den_key = Item("House Key", element="PuzzleItem23", image="den_key_inventory", cost=0)
        room4_key = Item("Room 4 Key", element="PuzzleItem24", image="room4_key_inventory", cost=0)
    $ inventory.add(den_key)
    $ den_location_available = True
    $ time_to_sort_through_scarlett_case_clues = False
    $ time_of_day = Set_Time_of_Day('ÖĞLEN')
    $ hints_counter += 1
    jump city_map
