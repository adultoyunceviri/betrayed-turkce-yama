
screen city_map:
    on "show" action Play('music', "sounds/music/Sexy_music3_Sunday_Plans.ogg", if_changed=True)
    imagemap:
        if time_of_day == 'GECE':
            ground "map/city_map_night.webp"
        else:
            ground "map/city_map.webp"
        add "time_%s"%(TimeOfDay_Dict.keys()[TimeOfDay_Dict.values().index(time_of_day)])#time)

        imagebutton: # School
            idle "marker_idle"
            hover "marker_hover"
            xpos 140 ypos 227
            if time_of_day in ('AKŞAM', 'GECE'):
                action Jump("interaction_city_map_school_closed") hovered ShowTransient ("school_overlay") unhovered Hide("school_overlay")
            else:
                if currently_posessed_homeless_guy == True:
                    action Jump("scene_homeless_guy_security_guard_enter_school") hovered ShowTransient ("school_overlay") unhovered Hide("school_overlay")
                elif ready_for_call_from_dealer == True:
                    action Jump("scene_brandon_and_security_guard") hovered ShowTransient ("school_overlay") unhovered Hide("school_overlay")
                elif cop_ready_to_request_pills_from_megan:
                    action Jump("scene_cop_requesting_pills_from_megan") hovered ShowTransient ("school_overlay") unhovered Hide("school_overlay")
                elif cop_ready_to_collect_pills_from_megan:
                    action Jump("scene_cop_collecting_pills_from_megan") hovered ShowTransient ("school_overlay") unhovered Hide("school_overlay")
                elif time_to_look_at_scarletts_flash_drive:
                    action Jump("sophia_upset_in_school_on_bikini_competition_day") hovered ShowTransient ("school_overlay") unhovered Hide("school_overlay")
                elif double_check_the_hospital_after_paying_first_rent:
                    action Jump("interaction_city_map_school_need_to_check_hospital_first") hovered ShowTransient ("school_overlay") unhovered Hide("school_overlay")
                elif megan_desperately_needs_scarlett_in_lab:
                    action Jump("scene_megan_needs_scarlett_in_lab_immediately") hovered ShowTransient ("school_overlay") unhovered Hide("school_overlay")
                elif have_to_return_found_pill_to_meg:
                    action Jump("scene_as_scarlett_returning_lost_pill_to_meg_in_lab") hovered ShowTransient ("school_overlay") unhovered Hide("school_overlay")
                elif have_to_get_meg_coffee_from_shop:
                    action Jump("interaction_city_map_school_need_to_get_megan_coffee_first") hovered ShowTransient ("school_overlay") unhovered Hide("school_overlay")
                elif onetime_megan_asks_to_speak_to_mc_anders_in_school:
                    action Jump("scene_megan_asks_to_talk_to_mc_anders_in_school") hovered ShowTransient ("school_overlay") unhovered Hide("school_overlay")
                elif onetime_mc_anders_needs_to_deliver_pills_file_to_megan:
                    action Jump("scene_as_anders_deliver_pills_file_to_megan") hovered ShowTransient ("school_overlay") unhovered Hide("school_overlay")
                elif onetime_time_for_at_school_consequences_of_winners_party:
                    action Jump("scene_enter_school_day_after_winners_party") hovered ShowTransient ("school_overlay") unhovered Hide("school_overlay")
                else:
                    action Jump("school") hovered ShowTransient ("school_overlay") unhovered Hide("school_overlay")

        imagebutton: # Crash Site
            idle "marker_idle"
            hover "marker_hover"
            xpos 616 ypos 379
            action Jump("crash_site") hovered ShowTransient ("crash_overlay") unhovered Hide("crash_overlay")

        imagebutton: # Apartment
            idle "marker_idle"
            hover "marker_hover"
            xpos 1145 ypos 219
            if have_taken_keys_from_sewer == True:
                if currently_posessed_homeless_guy == True:
                    if time_of_day == 'GECE':#TODO refactor cases for going to apartment
                        action Jump("interaction_city_map_apartment_sophia_hobo") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                    else:
                        action SetVariable("hints_counter", hints_counter + 1), Jump("apartment_map") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                elif currently_possessed_brandon:
                    if has_stuff_been_moved_from_apartment:
                        action Jump("interaction_city_map_apartment_map_stuff_moved_out") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                    else:
                        action Jump("apartment_map") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                elif currently_possessed_cop:
                    if sophia_waiting_for_cop_in_her_apartment:
                        action Jump("scene_cop_questions_sophia_in_apartment_about_scarlett") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                    else:
                        action Jump("interaction_city_map_apartment_map_stuff_moved_out") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                elif currently_possessed_scarlett:
                    if not have_gotten_old_apartment_room_back:
                        if scarlett_kicked_out_of_ivanas_apartment:
                            action Jump("scene_as_scarlett_sophia_apartment_first_time") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                        else:
                            action Jump("no_need_to_go_to_hospital") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                    else:
                        if need_to_get_scarlets_stuff_from_police_station:
                            action Jump("interaction_city_map_apartment_map_need_to_get_stuff") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                        elif looking_for_a_job_as_scarlett:
                            action Jump("interaction_city_map_apartment_map_need_to_get_job") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                        elif double_check_the_hospital_after_paying_first_rent:
                            action Jump("interaction_city_map_apartment_map_need_to_get_to_school") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                        elif checking_hospital_again_after_first_lab_tests:
                            action Jump("interaction_city_map_apartment_map_need_to_get_to_check_hospital_again") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                        elif have_to_tell_sophia_about_beth_brooke_talk:
                            action Jump("scene_go_to_apartment_to_tell_sophia_about_beth_brook_talk") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                        elif have_to_return_found_pill_to_meg:
                            action Jump("interaction_city_map_apartment_map_need_to_get_to_return_lost_pill") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")

                        else:
                            action Jump("apartment_map") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                elif currently_possessed_anders:
                    if onetime_mc_anders_ready_for_winners_party:
                        action Jump("scene_mc_anders_arrives_at_winners_party") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                    else:
                        action Jump("interaction_city_map_apartment_map_cant_enter_as_anders") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
                else:
                    action Jump("apartment_map") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")
            else:
                action Jump("interaction_city_map_apartment_map_cant_enter") hovered ShowTransient ("apartment_overlay") unhovered Hide("apartment_overlay")

        imagebutton: # Beach
            idle "marker_idle"
            hover "marker_hover"
            xpos 976 ypos 755
            if time_to_give_pills_to_sophia_for_bikini_competition:
                action Jump("scene_beach_bikini_competition") hovered ShowTransient ("beach_overlay") unhovered Hide("beach_overlay")
            elif time_for_afternoon_choices_after_pills_colouring:
                action Jump("scene_one_of_three_beach") hovered ShowTransient ("beach_overlay") unhovered Hide("beach_overlay")
            else:
                action Jump("beach") hovered ShowTransient ("beach_overlay") unhovered Hide("beach_overlay")

        imagebutton: # Shop
            idle "marker_idle"
            hover "marker_hover"
            xpos 1146 ypos 557
            if time_of_day == 'GECE':
                action Jump("interaction_city_map_shop_closed") hovered ShowTransient ("shop_overlay") unhovered Hide("shop_overlay")
            else:
                if time_for_coffee_and_researching_scarlett_case == True:
                    action Jump("scene_coffee_shop_before_researching_scarlett_case") hovered ShowTransient ("shop_overlay") unhovered Hide("shop_overlay")
                elif looking_for_a_job_as_scarlett and not strip_club_location_available:
                    action Jump("scene_coffee_shop_ask_about_job_as_scarlet") hovered ShowTransient ("shop_overlay") unhovered Hide("shop_overlay")
                elif have_to_get_meg_coffee_from_shop:
                    action Jump("scene_return_to_lab_after_buying_coffee_for_meg") hovered ShowTransient ("shop_overlay") unhovered Hide("shop_overlay")
                elif have_to_meet_megan_at_coffee_shop:
                    action Jump("scene_mc_scarlett_coffee_shop_with_megan") hovered ShowTransient ("shop_overlay") unhovered Hide("shop_overlay")
                elif time_for_afternoon_choices_after_pills_colouring:
                    action Jump("scene_one_of_three_coffee_shop") hovered ShowTransient ("shop_overlay") unhovered Hide("shop_overlay")
                elif onetime_mc_anders_time_for_restaurant_before_party:
                    action Jump("scene_mc_anders_at_restaurant_before_party") hovered ShowTransient ("shop_overlay") unhovered Hide("shop_overlay")
                else:
                    action Jump("shop_main") hovered ShowTransient ("shop_overlay") unhovered Hide("shop_overlay")

        imagebutton: # Warehouse
            idle "marker_idle"
            hover "marker_hover"
            xpos 217 ypos 421
            if brandon_waiting_at_warehouse_for_cop:
                action Jump("scene_cop_meets_brandon_at_warehouse") hovered ShowTransient ("warehouse_overlay") unhovered Hide("warehouse_overlay")
            elif time_to_meet_brandon_at_warehouse_for_drug_sale:
                action Jump("scene_cop_brandon_drug_sale_at_warehouse") hovered ShowTransient ("warehouse_overlay") unhovered Hide("warehouse_overlay")
            else:
                action Jump("warehouse_main") hovered ShowTransient ("warehouse_overlay") unhovered Hide("warehouse_overlay")

        imagebutton: # Park
            idle "marker_idle"
            hover "marker_hover"
            xpos 225 ypos 104
            if has_learned_about_posession == False:
                action Jump("interaction_city_map_park_no_time") hovered ShowTransient ("park_overlay") unhovered Hide("park_overlay")
            else:
                action Jump("park_main") hovered ShowTransient ("park_overlay") unhovered Hide("park_overlay")
        if is_taxi_stand_available:
            imagebutton: # Taxi Stand
                idle "marker_idle"
                hover "marker_hover"
                xpos 944 ypos 524
                if need_to_take_taxi_to_brandons_house == True:
                    action Jump("scene_brandon_at_home_first_time") hovered ShowTransient ("taxi_overlay") unhovered Hide("taxi_overlay")
                else:
                    action Jump("interaction_city_map_taxi_stand_no_time") hovered ShowTransient ("taxi_overlay") unhovered Hide("taxi_overlay")
        if is_cops_apartment_available:
            imagebutton: # Cops Apartment
                idle "marker_idle"
                hover "marker_hover"
                xpos 586 ypos 34
                if not den_location_available:
                    if cop_can_hear_muffled_voice:
                        action Jump("scene_cops_apartment_hallway_can_hear_muffled_voice") hovered ShowTransient ("cop_overlay") unhovered Hide("cop_overlay")
                    elif drug_sell_choice_consequence_time:
                        if chose_to_sell_drugs_to_brandon:
                            action Jump("idle_cop_apartment_drug_sale_reminder") hovered ShowTransient ("cop_overlay") unhovered Hide("cop_overlay")
                        elif not chose_to_sell_drugs_to_brandon:
                            action Jump("cop_apartment_main") hovered ShowTransient ("cop_overlay") unhovered Hide("cop_overlay")
                    elif night_before_interrogation_consequence_time:
                        action Jump("scene_cops_apartment_night_before_interrogation_consequence_time") hovered ShowTransient ("cop_overlay") unhovered Hide("cop_overlay")
                    elif time_for_bed_after_bikini_competition:
                        action Jump("idle_cop_apartment_tired_after_bikini_competition") hovered ShowTransient ("cop_overlay") unhovered Hide("cop_overlay")
                    elif time_to_sort_through_scarlett_case_clues:
                        action Jump("scene_cop_apartment_sorting_through_scarlett_case_info") hovered ShowTransient ("cop_overlay") unhovered Hide("cop_overlay")
                    elif have_changed_clothes_as_cop:
                        action Jump("cop_apartment_main") hovered ShowTransient ("cop_overlay") unhovered Hide("cop_overlay")
                    else:
                        action Jump("scene_cops_apartment_first_time") hovered ShowTransient ("cop_overlay") unhovered Hide("cop_overlay")
                else:
                    action Jump("no_need_to_go_to_hospital") hovered ShowTransient ("cop_overlay") unhovered Hide("cop_overlay")
        if hospital_location_available:
            imagebutton: # Hospital
                idle "marker_idle"
                hover "marker_hover"
                xpos 510 ypos 614
                if have_apointment_at_hospital:
                    action Jump("scene_hospital_first_time") hovered ShowTransient ("hospital_overlay") unhovered Hide("hospital_overlay")
                elif looking_for_a_job_as_scarlett:
                    action Jump("scene_hospital_carpark_no_car") hovered ShowTransient ("hospital_overlay") unhovered Hide("hospital_overlay")
                elif double_check_the_hospital_after_paying_first_rent:
                    action Jump("scene_hospital_carpark_double_check") hovered ShowTransient ("hospital_overlay") unhovered Hide("hospital_overlay")
                elif checking_hospital_again_after_first_lab_tests:
                    action Jump("scene_devil_at_hospital_when_looking_for_mom") hovered ShowTransient ("hospital_overlay") unhovered Hide("hospital_overlay")
                elif mc_anders_wants_to_visit_scarlett_in_hospital:
                    action Jump("scene_mc_anders_checking_on_scarlett_in_hospital") hovered ShowTransient ("hospital_overlay") unhovered Hide("hospital_overlay")
                elif onetime_megan_referred_mc_anders_to_kate_at_hospital:
                    action Jump("scene_mc_anders_referred_by_meg_to_kate") hovered ShowTransient ("hospital_overlay") unhovered Hide("hospital_overlay")
                elif onetime_mc_anders_needs_to_collect_dna_results:
                    action Jump("scene_mc_anders_collects_dna_results") hovered ShowTransient ("hospital_overlay") unhovered Hide("hospital_overlay")
                else:
                    action Jump("no_need_to_go_to_hospital") hovered ShowTransient ("hospital_overlay") unhovered Hide("hospital_overlay")
        if ivana_apartment_available:
            imagebutton: # Ivana's apartment
                idle "marker_idle"
                hover "marker_hover"
                xpos 810 ypos 384
                if currently_possessed_cop:
                    if not been_to_ivanas_apartment_first_time:
                        action Jump("scene_ivanas_apartment_first_time") hovered ShowTransient ("ivana_overlay") unhovered Hide("ivana_overlay")
                    elif not made_entrapment_deal_with_ivana:
                        if cop_can_hear_muffled_voice or cop_ready_to_request_pills_from_megan:
                            action Jump("interaction_city_map_ivanas_apartment_no_need_to_bother_her") hovered ShowTransient ("ivana_overlay") unhovered Hide("ivana_overlay")
                        else:
                            action Jump("scene_cop_makes_entrapment_deal_with_ivana") hovered ShowTransient ("ivana_overlay") unhovered Hide("ivana_overlay")
                    elif made_entrapment_deal_with_ivana:
                        if not done_anders_sting_operation_at_ivanas:
                            if gun in inventory.items and pills in inventory.items:
                                action Jump("scene_sting_operation_at_ivanas") hovered ShowTransient ("ivana_overlay") unhovered Hide("ivana_overlay")
                            else:
                                action Jump("interaction_city_map_ivanas_apartment_not_time_for_sting") hovered ShowTransient ("ivana_overlay") unhovered Hide("ivana_overlay")
                        elif done_anders_sting_operation_at_ivanas:
                            if as_cop_ready_to_search_for_scarlets_diary:
                                action Jump("scene_search_for_scarlet_diary_at_ivanas") hovered ShowTransient ("ivana_overlay") unhovered Hide("ivana_overlay")
                            else:
                                action Jump("interaction_city_map_ivanas_apartment_no_need_to_bother_her") hovered ShowTransient ("ivana_overlay") unhovered Hide("ivana_overlay")
                elif currently_possessed_scarlett:
                    if not scarlett_kicked_out_of_ivanas_apartment:
                        action Jump("scene_as_scarlett_ivanas_apartment_first_time") hovered ShowTransient ("ivana_overlay") unhovered Hide("ivana_overlay")
                    else:
                        action Jump("no_need_to_go_to_hospital") hovered ShowTransient ("ivana_overlay") unhovered Hide("ivana_overlay")
                else:
                    action Jump("no_need_to_go_to_hospital") hovered ShowTransient ("ivana_overlay") unhovered Hide("ivana_overlay")
        if gym_location_available:
            imagebutton: # Gym
                idle "marker_idle"
                hover "marker_hover"
                xpos 15 ypos 290
                if looking_for_sophia_about_pills_progress:
                    action Jump("scene_girls_playing_volleyball_at_gym") hovered ShowTransient ("gym_overlay") unhovered Hide("gym_overlay")
                elif time_to_punish_beth_n_brooke_in_sports_hall:
                    action Jump("scene_girls_playing_volleyball_at_gym_again") hovered ShowTransient ("gym_overlay") unhovered Hide("gym_overlay")
                else:
                    action Jump("no_need_to_go_to_hospital") hovered ShowTransient ("gym_overlay") unhovered Hide("gym_overlay")

        if police_station_location_available:
            imagebutton: # Police Station
                idle "marker_idle"
                hover "marker_hover"
                xpos 416 ypos 359
                if currently_possessed_cop:
                    if as_cop_ready_to_interrogate_brandon:
                        action Jump("police_station_interrogation_room") hovered ShowTransient ("police_overlay") unhovered Hide("police_overlay")
                    else:
                        action Jump("no_need_to_go_to_hospital") hovered ShowTransient ("police_overlay") unhovered Hide("police_overlay")
                elif currently_possessed_scarlett:
                    if need_to_get_scarlets_stuff_from_police_station:
                        action Jump("scene_as_scarlett_police_station_first_time") hovered ShowTransient ("police_overlay") unhovered Hide("police_overlay")
                    else:
                        action Jump("no_need_to_go_to_hospital") hovered ShowTransient ("police_overlay") unhovered Hide("police_overlay")
                else:
                    action Jump("no_need_to_go_to_hospital") hovered ShowTransient ("police_overlay") unhovered Hide("police_overlay")
        if den_location_available:
            imagebutton: # Den
                idle "marker_idle"
                hover "marker_hover"
                 # xpos 988 ypos 289
                xpos 104 ypos 95
                if currently_possessed_cop:
                    action Jump("scene_first_time_at_den") hovered ShowTransient ("den_overlay") unhovered Hide("den_overlay")
                else:
                    action Jump("no_need_to_go_to_hospital") hovered ShowTransient ("den_overlay") unhovered Hide("den_overlay")

        if strip_club_location_available:
            imagebutton: # Strip Club
                idle "marker_idle"
                hover "marker_hover"
                xpos 1446 ypos 657
                if looking_for_a_job_as_scarlett:
                    action Jump("scene_as_scarlett_at_strip_first_time") hovered ShowTransient ("strip_overlay") unhovered Hide("strip_overlay")
                else:
                    action Jump("no_need_to_go_to_hospital") hovered ShowTransient ("strip_overlay") unhovered Hide("strip_overlay")

        if anders_apartment_available:
            imagebutton: # Anders Apartment
                idle "marker_idle"
                hover "marker_hover"
                xpos 904 ypos 14
                if not mc_anders_settled_in_as_anders:
                    action Jump("scene_first_time_in_anders_apartment") hovered ShowTransient ("anders_overlay") unhovered Hide("anders_overlay")
                elif onetime_mc_anders_ready_for_winners_party:
                    action Jump("no_need_late_for_winners_party") hovered ShowTransient ("anders_overlay") unhovered Hide("anders_overlay")
                else:
                    action Jump("anders_flat") hovered ShowTransient ("anders_overlay") unhovered Hide("anders_overlay")


        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "city_map"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "city_map"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "city_map"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "city_map"), Jump("joraell_message_no_phone")
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

