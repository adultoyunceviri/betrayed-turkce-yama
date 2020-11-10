
screen school_map:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/school_map.webp"
        hover "school_map_glow"

        hotspot (1235, 810, 100, 90):#exit
            if beth_waiting_in_female_wc:
                action Jump("interaction_school_map_exit_beth_waiting_in_female_wc")
            elif called_to_deans_office:
                action Jump("interaction_school_map_exit_dean_waiting_in_office")
            elif looking_for_ivana_in_school_after_searching_anders_office:
                action Jump("still_trying_to_find_ivana_in_school_after_searching_anders_office")
            elif have_talked_to_sophia_in_kitchen_as_scarlett and not have_talked_to_dean_as_scarlett_to_reenroll:
                action Jump("interaction_school_map_exit_need_to_see_dean_to_reenroll")
            elif need_to_pee_as_scarlett:
                action Jump("interaction_school_map_exit_have_to_pee")
            elif as_scarlett_feeling_weird_after_first_lab_tests:
                action Jump("interaction_school_map_exit_feeling_weird_after_lab_tests")
            elif have_a_bunch_of_pills_to_test_on_ivana_and_sophia or mc_scarlett_upstairs_when_looking_for_ivana_n_sophia_available:
                action Jump("interaction_school_map_exit_not_found_ivana_n_sophia")
            elif need_to_hide_unlabebeled_pills_in_apartment:
                action Jump("scene_beth_and_brooke_bullying_megan_outside_school")
            elif time_to_see_ivana_after_threesome_outside_school:
                action Jump("scene_mc_scarlett_leaving_school_after_seeing_meg_in_deans_office")
            elif mc_has_keys_to_anders_house and not anders_apartment_available:
                action Jump("interaction_school_map_can_now_go_to_anders_apartment")
            elif onetime_mc_anders_asked_sophia_to_watch_his_fifth_class:
                action Jump("scene_school_map_exit_mc_anders_mees_mrs_baber")
            else:
                action Jump("city_map")

        hotspot (855, 530, 130, 90) action Jump("main_hall")#main_hall

        hotspot (400, 390, 90, 50):#class1
            if ready_to_sneak_into_anders_office_stage > 0:
                action Jump("anders_is_teaching_time_to_sneak_into_office")
            elif classes_have_started == True:
                action Jump("interaction_school_map_classes_already_in_session")
            elif mc_anders_late_for_anders_class:
                action Jump("scene_mc_anders_teaches_anders_class")
            elif mc_anders_taught_anders_class and not mc_anders_settled_in_as_anders:
                action Jump("need_to_find_anders_house_keys_now")
            elif mc_anders_settled_in_as_anders and not mc_anders_caught_rebecca_in_shower_milestone:
                if not mc_anders_wants_to_visit_scarlett_in_hospital:
                    action Jump("scene_mc_anders_teaching_class_scarlett_not_there_still")
                elif mc_anders_wants_to_visit_scarlett_in_hospital:
                    action Jump("need_to_visit_scarlett_in_hopital_now")
                else:
                    action Jump("class1")
            elif onetime_mc_anders_needs_to_teach_class_third_time:
                action Jump("scene_mc_anders_teaching_class_third_time")
            elif onetime_mc_anders_needs_to_check_anders_laptop_for_pills_info or onetime_mc_anders_needs_to_get_file_in_apartment_for_megan:
                action Jump("interaction_anders_class_students_have_their_third_task")
            elif onetime_mc_anders_fourth_time_teaching:
                action Jump("scene_mc_anders_fourth_time_teaching")
            elif onetime_mc_anders_needs_to_collect_dna_results:
                action Jump("interaction_anders_class_students_left_alone_fourth_time")
            elif onetime_mc_anders_about_to_meet_scarlett_back_at_school:
                action Jump("scene_as_anders_meeting_scarlet_back_at_school_from_hospital")
            elif onetime_mc_anders_asked_sophia_to_watch_his_fifth_class:
                action Jump("interaction_anders_class_have_sophia_watching_it")

            else:
                action Jump("class1")

        hotspot (675, 310, 100, 50):#class2
            if classes_have_started == True:
                if ready_to_sneak_into_anders_office_stage == 1:
                    action Jump("interaction_school_map_looking_for_anders_not_in_there")
                else:
                    action Jump("interaction_school_map_classes_already_in_session")
            else:
                action Jump("class2")

        hotspot (570, 580, 200, 100):#computer_class
            if classes_have_started == True:
                if ready_to_sneak_into_anders_office_stage == 1:
                    action Jump("interaction_school_map_looking_for_anders_not_in_there")
                else:
                    action Jump("interaction_school_map_classes_already_in_session")
            elif need_to_access_flash_drive_at_school == True:
                action Jump("scene_try_flash_drive_on_school_computer")
            elif looking_for_ivana_in_school_after_searching_anders_office:
                action Jump("scene_looking_for_ivana_found_bethany")
            elif need_to_tell_sophia_about_pills_colour_change:
                action Jump("scene_finding_sophia_and_telling_her_about_pills_colour_change")
            elif onetime_mc_anders_asked_sophia_to_watch_his_fifth_class:
                action Jump("interaction_computer_class_no_reason_for_anders_to_enter")
            elif onetime_mc_anders_needs_to_see_brooke_before_restaurant_party:
                action Jump("scene_mc_anders_sees_brooke_in_computer_class_before_restaurant_party")
            elif onetime_mc_anders_needs_talk_brooke_morning_after_winners_party:
                action Jump("scene_mc_anders_talks_brooke_in_computer_class_after_winners_party")
            else:
                action Jump("computer_class")

        hotspot (1070, 445, 130, 80):
            if currently_possessed_scarlett:
                if need_to_pee_as_scarlett:
                    action Jump("scene_go_into_wrong_toilets_as_scarlett")
                else:
                    action Jump("interaction_school_map_male_wc_scarlett_cant_enter")
            else:
                action Jump("male_wc")#male_wc

        hotspot (1220, 540, 150, 105):#female_wc
            if beth_waiting_in_female_wc:
                action Jump("female_wc")#scene_bethany_waiting_in_female_wc
            elif currently_possessed_brandon:
                action Jump("interaction_school_map_female_wc_brandon_cant_enter")
            elif currently_possessed_cop:
                if ready_to_sneak_into_anders_office_stage == 1:
                    action Jump("interaction_school_map_female_wc_cop_anders_probably_not_there")
                else:
                    action Jump("interaction_school_map_female_wc_cop_cant_enter")
            elif currently_possessed_scarlett:
                if need_to_pee_as_scarlett:
                    action Jump("scene_go_into_good_toilets_as_scarlett")
                elif have_a_bunch_of_pills_to_test_on_ivana_and_sophia:
                    action SetVariable("hints_counter", hints_counter+1), Jump("female_wc")
                else:
                    action Jump("female_wc")
            elif currently_possessed_anders:
                action Jump("interaction_school_map_female_wc_anders_cant_enter")

        hotspot (955, 405, 110, 75):#upstairs
            if called_to_deans_office == True:
                action Jump("scene_brandon_in_deans_office")
            elif cop_needs_to_visit_dean == True:
                action Jump("scene_cop_visits_dean_in_office")
            elif cop_needs_to_visit_dean_again == True:
                action Jump("scene_cop_visits_dean_in_office_again")
            elif ready_to_sneak_into_anders_office_stage > 0:
                if ready_to_sneak_into_anders_office_stage == 1:
                    action Jump("need_to_see_where_anders_is_first")
                elif ready_to_sneak_into_anders_office_stage == 2:
                    action Jump("anders_office_open_door")
            elif anders_office_trashed:
                action Jump("anders_office_trashed")
            elif time_to_deliver_anders_documents_to_dean:
                action Jump("scene_delivering_anders_documents_to_deans_office")
            elif currently_possessed_scarlett and settled_as_scarlett:
                if not have_talked_to_dean_as_scarlett_to_reenroll:
                    action Jump("scene_as_scarlet_go_to_deans_office")
                elif have_a_bunch_of_pills_to_test_on_ivana_and_sophia:
                    action Jump("interaction_school_map_upstairs_not_seen_meg_in_stall")
                elif mc_scarlett_upstairs_when_looking_for_ivana_n_sophia_available:
                    action Jump("scene_mc_scarlett_upstairs_looking_for_ivana_n_sophia_run_into_anders")
                elif need_to_meet_meg_in_deans_office_after_threesome:
                    action Jump("scene_mc_scarlett_meet_megan_in_deans_after_threesome")
                elif time_for_afternoon_choices_after_pills_colouring:
                    if not mc_scarlett_refused_anders_offer_for_scarlett_help:
                        action Jump("scene_one_of_three_anders_office")
                    else:
                        action Jump("interaction_school_map_upstairs_dont_want_anders_offer")
                else:
                    action Jump("interaction_school_map_upstairs")
            elif mc_anders_needs_to_find_anders_keys_in_office:
                if mc_anders_late_for_anders_class:
                    action Jump("interaction_school_map_upstairs_mc_anders_late_for_class")
                else:
                    action Jump("anders_office")
            elif onetime_mc_anders_needs_to_teach_class_third_time:
                action Jump("interaction_school_map_upstairs_mc_anders_late_for_class")
            elif onetime_mc_anders_needs_to_check_anders_laptop_for_pills_info:
                action Jump("scene_mc_anders_needs_to_check_anders_laptop_for_pills_info")
            elif onetime_mc_anders_needs_to_talk_to_dean_before_party:
                action Jump("scene_mc_anders__needs_to_talk_to_dean_before_party")
            else:
                action Jump("interaction_school_map_upstairs")

