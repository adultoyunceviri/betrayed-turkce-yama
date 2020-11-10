
screen apartment_map:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "apartment"
        hover "apartment_glow"

        hotspot (1060, 640, 80, 100):
            if have_taken_keys_from_sewer == True:
                if currently_posessed_homeless_guy:
                    action Jump("interaction_apartment_map_hobo_should_stay")
                elif currently_possessed_scarlett:
                    if not have_talked_to_sophia_in_kitchen_as_scarlett:
                        action Jump("interaction_apartment_map_as_scarlett_need_talk_sophia")
                    elif mc_scarlett_needs_shower_after_threesome:
                        action Jump("interaction_apartment_map_mc_scarlett_need_shower_after_threesome")
                    elif need_to_hide_pills_after_threesome:
                        action Jump("interaction_apartment_map_mc_scarlett_need_bed_after_threesome")
                    elif mc_scarlett_leaving_apartment_morning_after_threesome:
                        action Jump("scene_leaving_apartment_morning_after_threesome")
                    else:
                        action Jump("city_map")
                else:
                    action Jump("city_map")
            else:
                action Jump("interaction_apartment_map_closed_doors")

        hotspot (360, 280, 195, 120):
            if have_policemen_left_the_apartment == True:
                if currently_possessed_scarlett and time_to_find_growing_pill_on_clothes:
                    action Jump("scene_find_lost_pill_on_clothes")
                else:
                    action Jump("mc_room")
            else:
                action Jump("interaction_apartment_map_mc_room_police_still_there")


        hotspot (605, 510, 180, 120):
            if have_taken_keys_from_sewer == True:
                action Jump("roommate_room")
            else:
                action Jump("interaction_apartment_map_closed_doors")

        hotspot (635, 150, 190, 120):
            if have_policemen_left_the_apartment == True:
                action Jump("bathroom")
            else:
                action Jump("bathroom_with_policeman_sniffing_panties")

        hotspot (800, 280, 160, 120):
            if have_taken_keys_from_sewer == True:
                action Jump("living_room")
            else:
                action Jump("interaction_apartment_map_closed_doors")


        hotspot (1000, 450, 160, 120):
            if have_taken_keys_from_sewer == True:
                action Jump("kitchen")
            else:
                action Jump("interaction_apartment_map_closed_doors")

label apartment_map:
    call screen apartment_map

screen apartment_map_winners_party:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "apartment_winners_party"
        hover "apartment_winners_party_glow"

        hotspot (1060, 640, 80, 100):
            action Jump("exit_block_apartment_map_winners_party_no_leaving")

        hotspot (360, 280, 195, 120):
            action Jump("scarletts_room_winners_party")

        hotspot (605, 510, 180, 120):
            action Jump("sophias_room_winners_party")

        hotspot (635, 150, 190, 120):
            action Jump("bathroom_winners_party")

        hotspot (800, 280, 160, 120):
            action Jump("living_room_winners_party")

        hotspot (1000, 450, 160, 120):
            action Jump("kitchen_winners_party")

label apartment_map_winners_party:
    call screen apartment_map_winners_party

### MC room
screen mc_room:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        if not currently_possessed_scarlett:
            if mc_room_window_opened == True:
                ground "destinations/02_apartment/02_mcroom/mc_room_openedwindow.webp"
                hover "destinations/02_apartment/02_mcroom/mc_room_openedwindow_glow.webp"
            else:
                ground "destinations/02_apartment/02_mcroom/mc_room_day.webp"
                hover "destinations/02_apartment/02_mcroom/mc_room_day_glow.webp"
        else:
            if time_of_day == 'GECE':
                ground "destinations/02_apartment/02_mcroom/mc_room_night.webp"#TODO scarlett room pics
                hover "destinations/02_apartment/02_mcroom/mc_room_night_glow.webp"
            else:
                ground "destinations/02_apartment/02_mcroom/mc_room_day.webp"#TODO scarlett room pics
                hover "destinations/02_apartment/02_mcroom/mc_room_day_glow.webp"

        if currently_possessed_scarlett and not have_opened_scarletts_box:
            imagebutton:#scarlet_box
                idle "destinations/02_apartment/02_mcroom/mc_room_box.png"
                hover "destinations/02_apartment/02_mcroom/mc_room_box_glow.png"
                xpos 750 ypos 650
                action Jump("interaction_scarletts_box_open")

        if not currently_possessed_scarlett:
            hotspot (175, 466, 100, 160) action Jump("interaction_mc_room_computer")#computer

        hotspot (296, 497, 127, 63):#bedside_table
            if not currently_possessed_scarlett:
                action Jump("interaction_mc_room_bedside_table")
            else:
                action Jump("interaction_mc_room_bedside_table_scarlett")

        hotspot (1429, 99, 171, 739):#wardrobe
            if not currently_possessed_scarlett:
                action Jump("interaction_mc_room_wardobe")
            else:
                action Jump("interaction_mc_room_wardobe_scarlett")

        hotspot (1317, 160, 104, 456):#door
            if currently_posessed_homeless_guy:
                if have_showered_as_hobo == True:
                    action Jump("interaction_mc_room_door_sophia_home_early")
                else:
                    action Jump("apartment_map")
            elif currently_possessed_scarlett:
                if settled_as_scarlett:
                    action Jump("apartment_map")
                else:
                    action Jump("interaction_mc_room_door_not_settled_as_scarlett")

            else:
                if HaveLookedAtAllItemsInMCRoom() == True:
                    action Jump("apartment_map")
                else:
                    action Jump("interaction_mc_room_door_cant_get_out")

        if not currently_possessed_scarlett:
            hotspot (1068, 468, 60, 40) action Jump("interaction_mc_room_small_box")#box

        if have_taken_keys_from_sewer == True and not currently_possessed_scarlett:
            hotspot (700, 180, 300, 300) action Jump("interaction_mc_room_window")#window

        #textbutton "Show Inventory" action [ Hide("Show Inventory"), Show("inventory_screen")] align (.95,.96)

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "mc_room"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "mc_room"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "mc_room"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "mc_room"), Jump("joraell_message_no_phone")
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
        #screen inventory_button #TODO see if can call screen in a screen
        #if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
        #    imagebutton:
        #        idle "inventory_button_idle"
        #        hover "inventory_button_glow"
        #        xpos 3 ypos 3
        #        action [Show("inventory_screen")]#, SetVariable("can_show_inventory_button", False)

        #imagebutton:
        #    idle "back_button_idle"
        #    hover "back_button_hover"
        #    xpos 1405 ypos 820
        #    action Jump("apartment")

label mc_room:
    if listened_to_sophia_with_policeman_in_mc_room == False and HaveLookedAtAllItemsInMCRoom() == True:
        jump scene_sophia_policeman_mc_room_entering
    #show screen inventory_button
    call screen mc_room

### MC room
screen mc_room_computer_turn_on_folder_visible:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:

        ground "Other_things/computer/computer_desktop_test.png"

        #hotspot (540, 260, 120, 155) action Jump("scenes_mc_room_computer_folder_ex")#folder

        imagebutton:
            idle "Other_things/computer/folder_day_on_beach.png"
            hover "Other_things/computer/folder_day_on_beach_glow.png"
            xpos 541 ypos 231
            action Jump("scenes_mc_room_computer_folder_ex")
        imagebutton:
            idle "Other_things/computer/folder_secret.png"
            hover "Other_things/computer/folder_secret_glow.png"
            xpos 1433 ypos 450
            action Jump("scenes_mc_room_computer_folder_secret")
        imagebutton:
            idle "Other_things/computer/Power_off.png"
        #    hover "back_button_hover"
            xpos 1435 ypos 760
            action Jump("mc_room")


label mc_room_computer_turn_on_folder_visible:
    call screen mc_room_computer_turn_on_folder_visible

### MC room
screen mc_room_with_sofia_and_policeman:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        #if listened_to_sophia_with_policeman_in_mc_room == False and HaveLookedAtAllItemsInMCRoom() == True:
        ground "destinations/02_apartment/02_mcroom/mc_room_day_cathy_policeman.webp"
        hover "destinations/02_apartment/02_mcroom/mc_room_day_cathy_policeman_glow.webp"

        hotspot (1320, 160, 110, 460):
            if listened_to_sophia_with_policeman_in_mc_room:
                action Jump("apartment_map")#door
            else:
                action Jump("interaction_mc_room_door_cant_leave_yet")#door
        hotspot (815, 250, 300, 500):
            if listened_to_sophia_with_policeman_in_mc_room == False:
                action Jump("scene_sophia_policeman_mc_room_conversation")#sophia_and_policeman
            else:
                action Jump("idle_sophia_policeman_mc_room_conversation")#sophia_and_policeman
        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "mc_room_with_sofia_and_policeman"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "mc_room_with_sofia_and_policeman"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "mc_room_with_sofia_and_policeman"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "mc_room_with_sofia_and_policeman"), Jump("joraell_message_no_phone")
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

label mc_room_with_sofia_and_policeman:
    call screen mc_room_with_sofia_and_policeman


### MC room
screen scarletts_room_winners_party:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:

        ground "mc_room_night"
        hover "mc_room_night_glow"

        if not milestone_mc_anders_found_scarletts_flash_drive:
            imagebutton:
                idle "mcroom_party_scarlett"
                hover "mcroom_party_scarlett_glow"
                xpos 951 ypos 388
                action Jump("interaction_scarlett_scarletts_room_winners_party")
        if not milestone_winners_party_sophia_asked_for_drinks:
            imagebutton:
                idle "mcroom_party_others"
                hover "mcroom_party_others_glow"
                xpos 501 ypos 228
                action Jump("interaction_others_scarletts_room_winners_party")

        if onetime_mc_anders_looking_for_scarletts_flash_drive or onetime_mc_anders_time_to_recover_pills_from_bedstand:
            hotspot (296, 497, 127, 63):#bedside_table
                action Jump("interaction_scarletts_room_bedside_table")

        if onetime_mc_anders_looking_for_scarletts_flash_drive:
            hotspot (175, 466, 100, 160) action Jump("interaction_scarletts_room_computer")#computer


            hotspot (1429, 99, 171, 739):#wardrobe

                action Jump("interaction_scarletts_room_wardobe")


        hotspot (1317, 160, 104, 456):#door
            action Jump("interaction_scarletts_room_door")


            #hotspot (700, 180, 300, 300) action Jump("interaction_mc_room_window")#window

        if not winners_party_scarletts_room_secret11_found:
            imagebutton:
                idle "mcroom_party_secret11"
                focus_mask True
                xpos 88 ypos 708
                hover "mcroom_party_secret11_glow"
                action Jump("interaction_winners_party_scarletts_room_secret11")


        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "scarletts_room_winners_party"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "scarletts_room_winners_party"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "scarletts_room_winners_party"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "scarletts_room_winners_party"), Jump("joraell_message_no_phone")
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
        #screen inventory_button #TODO see if can call screen in a screen
        #if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
        #    imagebutton:
        #        idle "inventory_button_idle"
        #        hover "inventory_button_glow"
        #        xpos 3 ypos 3
        #        action [Show("inventory_screen")]#, SetVariable("can_show_inventory_button", False)

        #imagebutton:
        #    idle "back_button_idle"
        #    hover "back_button_hover"
        #    xpos 1405 ypos 820
        #    action Jump("apartment")