screen school_overlay:
    frame:
        background Frame("map/school_overlay.png")
        transclude

screen crash_overlay:
    frame:
        background Frame("map/crash_overlay.png")
        transclude

screen apartment_overlay:
    frame:
        background Frame("map/apartment_overlay.png")
        transclude

screen beach_overlay:
    frame:
        background Frame("map/beach_overlay.png")
        transclude

screen shop_overlay:
    frame:
        background Frame("map/shop_overlay.png")
        transclude

screen park_overlay:
    frame:
        background Frame("map/park_overlay.png")
        transclude

screen warehouse_overlay:
    frame:
        background Frame("map/warehouse_overlay.png")
        transclude

screen taxi_overlay:
    frame:
        background Frame("map/taxi_overlay.png")
        transclude

screen cop_overlay:
    frame:
        background Frame("map/cop_overlay.png")
        transclude

screen hospital_overlay:
    frame:
        background Frame("map/hospital_overlay.png")
        transclude

screen ivana_overlay:
    frame:
        background Frame("map/ivana_overlay.png")
        transclude

screen gym_overlay:
    frame:
        background Frame("map/gym_overlay.png")
        transclude
screen den_overlay:
    frame:
        background Frame("map/unknown_house_overlay.png")
        transclude
screen police_overlay:
    frame:
        background Frame("map/police_overlay.png")
        transclude
