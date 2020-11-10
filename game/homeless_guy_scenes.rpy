label scene_possess_homeless_guy_day:
    scene hobos01_during_day
    p "Damn, this guy stinks like Pepé from Looney tunes."
    p "Hmm... but on the other hand, he can be my first victim."
    p "Looks like he’s drinking a lot - but it's still not enough. I will have to wait till night time."
    p "Hope I will be in luck."
    p "I think I will get a little rest on the bench near here."
    p "This day was really hard."
    $ tried_to_possess_hobo_during_day = True
    $ hints_counter += 1
    jump hobo_tunnel

label scene_possess_homeless_guy_night:
    stop music
    play music "sounds/music/sexy_music4_Tripst_topher.ogg"
    scene hobos01_during_night01
    p "Now he looks really drunk. This is my chance. I feel his spirit. Ehm... real spirit."
    scene hobos01_during_night02
    p "Yes! Something’s happening."
    scene hobos01_during_night03
    hobo "What is this!!!"
    scene hobos01_during_night04
    hobo "Ohhhhh! That pain!"
    scene hobos01_during_night05
    $ renpy.pause(0.5, hard=True)
    scene hobos01_during_night06
    $ renpy.pause(0.5, hard=True)
    scene hobos01_during_night07
    $ renpy.pause(0.5, hard=True)
    stop music fadeout (1.0)
    scene hobos01_during_night08 with Pause(1)
    p "I can feel my hands and face again. Well... his..."
    p "It worked!"
    scene hobos01_during_night09
    p "Hahaaaa! YES!, YES!! I made it... woohoo..!"
    scene hobos01_during_night10
    p "What the hell?!"
    scene hobos01_during_night11
    p "The world is spinning. Why?"
    scene hobos01_during_night12
    $ "Ooooooooh... uuuuh..."
    scene hobos01_during_night13 with Pause(1)
    scene hobos01_during_night14
    p "Zzzzzzzz...  zzZZzzzz..."
    show black_screen
    "* Because of a really high amount of alcohol in your blood, you passed out till the next morning. *"
    $ currently_posessed_homeless_guy = True
    $ looking_for_someone_to_possess = False
    $ time_of_day = Set_Time_of_Day('SABAH')

    show park_hobo_tunnel_day
    p "Urghhh... This guy’s drinking is first class! Disgusting."
    p "Now I must, somehow get to my apartment."
    p "What do I have in my pockets?"
    $ hints_counter += 1
    $ can_show_inventory_button = True
    #$ inventory.add(cash)
    $ inventory.add(bath_brush)
    $ inventory.money = 9
    $ money = 9
    $ return_label = "hobo_tunnel"
    $ special_inventory_display = True
    call screen inventory_screen


label scene_homeless_guy_security_guard_enter_school:
    scene security_hobo_entrance
    sec "Get out of here, you bum! Students only!"
    p "I guess I need to possess a student."
    jump city_map

label scene_homeless_guy_barista_enter_shop:
    scene shop_main
    brst "Um... I'll have to ask you to leave, sir."
    brst "You're disturbing the other customers."
    p "I guess I need to possess someone cleaner."
    jump city_map

label scene_homeless_guy_sewer_use_wire_get_keys:
    scene hobo_finded_keys
    p "Easy does it..."
    $ hints_counter += 1
    $ have_taken_keys_from_sewer = True
    $ inventory.drop(wire)
    $ inventory.add(apartment_keys)
    jump crash_site

label scene_homeless_guy_mc_room_money_stolen:
    scene hobo_mad
    p "What the fuck!? Where the fuck is my money!"
    $ seen_hobo_mad = True
    if have_showered_as_hobo == True:
        jump scene_sophia_comes_home_when_hobo_there
    jump mc_room

label scene_homeless_guy_bathroom_shower:
    show bathroom_main
    p "I'll need to get rid of this guy's stink."
    scene hobo_showering
    p "This might take a while..."
    scene hobo_showering2
    p "I've showered and washed his clothes. But I can't completely get rid of his stink."
    p "I guess he passes for acceptable."
    $ have_showered_as_hobo = True
    if seen_hobo_mad == True:
        jump scene_sophia_comes_home_when_hobo_there

    call screen bathroom

label scene_give_cursed_dollar_to_homeless_guy_night:
    scene hobos02_money_give1
    hobo "Hey man!? What'd ya think you’re doing here so late?! Go away, if you know what’s good for you!"
    p "Calm down, man. I just recently saw the light and made the decision to give you some money."
    scene hobos02_money_give2
    hobo "Aaah! I’m really sorry! I was not really expecting something like this, so late."
    p "It’s okay. No need to apologize."
    scene hobos02_money_give3
    p "Here, I have 100 bucks for you."
    scene hobos02_money_give4
    a "Ehemmm..."
    p "Holy FUCK! You scared me!"
    scene hobos02_money_give5
    a "What do you think you're doing?"
    p "Nothing... It’s none of your business... I have a deal with..."
    scene hobos02_money_give6
    a "Yes, I know. But don’t you care that you will inadvertently kill him with it."
    p "How can you know that?! You know noth-"
    a "No! I know everything. I’m an angel, remember that?"
    p "Yes, I remember. Where was my angel when that car took me down, huh? If that car had stopped, none of this would be happening."
    a "Hmm... you know you might one day regret these choices... (... when that car really does stop.)"
    scene hobos02_money_give7
    a "It is on you. Do what you want. What is your decision?"
    menu:
        "Give 100 Dollars to Homeless Man.":
            $ reputation_number -= 2
            scene hobos02_money_give9
            p "And use it wisely."
            hobo "Damn, man, you don’t even know how much you've helped me! Really, thank you! I owe you one."
            p "(I'm not so sure about that.)"
            $ given_hobo_cursed_dollar = True
        "Throw 100 Dollars into the Fire":
            $ reputation_number += 1
            scene hobos02_money_give8
            p "You know what? I've changed my mind."
            scene hobos02_money_give10
            hobo "Are you kidding?! What the fuck! You come here to make fun of me?! I’ll kill you, you bastard!"
            scene black_screen
            play sound 'sounds/effects/punch_sound.ogg'
            $ renpy.pause(2)

    $ inventory.drop(cursed_dollar)
    $ have_cursed_dollar_for_hobo = False
    jump city_map_brandon_calling_taxi