label scarletts_room_winners_party:
    call screen scarletts_room_winners_party

### Room-mate room
screen roommate_room:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/02_apartment/05_roommate_room/roommate_room_day.webp"
        hover "destinations/02_apartment/05_roommate_room/roommate_room_day_glow.webp"

        #hotspot (1480, 115, 120, 785) action NullAction()#closet

        hotspot (363, 159, 95, 580) action Jump("apartment_map")#door


        if currently_possessed_scarlett and turned_down_strip_club_owner and sophia_in_her_room_for_webshow:
            imagebutton:
                idle "destinations/02_apartment/05_roommate_room/rm_room_sophia_webcam.png"
                hover "destinations/02_apartment/05_roommate_room/rm_room_sophia_webcam_glow.png"
                xpos 485 ypos 294
                if not had_first_web_show_with_sophia_as_scarlett:
                    action Jump("scenes_sophia_room_accept_webshow_offer")
                elif had_web_show_with_sophia_that_night:
                    action Jump("interaction_mc_apartment_sofias_room_web_cam_sofia") # TODO change sophia position here too

        elif True in (mc_scarlett_needs_shower_after_threesome, need_to_hide_pills_after_threesome, mc_scarlett_leaving_apartment_morning_after_threesome):
            imagebutton:
                idle "destinations/02_apartment/05_roommate_room/sophia_and_ivana_after_threesome_idle.png"
                hover "destinations/02_apartment/05_roommate_room/sophia_and_ivana_after_threesome_glow.png"
                xpos 1001 ypos 228
                action Jump("zoom_sophia_and_ivana_sleeping_after_threesome")
        else:

            hotspot (143, 119, 150, 790) action Jump("interaction_mc_apartment_sofias_room_wardrobe")#wardrobe

            hotspot (1205, 406, 110, 130) action Jump("interaction_mc_apartment_sofias_room_computer")#computer

            #hotspot (1175, 560, 60, 140) action NullAction()#drawer

            hotspot (985, 460, 50, 165) action Jump("interaction_mc_apartment_sofias_room_under_bed")#safe


        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "roommate_room"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "roommate_room"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "roommate_room"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "roommate_room"), Jump("joraell_message_no_phone")
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
        #imagebutton:
        #    idle "back_button_idle"
        #    hover "back_button_hover"
        #    xpos 1405 ypos 820
        #    action Jump("apartment")

label roommate_room:
    if not know_sofias_room_is_unlocked:
        $ know_sofias_room_is_unlocked = True
        scene apartment
        p "Wow, her room is unlocked? That is unusual. Sofia’s room was always locked! I guess there's nobody to keep out anymore."
    call screen roommate_room

screen sophias_room_winners_party:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/02_apartment/05_roommate_room/roommate_room_night.webp"
        hover "destinations/02_apartment/05_roommate_room/roommate_room_night_glow.webp"

        #hotspot (1480, 115, 120, 785) action NullAction()#closet

        hotspot (363, 159, 95, 580) action Jump("apartment_map_winners_party")#door



            #hotspot (143, 119, 150, 790) action Jump("interaction_mc_apartment_sofias_room_wardrobe")#wardrobe
        if had_first_web_show_with_sophia_as_scarlett:
            hotspot (1205, 406, 110, 130) action Jump("interaction_sofias_room_winners_party_computer")#computer

            #hotspot (1175, 560, 60, 140) action NullAction()#drawer

            #hotspot (985, 460, 50, 165) action Jump("interaction_mc_apartment_sofias_room_under_bed")#safe


        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "sophias_room_winners_party"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "sophias_room_winners_party"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "sophias_room_winners_party"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "sophias_room_winners_party"), Jump("joraell_message_no_phone")
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
label sophias_room_winners_party:
    call screen sophias_room_winners_party
### Bathroom
screen bathroom:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/02_apartment/03_bathroom/bathroom_main.webp"
        hover "destinations/02_apartment/03_bathroom/bathroom_main_glow.webp"

        hotspot (595, 390, 80, 80) action Jump("interaction_mc_apartment_bathroom_drawer")#drawer_top_left
        hotspot (755, 390, 80, 85) action Jump("interaction_mc_apartment_bathroom_drawer")#drawer_top_right
        hotspot (595, 510, 80, 170) action Jump("interaction_mc_apartment_bathroom_drawer")#drawer_bottom_left
        hotspot (745, 520, 100, 175) action Jump("interaction_mc_apartment_bathroom_drawer")#drawer_bottom_right

        if currently_posessed_homeless_guy == True and have_showered_as_hobo == False:
            hotspot (200, 20, 220, 583) action Jump("scene_homeless_guy_bathroom_shower")#shower
        elif currently_possessed_scarlett and mc_scarlett_needs_shower_after_threesome:
            hotspot (200, 20, 220, 583) action Jump("scene_mc_scarlett_taking_shower_in_apartment_after_threesome")#shower

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "bathroom"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "bathroom"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "bathroom"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "bathroom"), Jump("joraell_message_no_phone")
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
            action Jump("apartment_map")

label bathroom:
    call screen bathroom

### Bathroom
screen bathroom_with_policeman_sniffing_panties:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/02_apartment/03_bathroom/bathroom_main_policeman.webp"
        hover "destinations/02_apartment/03_bathroom/bathroom_main_policeman_glow.webp"


        hotspot (380, 130, 300, 820) action Jump("sophia_apartment_policeman_dreaming")#pervert_policeman

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "bathroom_with_policeman_sniffing_panties"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "bathroom_with_policeman_sniffing_panties"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "bathroom_with_policeman_sniffing_panties"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "bathroom_with_policeman_sniffing_panties"), Jump("joraell_message_no_phone")
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
            action Jump("apartment_map")

label bathroom_with_policeman_sniffing_panties:
    call screen bathroom_with_policeman_sniffing_panties

screen bathroom_winners_party:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/02_apartment/03_bathroom/bathroom_main.webp"
        hover "destinations/02_apartment/03_bathroom/bathroom_main_glow.webp"


        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "bathroom_winners_party"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "bathroom_winners_party"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "bathroom_winners_party"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "bathroom_winners_party"), Jump("joraell_message_no_phone")
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
            action Jump("apartment_map_winners_party")

label bathroom_winners_party:
    call screen bathroom_winners_party

### Living room
screen living_room:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/02_apartment/04_livingroom/livingroom_main.webp"
        hover "destinations/02_apartment/04_livingroom/livingroom_main_glow.webp"

        hotspot (110, 130, 170, 310) action Jump("apartment_map")#door

        #hotspot (385, 159, 105, 185) action NullAction()#cabinet

        #hotspot (890, 430, 80, 115) action NullAction()#drawer

        #hotspot (1250, 470, 350, 440) action NullAction()#sofa_chair


        if time_to_sleep_after_choices_afternoon or time_to_meet_up_with_ivana_n_sophia_after_choices_afternoon or time_to_test_unlabelled_pills_on_ivana_n_sophia:# or mc_scarlett_needs_shower_after_threesome
            imagebutton:
                idle "destinations/02_apartment/04_livingroom/livingroom_button_girls.png"
                xpos 607 ypos 431
                hover "destinations/02_apartment/04_livingroom/livingroom_button_girls_glow.png"
                if not time_to_test_unlabelled_pills_on_ivana_n_sophia:
                    action Jump("scene_meet_up_with_ivana_n_sophia_after_choices_afternoon")
                else:
                    action Jump("scene_mc_scarlett_with_ivana_n_sophia_threesome")
        else:
            hotspot (570, 540, 260, 130) action Jump("interaction_mc_apartment_living_room_board_game")#board_game

            hotspot (835, 75, 400, 310):#tv
                if currently_posessed_homeless_guy:
                    action Jump("interaction_mc_apartment_living_room_tv")
                else:
                    action Jump("interaction_mc_apartment_living_room_no_watch_tv")

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "living_room"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "living_room"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "living_room"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "living_room"), Jump("joraell_message_no_phone")
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

        #imagebutton:
        #    idle "back_button_idle"
        #    hover "back_button_hover"
        #    xpos 1405 ypos 820
        #    action Jump("apartment")

label living_room:
    call screen living_room

screen living_room_winners_party:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "scenes/Mranders/40_winners_party/sprites/livingroom_party.png"
        hover "scenes/Mranders/40_winners_party/sprites/livingroom_party_glow.png"

        hotspot (110, 130, 170, 310) action Jump("interaction_living_room_door_winners_party")#door

        #hotspot (385, 159, 105, 185) action NullAction()#cabinet

        #hotspot (890, 430, 80, 115) action NullAction()#drawer

        #hotspot (1250, 470, 350, 440) action NullAction()#sofa_chair
        if milestone_mc_anders_recovered_pills_from_scarletts_bedstand:
            imagebutton:
                idle "scenes/Mranders/40_winners_party/sprites/livingroom_party_megan.png"
                xpos 800 ypos 200
                hover "scenes/Mranders/40_winners_party/sprites/livingroom_party_megan_glow.png"
                action Jump("interaction_livingroom_winners_party_megan")

        imagebutton:
            idle "scenes/Mranders/40_winners_party/sprites/livingroom_party_sophia.png"
            xpos 1175 ypos 415
            hover "scenes/Mranders/40_winners_party/sprites/livingroom_party_sophia_glow.png"
            action Jump("interaction_livingroom_winners_party_sophia")

        imagebutton:
            idle "scenes/Mranders/40_winners_party/sprites/livingroom_party_tracyandbrandon.png"
            focus_mask True
            xpos 53 ypos 385
            hover "scenes/Mranders/40_winners_party/sprites/livingroom_party_tracyandbrandon_glow.png"
            action Jump("interaction_livingroom_winners_party_tracyandbrandon")

        imagebutton:
            idle "scenes/Mranders/40_winners_party/sprites/livingroom_party_trophy.png"
            focus_mask True
            xpos 560 ypos 400
            hover "scenes/Mranders/40_winners_party/sprites/livingroom_party_trophy_glow.png"
            action Jump("interaction_livingroom_winners_party_trophy")

        if milestone_winners_party_sophia_asked_for_drinks:
            imagebutton:
                idle "scenes/Mranders/40_winners_party/sprites/livingroom_party_others.png"
                focus_mask True
                xpos 190 ypos 190
                hover "scenes/Mranders/40_winners_party/sprites/livingroom_party_others_glow.png"
                action Jump("interaction_livingroom_winners_party_others")

        if not winners_party_livingroom_secret10_found:
            imagebutton:
                idle "livingroom_party_secret10"
                focus_mask True
                xpos 554 ypos 478
                hover "livingroom_party_secret10_glow"
                action Jump("interaction_winners_party_livingroom_secret10")

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "living_room_winners_party"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "living_room_winners_party"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "living_room_winners_party"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "living_room_winners_party"), Jump("joraell_message_no_phone")
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

        #imagebutton:
        #    idle "back_button_idle"
        #    hover "back_button_hover"
        #    xpos 1405 ypos 820
        #    action Jump("apartment")