screen strip_overlay:
    frame:
        background Frame("map/strip_overlay.png")
        transclude
screen anders_overlay:
    frame:
        background Frame("map/anders_overlay.png")
        transclude

label city_map:
    scene black_screen
    #$ renpy.pause(0.1, hard=True)
    if not done_anders_sting_operation_at_ivanas and made_entrapment_deal_with_ivana:
        if gun in inventory.items and pills in inventory.items:
            scene city_map
            p "I have everything I need. I should head to Ivana's."
            $ time_of_day = Set_Time_of_Day('AKŞAM')
    call screen city_map

label interaction_city_map_apartment_map_cant_enter:

    if time_of_day == 'GECE':
        scene city_map_night
    else:
        scene city_map
    p "It’s locked and I don’t have my keys."
    if time_of_day in ('SABAH', 'ÖĞLEN'):
        p "And Sophia is at school, right now."

    jump city_map

label interaction_city_map_apartment_map_stuff_moved_out:

    if time_of_day == 'GECE':
        scene city_map_night
    else:
        scene city_map
    p "Mom already moved my stuff out. No point in going back there right now."
    jump city_map

label interaction_city_map_school_closed:
    if time_of_day == 'GECE':
        scene city_map_night
    else:
        scene city_map
    p "The campus is closed at this time."

    jump city_map

label interaction_city_map_shop_closed:
    scene city_map_night
    p "The coffee shop is closed at night."

    jump city_map


label interaction_city_map_park_no_time:
    scene city_map
    p "This isn't the time for a stroll in the park."

    jump city_map

label interaction_city_map_apartment_sophia_hobo:
    show sophia_angry_at_hobo
    sop "Who are you!? I don’t have any money for you. Go away, or I will call the police!"
    jump city_map

label interaction_city_map_taxi_stand_no_time:
    if time_of_day == 'GECE':
        scene city_map_night
    else:
        scene city_map
    p "I don't need a taxi right now."

    jump city_map

label interaction_city_map_ivanas_apartment_not_time_for_sting:
    scene city_map
    p "I still need to pick up some things before going back for the sting operation."

    jump city_map

label interaction_city_map_ivanas_apartment_no_need_to_bother_her:
    if time_of_day == 'GECE':
        scene city_map_night
    else:
        scene city_map
    p "I have nothing to talk to her about right now."

    jump city_map

label no_need_to_go_to_hospital:
    if time_of_day == 'GECE':
        scene city_map_night
    else:
        scene city_map
    p "I don't need to go there right now."

    jump city_map

label interaction_city_map_apartment_map_need_to_get_stuff:
    scene city_map
    p "I need to go and get Scarlett's stuff from the police station."
    jump city_map

label interaction_city_map_apartment_map_need_to_get_job:
    scene city_map
    p "I need to try and find a job today before I go back."
    jump city_map

label interaction_city_map_apartment_map_need_to_get_to_school:
    scene city_map
    p "Sophia already left and is waiting for us to go to school."
    jump city_map

label interaction_city_map_school_need_to_check_hospital_first:
    scene city_map
    p "I want to check out the hospital again before school."
    jump city_map

label interaction_city_map_apartment_map_need_to_get_to_check_hospital_again:
    scene city_map
    p "I want to check out the hospital again before going back to the apartment."
    jump city_map

label interaction_city_map_apartment_map_need_to_get_to_return_lost_pill:
    scene city_map
    p "No time for that. I need to return this pill to Meg and get more growing pills for Sophia and Ivana."
    jump city_map

label interaction_city_map_school_need_to_get_megan_coffee_first:
    scene city_map
    p "I can't go back without getting Megan her coffee first."
    jump city_map

label interaction_city_map_apartment_map_cant_enter_as_anders:

    if time_of_day == 'GECE':
        scene city_map_night
    else:
        scene city_map
    p "I no longer live there anymore. Now that I'm not Scarlett."

    jump city_map

label no_need_late_for_winners_party:
    scene city_map_night
    p "No time for anything else. I'm getting late for the party at Sophia's."
    jump city_map


label joraell_message_no_phone:
    $ menu_can_show_hint_hover = False
    $ menu_can_show_phone_hover = False
    $ menu_can_show_inventory_hover = False
    if current_screen == "mc_room":
        if mc_room_window_opened == True:
            scene mc_room_openedwindow
            jor "You do not currently have a phone."
            jump mc_room
        else:
            scene mc_room_day
            jor "You do not currently have a phone."
            jump mc_room
    elif current_screen == "mc_room_with_sofia_and_policeman":
        scene mc_room_day_cathy_policeman
        jor "You do not currently have a phone."
        jump mc_room_with_sofia_and_policeman
    elif current_screen == "city_map":
        if time_of_day == 'GECE':
            scene city_map_night
        else:
            scene city_map
        jor "You do not currently have a phone."
        jump city_map
    elif current_screen == "roommate_room":
        scene roommate_room_day
        jor "You do not currently have a phone."
        jump roommate_room
    elif current_screen == "bathroom":
        scene bathroom_main
        jor "You do not currently have a phone."
        jump bathroom
    elif current_screen == "bathroom_with_policeman_sniffing_panties":
        scene bathroom_main_policeman
        jor "You do not currently have a phone."
        jump bathroom_with_policeman_sniffing_panties
    elif current_screen == "living_room":
        scene livingroom_main
        jor "You do not currently have a phone."
        jump living_room
    elif current_screen == "kitchen":
        scene kitchen_main
        jor "You do not currently have a phone."
        jump kitchen
    elif current_screen == "warehouse_main":
        if time_of_day == 'GECE':
            scene warehouse_main_night
        else:
            scene warehouse_main_day
        jor "You do not currently have a phone."
        jump warehouse_main
    elif current_screen == "beach_main":
        if time_of_day == 'GECE':
            scene beach_main_night
        else:
            scene beach_main
        jor "You do not currently have a phone."
        jump beach
    elif current_screen == "crash_site":
        if time_of_day == 'GECE':
            scene crash_site_night
        else:
            scene crash_site_day
        jor "You do not currently have a phone."
        jump crash_site
    elif current_screen == "roses":
        if time_of_day == 'GECE':
            scene crash_site_roses_night
        else:
            scene crash_site_roses_day
        jor "You do not currently have a phone."
        jump roses
    elif current_screen == "sewer":
        if time_of_day == 'GECE':
            scene crash_site_sewer_night
        else:
            scene crash_site_sewer_day
        jor "You do not currently have a phone."
        jump sewer
    elif current_screen == "park_main":
        if time_of_day == 'GECE':
            scene park_perspective_night
        else:
            scene park_perspective_day
        jor "You do not currently have a phone."
        jump park_main
    elif current_screen == "park_bench":
        if time_of_day == 'GECE':
            scene park_bench_night
        else:
            scene park_bench_day
        jor "You do not currently have a phone."
        call screen park_bench
    elif current_screen == "hobo_tunnel":
        if time_of_day == 'GECE':
            scene park_hobo_tunnel_night
            if currently_posessed_homeless_guy == False:
                show park_homeless_guy_night
        else:
            scene park_hobo_tunnel_day
            if currently_posessed_homeless_guy == False:
                show park_homeless_guy_day:
                    xpos 600 ypos 465
        jor "You do not currently have a phone."
        jump hobo_tunnel
    elif current_screen == "shop_main":
        scene shop_main

        jor "You do not currently have a phone."
        call screen shop_main
    elif current_screen == "main_hall":
        scene main_hall
        jor "You do not currently have a phone."
        jump main_hall
    elif current_screen == "female_wc_with_megan":
        scene female_wc_main_megan
        jor "You do not currently have a phone."
        jump female_wc_with_megan
    elif current_screen == "dining_hall":
        scene school_dining_hall
        jor "You do not currently have a phone."
        jump dining_hall

