
screen beach_main:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        if time_of_day == 'GECE':
            ground "destinations/07_beach/Beach_main_night.webp"
        else:
            ground "destinations/07_beach/beach_main.webp"
            hover "destinations/07_beach/beach_main_glow.webp"

            hotspot (415, 35, 120, 120) action NullAction()#top deckchair

            hotspot (540, 260, 120, 155) action NullAction()#bottom deckchair

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "beach_main"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "beach_main"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "beach_main"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "beach_main"), Jump("joraell_message_no_phone")
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

        if looking_for_someone_to_possess == True and time_of_day == 'AKŞAM':
            imagebutton:
                idle "ivana_on_beach"
                hover "ivana_on_beach_glow"
                xpos 500 ypos 125
                action Jump("ivana_on_beach_after_class")


        imagebutton:
            idle "back_button_idle"
            hover "back_button_hover"
            xpos 1405 ypos 820
            action Jump("city_map")


label beach:
    if looking_for_someone_to_possess == True and time_of_day == 'GECE':
        jump idle_beach_nobody_there
    call screen beach_main

label idle_beach_nobody_there:#ivana_on_beach_after_class
show beach_main_night
p "Where is everyone. The beach is totally empty."
call screen beach_main