label living_room_winners_party:
    if toggle_mc_anders_talked_to_ivana_at_winners_party and not milestone_winners_party_sophia_asked_for_drinks:
        $ milestone_winners_party_sophia_asked_for_drinks = True
        $ hints_counter += 1
        scene anders_s40_winners_party23
        sop "We are really happy to see so many faces at our winning party."
        scene anders_s40_winners_party24 with dissolve
        iva "Yes. It’s the first time we won this tournament."
        sop "And it’s amazing that you all came here to celebrate this victory with us."
        scene anders_s40_winners_party25 with dissolve
        iva "So, enjoy the party. I’m going to prepare drinks for celebrating."

    call screen living_room_winners_party

### Kitchen
screen kitchen:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/02_apartment/01_kitchen/kitchen_main.webp"
        hover "destinations/02_apartment/01_kitchen/kitchen_main_glow.webp"

        #hotspot (0, 573, 400, 340) action NullAction()#chair

        hotspot (103, 20, 220, 583) action Jump("interaction_mc_apartment_kitchen_fridge")#fridge - mast be below chair for hover glow overdraw

        hotspot (495, 370, 230, 190) action Jump("interaction_mc_apartment_kitchen_oven")#oven

        #hotspot (845, 440, 100, 175) action NullAction()#bottom_cuboard

        #hotspot (655, 0, 100, 260) action NullAction()#top_cupboard
        if currently_possessed_scarlett and settled_as_scarlett and not True in (sophia_in_her_room_for_webshow, time_to_sleep_after_choices_afternoon, time_to_meet_up_with_ivana_n_sophia_after_choices_afternoon, mc_scarlett_needs_shower_after_threesome, time_to_test_unlabelled_pills_on_ivana_n_sophia, need_to_hide_pills_after_threesome, mc_scarlett_leaving_apartment_morning_after_threesome,time_to_punish_beth_n_brooke_in_sports_hall):#time_of_day in ('SABAH', 'GECE')
            imagebutton:
                idle "destinations/02_apartment/01_kitchen/sophia_kitchen_button.png"
                hover "destinations/02_apartment/01_kitchen/sophia_kitchen_button_glow.png"
                xpos 733 ypos 160
                if not have_talked_to_sophia_in_kitchen_as_scarlett:
                    action Jump("scenes_kitchen_as_scarlett_talk_to_sophia_after_settled_in")
                elif not have_paid_first_rent_to_sophia_as_scarlett:
                    action Jump("scenes_kitchen_as_scarlett_settle_first_rent_with_sophia")
        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "kitchen"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "kitchen"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "kitchen"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "kitchen"), Jump("joraell_message_no_phone")
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
            action Jump("apartment_map")

label kitchen:
    call screen kitchen

### Kitchen
screen kitchen_winners_party:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/02_apartment/01_kitchen/kitchen_main.webp"
        hover "destinations/02_apartment/01_kitchen/kitchen_main_glow.webp"

        #hotspot (0, 573, 400, 340) action NullAction()#chair
        if accepted_devils_offer_for_anders_soul:
            hotspot (103, 20, 220, 583) action Jump("interaction_kitchen_winners_party_fridge")#fridge - mast be below chair for hover glow overdraw

        if not toggle_mc_anders_talked_to_ivana_at_winners_party or milestone_winners_party_sophia_asked_for_drinks:
            imagebutton:
                idle "kitchen_party_ivana"
                hover "kitchen_party_ivana_glow"
                xpos 733 ypos 160
                action Jump("interaction_kitchen_winners_party_ivana")

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "kitchen_winners_party"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "kitchen_winners_party"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "kitchen_winners_party"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "kitchen_winners_party"), Jump("joraell_message_no_phone")
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
            if accepted_devils_offer_for_anders_soul and toggle_mc_anders_talked_to_ivana_at_winners_party and not toggle_mc_anders_spiked_drinks_at_winners_party:
                action Jump("exit_block_kitchen_winners_party")

            action Jump("apartment_map_winners_party")

label kitchen_winners_party:
    call screen kitchen_winners_party

### Scarlets Shoes
screen scarlets_shoes:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/02_apartment/02_mcroom/mc_room_shoes.png"
        hover "destinations/02_apartment/02_mcroom/mc_room_shoes_glow.png"

        hotspot (320, 196, 393, 501) action Jump("interaction_mc_wardrobe_scarlett_shoes_pink")#pink_shoes

        hotspot (740, 303, 282, 476) action Jump("scene_wardrobe_scarlett_chosen_shoes")#kicks

        hotspot (1030, 245, 435, 497) action Jump("interaction_mc_wardrobe_scarlett_shoes_stilletoes")#stiletoes


        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "scarlets_shoes"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "scarlets_shoes"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "scarlets_shoes"), Show("phone_screen")
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


label scarlets_shoes:
    call screen scarlets_shoes

### Dildo Choices
screen dildo_choices:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/02_apartment/02_mcroom/mc_room_toys.png"
        hover "destinations/02_apartment/02_mcroom/mc_room_toys_glow.png"

        hotspot (100, 180, 700, 150) action Jump("skip_to_sleep")#go_to_sleep

        hotspot (100, 425, 150, 345) action SetVariable("current_dildo_choice",1), Jump("scene_as_scarlett_dildo_choices")#choice_1

        hotspot (310, 445, 200, 325) action SetVariable("current_dildo_choice",2), Jump("scene_as_scarlett_dildo_choices")#choice_2

        hotspot (600, 375, 260, 435) action SetVariable("current_dildo_choice",3), Jump("scene_as_scarlett_dildo_choices")#choice_3

        hotspot (900, 430, 130, 340) action SetVariable("current_dildo_choice",4), Jump("scene_as_scarlett_dildo_choices")#choice_4

        hotspot (1050, 270, 190, 530) action SetVariable("current_dildo_choice",5), Jump("scene_as_scarlett_dildo_choices")#choice_5

        hotspot (1300, 190, 220, 630) action SetVariable("current_dildo_choice",6), Jump("scene_as_scarlett_dildo_choices")#choice_6


        #if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
        #    hotspot (0, 0, 70, 65):
        #        hovered SetVariable("menu_can_show_hint_hover", True)
        #        unhovered SetVariable("menu_can_show_hint_hover", False)
        #        if are_hints_available:
        #            action SetVariable("current_screen", "dildo_choices"), Jump("display_current_hint")
        #        else:
        #            action SetVariable("current_screen", "dildo_choices"), Jump("joraell_message_no_hints")
        #    hotspot (0, 65, 70, 65):
        #        hovered SetVariable("menu_can_show_phone_hover", True)
        #        unhovered SetVariable("menu_can_show_phone_hover", False)
        #        action SetVariable("current_screen", "dildo_choices"), Show("phone_screen")
        #    hotspot (0, 130, 70, 65):
        #        hovered SetVariable("menu_can_show_inventory_hover", True)
        #        unhovered SetVariable("menu_can_show_inventory_hover", False)
        #        action Show("inventory_screen")
        #    imagebutton:
        #        if menu_can_show_inventory_hover == False and menu_can_show_phone_hover == False and menu_can_show_hint_hover == False:
        #            idle "game_menu"
        #        elif menu_can_show_hint_hover == True:
        #            idle "game_menu_hint_glow"
        #        elif menu_can_show_phone_hover == True:
        #            idle "game_menu_phone_glow"
        #        elif menu_can_show_inventory_hover == True:
        #            idle "game_menu_inventory_glow"


label dildo_choices:
    scene scarlett_s20_toys01
    p "Hmmm… Maybe I can try one of these toys?"
    scene scarlett_s20_toys02
    p "Let’s see which one I'm in the mood for."
    call screen dildo_choices

label interaction_mc_room_door_cant_get_out:
    show mc_room_day
    p "I can't turn the door handle."
    jump mc_room

label interaction_mc_room_door_cant_leave_yet:
    show mc_room_day_cathy_policeman
    p "I can't leave just yet. I need to find out what happened."
    jump mc_room_with_sofia_and_policeman

label interaction_mc_room_door_sophia_home_early:
    if mc_room_window_opened == True:
        show mc_room_openedwindow
    else:
        show mc_room_day
    p "I can't let Sophia see me like this. She would freak out."
    jump mc_room

label interaction_mc_room_computer:
    if mc_room_window_opened == True:
        show mc_room_openedwindow
    else:
        show mc_room_day
    if need_to_access_flash_drive_at_home == True:
        jump scene_try_flash_drive_on_pc
    elif have_taken_keys_from_sewer == True:
        jump mc_room_computer_turn_on_folder_visible#TODO
    else:
        p "I can't turn on the computer."
        if mc_looked_at_computer == False:
            $ mc_looked_at_computer = True
    jump mc_room

label interaction_mc_room_small_box:
    if currently_posessed_homeless_guy == True and seen_hobo_mad == False:
        jump scene_homeless_guy_mc_room_money_stolen
    else:
        if mc_room_window_opened == True:
            show mc_room_openedwindow
        else:
            show mc_room_day
        if have_taken_keys_from_sewer == True:
            if currently_posessed_homeless_guy:
                p "(Who the fuck, stole my money! Do I have to fucking sleep under a fucking bridge!)"
            elif currently_possessed_brandon:
                p "Who the hell took my money anyway. It would have saved me a lot of trouble if I had it."
        else:
            p "I can't open the box."
            if mc_looked_at_small_box == False:
                $ mc_looked_at_small_box = True
        jump mc_room

label interaction_mc_room_bedside_table:
    if mc_room_window_opened == True:
        show mc_room_openedwindow
    else:
        show mc_room_day
    if have_taken_keys_from_sewer == True:
        p "Fuck! Where the hell's my stuff! Did the cops take it?"
    else:
        p "I can't open the drawer."
        if mc_looked_at_bedside_table == False:
            $ mc_looked_at_bedside_table = True
    jump mc_room