label joraell_message_no_hints:
    $ menu_can_show_hint_hover = False
    $ menu_can_show_phone_hover = False
    $ menu_can_show_inventory_hover = False
    if current_screen == "mc_room":
        if mc_room_window_opened == True:
            scene mc_room_openedwindow
            jor "İpuçları gelecek bir sürümde mevcut olacaktır."
            jump mc_room
        else:
            if time_of_day != 'GECE':
                scene mc_room_day
            else:
                scene mc_room_night
            jor "İpuçları gelecek bir sürümde mevcut olacaktır."
            jump mc_room
    elif current_screen == "mc_room_with_sofia_and_policeman":
        scene mc_room_day_cathy_policeman
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump mc_room_with_sofia_and_policeman
    elif current_screen == "city_map":
        if time_of_day == 'GECE':
            scene city_map_night
        else:
            scene city_map
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump city_map
    elif current_screen == "roommate_room":
        scene roommate_room_day
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump roommate_room
    elif current_screen == "bathroom":
        scene bathroom_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump bathroom
    elif current_screen == "bathroom_with_policeman_sniffing_panties":
        scene bathroom_main_policeman
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump bathroom_with_policeman_sniffing_panties
    elif current_screen == "living_room":
        scene livingroom_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump living_room
    elif current_screen == "kitchen":
        scene kitchen_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump kitchen
    elif current_screen == "warehouse_main":
        if time_of_day == 'GECE':
            scene warehouse_main_night
        else:
            scene warehouse_main_day
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump warehouse_main
    elif current_screen == "beach_main":
        if time_of_day == 'GECE':
            scene beach_main_night
        else:
            scene beach_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump beach
    elif current_screen == "crash_site":
        if time_of_day == 'GECE':
            scene crash_site_night
        else:
            scene crash_site_day
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump crash_site
    elif current_screen == "roses":
        if time_of_day == 'GECE':
            scene crash_site_roses_night
        else:
            scene crash_site_roses_day
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump roses
    elif current_screen == "sewer":
        if time_of_day == 'GECE':
            scene crash_site_sewer_night
        else:
            scene crash_site_sewer_day
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump sewer
    elif current_screen == "park_main":
        if time_of_day == 'GECE':
            scene park_perspective_night
        else:
            scene park_perspective_day
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump park_main
    elif current_screen == "park_bench":
        if time_of_day == 'GECE':
            scene park_bench_night
        else:
            scene park_bench_day
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        call screen park_bench
    elif current_screen == "hobo_tunnel":
        if time_of_day == 'GECE':
            scene park_hobo_tunnel_night
            if currently_posessed_homeless_guy == False:
                show park_homeless_guy_night
        else:
            scene park_hobo_tunnel_day
            if currently_posessed_homeless_guy == False:
                show park_homeless_guy_day:
                    xpos 600 ypos 465
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump hobo_tunnel
    elif current_screen == "main_hall":
        scene main_hall
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump main_hall
    elif current_screen == "female_wc_with_megan":
        scene female_wc_main_megan
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump female_wc_with_megan
    elif current_screen == "deans_office":
        scene deans_office_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump deans_office
    elif current_screen == "deans_office_board":
        scene office_board
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump deans_office_board
    elif current_screen == "deans_office_bookshelf":
        scene office_books
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump deans_office_bookshelf
    elif current_screen == "deans_office_certificates":
        scene office_certificates
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump deans_office_certificates
    elif current_screen == "deans_office_binder":
        scene office_note
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump deans_office_binder
    elif current_screen == "deans_office_binder":
        scene office_note
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump deans_office_binder
    elif current_screen == "deans_office_picture_frames":
        scene office_picture
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump deans_office_picture_frames
    elif current_screen == "deans_office_telephone":
        scene office_telephone
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump deans_office_telephone
    elif current_screen == "deans_office_trophies":
        scene office_trophy
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump deans_office_trophies
    elif current_screen == "main_hall_board":
        scene main_hall_board
        if sophia_roommate_ad_placed == True:
            show mainhall_board_roommate:
                xpos 300 ypos 400
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        hide mainhall_board_roommate
        jump main_hall_board
    elif current_screen == "main_hall_lockers1":
        scene Mainhall_lockers1B
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump main_hall_lockers1
    elif current_screen == "main_hall_lockers2":
        scene Mainhall_lockers1
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump main_hall_lockers2
    elif current_screen == "class1":
        scene classroom1
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump class1
    elif current_screen == "class2":
        scene classroom2
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump class2
    elif current_screen == "computer_class":
        scene computer_class_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump computer_class
    elif current_screen == "male_wc":
        scene male_wc_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump male_wc
    elif current_screen == "female_wc":
        scene female_wc_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        jump female_wc
    elif current_screen == "shop_main":
        scene shop_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        call screen shop_main
    elif current_screen == "cop_apartment_main":
        scene policeman_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        call screen cop_apartment_main
    elif current_screen == "cop_apartment_bedroom":
        if have_left_panties_in_cops_bedroom:
            scene policeman_bedroom_panties
        else:
            scene policeman_bedroom
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        call screen cop_apartment_bedroom
    elif current_screen == "anders_office":
        scene anders_office_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        call screen anders_office
    elif current_screen == "anders_office_trashed":
        scene anders_office_harsch
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
        call screen anders_office_trashed
    elif current_screen == "ivana_apartment_scarlett_room":
        scene scarlett_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "ivana_apartment_teddy_closeup":
        scene main_bear
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "police_station_interrogation_room":
        scene interrogation_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "cop_apartment_closet":
        scene cop_stuff_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "cop_apartment_closet_closeup":
        scene cop_stuff_key
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "den_basement":
        scene _unknown_house_basement
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "scarlets_shoes":
        scene mc_room_shoes
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "dining_hall":
        scene school_dining_hall
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "gym_janitor_closet":
        if not have_gym_janitors_key:
            scene sporthall_cleaningroom_key
        else:
            scene sporthall_cleaningroom_nokey
        show sporthall_cleaningroom_tree:
            xpos 1033 ypos 41
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "bad_girls_locker_room":
        scene sporthall_locker_room
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "anders_kitchen":
        scene anders_flat_kitchen
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "anders_livingroom":
        if time_of_day == 'GECE':
            scene anders_flat_livingroom_night
        else:
            scene anders_flat_livingroom
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "anders_bedroom":
        if time_of_day == 'GECE':
            scene anders_flat_bedroom_night
        else:
            scene anders_flat_bedroom
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "anders_guestroom":
        if time_of_day == 'GECE':
            scene anders_flat_rebecca_room_night
        else:
            scene anders_flat_rebecca_room
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "anders_bathroom":
        scene anders_flat_bathroom
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "scarletts_room_winners_party":
        scene mc_room_night
        if not milestone_mc_anders_found_scarletts_flash_drive:
            show mcroom_party_scarlett:
                xpos 951 ypos 388
        if not milestone_winners_party_sophia_asked_for_drinks:
            show mcroom_party_others:
                xpos 501 ypos 228
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "sophias_room_winners_party":
        scene roommate_room_night
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "bathroom_winners_party":
        scene bathroom_main
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "living_room_winners_party":
        scene livingroom_party
        show livingroom_party_sophia:
            xpos 1175 ypos 415
        show livingroom_party_tracyandbrandon:
            xpos 53 ypos 385
        show livingroom_party_trophy:
            xpos 560 ypos 400
        if not winners_party_livingroom_secret10_found:
            show livingroom_party_secret10:
                xpos 554 ypos 478
        if milestone_winners_party_sophia_asked_for_drinks:
            show livingroom_party_others:
                xpos 190 ypos 190
        if milestone_mc_anders_recovered_pills_from_scarletts_bedstand:
            show livingroom_party_megan:
                xpos 800 ypos 200
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."
    elif current_screen == "kitchen_winners_party":
        scene kitchen_main
        if not toggle_mc_anders_talked_to_ivana_at_winners_party or milestone_winners_party_sophia_asked_for_drinks:
            show kitchen_party_ivana:
                xpos 733 ypos 160
        jor "İpuçları gelecek bir sürümde mevcut olacaktır."


    #advance to next label