label school:
    if has_learned_about_posession == False:
        jump sophia_main_hall_talking
    elif classes_have_started == False and currently_possessed_brandon and have_looked_in_brandons_locker == False:
        show school_map
        p "I guess I should try to blend in, as Brandon."
        p "I have his locker key. I should find out where his locker is."
        $ hints_counter += 1
        $ classes_have_started = True
    call screen school_map

### Main Hall
screen main_hall:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/01_main_hall/main_hall.webp"
        hover "destinations/03_school/01_main_hall/main_hall_glow.webp"

        hotspot (55, 239, 125, 406) action Jump("main_hall_lockers1")#locker

        hotspot (220, 125, 180, 708) action NullAction()#door

        hotspot (680, 65, 92, 160):#picture
            #if sophia_roommate_ad_placed == True:
            #    action Jump("main_hall_board_with_roommate_ad")
            #else:
            action Jump("main_hall_board")

        hotspot (715, 245, 35, 183) action Jump("main_hall_lockers2")#locker2

        if currently_possessed_brandon and have_looked_in_brandons_locker and mom_in_main_hallway == True:
            imagebutton:
                idle "mainhall_mom_walking"
                hover "mainhall_mom_walking_glow"
                xpos 1150 ypos 255
                action Jump("scene_mom_walking_in_main_hall")

        if currently_possessed_cop and sophia_arguing_with_brandon_in_main_hall == True:
            imagebutton:
                idle "mainhall_brandon_sophia"
                hover "mainhall_brandon_sophia_glow"
                xpos 1150 ypos 255
                action Jump("scene_sophia_arguing_with_brandon_in_main_hall")

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "main_hall"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "main_hall"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "main_hall"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "main_hall"), Jump("joraell_message_no_phone")
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

        if saw_megan_scene_in_wc == True and not mom_in_main_hallway:
            imagebutton:
                idle "back_button_idle"
                hover "back_button_hover"
                xpos 1405 ypos 820
                action Jump("school")

label main_hall:

    call screen main_hall

### Main Hall Board
screen main_hall_board:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/01_main_hall/main_hall_board.webp"
        hover "destinations/03_school/01_main_hall/main_hall_board_glow.png"

        hotspot (200, 100, 400, 320) action Jump("interaction_main_hall_board_scarlett_picture")#picture

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "main_hall_board"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "main_hall_board"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "main_hall_board"), Show("phone_screen")
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

        if sophia_roommate_ad_placed == True:
            imagebutton:
                idle "mainhall_board_roommate"
                hover "mainhall_board_roommate_glow"
                xpos 300 ypos 400
                action NullAction()

        imagebutton:
            idle "back_button_idle"
            hover "back_button_hover"
            xpos 1405 ypos 820
            action Jump("main_hall")

label main_hall_board:
    call screen main_hall_board


### Main Hall Lockers Set 1
screen main_hall_lockers1:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/01_main_hall/Mainhall_lockers1B.webp"
        hover "destinations/03_school/01_main_hall/Mainhall_lockers1B_glow.webp"

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "main_hall_lockers1"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "main_hall_lockers1"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "main_hall_lockers1"), Show("phone_screen")
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
            action Call("main_hall")

label main_hall_lockers1:
    call screen main_hall_lockers1

### Main Hall Lockers Set 2
screen main_hall_lockers2:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/01_main_hall/Mainhall_lockers1.webp"
        hover "destinations/03_school/01_main_hall/Mainhall_lockers1_glow.webp"

        if currently_possessed_brandon == True and have_looked_in_brandons_locker == False:
            hotspot (620, 40, 370, 850) action Jump("interaction_main_hall_lockers2_open_brandons_locker")#brandonslocker

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "main_hall_lockers2"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "main_hall_lockers2"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "main_hall_lockers2"), Show("phone_screen")
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
            action Call("main_hall")

label main_hall_lockers2:

    call screen main_hall_lockers2

### Class 1
screen class1:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/02_classroom1/classroom1.webp"
        hover "destinations/03_school/02_classroom1/classroom1_glow.webp"

        hotspot (145, 218, 153, 445) action Jump("school")#door

        hotspot (615, 140, 670, 325) action NullAction()#board

        hotspot (812, 451, 103, 80) action NullAction()#teacherchair - need to be after board to overdraw hover glow

        hotspot (654, 450, 52, 80) action NullAction()#pens - need to be after board to overdraw hover glow

        hotspot (1120, 650, 290, 180):
            if saw_ivana_scene_in_class == False:
                action NullAction() #Jump("ivana_spy_in_class")#studentchair
            else:
                action NullAction()

        if looking_for_sophia_about_pills_progress:
            imagebutton:
                idle "classroom1_anders"
                hover "classroom1_anders_glow"
                xpos 781 ypos 371
                if not gym_location_available:
                    action Call("scene_ask_anders_where_sophia_is_and_unlock_gym")
                else:
                    action Call("interaction_anders_classroom1_already_know_sophia_at_gym")

            if not anders_desk_secret_found:
                imagebutton:
                    idle "classroom1_secret"
                    hover "classroom1_secret_glow"
                    xpos 838 ypos 623
                    action SetVariable("anders_desk_secret_found", True), Jump("interaction_anders_desk_found_secret4")#secret


        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "class1"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "class1"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "class1"), Show("phone_screen")
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
        #    action Jump("school")