label interaction_mc_room_wardobe:
    if mc_room_window_opened == True:
        show mc_room_openedwindow
    else:
        show mc_room_day
    if have_taken_keys_from_sewer == True:
        p "None of my stuff is going to fit this bum."
    else:
        p "I can't get in there."
        if mc_looked_at_wardrobe == False:
            $ mc_looked_at_wardrobe = True
    jump mc_room

label interaction_apartment_map_mc_room_police_still_there:
    show apartment
    p "I don't want to get trapped there again."

    jump apartment_map

label interaction_apartment_map_city_map_cant_leave_yet:
    show apartment
    p "I can't leave just yet. I should look around more."
    jump apartment_map

label interaction_apartment_map_closed_doors:
    show apartment
    p "The door's closed. I can't get through when I'm like this."
    jump apartment_map
label interaction_apartment_map_hobo_should_stay:
    show apartment
    p "I shouldn't chance it. I don't want to be seen leaving here like this."
    jump apartment_map

label interaction_apartment_map_as_scarlett_need_talk_sophia:
    show apartment
    p "I should talk with Sophia before I leave."
    jump apartment_map


label interaction_mc_room_window:
    show mc_room_openedwindow
    if mc_room_window_opened == True:
        if currently_posessed_homeless_guy == True:
            if have_showered_as_hobo == True:
                p "I need to get out of here before Sophia sees me."
                $ time_of_day = Set_Time_of_Day('GECE')
                jump park_main
            else:
                p "I'm not leaving by the fire escape unless I have to."
    else:

        p "In case I need to get back in here without using the door."
        $ mc_room_window_opened = True
    jump mc_room



label scenes_mc_room_computer_folder_ex:
if show_exgf_button_on_phone == False:
    $ show_exgf_button_on_phone = True
scene exgfs01_at_beach01
p "Aaah. These are my old photos of my ex."
scene exgfs01_at_beach02
p "Yeah, I remember that day."
scene exgfs01_at_beach03
p "We were both alone on the beach and I was taking those photos. She was so shy - but so damn beautiful."
scene exgfs01_at_beach04
p "Those were good times."
jump mc_room_computer_turn_on_folder_visible



label scenes_mc_room_computer_folder_secret:
    scene latex_angel1
    $ renpy.pause()
    scene latex_angel2
    $ renpy.pause()
    scene latex_angel3
    $ renpy.pause()
    scene megan_and_ivana1
    $ renpy.pause()
    scene megan_and_ivana2
    $ renpy.pause()
    scene megan_and_ivana3
    $ renpy.pause()
    scene megan_and_ivana4
    $ renpy.pause()
    scene megan_and_ivana5
    $ renpy.pause()
    scene mom_bath1
    $ renpy.pause()
    scene mom_bath2
    $ renpy.pause()
    scene mom_bath3
    $ renpy.pause()
    scene mom_bath4
    $ renpy.pause()
    if seen_secret_pics_mc_computer == False:
        $ seen_secret_pics_mc_computer = True
    jor "You found secret pics. You can view them again on your phone."
    jump mc_room_computer_turn_on_folder_visible


label interaction_mc_apartment_bathroom_drawer:
    scene bathroom_main
    p "Only Sophia’s stuff, nothing important."
    jump bathroom

label interaction_mc_apartment_living_room_tv:
    scene hobo_tv
    dr "It all happened so fast in just a moment really. He was suddenly standing in front of my car."
    p "I really do not want to be reminded of that again!"
    jump living_room

label interaction_mc_apartment_living_room_board_game:
    scene livingroom_main
    p "There is no time to play games right now."
    jump living_room

label interaction_mc_apartment_living_room_no_watch_tv:
    scene livingroom_main
    p "It's too depressing to watch tv, after last time."
    jump living_room

label interaction_mc_apartment_kitchen_oven:
    scene kitchen_main
    p "What am I expecting in the oven? Turkey?"
    jump kitchen

label interaction_mc_apartment_kitchen_fridge:
    scene kitchen_main
    p "Aeergh! As always, just full of vegetables and healthy food."
    jump kitchen

label interaction_mc_apartment_sofias_room_computer:
    scene roommate_room_day
    p "If I know Sophia, her computer probably doesn’t work properly."
    jump roommate_room

label interaction_mc_apartment_sofias_room_wardrobe:
    scene roommate_room_day
    p "Just full of her stuff. Especially shoes. Because she is a shoes freak!"
    jump roommate_room

label interaction_mc_apartment_sofias_room_under_bed:
    scene roommate_room_day
    p "Hmmm, this must be heaven for that perverted cop. Big drawer full of panties. Unfortunately, I’m not a collector of this stuff."
    jump roommate_room

label interaction_mc_wardrobe_scarlett_shoes_pink:
    scene mc_room_shoes
    p "Are those even shoes? Why do small girls wear these… these things? They look really weird."
    jump scarlets_shoes
label interaction_mc_wardrobe_scarlett_shoes_stilletoes:
    scene mc_room_shoes
    p "Hmm, hell no. I almost broke my ankles once, already."
    jump scarlets_shoes


label interaction_mc_room_door_not_settled_as_scarlett:
    show mc_room_day
    p "I don't want to do anything but go to bed. It's been a long day."
    jump mc_room


label interaction_mc_room_bedside_table_scarlett:
    if not settled_as_scarlett:
        scene mc_room_day
        if not have_changed_clothes_as_scarlett:
            if not have_opened_scarletts_box:
                show mc_room_box:
                    xpos 730 ypos 650
            p "I want to get out of these disgusting clothes, before I go to sleep."
            jump mc_room
        elif not have_opened_scarletts_box:
            show mc_room_box:
                xpos 730 ypos 650
            p "Before I go to sleep, I want to check out that box."
            jump mc_room
        jump dildo_choices
    else:
        if time_of_day != 'GECE':
            scene mc_room_day
            p "It's not time to go to bed yet."
            jump mc_room
        elif not have_paid_first_rent_to_sophia_as_scarlett:
            scene mc_room_night
            p "I should sort out the rent with Sophia before I go to sleep."
            jump mc_room
        elif mc_scarlett_needs_shower_after_threesome:
            scene mc_room_night
            p "I should get a shower before I go to sleep."
            jump mc_room
        elif need_to_hide_pills_after_threesome:
            jump scene_mc_scarlett_hiding_pills_behind_bedside_cabinet
        jump dildo_choices

label interaction_mc_room_wardobe_scarlett:
    if not have_changed_clothes_as_scarlett:
        jump scene_wardrobe_scarlett_changing_clothes
    else:
        if time_of_day != 'GECE':
            scene mc_room_day
        else:
            scene mc_room_night
        p "I have everything I need from there."
        jump mc_room

label interaction_mc_apartment_sofias_room_web_cam_sofia:
    scene roommate_room_day
    show rm_room_sophia_webcam:
        xpos 485 ypos 294
    p "I think that's enough for one night."
    jump roommate_room


label interaction_apartment_map_mc_scarlett_need_shower_after_threesome:
    show apartment
    p "I can't go out naked and soaked in juices. I should get a shower."
    jump apartment_map

label interaction_apartment_map_mc_scarlett_need_bed_after_threesome:
    show apartment
    p "I think I need to rest now. It's been an eventful day"
    jump apartment_map


label zoom_sophia_and_ivana_sleeping_after_threesome:
    scene sophia_and_ivana_after_threesome_zoom
    p "I should let them sleep. They need their rest."
    scene sophia_and_ivana_after_threesome_zoom2

    jump roommate_room

label interaction_living_room_door_winners_party:
    scene livingroom_party
    show livingroom_party_sophia:
        xpos 1175 ypos 415
    show livingroom_party_tracyandbrandon:
        xpos 53 ypos 385
    show livingroom_party_trophy:
        xpos 560 ypos 400
    if not toggle_mc_anders_talked_to_sophia_at_winners_party:
        p "I want to first talk to Sophia."
        jump living_room_winners_party
    jump apartment_map_winners_party

label interaction_livingroom_winners_party_megan:
    scene anders_s40_winners_party27
    p "Hi, Megan."
    scene anders_s40_winners_party28 with dissolve
    meg "Hello, Professor."
    p "Please, call me Thomas."
    scene anders_s40_winners_party29 with dissolve
    meg "Ah. I still can’t get used to it."
    p "How are you Megan?"
    scene anders_s40_winners_party31 with dissolve
    meg "A little sleepy. I think I need to move a little."
    scene anders_s40_winners_party27 with dissolve
    meg "Care to dance, Thomas?"
    p "Ehhm. I’m not the best dancer, but with a nice girl, dancing is always much easier."
    scene anders_s40_winners_party28 with dissolve
    meg "Hihi. So one dance with me?"
    p "Of course. That, I can’t refuse."
    scene anders_s40_winners_party30
    meg "Great."
    scene anders_s40_winners_party35
    pause
    scene anders_s40_winners_party33
    pause
    scene anders_s40_winners_party32
    meg "I must say, your dancing is really good."
    p "Like I said. With a nice girl it’s always easier. My body just feels your rhythm."
    scene anders_s40_winners_party34 with fade
    "After many more songs..."
    meg "Whuf. I think my legs will fall off."
    p "Mine too."
    meg "I enjoyed it a lot!"
    scene anders_s40_winners_party35
    p "It was my pleasure to dance with you, Megan."
    sop "Alright, people. It’s time for the celebration drink! Everybody please get your glasses from the table!"

    scene anders_s40_winners_party39
    pause
    scene anders_s40_winners_party40
    sop "As I said before, it’s amazing to be here with all of you great friends and awesome people."
    scrlt "For the WINNERS!!!"
    iva "Cheers!"
    scene anders_s40_winners_party42
    "Crowd" "Cheers!"
    jump scene_winners_party_winners_toast_choices

label interaction_livingroom_winners_party_sophia:
    if toggle_mc_anders_talked_to_sophia_at_winners_party:
        scene anders_s40_winners_party61
        p "I already talked to her. I have things to do."
    else:
        scene anders_s40_winners_party06
        sop "Are you enjoying the party?"
        p "Yes. It’s looking good so far. Where are the girls?"
        sop "I’m waiting on Ivana, she is preparing something in the kitchen. Can you please tell her that all the guests are here already and I need to talk to her."
        p "Of course."
        $ toggle_mc_anders_talked_to_sophia_at_winners_party = True
        $ hints_counter += 1
    jump living_room_winners_party

label interaction_livingroom_winners_party_tracyandbrandon:
    if toggle_mc_anders_talked_to_tracyandbrandon_at_winners_party:
        scene anders_s40_winners_party62
        p "I'll leave them to enjoy the party."
    else:
        scene anders_s40_winners_party14
        bran "Hello Mr. Anders."
        p "Hi Brandon."
        bran "This is our biology professor Mr. Anders and this is my friend Tracy."
        p "(Friend?. Damn, that little freak. He’s hiding, she\'s his sister?)"
        scene anders_s40_winners_party15 with dissolve
        trcy "Nice to meet you Mr. Anders."
        p "It’s nice to meet you too, young lady."
        p "I don\'t remember seeing you at our school..."
        trcy "No.. heh. I’m not going to the same school."
        p "Aah."
        scene anders_s40_winners_party16 with dissolve
        trcy "I’m here just for a short vacation."
        p "Cool. Enjoy the party guys."
        bran "We will."
        $ toggle_mc_anders_talked_to_tracyandbrandon_at_winners_party = True
    jump living_room_winners_party

