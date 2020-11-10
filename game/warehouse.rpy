
screen warehouse_main:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        if time_of_day == 'GECE':
            ground "destinations/05_warehouse/warehouse_main_night.webp"
            hover "destinations/05_warehouse/warehouse_main_night_glow.webp"
        else:
            ground "destinations/05_warehouse/warehouse_main_day.webp"
            hover "destinations/05_warehouse/warehouse_main_day_glow.webp"

        hotspot (0, 395, 133, 120) action Jump("interaction_warehouse_crates")#crates

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "warehouse_main"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "warehouse_main"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "warehouse_main"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "warehouse_main"), Jump("joraell_message_no_phone")
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


label warehouse_main:
    if looking_for_someone_to_possess == True:
        jump idle_warehouse_nobody_working
    call screen warehouse_main

label idle_warehouse_nobody_working:
    if time_of_day == 'GECE':
        show warehouse_main_night
    else:
        show warehouse_main_day
    p "Don't people work anymore. The whole place is empty."
    call screen warehouse_main

label interaction_warehouse_crates:
    if time_of_day == 'GECE':
        show warehouse_main_night
    else:
        show warehouse_main_day
    if have_found_wire_at_warehouse == False:
        p "What's this? Some wire... This could be handy..."
        if currently_posessed_homeless_guy == True:
            p "It might come in handy. I'll take it."
            $ inventory.add(wire)
            $ have_found_wire_at_warehouse = True
        else:
            p "I can't grab anything when I'm like this."

    else:
        p "Nothing left there."


    call screen warehouse_main