label class1:
    call screen class1

### Class 2
screen class2:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/05_classroom2/classroom2.webp"
        hover "destinations/03_school/05_classroom2/classroom2_glow.webp"

        hotspot (145, 218, 152, 444) action Jump("school")#door

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "class2"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "class2"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "class2"), Show("phone_screen")
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
        #    action Jump("school")

label class2:
    call screen class2

### Computer Class
screen computer_class:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/04_computer_class/computer_class_main.webp"
        hover "destinations/03_school/04_computer_class/computer_class_main_glow.webp"

        hotspot (133, 159, 145, 278) action Jump("school")#door

        hotspot (812, 395, 103, 60) action NullAction()#teacherchair

        hotspot (1047, 370, 286, 140) action NullAction()#studentcomputer

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "computer_class"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "computer_class"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "computer_class"), Show("phone_screen")
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
        #    action Jump("school")

label computer_class:
    call screen computer_class

### Male WC
screen male_wc:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/03_male_wc/male_wc_main.webp"
        hover "destinations/03_school/03_male_wc/male_wc_main_glow.webp"

        hotspot (90, 295, 145, 480) action Jump("interaction_male_wc_stall_door")#stall_door

        hotspot (915, 335, 100, 220) action Jump("interaction_male_wc_urinal")#urinal

        hotspot (1270, 215, 330, 290) action Jump("interaction_male_wc_mirror")#mirror

        hotspot (1267, 475, 150, 200) action NullAction()#sink - has to be below mirror for glow overdraw


        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "male_wc"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "male_wc"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "male_wc"), Show("phone_screen")
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
            action Jump("school")

label male_wc:
    call screen male_wc

### female WC
screen female_wc:
    on "show" action If(have_a_bunch_of_pills_to_test_on_ivana_and_sophia, Play('music', "sounds/effects/moaning_sound.ogg", if_changed=True), Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True))
    imagemap:
        ground "destinations/03_school/06_female_wc/female_wc_main.webp"
        hover "destinations/03_school/06_female_wc/female_wc_main_glow.webp"

        if saw_megan_scene_in_wc == False:
            imagebutton:#will need to go below hotspots later when proper imagebutton made TODO
                idle "destinations/03_school/06_female_wc/female_wc_main_megan.webp"
                hover "destinations/03_school/06_female_wc/female_wc_main_megan_glow.webp"
                #xpos 1405 ypos 820
                action Jump("megan_wc_spy")

        hotspot (0, 305, 115, 360):
            if beth_waiting_in_female_wc:
                action Jump("scene_bethany_waiting_in_female_wc")
            elif as_scarlett_feeling_weird_after_first_lab_tests:
                action Jump("scene_as_scarlett_female_wc_stall_feeling_weird")
            elif have_a_bunch_of_pills_to_test_on_ivana_and_sophia:
                action Jump("scene_female_wc_megan_jacking_in_stall")
            elif mc_scarlett_upstairs_when_looking_for_ivana_n_sophia_available:
                action Jump("interaction_school_map_female_wc_leave_her_to_happy_time")
            else:
                action NullAction()#stall_door

        hotspot (1125, 205, 475, 335) action NullAction()#mirror

        hotspot (1105, 518, 175, 210) action NullAction()#sink - has to be below mirror for glow overdraw

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "female_wc"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "female_wc"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "female_wc"), Show("phone_screen")
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
            if have_a_bunch_of_pills_to_test_on_ivana_and_sophia:
                action Jump("female_wc_cant_leave_megan_jacking_sounds")
            else:
                action Jump("school")

label female_wc:
    if beth_waiting_in_female_wc:
        scene female_wc_main
        p "This is risky. I hope I don't get caught."
    call screen female_wc

### female WC with megan
screen female_wc_with_megan:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:

        ground "destinations/03_school/06_female_wc/female_wc_main_megan.webp"
        hover "destinations/03_school/06_female_wc/female_wc_main_megan_glow.webp"

        hotspot (1205, 318, 195, 560) action Jump("scene_megan_wc_spy")#megan

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "female_wc_with_megan"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "female_wc_with_megan"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "female_wc_with_megan"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "female_wc_with_megan"), Jump("joraell_message_no_phone")
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
            action Jump("idle_female_wc_with_megan_back_button_cant_leave")

label female_wc_with_megan:
    call screen female_wc_with_megan


screen brandon_on_class_computer:
    imagemap:
        #ground "scenes/brandon/03_computer_class/brandons03_computer_class06.webp"
        #ground "other_things/computer/class_computer/brandon_in_classroom_test.png"
        ground "other_things/computer/class_computer/windows_frame.png"

        imagebutton:#girls_folder
            idle "folder_my_girls"
            hover "folder_my_girls_glow"
            xpos 105 ypos 120
            action Jump("scenes_computer_room_folder_brandons_girls")
        imagebutton:#codes_folder
            idle "folder_codes"
            hover "folder_codes_glow"
            xpos 205 ypos 120
            action Jump("scenes_brandon_sees_codenames_on_computer")

label brandon_on_class_computer:
    #scene TODO
    call screen brandon_on_class_computer

### Deans Office
screen deans_office:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/07_deans_office/deans_office_main.webp"
        hover "destinations/03_school/07_deans_office/deans_office_main_glow.png"

        hotspot (775, 205, 185, 315) action Jump("interaction_school_deans_office_door")#door

        hotspot (1360, 205, 160, 180) action Jump("deans_office_board")#board

        hotspot (305, 370, 53, 90) action Jump("deans_office_bookshelf")#bookshelf

        hotspot (1150, 205, 200, 130) action Jump("deans_office_certificates")#certificates

        hotspot (1270, 455, 100, 60) action Jump("deans_office_binder")#binder

        hotspot (1140, 365, 125, 85) action Jump("scene_brandon_in_deans_office_try_password")#deans_computer

        hotspot (390, 320, 90, 80) action Jump("deans_office_picture_frames")#pictures

        hotspot (1270, 375, 75, 70) action Jump("deans_office_telephone")#telephone

        hotspot (570, 300, 80, 100) action Jump("deans_office_trophies")#trophies


        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "deans_office"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "deans_office"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "deans_office"), Show("phone_screen")
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
        #    action Jump("main_hall")

label deans_office:
    call screen deans_office

### Deans Office Board
screen deans_office_board:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/07_deans_office/office_board.webp"


        #hotspot (200, 100, 400, 320) action Jump("interaction_main_hall_board_scarlett_picture")#picture

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "deans_office_board"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "deans_office_board"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "deans_office_board"), Show("phone_screen")
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
            action Jump("deans_office")

label deans_office_board:
    scene office_board
    if deans_password_guess_brooke == 0:
        $ deans_password_guess_brooke = 1
        p "Damn! Brooke is the Dean's niece? It looks like Brooke's stationery though. Did she write this?"
    else:
        p "It's no wonder Brooke owns the campus. She has friends in high places."
    call screen deans_office_board