label interaction_livingroom_winners_party_trophy:
    scene anders_s40_winners_party53
    $ renpy.pause(1.0)

    scene anders_s40_winners_party54
    p "It's a really nice looking trophy."
    jump living_room_winners_party

label interaction_livingroom_winners_party_others:
    scene anders_s40_winners_party63
    p "I don’t recognize any of these people. Probably just some friends of the girls."
    jump living_room_winners_party

label interaction_winners_party_livingroom_secret10:
    scene livingroom_party
    show livingroom_party_secret10:
        xpos 554 ypos 478
    show livingroom_party_sophia:
        xpos 1175 ypos 415
    show livingroom_party_tracyandbrandon:
        xpos 53 ypos 385
    show livingroom_party_trophy:
        xpos 560 ypos 400
    if milestone_mc_anders_recovered_pills_from_scarletts_bedstand:
        show livingroom_party_megan:
            xpos 800 ypos 200
    if milestone_winners_party_sophia_asked_for_drinks:
        show livingroom_party_others:
            xpos 190 ypos 190


    $ winners_party_livingroom_secret10_found = True
    jor "You have found secret 10. You can view it on your phone."
    jump living_room_winners_party

label interaction_winners_party_scarletts_room_secret11:
    scene mc_room_night
    if not milestone_mc_anders_found_scarletts_flash_drive:
        show mcroom_party_scarlett:
            xpos 951 ypos 388
    if not milestone_winners_party_sophia_asked_for_drinks:
        show mcroom_party_others:
            xpos 501 ypos 228
    show mcroom_party_secret11:
        xpos 88 ypos 708

    $ winners_party_scarletts_room_secret11_found = True
    jor "You have found secret 11. You can view it on your phone."
    jump scarletts_room_winners_party

label interaction_scarlett_scarletts_room_winners_party:
    if not milestone_winners_party_sophia_asked_for_drinks:
        scene anders_s40_winners_party64
        #show mcroom_party_scarlett:
            #xpos 951
            #ypos 388
        p "Looks like Scarlett’s looking for something. Maybe it will be better to talk first with Ivana. And after the party begins, they will all move to the living room."
    else:
        if onetime_mc_anders_looking_for_scarletts_flash_drive:
            scene anders_s40_winners_party17
            scrlt "Did you find that flash drive?"
            p "Not yet."
            scrlt "Keep looking."
        else:
            scene anders_s40_winners_party17
            p "Hi, Scarlett."
            scene anders_s40_winners_party18
            scrlt "Ooooh!"
            scene anders_s40_winners_party20 with dissolve
            scrlt "Oh. Professor."
            p "I’m sorry for scaring you."
            scrlt "It’s fine. I don’t know why I’m always scared by your voice, hihi."
            scrlt "Are you enjoying the party?"
            p "Yes, I am. But why aren't you with the others?"
            scene anders_s40_winners_party21
            scrlt "Cause I have prepared a nice song playlist on my flashdrive, but cannot find it anywhere."
            p "AAh. Maybe I can help you find it?"
            scrlt "That would be great."
            $ onetime_mc_anders_looking_for_scarletts_flash_drive = True
            $ hints_counter += 1
    jump scarletts_room_winners_party

label interaction_others_scarletts_room_winners_party:
    scene anders_s40_winners_party65
    p "Damn, I need to get the pills behind the bed stand, but I need this room to be empty first."
    jump scarletts_room_winners_party


label interaction_kitchen_winners_party_ivana:
    if milestone_winners_party_sophia_asked_for_drinks:
        scene anders_s40_winners_party66
        #show kitchen_party_ivana
        iva "I’m sorry. But I don’t have time right now. I must prepare the drinks."
    else:
        scene anders_s40_winners_party08
        p "Hi Ivana."
        scene anders_s40_winners_party09 with dissolve
        iva "Hello professor. I’m really happy that you came to the party."
        p "I’m happy too. I couldn’t refuse the invitation."

        if not mc_scarlett_accepted_devils_help_with_anders and not toggle_mc_scarlett_chose_sophia:#toggle_mc_scarlett_chose_ivana
            if toggle_mc_anders_fucked_ivana_in_office or renpy.seen_label("scene_mc_anders_office_sex_with_ivana"):
                scene anders_s40_winners_party11 with dissolve
                iva "Aaah. I know what you are talking about professor."
                scene anders_s40_winners_party12 with dissolve
                scene anders_s40_winners_party13 with dissolve
                iva "Maybe we can play a little..."
                p "Wow. I wish we had time now. But, I think Sophia is waiting for you in the living room."

            else:
                scene anders_s40_winners_party11 with dissolve
                iva "Aaah. I know what you are talking about, Professor. I think you have a crush on me."
                p "You are a really nice young lady, Ivana, but I think Sophia is waiting for you in the living room."
        else:
            p "Sophia is waiting for you in the living room."
            scene anders_s40_winners_party10 with dissolve
            iva "Aah, I almost forgot."
            scene anders_s40_winners_party09 with dissolve
            iva "I’m on my way."
        $ toggle_mc_anders_talked_to_ivana_at_winners_party = True
        if accepted_devils_offer_for_anders_soul:
            $ hints_counter += 1
        else:
            $ hints_counter += 2
    jump kitchen_winners_party


label interaction_kitchen_winners_party_fridge:
    scene kitchen_main
    if not toggle_mc_anders_talked_to_ivana_at_winners_party:
        show kitchen_party_ivana
        p "I must put the pills into drinks, but Ivana is still here. I can’t do it now."
    elif toggle_mc_anders_talked_to_ivana_at_winners_party:
        if not toggle_mc_anders_spiked_drinks_at_winners_party:
            $ toggle_mc_anders_spiked_drinks_at_winners_party = True
            $ hints_counter += 1
            p "Finally, the kitchen is empty for a while."
            scene anders_s40_winners_party37
            p "Looks like the girls are well prepared for the party."
            scene anders_s40_winners_party38
            p "Hopefully it will be enough. And all get sleep after that drink. Anyway with horny pills that can be much more fun party, but my pills are still hidden behind the bedstand in Scarlett’s room."
        else:
            if milestone_winners_party_sophia_asked_for_drinks:
                show kitchen_party_ivana
            p "It's done. I shouldn't arouse any more suspicion."
    jump kitchen_winners_party

label exit_block_kitchen_winners_party:
    scene kitchen_main
    p "Ivana's left the room. Now's my chance to do what Brooke said."
    jump kitchen_winners_party

label interaction_sofias_room_winners_party_computer:
    scene roommate_room_night
    play music "sounds/music/Background_music2_Brunno.ogg"
    p "Hmmm... Sophia has a video file with a recorded webshow. Is that the show I made with her as Scarlett?"
    scene anders_s43_sophia_and_scarlett01
    p "Hmm, nooo. Looks like this is another webshow."
    sop "Hello my supporters. I’m here with a new video for my fanclub."
    sop "And today I have here my good friend Scarlett!"
    scene anders_s43_sophia_and_scarlett02 with dissolve
    scrlt "Hi, guys!"
    scene anders_s43_sophia_and_scarlett03
    p "Mmm... Nice start."
    scene anders_s43_sophia_and_scarlett04
    sop "So, sit comfortably…"
    scene anders_s43_sophia_and_scarlett05 with dissolve
    scrlt "And enjoy the show!"
    scene anders_s43_sophia_and_scarlett06
    pause
    scene anders_s43_sophia_and_scarlett07
    p "Mmm. Some sweet asses..."
    scene anders_s43_sophia_and_scarlett08
    sop "Mlm mlmlm…."
    scene anders_s43_sophia_and_scarlett09
    pause
    scene anders_s43_sophia_and_scarlett10
    scrlt "Yes. I love it on that spot!"
    scene anders_s43_sophia_and_scarlett11
    sop "I know, baby…"
    scene anders_s43_sophia_and_scarlett12
    pause
    scene anders_s43_sophia_and_scarlett13
    scrlt "You’re making me so fucking horny!"
    scene anders_s43_sophia_and_scarlett14
    p "Looks like they both enjoy licking and kissing each other's necks..."
    scene anders_s43_sophia_and_scarlett15
    scrlt "Let’s take out that robe."
    scene anders_s43_sophia_and_scarlett16
    sop "Okay…."
    scene anders_s43_sophia_and_scarlett17
    scrlt "Turn around."
    scene anders_s43_sophia_and_scarlett19
    p "They’re starting to heat me up. Even on video. Wow."
    scene anders_s43_sophia_and_scarlett20
    pause
    scene anders_s43_sophia_and_scarlett22
    p "Woow. Sophia has pretty big boobs in that bra."
    scene anders_s43_sophia_and_scarlett21
    pause (0.5)
    scene anders_s43_sophia_and_scarlett25 with dissolve
    pause (1.0)
    scene anders_s43_sophia_and_scarlett23
    pause (0.5)
    sop "I love you squeezing my breast."
    scene anders_s43_sophia_and_scarlett26
    pause (0.5)
    scene anders_s43_sophia_and_scarlett24 with dissolve
    pause (1.0)
    scene anders_s43_sophia_and_scarlett27
    pause (0.5)
    scrlt "Mmmm. *lick*"
    scene anders_s43_sophia_and_scarlett28
    sop "Oh, yes…"
    scene anders_s43_sophia_and_scarlett29
    sop "I love your tongue, honey."
    scene anders_s43_sophia_and_scarlett30
    sop "And your touches."
    sop "I’m so wet already. I feel my panties are soaked. Just let me take care of you too."
    scene anders_s43_sophia_and_scarlett31
    pause (1.0)
    scene anders_s43_sophia_and_scarlett32 with dissolve
    pause (1.0)
    scrlt "Ohhh. You are so good!"
    scene anders_s43_sophia_and_scarlett33
    scrlt "Yes. YES!"
    scene anders_s43_sophia_and_scarlett34
    scrlt "I want your tongue in my pussy Sophia."
    scene anders_s43_sophia_and_scarlett35
    pause (0.5)
    scene anders_s43_sophia_and_scarlett36 with dissolve
    pause (1.0)
    #animation:  anders_s43_sophia_and_scarlett_panty
    scene anders_s43_sophia_and_scarlett37
    $ renpy.movie_cutscene("scenes/Mranders/43_sophia_and_scarlett/WEBM/anders_s43_sophia_and_scarlett_panty.webm", loops=0, delay=-1, stop_music=False)
    scene anders_s43_sophia_and_scarlett37
    pause (1.5)
    scene anders_s43_sophia_and_scarlett40
    scrlt "Aaah. You are a master at this baby!"
    scene anders_s43_sophia_and_scarlett41
    scrlt "Yes. Don’t even try to stop!!!"
    scene anders_s43_sophia_and_scarlett38
    pause(1.0)
    #animation
    # anders_s43_sophia_and_scarlett_fingering1
    scene anders_s43_sophia_and_scarlett_transfer1
    $ renpy.movie_cutscene("scenes/Mranders/43_sophia_and_scarlett/WEBM/anders_s43_sophia_and_scarlett_fingering1.webm", loops=0, delay=-1, stop_music=False)
    # anders_s43_sophia_and_scarlett_fingering2
    $ renpy.movie_cutscene("scenes/Mranders/43_sophia_and_scarlett/WEBM/anders_s43_sophia_and_scarlett_fingering2.webm", loops=0, delay=-1, stop_music=False)
    scene anders_s43_sophia_and_scarlett_transfer2
    $ renpy.movie_cutscene("scenes/Mranders/43_sophia_and_scarlett/WEBM/anders_s43_sophia_and_scarlett_fingering1.webm", loops=0, delay=-1, stop_music=False)
    # anders_s43_sophia_and_scarlett_fingering3
    scene anders_s43_sophia_and_scarlett_transfer3
    $ renpy.movie_cutscene("scenes/Mranders/43_sophia_and_scarlett/WEBM/anders_s43_sophia_and_scarlett_fingering3.webm", loops=0, delay=-1, stop_music=False)
    scene anders_s43_sophia_and_scarlett_transfer1
    $ renpy.movie_cutscene("scenes/Mranders/43_sophia_and_scarlett/WEBM/anders_s43_sophia_and_scarlett_fingering1.webm", loops=0, delay=-1, stop_music=False)
    $ renpy.movie_cutscene("scenes/Mranders/43_sophia_and_scarlett/WEBM/anders_s43_sophia_and_scarlett_fingering2.webm", loops=0, delay=-1, stop_music=False)
    $ renpy.movie_cutscene("scenes/Mranders/43_sophia_and_scarlett/WEBM/anders_s43_sophia_and_scarlett_fingering1.webm", loops=0, delay=-1, stop_music=False)
    scene anders_s43_sophia_and_scarlett39
    scrlt "I’m cummmming!!!"
    scene anders_s43_sophia_and_scarlett41
    scrlt "AAArrr!!!"
    #(whacking screen)
    with hpunch
    scrlt " Now is my turn, baby."
    scene anders_s43_sophia_and_scarlett42
    sop "Oh. Oh… Ah."
    scene anders_s43_sophia_and_scarlett43
    pause
    scene anders_s43_sophia_and_scarlett44
    pause
    scene anders_s43_sophia_and_scarlett45
    sop "You made me cum so fast!!!"
    with hpunch
    sop "OOOOH!!!"
    scene anders_s43_sophia_and_scarlett46
    sop "Mmmmm… *kisses*"
    scene anders_s43_sophia_and_scarlett47
    scrlt "Mmm. That was excellent!"
    scene anders_s43_sophia_and_scarlett48
    sop "Unforgettable…."
    stop music fadeout 2.0

    scene roommate_room_night
    p "Well. Pretty hot scene. The girls have some really nice skills."
    $ toggle_mc_anders_viewed_webshow_at_winners_party = True
    jump sophias_room_winners_party

