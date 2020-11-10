screen shop_main:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/06_shop/shop_main.webp"

        if enable_shopping == True:
            imagebutton:
                idle "shop_button_idle"
                hover "shop_button_glow"
                xpos 943 ypos 3
                action [Show("shopping_screen")]

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "shop_main"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "shop_main"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "shop_main"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "shop_main"), Jump("joraell_message_no_phone")
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


label shop_main:

    if looking_for_someone_to_possess == True:
        show shop_main
        jump idle_shop_too_crowded_to_possess

    elif looking_for_someone_to_possess == False:
        if has_learned_about_posession == True:
            if currently_posessed_homeless_guy == True:
                if have_showered_as_hobo == True:
                    call screen shop_main
                    #call screen shopping_screen
                elif have_showered_as_hobo == False:
                    jump idle_shop_hobo_smells
            elif currently_possessed_brandon == True:
                call screen shop_main
                #call screen shopping_screen
            elif currently_possessed_cop == True:
                call screen shop_main
                #call screen shopping_screen
            elif currently_possessed_scarlett == True:
                call screen shop_main
                #call screen shopping_screen
            elif currently_possessed_anders == True:
                call screen shop_main
                #call screen shopping_screen
        else:
            jump idle_shop_cant_drink_coffee


label idle_shop_cant_drink_coffee:
show shop_main
p "I don’t have money... and besides, she can’t even see me."
p "But later, I will be able to buy lots of handy things here."
p "It is one of those shops where they have almost everything. From donuts to guns… literally."
#hide shop_main
call screen shop_main

label idle_shop_too_crowded_to_possess:
show shop_main
p "I don't know what possession involves. I should find someone alone in a secluded place."
#hide shop_main
call screen shop_main

label idle_shop_hobo_smells:
show shop_main
brst "I'm sorry, sir. I will have to ask you to leave. You are distracting the other customers."
p "I guess I'm not the only one who notices, this guy smells."
jump city_map