### Deans Office Bookshelf
screen deans_office_bookshelf:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/07_deans_office/office_books.webp"

        #hotspot (200, 100, 400, 320) action Jump("interaction_main_hall_board_scarlett_picture")#picture

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "deans_office_bookshelf"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "deans_office_bookshelf"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "deans_office_bookshelf"), Show("phone_screen")
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

        if deans_office_secret_found == False:
            imagebutton:
                idle "secret2button"
                hover "secret2button_glow"
                xpos 1477 ypos 269
                action SetVariable("deans_office_secret_found", True), Jump("interaction_deans_office_found_secret2")
        imagebutton:
            idle "back_button_idle"
            hover "back_button_hover"
            xpos 1405 ypos 820
            action Jump("deans_office")

label deans_office_bookshelf:
    scene office_books
    if deans_office_secret_found == False:
        show secret2button:
            xpos 1477 ypos 269
    if deans_password_guess_best_teacher == 0:
        $ deans_password_guess_best_teacher = 1
        p "Best Teacher. I really don't think I would agree with the methods in that book. Hmm... What is this about Faith? Is it a person?"
    else:
        p "Best teacher... Yikes! I wonder if Faith means something?"
    call screen deans_office_bookshelf

### Deans Office Certificates
screen deans_office_certificates:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/07_deans_office/office_certificates.webp"

        #hotspot (200, 100, 400, 320) action Jump("interaction_main_hall_board_scarlett_picture")#picture

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "deans_office_certificates"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "deans_office_certificates"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "deans_office_certificates"), Show("phone_screen")
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
            action Jump("deans_office")

label deans_office_certificates:
    scene office_certificates
    if deans_password_guess_certificates == 0:
        $ deans_password_guess_certificates = 1
        p "So many certificates awarded to Dean Smith. I bet she's really proud of these."
    else:
        p "That's a lot of certificates for Dean Smith."
    call screen deans_office_certificates

### Deans Office Binder
screen deans_office_binder:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/07_deans_office/office_note.webp"

        #hotspot (200, 100, 400, 320) action Jump("interaction_main_hall_board_scarlett_picture")#picture

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "deans_office_binder"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "deans_office_binder"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "deans_office_binder"), Show("phone_screen")
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
            action Jump("deans_office")

label deans_office_binder:
    scene office_note
    if deans_password_guess_mirapill == 0:
        p "Mirapill. I guess it's supposed to sound like miracle. Looks like the Dean decided on a name. Just scientific stuff in here."
        $ deans_password_guess_mirapill = 1
    else:
        p "Mirapill. If I want to keep fucking Beth, I need more of these babies."
    call screen deans_office_binder

### Deans Office Picture Frames
screen deans_office_picture_frames:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/07_deans_office/office_picture.webp"

        #hotspot (200, 100, 400, 320) action Jump("interaction_main_hall_board_scarlett_picture")#picture

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "deans_office_picture_frames"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "deans_office_picture_frames"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "deans_office_picture_frames"), Show("phone_screen")
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
            action Jump("deans_office")

label deans_office_picture_frames:
    scene office_picture
    if deans_password_guess_salou == 0:
        $ deans_password_guess_salou = 1
        p "Salou, huh? Looks like a really nice place to visit. The Dean must like going there. And a diploma with her name on it... Mary."
    else:
        "Salou. Nice looking place. And her name is Mary."
    call screen deans_office_picture_frames

### Deans Office Telephone
screen deans_office_telephone:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/07_deans_office/office_telephone.webp"

        #hotspot (200, 100, 400, 320) action Jump("interaction_main_hall_board_scarlett_picture")#picture

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "deans_office_telephone"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "deans_office_telephone"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "deans_office_telephone"), Show("phone_screen")
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
            action Jump("deans_office")

label deans_office_telephone:
    scene office_telephone
    p "(A missed call from the lab. I wonder if that's where these pills are made.)"
    call screen deans_office_telephone

### Deans Office Trophies
screen deans_office_trophies:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/07_deans_office/office_trophy.webp"

        #hotspot (200, 100, 400, 320) action Jump("interaction_main_hall_board_scarlett_picture")#picture

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "deans_office_trophies"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "deans_office_trophies"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "deans_office_trophies"), Show("phone_screen")
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
            action Jump("deans_office")

label deans_office_trophies:
    scene office_trophy
    if deans_password_guess_highlanders == 0:
        $ deans_password_guess_highlanders = 1
        p "Highlanders? Oh yeah, that's the school football team. It's full of jocks, but the girls seem to like them."
        p "The Dean must be proud of this trophy, to display it like this."
    else:
        p "Highlanders. The college football team."
    call screen deans_office_trophies


### Anders Office
screen anders_office:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/08_anders_office/anders_office_main.webp"
        hover "destinations/03_school/08_anders_office/anders_office_main_glow.png"

        hotspot (15, 200, 215, 215) action Jump("interaction_school_anders_office_picture")#picture

        hotspot (0, 590, 265, 150) action Jump("interaction_school_anders_office_laptop")#laptop

        hotspot (1460, 455, 100, 100) action Jump("interaction_school_anders_office_books")#books

        hotspot (1155, 390, 175, 130) action Jump("interaction_school_anders_office_drawer")#drawer

        if currently_possessed_anders:
            hotspot (764, 569, 836, 565) action Jump("interaction_school_anders_office_couch")#couch W: 836 H:333 X:764 Y:567

        hotspot (968, 123, 136, 420) action Jump("interaction_school_anders_office_plant")#plant

        hotspot (761, 444, 204, 167) action Jump("interaction_school_anders_office_chest")#chest




        if not anders_office_secret_found:
            hotspot (300, 470, 70, 50) action SetVariable("anders_office_secret_found", True), Jump("interaction_anders_office_found_secret3")#secret


        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "anders_office"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "anders_office"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "anders_office"), Show("phone_screen")
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

        if currently_possessed_anders:
            imagebutton:
                idle "back_button_idle"
                hover "back_button_hover"
                xpos 1405 ypos 820
                action Jump("interaction_anders_office_exit")
        #imagebutton:
        #    idle "back_button_idle"
        #    hover "back_button_hover"
        #    xpos 1405 ypos 820
        #    action Jump("main_hall")

label anders_office:
    if mc_anders_needs_to_find_anders_keys_in_office and not mc_anders_taught_anders_class:
        scene anders_office_main
        p "Damn, I’m like a walking corpse. This couch looks so great right now."
        $ hints_counter = 122#MAGIC
    call screen anders_office

### Anders Office Trashed
screen anders_office_trashed:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/08_anders_office/anders_office_harsch.webp"
        hover "destinations/03_school/08_anders_office/anders_office_harsch_glow.png"

        hotspot (595, 368, 2755, 450) action Jump("scene_anders_looking_for_bug_in_office")#anders

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "anders_office_trashed"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "anders_office_trashed"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "anders_office_trashed"), Show("phone_screen")
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
        #    action Jump("main_hall")

label anders_office_trashed:
    call screen anders_office_trashed

### Anders Drawer
screen anders_office_drawer:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:

        if have_accepted_anders_offer_for_scarlett_help:
            ground "destinations/03_school/08_anders_office/anders_office_drawer_whip.png"
            hover "destinations/03_school/08_anders_office/anders_office_drawer_whip_glow.png"

            hotspot (400, 300, 400, 320) action Jump("interaction_anders_office_whip_in_drawer")#whip
        else:
            ground "destinations/03_school/08_anders_office/anders_office_drawer_empty.png"



        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "anders_drawer"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "anders_drawer"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "anders_drawer"), Show("phone_screen")
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
            action Jump("anders_office")