label current_screen_selector:
    if current_screen == "mc_room":
        jump mc_room
    elif current_screen == "city_map":
        jump city_map
    elif current_screen == "roommate_room":
        jump roommate_room
    elif current_screen == "bathroom":
        jump bathroom
    elif current_screen == "bathroom_with_policeman_sniffing_panties":
        jump bathroom_with_policeman_sniffing_panties
    elif current_screen == "living_room":
        jump living_room
    elif current_screen == "kitchen":
        jump kitchen
    elif current_screen == "warehouse_main":
        jump warehouse_main
    elif current_screen == "beach_main":
        jump beach
    elif current_screen == "crash_site":
        jump crash_site
    elif current_screen == "roses":
        jump roses
    elif current_screen == "sewer":
        jump sewer
    elif current_screen == "park_main":
        jump park_main
    elif current_screen == "park_bench":
        if time_of_day == 'GECE':
            scene park_bench_night
        else:
            scene park_bench_day
        call screen park_bench
    elif current_screen == "hobo_tunnel":
        jump hobo_tunnel
    elif current_screen == "main_hall":
        jump main_hall
    elif current_screen == "female_wc_with_megan":
        jump female_wc_with_megan
    elif current_screen == "deans_office":
        jump deans_office
    elif current_screen == "deans_office_board":
        jump deans_office_board
    elif current_screen == "deans_office_bookshelf":
        jump deans_office_bookshelf
    elif current_screen == "deans_office_certificates":
        jump deans_office_certificates
    elif current_screen == "deans_office_binder":
        jump deans_office_binder
    elif current_screen == "deans_office_binder":
        jump deans_office_binder
    elif current_screen == "deans_office_picture_frames":
        jump deans_office_picture_frames
    elif current_screen == "deans_office_telephone":
        jump deans_office_telephone
    elif current_screen == "deans_office_trophies":
        jump deans_office_trophies
    elif current_screen == "main_hall_board":
        jump main_hall_board
    elif current_screen == "main_hall_lockers1":
        jump main_hall_lockers1
    elif current_screen == "main_hall_lockers2":
        jump main_hall_lockers2
    elif current_screen == "class1":
        jump class1
    elif current_screen == "class2":
        jump class2
    elif current_screen == "computer_class":
        jump computer_class
    elif current_screen == "male_wc":
        jump male_wc
    elif current_screen == "female_wc":
        jump female_wc
    elif current_screen == "shop_main":
        jump shop_main
    elif current_screen == "cop_apartment_main":
        scene policeman_main
        jump cop_apartment_main
    elif current_screen == "cop_apartment_bedroom":
        jump cop_apartment_bedroom
    elif current_screen == "anders_office":
        jump anders_office
    elif current_screen == "anders_office_trashed":
        jump anders_office_trashed
    elif current_screen == "ivana_apartment_scarlett_room":
        jump ivana_apartment_scarlett_room
    elif current_screen == "ivana_apartment_teddy_closeup":
        jump ivana_apartment_teddy_closeup
    elif current_screen == "police_station_interrogation_room":
        call screen police_station_interrogation_room
    elif current_screen == "cop_apartment_closet":
        jump cop_apartment_closet
    elif current_screen == "cop_apartment_closet_closeup":
        jump cop_apartment_closet_closeup
    elif current_screen == "den_basement":
        jump den_basement
    elif current_screen == "scarlets_shoes":
        jump scarlets_shoes
    elif current_screen == "dining_hall":
        jump dining_hall
    elif current_screen == "gym_janitor_closet":
        jump gym_janitor_closet
    elif current_screen == "bad_girls_locker_room":
        jump bad_girls_locker_room
    elif current_screen == "anders_kitchen":
        jump anders_kitchen
    elif current_screen == "anders_livingroom":
        jump anders_livingroom
    elif current_screen == "anders_bedroom":
        jump anders_bedroom
    elif current_screen == "anders_guestroom":
        jump anders_guestroom
    elif current_screen == "anders_bathroom":
        jump anders_bathroom
    elif current_screen == "scarletts_room_winners_party":
        jump scarletts_room_winners_party
    elif current_screen == "sophias_room_winners_party":
        jump sophias_room_winners_party
    elif current_screen == "bathroom_winners_party":
        jump bathroom_winners_party
    elif current_screen == "living_room_winners_party":
        jump living_room_winners_party
    elif current_screen == "kitchen_winners_party":
        jump kitchen_winners_party