label exit_block_apartment_map_winners_party_no_leaving:
    scene apartment_winners_party
    p "I shouldn\'t leave right now."
    jump apartment_map_winners_party

label interaction_scarletts_room_computer:
    scene anders_s40_winners_party57
    p "Here's the flash drive here."
    p "Here Scarlett. You forgot to check behind the computer."
    scene anders_s40_winners_party58
    scrlt "Thank you."
    #after this remove scarlett sprite from room.
    $ onetime_mc_anders_looking_for_scarletts_flash_drive = False
    $ milestone_mc_anders_found_scarletts_flash_drive = True
    $ onetime_mc_anders_time_to_recover_pills_from_bedstand = True
    $ hints_counter += 1
    #$ inventory.add(assorted_pills)

    jump scarletts_room_winners_party

label interaction_scarletts_room_door:
    scene mc_room_night
    if not winners_party_scarletts_room_secret11_found:
        show mcroom_party_secret11:
            xpos 88 ypos 708
    if onetime_mc_anders_looking_for_scarletts_flash_drive:
        show mcroom_party_scarlett:
            xpos 951 ypos 388
        p "(I need to help find that flashdrive.)"
        jump scarletts_room_winners_party
    elif onetime_mc_anders_time_to_recover_pills_from_bedstand:
        p "(The room is clear. Now's my chance to get back the pills.)"
        jump scarletts_room_winners_party
    else:
        jump apartment_map_winners_party

label interaction_scarletts_room_wardobe:
    scene mc_room_night
    show mcroom_party_scarlett:
        xpos 951 ypos 388
    if not winners_party_scarletts_room_secret11_found:
        show mcroom_party_secret11:
            xpos 88 ypos 708
    p "I looked into the pockets of her jacket and found nothing."

    jump scarletts_room_winners_party

label interaction_scarletts_room_bedside_table:
    scene anders_s40_winners_party22
    if onetime_mc_anders_looking_for_scarletts_flash_drive:
        p "I know what is hidden behind this. Hopefully Scarlett didn’t find that secret place yet."
    elif onetime_mc_anders_time_to_recover_pills_from_bedstand:
        $ onetime_mc_anders_time_to_recover_pills_from_bedstand = False
        $ milestone_mc_anders_recovered_pills_from_scarletts_bedstand = True
        p "Hmmm. Looks like nobody found the secret place."
        scene anders_s40_winners_party26
        p "Great! I have them all. Finally. Now, let’s party!"
        $ hints_counter += 1
        if horny_pills in inventory.items:
            $ inventory.drop(horny_pills)
        if shrinking_pills in inventory.items:
            $ inventory.drop(shrinking_pills)
        $ horny_pills = Item("Horny Pills", element="PuzzleItem28", image="hornypills_inventory", cost=0)
        $ renpy.pause(0.001)
        $ inventory.add(horny_pills)
        $ inventory.add(growing_pills)
        $ inventory.add(reducing_pills)

    jump scarletts_room_winners_party

label scene_winners_party_winners_toast_choices:
    scene anders_s40_winners_party60
    if accepted_devils_offer_for_anders_soul:
        menu:
            p "Should I let Megan drink that spiked drink?"
            "YES":
                p "(Aaah, party is over)"
                jump scene_winners_party_winners_toast_all_sleep
            "NO":
                $ toggle_mc_anders_spilled_megans_spiked_drink_winners_party = True
                jump scene_mc_anders_spilled_megans_drink_winners_party
    else:
        jump scene_winners_party_winners_toast_all_sleep
label scene_winners_party_winners_toast_all_sleep:
    scene anders_s40_winners_party59
    "After a short time..."
    scene anders_s40_winners_party49
    meg "Aaaawwww. I’m feeling sooo sleepy."
    scene anders_s40_winners_party50
    if accepted_devils_offer_for_anders_soul:
        p "(I think it will be better to pretend to be sleeping too. To not get anyone suspicious.)"
    p "Eeeeh. What’s happening?"
    scene anders_s40_winners_party51
    bran "ZZZzzzzZZzzZZzZ"
    scene anders_s40_winners_party52
    iva "Shhhh….. Zzzzzz."
    scene anders_s40_winners_party56
    sop "ZzzzzzzZZzzzZZ."
    scene anders_s40_winners_party55
    jump scene_brooke_and_gang_showing_up_at_winners_party

label scene_brooke_and_gang_showing_up_at_winners_party:
    scene black
    "Meanwhile at the party..."
    scene anders_s41_steal_the_trophy01
    brook "Finally, you two arrived."
    scene anders_s41_steal_the_trophy02
    nick "Aww, sorry honey, I was looking for a mask."
    scene anders_s41_steal_the_trophy03
    brook "Fine. Hey Beth. Are you going to a BDSM party?"
    scene anders_s41_steal_the_trophy04
    beth "Heh heh. I don’t have any other tight suits at home."
    brook "Fine. Masks on."
    scene anders_s41_steal_the_trophy05
    beth "AAaaah!!!"
    scene anders_s41_steal_the_trophy07
    brook "Oh my fucking god? !!! Why are you screaming?"
    beth "I’m sorry, but that mask looks so scary."
    brook "Aarrgh…. Cool. Please be quiet from now on."
    scene anders_s41_steal_the_trophy08
    nick "Hahaha. Aaaah…"
    scene anders_s41_steal_the_trophy06
    beth "Fiiiine. I won’t make any more noise from now on."

    scene anders_s41_steal_the_trophy09
    $ renpy.pause(2.0)

    scene anders_s41_steal_the_trophy10
    $ renpy.pause(2.0)
    scene anders_s40_winners_party55
    brook "Everything looks in order…."
    if accepted_devils_offer_for_anders_soul and not toggle_mc_anders_spilled_megans_spiked_drink_winners_party:
        scene anders_s41_steal_the_trophy11
        $ renpy.pause(2.0)
    scene anders_s41_steal_the_trophy14
    nick "Looks like they’re all asleep. Cool…."
    scene anders_s41_steal_the_trophy12
    brook "Haha. There’s my trophy."
    scene anders_s41_steal_the_trophy22
    beth "Mmm, smells so nice. My favorite."
    brook "What the fuck are you doing?"
    scene anders_s41_steal_the_trophy23
    beth "What? I just want to try one of these drinks. Take your own. There are enough drinks."
    brook "Eeeh? What?? In those drinks, are our sleeping pills, don’t you remember?"
    scene anders_s41_steal_the_trophy24
    beth "Aaaaahhh. Yeah. Heh, I forgot. Hih."
    brook "Be of some use and take a few photos."
    scene anders_s41_steal_the_trophy13
    beth "One special photo for you, Sophia."
    scene anders_s41_steal_the_trophy15
    beth "And another one."
    brook "Shame that I will never be able to show her that one. Haha."
    if accepted_devils_offer_for_anders_soul and not toggle_mc_anders_spilled_megans_spiked_drink_winners_party:
        scene anders_s41_steal_the_trophy16
        nick "What the hell is happening here?"
        nick "Why is she sleeping like that?"
        scene anders_s41_steal_the_trophy17
        nick "And why does he have that stupid expression?"
    scene anders_s41_steal_the_trophy18
    beth "Pleaseee, Brooke, take one photo of me too."
    brook "We don’t have time."
    scene anders_s41_steal_the_trophy19
    beth "Aww… Okay…"
    scene anders_s41_steal_the_trophy20
    beth "Peace out, losers!"
    scene anders_s41_steal_the_trophy21
    beth "Who is the winner now?"
    brook "Haha. That was an easy win."
    if accepted_devils_offer_for_anders_soul:
        if toggle_mc_anders_spilled_megans_spiked_drink_winners_party:
            jump scene_mc_anders_arrives_at_home_with_megan_after_winners_party
        elif not toggle_mc_anders_spilled_megans_spiked_drink_winners_party:
            jump scene_mc_anders_winners_party_fun_with_sleeping_girls
    elif not accepted_devils_offer_for_anders_soul:
        jump scene_waking_up_after_winners_party_with_mc_anders