label anders_office_drawer:

    if not have_accepted_anders_offer_for_scarlett_help:
        scene anders_office_drawer_empty
        p "Nothing here. Just an empty drawer."
    elif have_accepted_anders_offer_for_scarlett_help:
        scene anders_office_drawer_whip
        p "Hah. I have bad memories about this one."
    call screen anders_office_drawer

### Dining Hall
screen dining_hall:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "scenes/Scarlett/11_dining_hall/school_dining_hall.png"
        hover "scenes/Scarlett/11_dining_hall/school_dining_hall_glow.png"

        hotspot (50, 532, 429, 385) action Jump("scene_dining_hall_megan")#megan

        hotspot (931, 318, 478, 431) action Jump("interaction_dining_hall_brooke_and_beth")#brooke_and_beth


        imagebutton:
            idle "scenes/Scarlett/11_dining_hall/school_dining_hall_secret.png"
            xpos 535 ypos 460
            if not cafeteria_room_secret_found:
                hover "scenes/Scarlett/11_dining_hall/school_dining_hall_secret_glow.png"
                action SetVariable("cafeteria_room_secret_found", True), Jump("interaction_cafeteria_found_secret6")#secret

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "dining_hall"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "dining_hall"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "dining_hall"), Show("phone_screen")
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


label dining_hall:
    if not have_talked_with_beth_and_brooke_in_dining_hall:
        $ have_talked_with_beth_and_brooke_in_dining_hall = True
        jump scene_dining_hall_brooke_and_beth
    call screen dining_hall

label gym_locker_room_left_1:
    scene sporthall_door_other
    #"locker room left 1"
    if mc_anders_need_to_hide_scarlett_somewhere:
        p "Hah, that is not a good idea. What if someone came back to this locker room."
    else:
        if not have_found_bad_girls_locker_room:
            p "that could be the right locker room, but better to check other’s first."
        else:
            p "Brooke’s locker is next to the male restrooms."

    call screen gym_map
label gym_locker_room_left_2:
    scene sporthall_door_other
    #"locker room left 2"
    if mc_anders_need_to_hide_scarlett_somewhere:
        p "Hah, that is not a good idea. What if someone came back to this locker room."
    else:
        if not have_found_bad_girls_locker_room:
            p "that could be the right locker room, but better to check other’s first."
        else:
            p "Brooke’s locker is next to male restrooms."
    call screen gym_map
label gym_locker_room_left_3:
    scene sporthall_door_other
    #"locker room left 3"
    if mc_anders_need_to_hide_scarlett_somewhere:
        p "Hah, that is not a good idea. What if someone came back to this locker room."
    else:
        if not have_found_bad_girls_locker_room:
            p "that could be the right locker room, but better to check other’s first."
        else:
            p "Brooke’s locker is next to male restrooms."
    call screen gym_map
label gym_main_hall:
    #"gym_main_hall"
    if mc_anders_need_to_hide_scarlett_somewhere:
        scene sportshall_background
        p "Yeah, great idea: Going out in front of a packed sports hall with an unconscious girl hanging over my shoulder."
    elif mc_anders_spiked_drinks_fun_begins:
        scene sportshall_background
        jump scene_girls_drinks_spiked_fun_begins
    else:
        scene sportshall_background
        p "I can't waste time going back in there right now."
    call screen gym_map

label gym_exercise_area:
    scene sporthall_gym
    #"gym_exercise_area"
    if mc_anders_need_to_hide_scarlett_somewhere:
        p "Bad idea, I must find a better place."
    elif currently_possessed_anders:
        p "No time for building muscles right now."
    else:
        p "School gym. Well equipped. I spent some time here before..."
    call screen gym_map
label gym_male_wc:
    scene sportshall_background
    #"gym_male_wc"
    if mc_anders_need_to_hide_scarlett_somewhere:
        p "Bad idea. I must find a better place."
    else:
        p "I don’t need to go there."
    call screen gym_map
label gym_female_wc:
    scene sportshall_background
    #"gym_female_wc"
    if mc_anders_need_to_hide_scarlett_somewhere:
        p "Bad idea. I must find a better place."
    else:
        p "I don’t need to go there."
    call screen gym_map
label locker_room_opposite_male_wc:
    scene sporthall_door_other
    #"locker_room_opposite_male_wc"
    if mc_anders_need_to_hide_scarlett_somewhere:
        p "Hah, that is not a good idea. What if someone came back to this locker room."
    else:
        if not have_found_bad_girls_locker_room:
            p "That could be the right locker room, but better to check the others first."
        else:
            p "Brooke’s locker is next to the male restrooms."
    call screen gym_map
label locker_room_opposite_female_wc:#bad_girls_locker_room
    scene sporthall_door_brooke
    #"locker_room_opposite_female_wc"
    if not have_found_bad_girls_locker_room:
        $ have_found_bad_girls_locker_room = True
        p "Hmm. They are making it much too easy for me."
    elif mc_anders_needs_to_finish_what_mc_scarlett_started:
        scene black with fade
        jump bad_girls_locker_room
    elif mc_anders_need_to_hide_scarlett_somewhere:
        scene sportshall_background
        p "I can't go in there right now, till I take care of Scarlett."
        jump gym_map
    if not have_gym_janitors_key:
        p "But it’s locked."
        p "I need to find the key somewhere."
        $ hints_counter += 1
        jump gym_map
    elif have_gym_janitors_key:
        if not currently_possessed_anders:
            $ hints_counter = 115 #MAGIC
            jump scene_sneak_into_bad_girls_locker_room
        elif bad_girls_lose_volleyball_horny:
            jump scene_bad_girls_locker_room_horny_after_volleyball
        else:
            scene sportshall_background
            p "No point in going back in there. The bad girls already drained me."
            jump gym_map

    call screen gym_map

label locker_room_opposite_closet:
    scene sporthall_door_other
    #"locker_room_opposite_closet"
    if mc_anders_need_to_hide_scarlett_somewhere:
        p "Hah, that is not a good idea. What if someone came back back to this locker room."
    else:
        if not have_found_bad_girls_locker_room:
            p "that could be the right locker room, but better to check other’s first."
        else:
            p "Brooke’s locker is next to the male restrooms."
    call screen gym_map

label gym_drinks:
    if not bad_girls_lose_volleyball_horny:
        scene sportshall_background
        p "I don't need a drink right now."
        jump gym_map
    else:
        if not mc_anders_has_drink_for_horny_bad_girls:
            $ mc_anders_has_drink_for_horny_bad_girls = True
            scene anders_s04_aftermatch_threesome01
            p "Hmm, I need some kind of excuse."
            scene anders_s04_aftermatch_threesome02
            p "Of course. A drink is just the thing, after a good workout."
            scene anders_s04_aftermatch_threesome03
            p "Hmm. Interesting name. Probably a really enjoyable drink. Fine, I have two of theese and I’m ready now."
            $ hints_counter = 120#MAGIC
            jump gym_map

        else:
            scene sportshall_background
            p "I don't need any more drinks just now."
            jump gym_map