label display_current_hint:
    $ hint_system_dict = {0: 'İpucu: Odadaki her şeye dokunmamışsın. Odadaki her şeyi denemeye çalış..',
    1: 'İpucu: Sophia ve Polis ne hakkında konuşuyor öğrenmeye çalış.',
    2: 'İpucu: Burada öğrenebildiğin her şeyi öğrendin. Artık kapı açık, evin geri kalanını keşfet ve ne bulup, ne yapabileceğini öğren.',
    3: 'İpucu: Şu an bir şey yapamazsın. Sanırsam Sophia\'yı okula kadar takip etmelisin.',
    4: 'İpucu: Okulda kapana mı kısıldın? Sanırsam bir şeyler okuyarak zamanın geçmesini beklemelisin.',
    5: 'İpucu: Potansiyel mülk kurbanı. Neden yakından bakmıyorsun?',
    6: 'İpucu: İçine girecek birini bulmak için kasabaya bakma zamanı.',
    7: 'İpucu: Hobo daha yeterince sarhoş değil. Neden beklerken yakınlarda dinlenmiyorsun?',
    8: 'İpucu: Hobo artık yeterince sarhoş olmalı. Kontrol altına alma gücünü onun üstünde dene.',
    9: 'İpucu: Artık bir şeylere dokunabilirsin, Crash siteta önemli bir eşyan var. Alete ihtiyacın olacak.',
    10: 'İpucu: Apartman anahtarların yanında. Onları kullanmanın zamanı.',
    11: 'İpucu: Sana yardım edebilecek bir şey için apartmanın etrafına bak. Ayrıca Hobo\'nun kokusundan kurtul.',
    12: 'İpucu: Sophia şu an evde. O fark etmen gitsen iyi olacak.',
    13: 'İpucu: Paran yok. Apartmanını terk etmek zorundasın. Öyle görünüyor ki bugün yine parkta yatacaksın.',
    14: 'İpucu: Göletten gelen bazı sesler var. Gidip bir bakmak isteyebilirsin.',
    15: 'İpucu: Dolabın anatharı sen de var. 125. dolaba bak.',
    16: 'İpucu: Bu kadın kim? Yakından bir bak.',
    17: 'İpucu: Garip bir flash disk buldun. Apartmanındaki bilgisayarda içinde ne olduğuna bak.',
    18: 'İpucu: Bilgisayarın artık apartmanda değil. Okuldaki bilgisayarı aç ve flash disk\'in içinde ne olduğuna bak.',
    19: 'İpucu: Bethany kızlar tuvaletinde bekliyor. Gidip ne istediğine bir bak.',
    20: 'İpucu: Okul Dekan\'ı merdivenlerin yukarısındaki ofisinde bekliyor.',
    21: 'İpucu: Ofisin etrafında şifre için ipuçları ara.',
    22: 'İpucu: Şeytan Hobo\'ya bu $100\'ı vermeni söyledi. O genellikle parkın oradaki köprünün altında bekler.',
    23: 'İpucu: Artık Brandon\'ın nerede yaşadığını biliyorsun. Oraya gitmek için taksi tutabilirsin. Taksi durağı market\'in yanında.',
    24: 'İpucu: Artık polislerin apartmanını ziyaret edebilirsin.',
    25: 'İpucu: Kıyafetlerin rahat değiller. Onları değiştirmelisin. Ayrıca orada şu polis hakkında birkaç bilgi var.',
    26: 'İpucu: Belki daha fazla bilgi için polisin bilgisayarını kontrol edebilirsin.',
    27: 'İpucu: Uyku vakti.',
    28: 'İpucu: Dekan\'ın merdivenlerin yukarısındaki ofisine gitmelisin.',
    29: 'İpucu: Nick orada mı bakmak için devlet hastanesine gitmeye zamanın var.',
    30: 'İpucu:Şu an ambarda olan Brandon ile buluşmalısın.',
    31: 'İpucu: Uyku vakti.',
    32: 'İpucu: Merdivenlerin yukarısındaki Dekan\'ın ofisine tekrar gitmelisin',
    33: 'İpucu: Ivana\'yı evinde ziyaret etmelisin.',
    34: 'İpucu: Şu an yapacak bir şey yok. Polislerin apartmanına git.',
    35: 'İpucu: Uyku vakti.',
    36: 'İpucu: Okul laboratuvarında Megan\'ı ziyaret etmelisin.',
    37: 'İpucu: Anders\'in ofisine sızmak için zamanın var. Ofisi merdivenlerin yukarısında. Önce Anders\'i bulmalısın ve meşgul olduğundan emin olmalısın.',
    38: 'İpucu: Anders\'in ofisine bak ve onu ortadan kaldırmak için kanıt ara.',
    39: 'İpucu: Ivana\'yı bulman lazım. O hala sınıflardan birinde olmalı.',
    40: 'İpucu: Ivana çoktan evine gitmiş. Oraya gidip onu görmelisin.',
    41: 'İpucu: Anders\'e karşı ne olur olmaz diye polisin silahını almalısın. Ayrıca Megan\'dan ilaçları almalısın. Sonra operasyon için Ivana\'nın evine geri dön.',
    42: 'İpucu: Önce, silahı boşaltmalısın.',
    43: 'İpucu: Yatsan iyi olacak. Yarın uzun bir gün olacak.',
    44: 'İpucu: Okulda Sophia ile konuşmalısın.',
    45: 'İpucu: Anders\'in üzerinde bir şey var. Okul vakti onu ofisinde ziyaret etsen iyi olucak.',
    46: 'İpucu: Sophia\'yı eski evinde ziyaret etmelisin.',
    47: 'İpucu: Şu an yapacak bir şey yok. Eve gitsen iyi olacak.',
    48: 'İpucu: Bir ziyaretçin var gibi. Bakalım ne istiyormuş?',
    49: 'İpucu: Güzel bir şaraptan sonra uyuma vakti.',
    50: 'İpucu: Silahı ve uyuşturucu zulasını alıp ambarda Brandon ile buluşmalısın.',
    51: 'İpucu: Öncelikle silahı saklamalısın.',
    52: 'İpucu: Yatağa gitmeli ve bu günü unutmalısın.',
    53: 'İpucu: Bir ziyaretçin var gibi. Bakalım ne istiyormuş?.',
    54: 'İpucu: Sarışın komşunu ziyaret etme vakti.',
    55: 'İpucu: Okulda Sophia\'yı bulman lazım, etrafta onun nerede olduğunu sor.',
    56: 'İpucu: Sophia okul binasının arkasındaki spor salonunda. Oraya git.',
    57: 'İpucu: Ivana\'yı evinde ziyaret etmelisin.',
    58: 'İpucu: Burada bir şey var. Dikkatlice bakman gerek.',
    59: 'İpucu: Eve geri dönmen gerek.',
    60: 'İpucu: Anders için bulduğun kanıtları bir araya getirmelisin. Gereken her şey masada var.',
    61: 'İpucu: Yoruldun. Uyumalısın.',
    62: 'İpucu: Polis merkezine gitmelisin.',
    63: 'İpucu: Brandon ile konuşmalısın.',
    64: 'İpucu: Bilgisayar sınıfına git.',
    65: 'İpucu: Anders\'in kanıtlarını Dekan\'ın ofisine teslim etmen gerek.',
    66: 'İpucu: Çabuk olmalısın. Sophia seni sahilde bekliyor.',
    67: 'İpucu: Uzun bir gündü. Biraz uyumalısın.',
    68: 'İpucu: Canın kahve çekiyor. Kahve dükkanına git.',
    69: 'İpucu: Evdeki tüm ipuçlarını incelemelisin.',
    70: 'İpucu: Bulduğun anahtar kitli kapı için. Polisin dolabında başka ne taslaklar var diye bak.',
    71: 'İpucu: Kızlarla buluşmadan önce biraz zamanın var. Anahtardaki adrese gidip bir bak.',
    72: 'İpucu: Odaların içine bakmak için bir yol bulmalısın.',
    73: 'İpucu: Scarlett kaçırılmadan önce Ivana ile yaşıyordu. Önce Ivana\'nın evine git.',
    74: 'İpucu: Beklediğin gibi gitmedi. Umarım ileride Sophia ile işler iyi gider.',
    75: 'İpucu: Scarlett\'ın eşyalarını polis merkezinden alman gerektiğini hatırla.',
    76: 'İpucu: Bu seks odası kıyafetlerinden kurtulmalısın.',
    77: 'İpucu: Giyerken rahat olacağın ayakkabılar seç.',
    78: 'İpucu: Yatağa gitmeden önce, şu koca kutuda ne var bir bak.',
    79: 'İpucu: Sophia ile konuşup yeni neler var görmelisin.',
    80: 'İpucu: Scarlett\'ın kaybolması ile ilgili Dekanla konuşmalısın. Merdivenlerin yukarısındaki ofisinde olmalı.',
    81: 'İpucu: İşemelisin. Bunun icabına bakmalısın yoksa külotun felaket kötü olacak.',
    82: 'İpucu: Megan\'ı buldun. İlaçlar hakkında onunla konuşman gerek.',
    83: 'İpucu: Kirayı ödemek için iş bulman gerek. Belki kahve dükkanı birilerini arıyordur. Ayrıca Anne\'nin arabası orada mı diye hastaneye bakman gerek.',
    84: 'İpucu: Barista striptiz kulübüyle ilgili şaka yaptı. Ama belkide o kadar kötü bir fikir değildir. Hızlıca para kazanmak için iyi bir firsat.',
    85: 'İpucu: Sophia için parayı almadın. Teklifi kabul etmekten başka çaren yok. Umarım o hala ayaktadır.',
    86: 'İpucu: Sophia seninle kamera şovu yapmak konusunda heyecanlı. Neden denemiyorsun?',
    87: 'İpucu: Öyle ya da böyle, kira için olan parayı topladın. Sophia\'ya ödeme vakti. Umarım o hala ayaktadır.',
    88: 'İpucu: Uzun ve yorucu bir gün oldu. Uyku vakti.',
    89: 'İpucu: Annenin arabası için tekrar hastaneyi kontrol etmelisin.',
    90: 'İpucu: Megan laboratuvarda yardımına ihtiyacı var. Onu bekletmemelisin.',
    91: 'İpucu: Tekrar tuvaleti kullanman gerek. İlaçları denemek çok zorlu bir iş.',
    92: 'İpucu: Annen hala hastanede mi bakmalısın.',
    93: 'İpucu: Yapacak pek bir şey yok eve git.',
    94: 'İpucu: Uyku vakti.',
    95: 'İpucu: Dün kıyafetinde ilaç buldun. Onu Megan\'a geri vermelisin.',
    96: 'İpucu: Megan\'a kahve almalısın. Unuttun mu?',
    96: 'İpucu: Megan\'a kahve almalısın. Unuttun mu?',
    97: 'İpucu: Ivana ve Sophia\'yı bulmalısın. Okulu araştır.',
    98: 'İpucu: Ahırda biri var.',
    99: 'İpucu: Aşağıda değiller gibi görünüyor. Yukarıya baktın mı?',
    100: 'İpucu: İlaçları evinde güvenli bir yere saklamak iyi olur.',
    101: 'İpucu: Megan ile kahve dükkanına git.',
    102: 'İpucu: Kızlar seni evde bekliyor olmalı.',
    103: 'İpucu: Duş alma vakti değil mi?',
    104: 'İpucu: İlaçlaro saklamak için iyi bir yer bulmalısın.',
    105: 'İpucu: Megan varmadan Dekan\'ın odasında olmalısın.',
    106: 'İpucu: Sophia ile konuşmalısın. Bilgisayar odasında olmalı.',
    107: 'İpucu: Ivana\'nın okuldan çıktığını gördün. Bakalım ona yetişebilecek misin?',
    108: 'İpucu: Şu an 3 seçeneğin var: Anders\'in ofisini ziyaret et, Ivana ile sahile git ya da Sophia ile alışverişe git.',
    109: 'İpucu: Oturma odasında kızlarla başka bir buluşman var.',
    110: 'İpucu: Çok yorgun görünüyorsun. Yatma vakti',
    111: 'İpucu: Bugün intikam günü! Okul spor salonunda çalışmalısın.',
    112: 'İpucu: Brooke ve Beth\'in dolaplarını bulmalısın.',
    113: 'İpucu: Dolapların anahtarlarını bulmalısın.',
    114: 'İpucu: Dolapların anahtarlarını buldun. Dene bakalım.',
    115: 'İpucu: Scarlett\'i bir yere saklamalısın. İyi bir yer ara.',
    116: 'İpucu: Artık seni durduracak bir şey yok, Brooke ve Beth\'in dolaplarını bul.',
    117: 'İpucu: Her şey hazır. Ana spor salonuna git.',
    118: 'İpucu: Brooke ve Bethany spor salonunda çok azmış görünüyorlar. Onların yanına gitmek eğlenceli olabilir.',
    119: 'İpucu: Onların soyunma odasında kapana kısıldığın için bir bahaneye ihtiyacın var. Turnuvadan sonra çok sıcak ve terli olmalılar.',
    120: 'İpucu:İçkileri aldın. Kötü kızların soyunma odasına git.',
    121: 'İpucu: Tüm o sikişten ve boşalmadan sonra yoruldun. Anders\'in evinin anahtarlarını bulman gerek. Muhtemelen onun ofisindedir.',
    122: 'İpucu: Yürüyen ölüye benziyorsun. Muhtemelen eve kadar gidemezsin. Biraz dinlenmek için bir yer bulmalısın.',
    123: 'İpucu: Varman gereken bir dersin var ama geç kaldın. Hangisi Anders\'in sınıfıydı hatırla',
    124: 'İpucu: Şu an Anders\'in evi için anahtarları bulmaya vaktin var.',
    125: 'İpucu: Anahtarları buldun. Anders\'in apartmanına gitme vakti.',
    126: 'İpucu: Anders\'in ofis koltuğunda bir gece geçirdikten sonra bok gibi kokuyorsun.',
    127: 'İpucu: Tüm daireyi aradın mı?',
    128: 'İpucu: Artık düzgünce uyuma vakti.',
    129: 'İpucu: Okulda dersin var ve bu sefer geç kalmak istemiyorsun.',
    130: 'İpucu: Scarlett\'i hastanede buldun. Gidip ne hatırlıyor baksan iyi olur.',
    131: 'İpucu: Doktor gibi kokuyorsun. Bu hastane kokusundan nefret etmiyor musun? Eve gidip duş alsan iyi olur.',
    132: 'İpucu: Rebecca oturma odasında televizyon izliyor. Gidip ona kendini açıklasan iyi olur.',
    133: 'İpucu: Geç oldu. Yatağa gitsen iyi olur.',
    #After morning:
    134: 'İpucu: Okula gitmeli ve Anders\'in sınıfına ders vermelisin.',

    #After Megan talk:
    135: 'İpucu: Anders\'in sınıfı: sınıf 1',

    #After class:
    136: 'İpucu: Sınıf\'ı hallettin. Ofisinde Anders\'in bilgisayarını kontrol etmelisin.',

    #After checked laptop:
    137: 'İpucu: Anders\'in dairesinden Mirapill notlarını toplamalısın.',

    #Obtain Rebecca DNA:
    138: 'İpucu: DNA için, kan veya vücut sıvısı lazım. Temizlik ürünlerine bakmaya ne dersin?',

    #after found toothbrushes:
    139: 'İpucu: Sahip olman gereken her şeye sahipsin. Megan\'ın laboratuvarına gitme vakti.',

    #after Megan’s lab:
    140: 'İpucu: Megan\'ın test yapmaya zamanı yoktu ama seni hastanedeki bir arkadaşına yönlendirdi.',

    #after hospital:
    141: 'İpucu: Çoktan akşam oldu. Rebecca büyük ihtimalle şehirden eve dönmüştür.',

    #before Rebecca goes to bed:
    142: 'İpucu: Rebecca\'nın hediyesini vermek için geç kaldın. Uyumadan önce onu yakala.',
    #next morning:
    143: 'İpucu: her okul sabahında olduğu gibi, Anders\'in öğrencilerine öödev vermelisin.',


    #After class:
    144: 'İpucu: Hastaneden DNA sonuçlarını alma vakti.',

    #after hospital:
    145: 'İpucu: Rebecca\'yı evinden al ve öğlen yemeğine götür.',

    #after shopping:
    146: 'İpucu: Şu an Rebeccaya DNA sonuçlarını söyleme vakti.',

    #After ressults talk:
    147: 'İpucu: Uyku vakti geldi.',

    #morning:
    148: 'İpucu: Tekrar, Anders\'in öğrencilerine ödev verme vakti.',

    #after class:
    149: 'İpucu: Rebeccayı alma zamanı.',

    #After shower:
    150: 'İpucu: Rebecca randevu için seni oturma odasında bekliyor.',

    #Rebecca left early:
    151: 'İpucu: Rebecca eve erken gitti ama yarın partin var git uyu.',

    #didnt fuck rebecca
    152: 'İpucu: Onun tarafından baştan çıkarılmadın. Helal olsun. Yapacak başka bir şey yok yatağa git.',

    #shower fucked rebecca secretly:
    153: 'İpucu: Eğlenceli zaman geçirdin. Gidip duş alsan iyi olur. Rebecca yarın erken gidicel.',

    #shower fucked rebecca mutually:
    154: 'İpucu: Rebecca dünden sonra uyuyor. Duş alma vakti. Bok gibi kokuyorsun.',

    #reb about to leave:
    155: 'İpucu: Rebecca bugün gidiyor. Seni oturma odasında bekliyor.',

    #reb seen off:
    #156: 'İpucu: Bugün voleyball kazananları partisi var. Şimdilik sınıfa gitsen iyi olur.',

    #After talking with Devil/Angel during TV:
    156: 'Yazdığına göre Dekan\'ının odasına gitmelisin',

    #If working for Brooke:
    157: 'Dekan Brooke\'un seni aradığını söyledi. O bilgisayar odasında olmalı.',

    #After dean:
    158: 'Güçlü arkadaşın alışveriş merkezindeki restaurantta bekliyor.',

    #After lunch:
    159: 'Partiye gitmeden önce parçaya bakman gerek. Git üstünü değiş.',

    #after:
    160: 'Parti zamanı! Eski evine git.',

    #At party:
    161: 'Etrafa bakmak ve insanlarla konuşmak için vaktin var.',

    #After talk to Sophia:
    162: 'Ivana mutfakta.',

    #After Ivana talk:
    #If working for Brooke:
    163: 'Şimdi ilacı içkisine katma vakti.',

    #if not working for Brooke:
    164: 'Oturma odasına git. Kızlar partinin başlamasını istiyor.',

    #After party started:
    165: 'Eski odandaki saklı yerden ilaçları almalısın.',

    #After talk to scarlett:
    166: 'Scarlett\'a flash diskini bulmasında yardımcı olmalısın.',

    #after helped Scarlett:
    167: 'Artık oda temiz. İlaçlarını geri alabilirsin.',

    #after:
    168: 'Tüm ilaçları aldın. Partide eğlenmenin vakti geldi. Oturma odasına git.',

    #after party:
    169: 'Parti bitti. Uyuma vakti.',

    #At morning:
    170: 'Laboratuvarda Meganla konuşmalısın.',

    ##after:
    171: 'Umarım Brooke bilgisayar sınıfındadır.',

    }#TEMP
    $ menu_can_show_hint_hover = False
    $ menu_can_show_phone_hover = False
    $ menu_can_show_inventory_hover = False
    $ current_hint = hint_system_dict[hints_counter]
    if current_screen == "mc_room":
        if mc_room_window_opened == True:
            scene mc_room_openedwindow
            "[current_hint]"
            jump mc_room
        else:
            if time_of_day != 'GECE':
                scene mc_room_day
            else:
                scene mc_room_night
            "[current_hint]"
            jump mc_room
    elif current_screen == "mc_room_with_sofia_and_policeman":
        scene mc_room_day_cathy_policeman
        "[current_hint]"
        jump mc_room_with_sofia_and_policeman
    elif current_screen == "city_map":
        if time_of_day == 'GECE':
            scene city_map_night
        else:
            scene city_map
        "[current_hint]"
        jump city_map
    elif current_screen == "roommate_room":
        scene roommate_room_day
        if currently_possessed_scarlett and turned_down_strip_club_owner and sophia_in_her_room_for_webshow:
            show rm_room_sophia_webcam:
                xpos 485 ypos 294
        "[current_hint]"
        jump roommate_room
    elif current_screen == "bathroom":
        scene bathroom_main
        "[current_hint]"
        jump bathroom
    elif current_screen == "bathroom_with_policeman_sniffing_panties":
        scene bathroom_main_policeman
        "[current_hint]"
        jump bathroom_with_policeman_sniffing_panties
    elif current_screen == "living_room":
        scene livingroom_main
        if True in (time_to_sleep_after_choices_afternoon, time_to_meet_up_with_ivana_n_sophia_after_choices_afternoon, time_to_test_unlabelled_pills_on_ivana_n_sophia):
            show livingroom_button_girls:
                xpos 607 ypos 431
        "[current_hint]"
        jump living_room
    elif current_screen == "kitchen":
        scene kitchen_main
        if currently_possessed_scarlett and settled_as_scarlett and not sophia_in_her_room_for_webshow:
            show sophia_kitchen_button:
                xpos 733 ypos 160
        "[current_hint]"
        jump kitchen
    elif current_screen == "warehouse_main":
        if time_of_day == 'GECE':
            scene warehouse_main_night
        else:
            scene warehouse_main_day
        "[current_hint]"
        jump warehouse_main
    elif current_screen == "beach_main":
        if time_of_day == 'GECE':
            scene beach_main_night
        else:
            scene beach_main
        "[current_hint]"
        jump beach
    elif current_screen == "crash_site":
        if time_of_day == 'GECE':
            scene crash_site_night
        else:
            scene crash_site_day
        "[current_hint]"
        jump crash_site
    elif current_screen == "roses":
        if time_of_day == 'GECE':
            scene crash_site_roses_night
        else:
            scene crash_site_roses_day
        "[current_hint]"
        jump roses
    elif current_screen == "sewer":
        if time_of_day == 'GECE':
            scene crash_site_sewer_night
        else:
            scene crash_site_sewer_day
        "[current_hint]"
        jump sewer
    elif current_screen == "park_main":
        if time_of_day == 'GECE':
            scene park_perspective_night
        else:
            scene park_perspective_day
        "[current_hint]"
        jump park_main
    elif current_screen == "park_bench":
        if time_of_day == 'GECE':
            scene park_bench_night
        else:
            scene park_bench_day
        "[current_hint]"
        call screen park_bench
    elif current_screen == "hobo_tunnel":
        if time_of_day == 'GECE':
            scene park_hobo_tunnel_night
            if currently_posessed_homeless_guy == False:
                show park_homeless_guy_night
        else:
            scene park_hobo_tunnel_day
            if currently_posessed_homeless_guy == False:
                show park_homeless_guy_day:
                    xpos 600 ypos 465
        "[current_hint]"
        jump hobo_tunnel
    elif current_screen == "main_hall":
        scene main_hall
        if mom_in_main_hallway == True:
            show mainhall_mom_walking:
                xpos 1150 ypos 255
        elif sophia_arguing_with_brandon_in_main_hall:
            show mainhall_brandon_sophia:
                xpos 1150 ypos 255
        "[current_hint]"
        jump main_hall
    elif current_screen == "female_wc_with_megan":
        scene female_wc_main_megan
        "[current_hint]"
        jump female_wc_with_megan
    elif current_screen == "deans_office":
        scene deans_office_main
        "[current_hint]"
        jump deans_office
    elif current_screen == "deans_office_board":
        scene office_board
        "[current_hint]"
        jump deans_office_board
    elif current_screen == "deans_office_bookshelf":
        scene office_books
        "[current_hint]"
        call screen deans_office_bookshelf
    elif current_screen == "deans_office_certificates":
        scene office_certificates
        "[current_hint]"
        jump deans_office_certificates
    elif current_screen == "deans_office_binder":
        scene office_note
        "[current_hint]"
        jump deans_office_binder
    elif current_screen == "deans_office_binder":
        scene office_note
        "[current_hint]"
        jump deans_office_binder
    elif current_screen == "deans_office_picture_frames":
        scene office_picture
        "[current_hint]"
        jump deans_office_picture_frames
    elif current_screen == "deans_office_telephone":
        scene office_telephone
        "[current_hint]"
        jump deans_office_telephone
    elif current_screen == "deans_office_trophies":
        scene office_trophy
        "[current_hint]"
        jump deans_office_trophies
    elif current_screen == "main_hall_board":
        scene main_hall_board
        if sophia_roommate_ad_placed == True:
            show mainhall_board_roommate:
                xpos 300 ypos 400
        "[current_hint]"
        hide mainhall_board_roommate
        jump main_hall_board
    elif current_screen == "main_hall_lockers1":
        scene mainhall_lockers1b
        "[current_hint]"
        jump main_hall_lockers1
    elif current_screen == "main_hall_lockers2":
        scene mainhall_lockers1
        "[current_hint]"
        jump main_hall_lockers2
    elif current_screen == "class1":
        scene classroom1
        if looking_for_sophia_about_pills_progress:
            show classroom1_anders:
                xpos 781 ypos 371
        "[current_hint]"
        jump class1
    elif current_screen == "class2":
        scene classroom2
        "[current_hint]"
        jump class2
    elif current_screen == "computer_class":
        scene computer_class_main
        "[current_hint]"
        jump computer_class
    elif current_screen == "male_wc":
        scene male_wc_main
        "[current_hint]"
        jump male_wc
    elif current_screen == "female_wc":
        scene female_wc_main
        "[current_hint]"
        jump female_wc
    elif current_screen == "shop_main":
        scene shop_main
        "[current_hint]"
        call screen shop_main
    elif current_screen == "cop_apartment_main":
        scene policeman_main
        if drug_sell_choice_consequence_time and not chose_to_sell_drugs_to_brandon:
            show policeman_main_angel:
                xpos 210 ypos 415
        elif morning_after_drug_sell_choice_consequenses and chose_to_sell_drugs_to_brandon and devil_or_angel_explained_the_secret_of_the_pills == False:
            show policeman_main_devil:
                xpos 270 ypos 395
        "[current_hint]"
        call screen cop_apartment_main
    elif current_screen == "cop_apartment_bedroom":
        if have_left_panties_in_cops_bedroom:
            scene policeman_bedroom_panties
        else:
            scene policeman_bedroom
        "[current_hint]"
        call screen cop_apartment_bedroom
    elif current_screen == "anders_office":
        scene anders_office_main
        "[current_hint]"
        call screen anders_office
    elif current_screen == "anders_office_trashed":
        scene anders_office_harsch
        "[current_hint]"
        call screen anders_office_trashed
    elif current_screen == "ivana_apartment_scarlett_room":
        scene scarlett_main
        "[current_hint]"
        call screen ivana_apartment_scarlett_room
    elif current_screen == "ivana_apartment_teddy_closeup":
        scene main_bear
        "[current_hint]"
        call screen ivana_apartment_teddy_closeup
    elif current_screen == "police_station_interrogation_room":
        scene interrogation_main
        "[current_hint]"
        call screen police_station_interrogation_room
    elif current_screen == "cop_apartment_closet":
        scene cop_stuff_main
        "[current_hint]"
        call screen cop_apartment_closet
    elif current_screen == "cop_apartment_closet_closeup":
        scene cop_stuff_key
        "[current_hint]"
        call screen cop_apartment_closet_closeup
    elif current_screen == "den_basement":
        scene _unknown_house_basement
        "[current_hint]"
        call screen den_basement
    elif current_screen == "scarlets_shoes":
        scene mc_room_shoes
        "[current_hint]"
        call screen scarlets_shoes
    elif current_screen == "dining_hall":
        scene school_dining_hall
        "[current_hint]"
        call screen dining_hall
    elif current_screen == "gym_janitor_closet":
        if not have_gym_janitors_key:
            scene sporthall_cleaningroom_key
        else:
            scene sporthall_cleaningroom_nokey
        show sporthall_cleaningroom_tree:
            xpos 1033 ypos 41
        "[current_hint]"
        call screen gym_janitor_closet
    elif current_screen == "bad_girls_locker_room":
        scene sporthall_locker_room
        "[current_hint]"
        call screen bad_girls_locker_room
    elif current_screen == "anders_kitchen":
        scene anders_flat_kitchen
        "[current_hint]"
        call screen anders_kitchen
    elif current_screen == "anders_livingroom":
        if time_of_day == 'GECE':
            scene anders_flat_livingroom_night
        else:
            scene anders_flat_livingroom
        "[current_hint]"
        call screen anders_livingroom
    elif current_screen == "anders_bedroom":
        if time_of_day == 'GECE':
            scene anders_flat_bedroom_night
        else:
            scene anders_flat_bedroom
        "[current_hint]"
        call screen anders_bedroom
    elif current_screen == "anders_guestroom":
        if time_of_day == 'GECE':
            scene anders_flat_rebecca_room_night
        else:
            scene anders_flat_rebecca_room
        "[current_hint]"
        call screen anders_guestroom
    elif current_screen == "anders_bathroom":
        scene anders_flat_bathroom
        "[current_hint]"
        call screen anders_bathroom
    elif current_screen == "scarletts_room_winners_party":
        scene mc_room_night
        if not milestone_mc_anders_found_scarletts_flash_drive:
            show mcroom_party_scarlett:
                xpos 951 ypos 388
        if not milestone_winners_party_sophia_asked_for_drinks:
            show mcroom_party_others:
                xpos 501 ypos 228
        "[current_hint]"
        call screen scarletts_room_winners_party
    elif current_screen == "sophias_room_winners_party":
        scene roommate_room_night
        "[current_hint]"
        call screen sophias_room_winners_party
    elif current_screen == "bathroom_winners_party":
        scene bathroom_main
        "[current_hint]"
        call screen bathroom_winners_party
    elif current_screen == "living_room_winners_party":
        scene livingroom_party
        show livingroom_party_sophia:
            xpos 1175 ypos 415
        show livingroom_party_tracyandbrandon:
            xpos 53 ypos 385
        show livingroom_party_trophy:
            xpos 560 ypos 400
        if not winners_party_livingroom_secret10_found:
            show livingroom_party_secret10:
                xpos 554 ypos 478
        if milestone_winners_party_sophia_asked_for_drinks:
            show livingroom_party_others:
                xpos 190 ypos 190
        if milestone_mc_anders_recovered_pills_from_scarletts_bedstand:
            show livingroom_party_megan:
                xpos 800 ypos 200
        "[current_hint]"
        call screen living_room_winners_party
    elif current_screen == "kitchen_winners_party":
        scene kitchen_main
        if not toggle_mc_anders_talked_to_ivana_at_winners_party or milestone_winners_party_sophia_asked_for_drinks:
            show kitchen_party_ivana:
                xpos 733 ypos 160
        "[current_hint]"
        call screen kitchen_winners_party