label scene_mc_anders_winners_party_fun_with_sleeping_girls:
    scene black
    "After a while..."
    scene anders_s42_sleeping_bj05
    p "Finally, they’re gone."
    scene anders_s42_sleeping_bj01
    p "And the Trophy is gone. Brooke got what she wanted."
    scene anders_s42_sleeping_bj02 with dissolve
    p "All these girls sleeping around. And will definitely be sleeping for a while. Maybe it's time for my reward?"
    scene anders_s42_sleeping_bj03 with dissolve
    p "Or maybe, I may just wait for them to wake up?"
    scene anders_s42_sleeping_bj06
    menu:
        p "So, what should I do?"
        "Just pretend to sleep":
            p "(Aaah, party is over)"
            jump scene_waking_up_after_winners_party_with_mc_anders
        "Have fun with girls":
            jump scene_mc_anders_playing_with_sleeping_girls_at_winners_party

label scene_mc_anders_playing_with_sleeping_girls_at_winners_party:
    scene anders_s42_sleeping_bj04
    p "I cannot let Megan lay here like that. And the other girls too."
    scene anders_s42_sleeping_bj07
    p "Much better. What a view!"
    scene anders_s42_sleeping_bj08
    p "All so defenseless."
    scene anders_s42_sleeping_bj09
    $ renpy.pause(2.0)
    label winners_party_sleeping_girls_choices:
    scene anders_s42_sleeping_bj10
    if counter_sleeping_girls_winners_party == 0:
        p "So girls, which one of you wants to start?"
        p "Hmm? No one? That\'s a shame. So, I must pick."
    elif counter_sleeping_girls_winners_party == 1:
        p "I think I have time for one more."
    elif counter_sleeping_girls_winners_party == 2:
        p "I think that’s enough. Better clean the mess and pretend to be sleeping to not get anyone suspicious."
        scene anders_s42_sleeping_bj05 with fade
        p "All is cleaned and in order. I think I will really sleep now."
        #TODO missingtrophy
        scene anders_s45_wake_up01 with fade
        "After few hours."
        meg "Mmmmmm…. oh…?"
        scene anders_s45_wake_up02 with dissolve
        meg "What?"
        scene anders_s45_wake_up04
        p "Eeeh."
        scene anders_s45_wake_up06 with dissolve
        p "Eeewww…."
        scene anders_s45_wake_up07 with dissolve
        p "Heh. Hi, Meg."
        scene anders_s45_wake_up08 with dissolve
        p "Is it morning already?"
        scene anders_s45_wake_up03
        meg "What happened here? Why was I sleeping like this?!"
        scene anders_s45_wake_up09
        iva "That was a really wild party..."
        scene anders_s45_wake_up11
        pause
        scene anders_s45_wake_up10 with dissolve
        iva "Wait a second… Where is the trophy? It disappeared?!!"
        scene anders_s45_wake_up12
        sop "Damn. My head is spinning like crazy. I don’t remember anything…"
        scene anders_s45_wake_up05 with dissolve
        iva "Wait a second. It was just a few hours. Look at the time."
        scene anders_s45_wake_up13 with dissolve
        sop "That means...!!!"
        iva "I only know one bitch that would do something like this to us... Brooke."
        sop "I will pluck her hair out…."
        sop "And I won’t be waiting until morning. I’m doing it now…"
        scene anders_s45_wake_up14
        p "Hey girls. Calm down a little. This can get you in a lot of trouble. Let me first talk to her tomorrow and see what happened."
        scene anders_s45_wake_up05
        sop "Pfff... fine. I’m not in the mood to see her stupid face right now, anyway."
        scene anders_s45_wake_up15
        p "Fine."
        scene anders_s45_wake_up05
        iva "I think the party is over."
        sop "Yeah…"
        scene anders_s40_winners_party31
        p "Can I escort you home Megan?"
        meg "Sorry. I think it is not the best idea. Nick is already home, maybe another time..."
        p "But..."
        scene anders_s40_winners_party27 with dissolve
        meg "See you tomorrow at school. Bye, Thomas"
        p "Bye. Megan"
        jump convergence_map_after_winners_party
    $ counter_sleeping_girls_winners_party +=1
    menu:
        "Which girl do I want?"
        "Megan"if not toggle_winners_party_sleeping_girls_chose_megan:
            $ toggle_winners_party_sleeping_girls_chose_megan = True
            #animation:
            #anders_s42_sleeping_bj_megan1 Loop 2 times
            scene anders_s42_sleeping_bj_megan_trans1
            $ renpy.movie_cutscene("scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_megan1.webm", loops=1, delay=-1, stop_music=False)
            #and
            #anders_s42_sleeping_bj_megan2
            $ renpy.movie_cutscene("scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_megan2.webm", loops=0, delay=-1, stop_music=False)
            scene anders_s42_sleeping_bj15
            p "Owww. You have such a nice month Megan."
            scene anders_s42_sleeping_bj16 with dissolve
            scene anders_s42_sleeping_bj17 with dissolve
            p "Aaaaaah!"
            scene anders_s42_sleeping_bj18
            scene anders_s42_sleeping_bj19
            p "Wooow. You made me cum so good!"

        "Sophia"if not toggle_winners_party_sleeping_girls_chose_sophia:
            $ toggle_winners_party_sleeping_girls_chose_sophia = True
            scene anders_s42_sleeping_bj12
            p "I see your smile there, Sophia. You definitely cannot wait to have it fully inside right?"
            scene anders_s42_sleeping_bj13
            p "Oooh yeah, you little slut."
            scene anders_s42_sleeping_bj14
            p "Take it all!"
            scene anders_s42_sleeping_bj15
            p "Oh YEAAH! You started drooling...Niiice!"
            #animation anders_s42_sleeping_bj_sophia1 and anders_s42_sleeping_bj_sophia2
            scene anders_s42_sleeping_bj_sophia_trans1
            $ renpy.movie_cutscene("scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_sophia1.webm", loops=1, delay=-1, stop_music=False)
            $ renpy.movie_cutscene("scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_sophia2.webm", loops=1, delay=-1, stop_music=False)
            scene anders_s42_sleeping_bj15
            p "Owww. Sophia!!"
            scene anders_s42_sleeping_bj16 with dissolve
            scene anders_s42_sleeping_bj17 with dissolve
            p "Sophia!! Aaargh..."
            scene anders_s42_sleeping_bj11
            pause
            scene anders_s42_sleeping_bj26
            p "Wooow. You made me cum so good!"

        "Tracy"if not toggle_winners_party_sleeping_girls_chose_tracy:
            $ toggle_winners_party_sleeping_girls_chose_tracy = True
            p "Time for Brandon’s slutty sister."
            #animation: anders_s42_sleeping_bj_tracy2 and anders_s42_sleeping_bj_tracy1
            scene anders_s42_sleeping_bj_tracy_trans1
            $ renpy.movie_cutscene("scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_tracy1.webm", loops=1, delay=-1, stop_music=False)
            $ renpy.movie_cutscene("scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_tracy2.webm", loops=1, delay=-1, stop_music=False)
            scene anders_s42_sleeping_bj24
            p "YES! You have such a deep throat. Wow!"
            p "You must have trained a lot from our last meeting, hehe. You probably found your calling… haha."
            scene anders_s42_sleeping_bj15
            p "Owww!!"
            scene anders_s42_sleeping_bj16 with dissolve
            scene anders_s42_sleeping_bj17 with dissolve
            scene anders_s42_sleeping_bj25
            p "DAAMN! I came so hard and so deep in her throat that semen is dripping from her nose. Good skills young lady!"

        "Scarlett"if not toggle_winners_party_sleeping_girls_chose_scarlett:
            $ toggle_winners_party_sleeping_girls_chose_scarlett = True
            #animation anders_s42_sleeping_bj_scarlett2 and anders_s42_sleeping_bj_scarlett1
            scene anders_s42_sleeping_bj_scarlett_trans1
            $ renpy.movie_cutscene("scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_scarlett1.webm", loops=1, delay=-1, stop_music=False)
            scene anders_s42_sleeping_bj15
            p "Holy shit. That throat bulge is HUGE! Your throat is tight like no one's Scarlett. I can’t get enough of it!"
            #animation anders_s42_sleeping_bj_scarlett2 and anders_s42_sleeping_bj_scarlett1
            $ renpy.movie_cutscene("scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_scarlett2.webm", loops=1, delay=-1, stop_music=False)
            scene anders_s42_sleeping_bj15
            p "It’s commming..."
            scene anders_s42_sleeping_bj16 with dissolve
            p "Aaaawww..."
            scene anders_s42_sleeping_bj17 with dissolve
            p "YEAAH. I’m pumping her throat!! Aaah!"
            scene anders_s42_sleeping_bj21
            p "YES!! And DEEPER!"
            scene anders_s42_sleeping_bj20
            p "Mmmmmm…."

        "Ivana" if not toggle_winners_party_sleeping_girls_chose_ivana:
            $ toggle_winners_party_sleeping_girls_chose_ivana = True
            #animation:anders_s42_sleeping_bj_Ivana2 and anders_s42_sleeping_bj_Ivana1
            scene anders_s42_sleeping_bj_ivana_trans1
            $ renpy.movie_cutscene("scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_Ivana1.webm", loops=1, delay=-1, stop_music=False)
            scene anders_s42_sleeping_bj15
            p "Hey Ivana. Looks like you need more training. Your throat seems almost unused. Looks like I brought you to tears too."
            #animation:anders_s42_sleeping_bj_Ivana2 and anders_s42_sleeping_bj_Ivana1
            $ renpy.movie_cutscene("scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_Ivana2.webm", loops=1, delay=-1, stop_music=False)
            scene anders_s42_sleeping_bj15
            p "I think it’s time to end this."
            scene anders_s42_sleeping_bj16 with dissolve
            p "Aaaawww..."
            scene anders_s42_sleeping_bj17 with dissolve
            p "YEAAH! That’s a big load!"
            scene anders_s42_sleeping_bj22
            p "I see her cheeks getting full."
            scene anders_s42_sleeping_bj23 with dissolve
            p "And now let it slide down…."


    jump winners_party_sleeping_girls_choices