label gym_exit:
    if not mc_anders_needs_to_find_anders_keys_in_office:
        scene sportshall_background
        p "I still have things to do here."
        jump gym_map
    else:
        jump city_map

screen gym_map:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/03_school/09_sporthall/sporthall.png"
        hover "destinations/03_school/09_sporthall/sporthall_glow.png"

        hotspot (1170, 635, 80, 50):#exit

            action Jump("gym_exit")

        hotspot (460, 310, 120, 40):#locker_room1
            action Jump("gym_locker_room_left_1")

        hotspot (520, 365, 120, 40):#locker_room2

            action Jump("gym_locker_room_left_2")

        hotspot (600, 430, 120, 40):#locker_room3

            action Jump("gym_locker_room_left_3")

        hotspot (835, 270, 50, 40):#gym_exercise_area

            action Jump("gym_exercise_area")

        hotspot (570, 230, 160, 60):#gym_main_hall
            action Jump("gym_main_hall")

        hotspot (740, 330, 60, 35):#drinks
            action Jump("gym_drinks")

        hotspot (980, 335, 140, 60):#janitors_closet
            action Jump("gym_janitor_closet")


        hotspot (810, 520, 140, 70):#gym_male_wc

            action Jump("gym_male_wc")

        hotspot (1200, 445, 160, 80):#gym_female_wc

            action Jump("gym_female_wc")

        hotspot (675, 480, 130, 45):#locker_room_opposite_closet
            action Jump("locker_room_opposite_closet")

        hotspot (1085, 390, 130, 55):#locker_room_opposite_male_wc
            action Jump("locker_room_opposite_male_wc")

        hotspot (890, 645, 120, 60):#locker_room_opposite_female_wc
            action Jump("locker_room_opposite_female_wc")

label gym_map:
    call screen gym_map


screen gym_janitor_closet:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        if not have_gym_janitors_key:
            ground "destinations/03_school/09_sporthall/sporthall_cleaningroom_key.png"
            hover "destinations/03_school/09_sporthall/sporthall_cleaningroom_key_glow.png"
        else:
            ground "destinations/03_school/09_sporthall/sporthall_cleaningroom_nokey.png"

        if not have_gym_janitors_key:
            hotspot (870, 490, 60, 65):#gym_janitors_key
                action Jump("interaction_gym_janitors_key")

        imagebutton:
            idle "destinations/03_school/09_sporthall/sporthall_cleaningroom_tree.png"
            xpos 1033 ypos 41
            if not janitors_closet_secret_found:
                hover "destinations/03_school/09_sporthall//sporthall_cleaningroom_tree_glow.png"
                action SetVariable("janitors_closet_secret_found", True), Jump("interaction_gym_janitors_closet_found_bonus2")#secret

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "gym_janitor_closet"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "gym_janitor_closet"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "gym_janitor_closet"), Show("phone_screen")
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
            action Jump("gym_map")


label gym_janitor_closet:
    if mc_anders_need_to_hide_scarlett_somewhere:
        jump scene_mc_anders_hiding_scarlett_in_janitors_closet
    elif currently_possessed_anders:
        scene sportshall_background
        p "I stashed Scarlett in there. I don't want to risk going back in."
        jump gym_map
    call screen gym_janitor_closet


screen bad_girls_locker_room:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:

        ground "destinations/03_school/09_sporthall/sporthall_locker_room.png"
        hover "destinations/03_school/09_sporthall/sporthall_locker_room_glow.png"

        if not mc_anders_has_spiked_brookes_drink:
            hotspot (319, 414, 112, 248):#brooke_locker
                action Jump("interaction_brooke_locker")
        if not mc_anders_has_spiked_beths_drink:
            hotspot (1427, 465, 102, 341):#beth_locker
                action Jump("interaction_beth_locker")
        hotspot (95, 153, 118, 266):#empty_locker
            action Jump("interaction_empty_locker")
        hotspot (415, 159, 110, 254):#empty_locker
                action Jump("interaction_empty_locker")
        hotspot (709, 401, 103, 239):#empty_locker
                action Jump("interaction_empty_locker")
        hotspot (1352, 113, 93, 349):#empty_locker
                action Jump("interaction_empty_locker")
        hotspot (1532, 81, 68, 408):#empty_locker
                action Jump("interaction_secret_locker")
        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "bad_girls_locker_room"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "bad_girls_locker_room"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "bad_girls_locker_room"), Show("phone_screen")
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
            action Jump("gym_map")

label bad_girls_locker_room:
    scene sporthall_locker_room with fade
    call screen bad_girls_locker_room

label interaction_brooke_locker:
    scene sporthall_locker_room_brooke_locker
    p "This is definitely Brooke’s locker."
    scene sporthall_locker_room_brooke_locker
    p "Yes, that’s her favorite dress."
    scene scarlett_s39_change06
    p "Done."
    $ mc_anders_has_spiked_brookes_drink = True
    jump check_if_both_beth_and_brookes_drinks_are_spiked

label interaction_beth_locker:
    scene sporthall_locker_room_beth_locker
    p "Hmm, bingo!"
    scene sporthall_locker_room_beth_locker3
    p "Yes, this is Bethany’s locker."
    scene sporthall_locker_room_beth_locker2
    p "But why does she have my photo?? With hearts? Is…"
    p "DAMN!"
    p "She is into me? WOW! She never even talked to me, and was always acting like I was not there."
    p "Whatever. I have some work to do now."
    scene scarlett_s39_change06
    p "Shaken, not stirred. Haha."
    p "Done."
    scene black with fade
    $ mc_anders_has_spiked_beths_drink = True
    jump check_if_both_beth_and_brookes_drinks_are_spiked

label interaction_empty_locker:
    scene sporthall_locker_room_empty_locker
    p "This locker is empty."
    scene black with fade
    jump bad_girls_locker_room

#secret7_bug
label interaction_secret_locker:
        scene sporthall_locker_room_empty_locker
        p "You found a new secret. Check your phone gallery."
        $ secret_locker_secret7_found = True
        scene black with fade
        jump bad_girls_locker_room

label check_if_both_beth_and_brookes_drinks_are_spiked:
    if mc_anders_has_spiked_beths_drink and mc_anders_has_spiked_brookes_drink:
        p "Now the fun can begin..."
        $ hints_counter += 1
        $ mc_anders_spiked_drinks_fun_begins = True
    scene black with fade
    jump bad_girls_locker_room

label interaction_gym_janitors_key:
    scene sporthall_cleaningroom_key
    p "Yes. This will come in handy. Master keys to the locker rooms and lockers. Cool."
    scene sporthall_cleaningroom_nokey
    scene black with fade
    $ have_gym_janitors_key = True
    if have_found_bad_girls_locker_room:
        $ hints_counter += 1
    jump gym_janitor_closet

label scenes_computer_room_folder_brandons_girls:
    $ gallery_added_to_phone = True
    show brandons05_brooke
    $ renpy.pause()
    p "(Wow! Brandon had Brooke in his bed. Looks like money CAN do everything. Damn, that “hungry” look!)"
    hide brandons05_brooke
    show brandons05_jasmine
    $ renpy.pause()
    p "(Oh, and another cutie here. Nice tattoos and great boobs! I see her sometimes, at school.)"
    hide brandons05_jasmine
    show brandons05_tracy
    p "(Hmmm... this girl, I don’t recognise from school, but looks good too! Now, as Brandon, I think I can visit all these girls.)"
    hide brandons05_tracy
    scene brandons03_computer_class06
    p "(Hopefully Brandon didn’t break up with them. Maybe I will have lady luck on my side. Haha! The time remaining for me here, will be GREAT!)"
    $ seen_secret_pics_brandon_flash_drive = True
    jump brandon_on_class_computer


