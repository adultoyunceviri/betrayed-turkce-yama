
screen crash_site:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        if time_of_day == 'GECE':
            ground "destinations/01_crash_site/crash_site_night.webp"
            hover "destinations/01_crash_site/crash_site_night_glow.png"
        else:
            ground "destinations/01_crash_site/crash_site_day.webp"
            hover "destinations/01_crash_site/crash_site_day_glow.png"
        alpha False

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "crash_site"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "crash_site"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "crash_site"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "crash_site"), Jump("joraell_message_no_phone")
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

        hotspot (540, 510, 120, 60) action Call("interaction_crash_site_roses") #hovered ShowTransient("roses_overlay") unhovered Hide("roses_overlay")roses

        hotspot (30, 715, 210, 50):#sewer
            if have_taken_keys_from_sewer == False:
                action Call("sewer") #hovered ShowTransient("sewer_overlay") unhovered Hide("sewer_overlay") TODO
            else:
                action Call("interaction_crash_site_sewer_empty")

        hotspot (930, 370, 70, 90):#ATM
            if credit_card in inventory.items:
                action Call("interaction_crash_site_ATM_PIN_not_known")
            else:
                action Call("interaction_crash_site_ATM_no_card")

screen roses_overlay:
    frame:
        background Frame("destinations/01_crash_site/crash_site_day_glow.png")#roses_overlay
        transclude

screen sewer_overlay:
    frame:
        background Frame("destinations/01_crash_site/crash_site_day_glow.png")#sewer_overlay
        transclude

label crash_site:
    screen black_screen
    call screen crash_site

### roses
screen roses:
    imagemap:
        if time_of_day == 'GECE':
            ground "destinations/01_crash_site/crash_site_roses_night.webp"
        else:
            ground "destinations/01_crash_site/crash_site_roses_day.webp"

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "roses"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "roses"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "roses"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "roses"), Jump("joraell_message_no_phone")
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
            action Jump("crash_site")

label roses:
    call screen roses

### sewer
screen sewer:
    imagemap:
        if time_of_day == 'GECE':
            ground "destinations/01_crash_site/crash_site_sewer_night.webp"
            hover "destinations/01_crash_site/crash_site_sewer_night_glow.png"
        else:
            ground "destinations/01_crash_site/crash_site_sewer_day.webp"
            hover "destinations/01_crash_site/crash_site_sewer_day_glow.webp"

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "sewer"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "sewer"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                if have_brandons_phone:
                    action SetVariable("current_screen", "sewer"), Show("phone_screen")
                else:
                    action SetVariable("current_screen", "sewer"), Jump("joraell_message_no_phone")
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
            action Jump("crash_site")

        if have_taken_keys_from_sewer == False:
            hotspot (900, 640, 120, 100):
                if currently_posessed_homeless_guy == True:
                    if wire in inventory.items:
                        action Jump("scene_homeless_guy_sewer_use_wire_get_keys")
                    else:
                        action Jump("interaction_crash_site_keys_cant_reach") #hovered Show("crash_site_sewer_day_glow") unhovered Hide("crash_site_sewer_day_glow")
                #elif looking_for_someone_to_possess == True:## TODO need image button of keys so we can not show them when we pick them up and it is  not attached to whichever sewer picture
                #    action Jump("interaction_crash_site_keys_cant_touch") hovered Show("crash_site_sewer_day_glow") unhovered Hide("crash_site_sewer_day_glow")##TODO day image will show at night but we are replacing this.
                else:
                    action Jump("interaction_crash_site_keys_cant_touch") #hovered Show("crash_site_sewer_day_glow") unhovered Hide("crash_site_sewer_day_glow")
label sewer:
    call screen sewer

label interaction_crash_site_keys_cant_reach:
    scene black_screen
    $ renpy.pause(0.05, hard=True)
    if time_of_day == 'GECE':
        show crash_site_sewer_night
    else:
        show crash_site_sewer_day
    p "I can't reach the keys. This bum's hands are too big."

    jump sewer

label interaction_crash_site_keys_cant_touch:
    scene black_screen
    $ renpy.pause(0.05, hard=True)
    if time_of_day == 'GECE':
        show crash_site_sewer_night
    else:
        show crash_site_sewer_day
    p "My hands can get through the bars, but I can't grab anything when I'm like this."

    jump sewer

label interaction_crash_site_roses:
    scene black_screen
    $ renpy.pause(0.05, hard=True)
    if time_of_day == 'GECE':
        show crash_site_roses_night
    else:
        show crash_site_roses_day
    p "I wonder who left these flowers."
    hide crash_site_roses_day
    hide crash_site_roses_night
    call screen roses

label interaction_crash_site_ATM_no_card:
    scene black_screen
    $ renpy.pause(0.05, hard=True)
    if time_of_day == 'GECE':
        show crash_site_night
    else:
        show crash_site_day
    p "I don’t have a credit card now."

    call screen crash_site

label interaction_crash_site_sewer_empty:
    scene black_screen
    $ renpy.pause(0.05, hard=True)
    if time_of_day == 'GECE':
        show crash_site_night
    else:
        show crash_site_day
    p "Nothing else there."
    jump crash_site

label interaction_crash_site_ATM_PIN_not_known:
    scene black_screen
    $ renpy.pause(0.05, hard=True)
    if time_of_day == 'GECE':
        show crash_site_night
    else:
        show crash_site_day
    p "I don’t know Brandon's PIN number."
    jump crash_site
