screen ivana_apartment_scarlett_room:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:

        ground "destinations/09_scarlett_room/scarlett_main.png"
        hover "destinations/09_scarlett_room/scarlett_main_glow.png"


        hotspot (1450, 640, 110, 120) action Jump("interaction_ivana_apartment_scarlett_room_flower")#flower

        hotspot (80, 426, 240, 120) action Jump("interaction_ivana_apartment_scarlett_room_main_books")#main_books

        hotspot (575, 636, 250, 180) action Jump("interaction_ivana_apartment_scarlett_room_under_bed")#underbed

        hotspot (1010, 440, 435, 330) action Jump("interaction_ivana_apartment_scarlett_room_main_table")#main_table

        hotspot (0, 606, 170, 180) action Jump("interaction_ivana_apartment_scarlett_room_drawer_under_window")#drawerunderwindow

        hotspot (1130, 90, 310, 310) action Jump("interaction_ivana_apartment_scarlett_room_collage")#collage



        hotspot (550, 406, 160, 160) action Jump("ivana_apartment_teddy_closeup")#teddy



        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "ivana_apartment_scarlett_room"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "ivana_apartment_scarlett_room"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "ivana_apartment_scarlett_room"), Show("phone_screen")
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
            if found_scarletts_flash_drive:
                action Jump("scene_leaving_scarlett_room_after_finding_drive")
            else:
                action Jump("interaction_ivana_apartment_scarlett_room_cant_leave")

label ivana_apartment_scarlett_room:
    call screen ivana_apartment_scarlett_room



### Teddy bear closeup
screen ivana_apartment_teddy_closeup:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/09_scarlett_room/main_bear.png"
        hover "destinations/09_scarlett_room/main_bear_glow.png"

        hotspot (700, 250, 160, 160) action Jump("interaction_ivana_apartment_scarlett_teddy_nose")#teddy

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "ivana_apartment_teddy_closeup"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "ivana_apartment_teddy_closeup"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "ivana_apartment_teddy_closeup"), Show("phone_screen")
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
            action Jump("ivana_apartment_scarlett_room")
### Photo collage closeup
screen ivana_apartment_scarlett_room_collage:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "destinations/09_scarlett_room/scarlett_main_photos.png"

        if not scarletts_room_secret_found:
            imagebutton:
                idle "main_photos_secret"
                hover "main_photos_secret_glow"
                xpos 453 ypos 62
                action SetVariable("scarletts_room_secret_found", True), Jump("interaction_ivana_apartment_scarlett_room_found_secret5")#secret

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "ivana_apartment_teddy_closeup"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "ivana_apartment_teddy_closeup"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "ivana_apartment_teddy_closeup"), Show("phone_screen")
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
            action Jump("ivana_apartment_scarlett_room")

label ivana_apartment_teddy_closeup:
    if found_scarletts_flash_drive:
        scene main_bear
        p "I'm done with that stupid bear."
        jump ivana_apartment_scarlett_room
    call screen ivana_apartment_teddy_closeup


label interaction_ivana_apartment_scarlett_teddy_nose:
    scene main_bear

    p "Huh?? This bear’s nose can be opened. Hah! And what do we have here - A usb drive. Cleverly hidden."
    python:
        scarlett_drive = Item("Scarletts Drive", element="PuzzleItem21", image="scarlett_drive_inventory", cost=0)
    $ inventory.add(scarlett_drive)
    $ found_scarletts_flash_drive = True
    jump ivana_apartment_scarlett_room


label interaction_ivana_apartment_scarlett_room_flower:
    scene scarlett_main
    p "Just a big flower. I’m no flower expert, but I don’t think there's anything interesting here."
    jump ivana_apartment_scarlett_room


label interaction_ivana_apartment_scarlett_room_main_books:
    scene scarlett_main_books
    p "Looks like Scarlett likes reading. That is the complete opposite of me. These books all look ordinary. Nothing interesting about them."
    jump ivana_apartment_scarlett_room

label interaction_ivana_apartment_scarlett_room_under_bed:
    scene scarlett_main_underbed
    p "Nothing... Not even an ugly monster, hehe…"
    jump ivana_apartment_scarlett_room

label interaction_ivana_apartment_scarlett_room_main_table:
    scene scarlett_main_table
    p "Nothing interesting on this table"
    jump ivana_apartment_scarlett_room

label interaction_ivana_apartment_scarlett_room_drawer_under_window:
    scene scarlett_main
    p "There's nothing here."
    jump ivana_apartment_scarlett_room

label interaction_ivana_apartment_scarlett_room_collage:
    scene scarlett_main_photos
    p "Hmmm... a collage of some photos. Nothing special here."
    call screen ivana_apartment_scarlett_room_collage


label interaction_ivana_apartment_scarlett_room_cant_leave:
    scene scarlett_main
    p "I can't leave, I haven't found what I came here for."
    jump ivana_apartment_scarlett_room

label interaction_ivana_apartment_scarlett_room_found_secret5:
    scene scarlett_main
    jor "You have found secret 5. You can view it on your phone."
    jump ivana_apartment_scarlett_room