label interaction_main_hall_board_scarlett_picture:
    scene main_hall_board # TODO possibly show a closup pic of scarlett
    if sophia_roommate_ad_placed == True:
        show mainhall_board_roommate:
            xpos 300 ypos 400
    if currently_possessed_cop:
        p "Yes, Scarlett is missing, but I will find her."
    else:
        p "Ah yes - Scarlett: One day she disappeared, and nobody knows where."
        p "She was talking about some trip to Europe, but who knows what happened..."
    if saw_megan_scene_in_wc == False:
        hide main_hall_board
        jump scene_megan_going_into_wc
    else:
        call screen main_hall_board

label interaction_main_hall_lockers2_open_brandons_locker:
    scene mainhall_lockers2
    p "Yes! Okay, let's see what's in here to help me."
    p "10 bucks and some condoms. Oh! What's this? A flash drive..?"
    $ have_looked_in_brandons_locker = True
    $ inventory.add(condoms)
    $ inventory.add(flash_drive)
    $ money += 10
    $ inventory.money += 10
    $ return_label = "main_hall"
    $ special_inventory_display = True
    $ mom_in_main_hallway = True
    $ hints_counter += 1
    hide mainhall_lockers
    call screen inventory_screen

label interaction_school_map_female_wc_brandon_cant_enter:
    show school_map
    p "I can't go in there as Brandon. I would get into trouble."
    call screen school_map

label interaction_school_map_female_wc_anders_cant_enter:
    show school_map
    p "I can't go in there as Anders. I would only get him fired."
    call screen school_map

label interaction_school_map_classes_already_in_session:
    show school_map
    p "Classes have already begun. I don't want to look suspicious, by walking into the wrong class."
    call screen school_map

label interaction_school_map_upstairs:
    show school_map
    p "No reason to go there, right now."
    call screen school_map

label interaction_school_deans_office_door:
    scene deans_office_main
    p "There's no time for that. I need to find a way into her computer."
    call screen deans_office

label interaction_school_map_exit_beth_waiting_in_female_wc:
    show school_map
    p "I can't leave yet. Beth is waiting for me in the girl's toilets."
    call screen school_map


label interaction_school_map_exit_dean_waiting_in_office:
    show school_map
    p "The Dean is waiting for me upstairs in her office."
    call screen school_map

label interaction_deans_office_found_secret2:
    show office_books
    jor "You have found secret 2. You can view it on your phone."
    call screen deans_office_bookshelf

label need_to_see_where_anders_is_first:
    scene school_map
    p "Before going up to his office, I need to see where Anders is first."
    jump school

label anders_is_teaching_time_to_sneak_into_office:
    scene mranderss01_teaching01
    p "Great, Anders is teaching his Biology class. Now is a good time to check out his office. It's upstairs, same as the Dean’s."
    $ ready_to_sneak_into_anders_office_stage = 2
    jump school

label still_trying_to_find_ivana_in_school_after_searching_anders_office:
    scene school_map
    p "I can't leave yet. I need to catch Ivana and tell her what I found."
    jump school


label interaction_school_anders_office_picture:
    scene anders_office_main
    if currently_possessed_anders:
        if not mc_anders_taught_anders_class:
            p "Hmm, yes. A nice park image."
            call screen anders_office
        else:
            p "An image of some park."
    else:
        p "Just one of this nature relaxation pictures."
    jump anders_office
label interaction_school_anders_office_laptop:
    scene anders_office_main

    if currently_possessed_anders:
        if not mc_anders_taught_anders_class:
            p "My eyes are almost drooping to the floor. I don’t want to look at a computer screen right now. I’m too tired."
            call screen anders_office
        else:
            p "Hmmm. This computer has nothing interesting. Only teachers things and e-mails. Nothing special."
    else:
        if anders_office_found_flash_drive:
            p "Hmm? Ivana’s folder looks bigger than the other student’s. Let’s see..."
            scene policeman_s15_ivana_anim1
            $ renpy.movie_cutscene("scenes/Policeman/15_searching_anders_office/ivana_dildo_cam2.webm", loops=2, delay=-1, stop_music=False)
            scene policeman_s15_ivana_anim2
            $ renpy.movie_cutscene("scenes/Policeman/15_searching_anders_office/ivana_move.webm", loops=0, delay=-1, stop_music=False)
            $ renpy.movie_cutscene("scenes/Policeman/15_searching_anders_office/ivana_face.webm", loops=2, delay=-1, stop_music=False)
            $ renpy.movie_cutscene("scenes/Policeman/15_searching_anders_office/ivana_final.webm", loops=0, delay=-1, stop_music=False)
            scene policeman_s15_ivana
            p "Wow, and there is even more of her."#TODO ivana pics and diary
            p "Where did he get that? Is Ivana his next target?!"
            scene policeman_s15_ivana2
            p "I will upload all this stuff to my files. Better to put everything back where I found it and go, before his biology class ends."
            p "I should find Ivana immediatelly and tell her what I found, before she leaves."
            jump scene_cop_runs_into_anders_in_main_hall

        else:
            p "There is a lot of teachers' stuff but nothing about Scarlett."
    jump anders_office
label interaction_school_anders_office_books:
    scene anders_office_main
    if currently_possessed_anders:
        if not mc_anders_taught_anders_class:
            p "Just some stupid literature. I will check it closely later."
            call screen anders_office
        else:
            p "Just school books. Nothing interesting."
    else:
        p "All the books are about Biology. There is nothing weird about them."
    jump anders_office
label interaction_school_anders_office_drawer:
    scene anders_office_main
    if currently_possessed_anders:
        if not mc_anders_taught_anders_class:
            p "I wanna sleep."
            call screen anders_office
        else:
            jump anders_office_drawer
    else:
        p "Only student’s information. Nothing special about Scarlett"
    jump anders_office
label interaction_school_anders_office_plant:
    scene anders_office_main
    if currently_possessed_anders:
        if not mc_anders_taught_anders_class:
            p "Really? Why should I look at some stupid plant right now?"
            call screen anders_office
        else:
            p "Nothing special about this plant. Nothing is hidden under it this time."
    else:
        p "Big plant."
        if anders_office_found_key == False:
            p "I’m not a plant lover, but I don’t think it’s supposed to stand uneven like that... Hah. What luck. There is a key under the plant."
            $ anders_office_found_key = True
    jump anders_office
label interaction_school_anders_office_couch:
    scene anders_office_main
    if currently_possessed_anders:
        if not mc_anders_taught_anders_class:
            jump scene_mc_anders_sleeps_on_office_couch
        else:
            p "My neck is feels like it's been rolled up by a bulldozer, after sleeping the whole night on this couch. I will not be trying that again."

    else:
        p "Just a couch."
    jump anders_office

