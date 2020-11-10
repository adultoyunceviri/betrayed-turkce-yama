
screen park_main:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        if time_of_day == 'GECE':
            ground "destinations/04_park/park_perspective_night.webp"
            hover "destinations/04_park/park_perspective_night_glow.webp"
        else:
            ground "destinations/04_park/park_perspective_day.webp"
            hover "destinations/04_park/park_perspective_day_glow.webp"

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "park_main"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "park_main"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "park_main"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "park_main"), Jump("joraell_message_no_phone")
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
            action Jump("city_map")

        hotspot (270, 465, 250, 150) action Jump("park_bench")

        hotspot (1120, 95, 250, 180) action Jump("hobo_tunnel")


label park_main:
    if time_of_day == 'GECE':
        show park_perspective_night
        if currently_posessed_homeless_guy == True and bethany_and_brandon_in_pond == False:
            p "Well, I made it back to the park without being arrested. That's good."
            p "I guess I can't stay in my room, as this hobo. Do I really have to live in his box home?"
            $ hints_counter += 1
            $ bethany_and_brandon_in_pond = True
        elif have_cursed_dollar_for_hobo == True:
            p "Okay, so the devil said: I just need to give this 100 dollar bill to the homeless guy, and the rest will take care of itself."
            p "Is it really okay to do this?"
    call screen park_main


### Park Bench
screen park_bench:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        if time_of_day == 'GECE':
            ground "destinations/04_park/01_park_bench/park_bench_night.webp"
            hover "destinations/04_park/01_park_bench/park_bench_night_glow.png"#TODO webp not same as png
        else:
            ground "destinations/04_park/01_park_bench/park_bench_day.webp"
            hover "destinations/04_park/01_park_bench/park_bench_day_glow.webp"

        hotspot (65, 300, 900, 500) action Jump("interact_park_bench_rest")#bench
        #if currently_posessed_homeless_guy == True: TODO
        if time_of_day == 'GECE' and bethany_and_brandon_in_pond == True:
            hotspot (415, 140, 200, 200) action Jump("scene_bethany_and_brandon_in_pond")#pond area sign - Better to be below bench

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "park_bench"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "park_bench"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "park_bench"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "park_bench"), Jump("joraell_message_no_phone")
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
            if bethany_and_brandon_in_pond:
                action Jump("interaction_park_bench_back_button_deny")
            else:
                action Jump("park_main")

label park_bench:
    if bethany_and_brandon_in_pond:
        jump trigger_park_bench_hear_bethany_and_brandon_in_pond
    else:
        call screen park_bench


### Hobo Tunnel
screen hobo_tunnel:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        if time_of_day == 'GECE':
            ground "destinations/04_park/02_hobo_tunnel/park_hobo_tunnel_night.webp"
            hover "destinations/04_park/02_hobo_tunnel/park_hobo_tunnel_night_glow.webp"
            #add "park_homeless_guy_night"#TODO need proper image not full screen image

        else:
            ground "destinations/04_park/02_hobo_tunnel/park_hobo_tunnel_day.webp"
            hover "destinations/04_park/02_hobo_tunnel/park_hobo_tunnel_day_glow.webp"


        hotspot (835, 380, 250, 250) action Jump("interaction_park_hobo_tunnel_cardboard_box")#cardboard_box

        hotspot (1052, 422, 283, 460) action NullAction()#oil_drum - has to be below cardboard_box for hover glow overdraw

        hotspot (268, 492, 198, 305) action NullAction()#rubbish_bag

        if not currently_posessed_homeless_guy and not given_hobo_cursed_dollar:
            if time_of_day == 'GECE':
                imagebutton:
                    idle "destinations/04_park/02_hobo_tunnel/park_homeless_guy_night.png"
                    hover "destinations/04_park/02_hobo_tunnel/park_homeless_guy_night_glow.png"
                    #xpos 1052 ypos 422
                    if have_cursed_dollar_for_hobo == True:
                        action Jump("scene_give_cursed_dollar_to_homeless_guy_night")
                    elif looking_for_someone_to_possess == True:
                        action Jump("scene_possess_homeless_guy_night")
            else:
                imagebutton:
                    idle "destinations/04_park/02_hobo_tunnel/park_homeless_guy_day.png"
                    hover "destinations/04_park/02_hobo_tunnel/park_homeless_guy_day_glow.png"
                    xpos 600 ypos 465
                    if tried_to_possess_hobo_during_day == False:
                        action Jump("scene_possess_homeless_guy_day")
                    else:
                        action Jump("idle_homeless_man_know_to_posess_at_night")

        imagebutton:
            idle "back_button_idle"
            hover "back_button_hover"
            xpos 1405 ypos 820
            action Jump("park_main")

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "hobo_tunnel"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "hobo_tunnel"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "hobo_tunnel"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "hobo_tunnel"), Jump("joraell_message_no_phone")
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

label hobo_tunnel:
    call screen hobo_tunnel

label interact_park_bench_rest:
    if time_of_day == 'GECE':
        show park_bench_night
        if looking_for_someone_to_possess == False:
            if bethany_and_brandon_in_pond == True:
                p "I shouldn't sleep while there's people nearby. I should check out the pond."
                call screen park_bench
            p "I don't need to do that anymore."
        else:
            p "I don't have time to waste here."
    else:
        show park_bench_day
        if looking_for_someone_to_possess == True:
            if tried_to_possess_hobo_during_day == True:
                p "I think I'll rest, for a little while."
                $ time_of_day = Increment_Time_Of_Day()
                $ hints_counter += 1
                scene black_screen
                $ renpy.pause(1.0, hard=True)
            else:
                p "Good idea! But I need to find someone to possess, first."
        else:
            p "I think I can do better."

    jump park_bench

label trigger_park_bench_hear_bethany_and_brandon_in_pond:
show park_bench_night
p "I hear some noises coming from the pond."
$ hints_counter += 1
call screen park_bench

label interaction_park_bench_back_button_deny:
show park_bench_night
p "I should see what those noises at the pond are."
call screen park_bench

label interaction_park_hobo_tunnel_cardboard_box:
    if time_of_day == 'GECE':
        show park_hobo_tunnel_night
    else:
        show park_hobo_tunnel_day

    if currently_posessed_homeless_guy:
        p "No! I can't do it! I can't live like a bum!"
        if bethany_and_brandon_in_pond == True:
            p "I guess, it's the park bench again."
    jump hobo_tunnel

label idle_homeless_man_know_to_posess_at_night:
    scene black_screen
    $ renpy.pause(0.05, hard=True)
    show hobos01_during_day
    p "He's still pretty sober. I should come back later on."
    call screen hobo_tunnel