label scene_mc_anders_spilled_megans_drink_winners_party:
    scene anders_s40_winners_party44
    p "Whoops."
    meg "Aaaah?!"
    scene anders_s40_winners_party43
    pause
    scene anders_s40_winners_party46
    p "Oh GOD! I’m so sorry!"
    scene anders_s40_winners_party47
    meg "Awww. Look at me, my dress is all ruined..."
    p "I’m really sorry."
    meg "I think I will go. I can’t stay here like that."
    scene anders_s40_winners_party45
    p "I’m so so sorry. Can I, at least, escort  you home?"
    scene anders_s40_winners_party48
    meg "Eeeh... You don’t want to stay here?"
    p "No. I want to go with you. I, at least, owe you that."
    meg "Well. Okay. Let’s go."

    scene anders_s44_walk_to_megans01
    p "Once again. I’m sorry for ruining the party for you."
    scene anders_s44_walk_to_megans02
    meg "It’s fine. You didn’t ruin the party for me. Accidents happen. I really enjoyed dancing with you though."
    p "Yeah, but still I'm a little sad about it."
    meg "You don’t need to be. Who knows, maybe the party is over anyway and everyone went to sleep."
    p "Ah, maybe you are right (literally)."

label scene_mc_anders_arrives_at_home_with_megan_after_winners_party:
    scene anders_s44_walk_to_megans03
    meg "We are here. Come in."
    p "Hmmm..."
    meg "This is my place. It’s a little small, but I like it."
    scene anders_s44_walk_to_megans04
    pause
    scene anders_s44_walk_to_megans05
    p "It looks fine to me."
    scene anders_s44_walk_to_megans06
    p "It may be smaller, but looks pretty comfy."
    scene anders_s44_walk_to_megans07
    p "And with a nice collection of wines..."
    scene anders_s44_walk_to_megans08
    meg "Do you like wine? I think we can open a bottle together."
    p "Of course."
    meg "So which one do you like?"
    p "I think I will let you pick your favorite."
    meg "Okay."
    scene anders_s44_walk_to_megans09
    meg "Hm hmmmm hmmmm…."
    scene anders_s44_walk_to_megans10
    meg "I think this one will be great for tonight."
    scene anders_s44_walk_to_megans11
    meg "Can you please serve it? I will go clean my cleavage from that drink. My dress already dried during the walk."
    p "Yeah sure."
    meg "Glasses are on the table."
    scene anders_s44_walk_to_megans12
    p "wine is almost ready… Buuuut maaaybe?"
    menu:
        "Do you want to use a horny pill on Megan now?"
        "YES":
            $ toggle_mc_anders_used_horny_pill_on_megan_after_winners_party = True
            scene anders_s44_walk_to_megans13
            p "Good that she picked red wine."
        "NO":
            pass
    scene anders_s44_walk_to_megans14
    meg "I’m back."
    p "Great. Just in time."
    scene anders_s44_walk_to_megans18
    p "I must say you have a really great view of the city from here."
    scene anders_s44_walk_to_megans15
    meg "Yes. That’s why I like this flat soo much. Sometimes I’m just sitting here by the window for hours and just watching the beauty of the city lights."
    scene anders_s44_walk_to_megans16
    p "Yes, that view is really magnificent."
    scene anders_s44_walk_to_megans17
    meg "I’m so happy that you are here with me."
    scene anders_s44_walk_to_megans19
    p "Me too. I think it’s the best place for me to be right now."
    meg "Hih."
    p "So, how about we take this to another level?"
    meg "Eeh?. You know, I…."
    scene anders_s44_walk_to_megans20 with dissolve
    p "I mean the wine…"
    meg "Hah. Of course, the wine..."
    scene anders_s44_walk_to_megans21
    meg "Cheers!"
    p "Cheers! To great people and relationships."
    meg "Yes!"
    scene anders_s44_walk_to_megans22 with dissolve
    scene anders_s44_walk_to_megans23
    meg "Mmmm... so gooood."
    scene anders_s44_walk_to_megans24
    p "Yes I like it."
    "After a few glasses of wine..."
    if toggle_mc_anders_used_horny_pill_on_megan_after_winners_party:
        scene anders_s44_walk_to_megans25
        p "(Looks like the pills are starting to work)."
        meg "I think... I think there is something I need to do."
        p "I feel the same Megan."
        scene anders_s44_walk_to_megans26 with dissolve
        p "Mmmm."
        play sound sound_phone_ringing
        scene anders_s44_walk_to_megans27 with dissolve
        meg "Huh?"
        p "Just ignore it."
        scene anders_s44_walk_to_megans28 with dissolve
        meg "Hey… don’t tell me what to do..."
        scene anders_s44_walk_to_megans29
        stop sound
        meg "Yes, Nick?"
        scene anders_s44_walk_to_megans30 with dissolve
        p "(Damn… that little cockblocker!)"
        meg "Yes. I’m home already. I will wait for you here. Yeah, cool, see you in a while. Bye bye..."
        scene anders_s44_walk_to_megans31 with dissolve
        meg "I’m so sorry. But I think it’s about time to…"
        p "Yeah. I don’t want to inconvenience you. It was a great day with you Megan. I liked it a lot."
        meg "Yeah, me too. It was great."
        p "So, I’ll see you tomorrow..."
        meg "Yeah. Bye."
        scene anders_s44_walk_to_megans32
        p "Aaah. Nick. Hi!"
        scene anders_s44_walk_to_megans33
        nick "Have a good night professor."
        scene anders_s44_walk_to_megans34
        p "(Grrr... that little prick will now have a heated Megan all because of me. DAMN! What a waste.)"

    elif not toggle_mc_anders_used_horny_pill_on_megan_after_winners_party:
        scene anders_s44_walk_to_megans25
        p "(Looks like Megan is feeling something for me too.)"
        meg "I think... I think there is something I need to do."
        p "I feel the same Megan."
        scene anders_s44_walk_to_megans26 with dissolve
        p "Mmmm."
        #*Phone ringing sound*
        play sound sound_phone_ringing
        scene anders_s44_walk_to_megans27 with dissolve
        meg "Huh?"
        p "Just ignore it."
        scene anders_s44_walk_to_megans28 with dissolve
        meg "Hey… don’t tell me what to do..."
        scene anders_s44_walk_to_megans29
        stop sound
        meg "Yes Nick?"
        scene anders_s44_walk_to_megans30 with dissolve
        p "(Damn… that little cockblocker!)"
        meg "Yes. I’m home already. I will wait for you here. Yeah, cool, see you in a while. Bye bye..."
        scene anders_s44_walk_to_megans31 with dissolve
        meg "I’m so sorry. But I think it’s about time to…"
        p "Yeah. I don’t want to inconvenience you. It was a great day with you Megan. I liked it a lot."
        meg "Yeah, me too. It was great."
        p "So, I’ll see you tomorrow..."
        meg "Yeah. Bye."
        scene anders_s44_walk_to_megans32
        p "Aaah. Nick. Hi!"
        scene anders_s44_walk_to_megans33
        nick "Have a good night professor."
        scene anders_s44_walk_to_megans34
        p "(Hmmm. The night had an interesting development.)"
    scene anders_s44_walk_to_megans35
    nick "(What the heck was HE doing here so late?)"
    jump scene_waking_up_after_winners_party_without_mc_anders

label scene_waking_up_after_winners_party_without_mc_anders:
    "Meanwhile at the party..."
    scene anders_s45_wake_up09
    iva "That was a really wild party."
    scene anders_s45_wake_up11
    pause
    scene anders_s45_wake_up10 with dissolve
    iva "Wait a second… Where is the trophy? It disappeared?!!"
    scene anders_s45_wake_up12
    sop "Damn. My head is spinning like crazy. I don’t remember anything…"
    scene anders_s45_wake_up05 with dissolve
    iva "Wait a second. It's only been a few hours. Look at the time."
    scene anders_s45_wake_up13 with dissolve
    sop "That means … !!!"
    iva "I only know one bitch that would do something like this to us... Brooke."
    sop "I will pluck her hair out…."
    scene anders_s45_wake_up05
    iva "I think the party is over."
    sop "Yeah…"
    jump convergence_map_after_winners_party

label scene_waking_up_after_winners_party_with_mc_anders:
    scene anders_s45_wake_up01
    meg "Mmmmmm…. oh…?"
    scene anders_s45_wake_up02 with dissolve
    meg "What?"
    scene anders_s45_wake_up04
    p "Eeeh."
    scene anders_s45_wake_up06 with dissolve
    p "Eeewww…."
    scene anders_s45_wake_up07 with dissolve
    p "Heh. Hi, Meg."
    scene anders_s45_wake_up08 with dissolve
    p "Is it morning already?"
    scene anders_s45_wake_up03
    meg "What happened here? Why was I sleeping like this?!"
    scene anders_s45_wake_up09
    iva "That was a really wild party..."
    scene anders_s45_wake_up11
    pause
    scene anders_s45_wake_up10 with dissolve
    iva "Wait a second… Where is the trophy? It disappeared?!!"
    scene anders_s45_wake_up12
    sop "Damn. My head is spinning like crazy. I don’t remember anything…"
    scene anders_s45_wake_up05 with dissolve
    iva "Wait a second. It was just a few hours. Look at the time."
    scene anders_s45_wake_up13 with dissolve
    sop "That means...!!!"
    iva "I only know one bitch that would do something like this to us... Brooke."
    sop "I will pluck her hair out…."
    sop "And I won’t be waiting until morning. I’m doing it now…"
    scene anders_s45_wake_up14
    p "Hey girls. Calm down a little. This can get you in a lot of trouble. Let me first talk to her tomorrow and see what happened."
    scene anders_s45_wake_up05
    sop "Pfff... fine. I’m not in the mood to see her stupid face right now, anyway."
    scene anders_s45_wake_up15
    p "Fine."
    scene anders_s45_wake_up05
    iva "I think the party is over."
    sop "Yeah…"
    scene anders_s40_winners_party31
    p "Can I escort you home Megan?"
    meg "Sorry. I think it is not the best idea. Nick is already home, maybe another time..."
    p "But..."
    scene anders_s40_winners_party27 with dissolve
    meg "See you tomorrow at school. Bye, Thomas"
    p "Bye. Megan"
    jump convergence_map_after_winners_party

label convergence_map_after_winners_party:
    $ milestone_winners_party_over = True
    $ onetime_time_to_go_to_sleep_after_winners_party = True
    $ hints_counter += 1
    scene city_map_night
    p "Well, I think the party didn’t end the way the girls wanted. Anyway, I’m ready for bed now."
    jump city_map