label interaction_school_anders_office_chest:
    scene anders_office_main

    if currently_possessed_anders:
        if not mc_anders_taught_anders_class:
            p "It’s unlocked. Full of lots of stuff. I will check it later. Right now, this couch behind me looks like the best thing to do."
            call screen anders_office
        else:
            if not mc_has_keys_to_anders_house:
                p "Hmmm, a lot of stuff here. I found some Keys likely for Anders’ place. I'll add them to his other keys. And hey, 50 bucks. That will come in handy."
                $ money += 50
                $ inventory.money += 50
                $ mc_has_keys_to_anders_house = True
                $ mc_anders_needs_to_find_anders_keys_in_office = False
                $ hints_counter += 1
                call screen anders_office
            else:
                p "Nothing else useful in there."
    else:
        if anders_office_found_key == False:
            p "It is locked. And without a key I absolutely cannot get inside."
        elif anders_office_found_flash_drive:
            p "Nothing interesting in there."
        else:
            p "What's in here? A lot of papers and a flashdrive. I can check it out on his laptop."
            $ anders_office_found_flash_drive = True
    jump anders_office

label interaction_school_map_female_wc_cop_anders_probably_not_there:
    scene school_map
    p "Could Anders be in the girls toilets? I wouldn't put it past him."
    jump school

label interaction_school_map_female_wc_cop_cant_enter:
    scene school_map
    p "I would rather avoid a public scandal."
    jump school

label interaction_school_map_looking_for_anders_not_in_there:
    scene school_map
    p "Anders is not in there."
    jump school

label interaction_anders_office_found_secret3:
    scene anders_office_main
    jor "You have found secret 3. You can view it on your phone."
    call screen anders_office

label interaction_anders_classroom1_already_know_sophia_at_gym:
    scene classroom1
    show classroom1_anders:
        xpos 781 ypos 371
    if not anders_desk_secret_found:
        show classroom1_secret:
            xpos 838 ypos 623
    p "I already know Sophia is at the gym behind the school."
    jump class1

label interaction_male_wc_stall_door:
    scene male_wc_main
    p "I don’t need to go there, right now."
    jump male_wc

label interaction_male_wc_mirror:
    scene male_wc_main
    if currently_possessed_cop:
        scene policeman_mirror
        p "This body really has power. And maybe the girls will appreciate it."
    elif currently_possessed_brandon:
        scene brandon_mirror
        p "Heh, much better than that bum. I think in the body of Brandon I can get almost every girl in this school."
    else:
        p "Nothing to see in a mirror. Nobody can see me. Not even a mirror."
    jump male_wc

label interaction_male_wc_urinal:
    scene male_wc_main
    if currently_possessed_cop or currently_possessed_brandon or currently_possessed_anders:
        scene mens_pissing
        p "Uhmmmmmm..."
    else:
        p "I'm scared to try, when I'm like this..."
    jump male_wc

label interaction_anders_desk_found_secret4:
    scene classroom1
    show classroom1_anders:
        xpos 781 ypos 371
    jor "You have found secret 4. You can view it on your phone."
    call screen class1



label interaction_school_map_exit_have_to_pee:
    show school_map
    p "No time for that now! I really gotta pee!"
    call screen school_map

label interaction_school_map_exit_need_to_see_dean_to_reenroll:
    show school_map
    p "No time to walk around, I need to see the Dean, to re-enroll Scarlett."
    call screen school_map

label interaction_dining_hall_brooke_and_beth:
    scene school_dining_hall
    show school_dining_hall_secret:
        xpos 535 ypos 460
    p "(I don't want to talk to those bitches.)"
    jump dining_hall

label interaction_school_map_male_wc_scarlett_cant_enter:
    show school_map
    p "I can't go in there as Scarlett. I would get into trouble."
    call screen school_map
label interaction_school_map_exit_feeling_weird_after_lab_tests:
    show school_map
    p "I'm feeling weird right now. I should sit on the toilet, just in case."
    call screen school_map

label interaction_cafeteria_found_secret6:
    scene school_dining_hall
    show school_dining_hall_secret:
        xpos 535 ypos 460
    jor "You have found secret 6. You can view it on your phone."
    call screen dining_hall

label interaction_school_map_female_wc_leave_her_to_happy_time:
    show female_wc_main
    p "I think I'll leave her to her happy time. I need to find Ivana and Sophia."
    call screen female_wc

label interaction_school_map_upstairs_not_seen_meg_in_stall:
    show school_map
    p "I should check downstairs for Ivana and Sophia first."
    call screen school_map


label interaction_school_map_exit_not_found_ivana_n_sophia:
    show school_map
    p "I have to find Ivana and Sophia first. They should still be here."
    call screen school_map

label female_wc_cant_leave_megan_jacking_sounds:
    scene female_wc_main
    p "I need to find out what those sounds are, before I go."
    jump female_wc

label interaction_school_map_upstairs_dont_want_anders_offer:
    show school_map
    p "No way am I going to go see Anders, right now. Unless I want to get fucked. Literally."
    call screen school_map

label interaction_gym_janitors_closet_found_bonus2:
    scene sporthall_cleaningroom_key
    show sporthall_cleaningroom_tree:
        xpos 1033 ypos 41
    jor "You have found bonus 2. You can view it on your phone."
    call screen gym_janitor_closet

label interaction_school_map_upstairs_mc_anders_late_for_class:
    show school_map
    p "I should probably get to Anders' class. Or he'll get in trouble."
    call screen school_map


label interaction_anders_office_whip_in_drawer:
    if not mc_anders_has_whipped_devil:
        jump scene_mc_anders_whipping_devil
    else:
        p "Let's just leave it alone now."
        call screen anders_office_drawer

label interaction_anders_office_exit:
    if mc_anders_taught_anders_class:
        if mc_has_keys_to_anders_house:
            jump school
        else:
            scene anders_office_main
            p "I have to find the keys to Anders' house before I go anywhere."
    else:
        scene anders_office_main
        p "I'm not going anywhere. I need to sleep."
        call screen anders_office
    jump anders_office

label interaction_school_map_can_now_go_to_anders_apartment:
    scene city_map
    p "Okay, now that I have Anders' keys, I can visit his apartment now."
    $ anders_apartment_available = True
    $ time_of_day = Set_Time_of_Day('ÖĞLEN')
    call screen city_map


label need_to_visit_scarlett_in_hopital_now:
    scene school_map
    p "I'll leave them to their video. I need to go see Scarlett in the hospital right now."
    jump school

label need_to_find_anders_house_keys_now:
    scene school_map
    p "I'll leave them to their video. Suckers..."
    jump school

label interaction_anders_class_students_have_their_third_task:
    scene school_map
    p "They have their task. They should be okay for now."
    jump school

label interaction_anders_class_students_left_alone_fourth_time:
    scene school_map
    p "I'm sure they'll be fine on their own. I need to collect the DNA results at the hospital."
    jump school

label interaction_anders_class_have_sophia_watching_it:
    scene school_map
    if accepted_devils_offer_for_anders_soul:
        p "No time for class. I need to look for Brooke."
    elif not accepted_devils_offer_for_anders_soul:
        p "As nice as it was to be invited by the girls, I think being instrumental in their win is enough thanks. Well, time to pick up Rebecca for lunch."
    jump school

label interaction_computer_class_no_reason_for_anders_to_enter:
    scene school_map
    p "As a teacher, I shouldn't be walking into other classes."
    if accepted_devils_offer_for_anders_soul:
        p "I need to look for Brooke."
    jump school
