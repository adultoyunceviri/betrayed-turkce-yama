### Den outside
screen den_basement:
    on "show" action Play('music', "sounds/music/intro_music2_Classical_Piano.ogg", if_changed=True)
    imagemap:
        ground "scenes/Policeman/40_unknown_house/_unknown_house_basement.png"
        hover "scenes/Policeman/40_unknown_house/_unknown_house_basement_glow.png"

        hotspot (1195, 430, 420, 600):#room1
            if thought_about_using_chair_in_den_basement:
                action Jump("interaction_den_basement_room1_window_look")
            else:
                action Jump("interaction_den_basement_locked_door")

        hotspot (0, 220, 360, 600):#room2
            if thought_about_using_chair_in_den_basement:
                action Jump("interaction_den_basement_room2_window_look")
            else:
                action Jump("interaction_den_basement_locked_door")

        hotspot (1138, 245, 155, 435):#room3
            if thought_about_using_chair_in_den_basement:
                action Jump("interaction_den_basement_room3_window_look")
            else:
                action Jump("interaction_den_basement_locked_door")

        hotspot (620, 250, 160, 160) action Jump("interaction_den_basement_chair")#chair
        #hotspot (700, 250, 160, 160) action Jump("interaction_den_basement_upstairs_door")#upstairs
        hotspot (430, 140, 160, 400) action Jump("interaction_den_basement_room4")#room4

        hotspot (760, 70, 60, 260):#room5
            if thought_about_using_chair_in_den_basement:
                action Jump("interaction_den_basement_room5_window_look")
            else:
                action Jump("interaction_den_basement_locked_door")

        if can_show_inventory_button == True and in_cutscene_or_idle_scene == False:
            hotspot (0, 0, 70, 65):
                hovered SetVariable("menu_can_show_hint_hover", True)
                unhovered SetVariable("menu_can_show_hint_hover", False)
                if are_hints_available:
                    action SetVariable("current_screen", "den_basement"), Jump("display_current_hint")
                else:
                    action SetVariable("current_screen", "den_basement"), Jump("joraell_message_no_hints")
            hotspot (0, 65, 70, 65):
                hovered SetVariable("menu_can_show_phone_hover", True)
                unhovered SetVariable("menu_can_show_phone_hover", False)
                action SetVariable("current_screen", "den_basement"), Show("phone_screen")
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
        #    action Jump("ivana_apartment_scarlett_room")

label den_basement:
    call screen den_basement

label scene_first_time_at_den:
scene policeman_s40_unknown_house01
p "Looks like I’m at the right place.  That house looks really neglected. Long grass over here and trees with messy branches all around. There is a light inside, but I don’t see anybody."
scene policeman_s40_unknown_house02
p "Maybe I can call for backup, like in the movies? But what if it is just a normal house, or maybe some kind of police “secret safe house”? I have to check it first, but I still need some insurance."
scene policeman_s40_unknown_house03
p "Hey Ivana? John Matrix. I need a little favour from you. It's about Scarlett’s case."
iva "Sure, Detective. What can I do to help?"
p "I just need you to call the cops to an address …… If I don’t call you in one hour from now, okay?"
iva "Are you in danger?"
p "No, I don’t think so, but it is just a precaution. So, if I don’t call you in one hour, call the police. Thanks, Ivana."
scene policeman_s40_unknown_house04
p " Fine... Now I can investigate more closely."
scene policeman_s40_unknown_house05
$ renpy.pause(1.5, hard=True)
scene policeman_s40_unknown_house06
p "Hah, like nothing."

scene policeman_s40_unknown_house07
"Stranger" "Hey you! Don't move! You are on private property."
p "I’m fucked!"
scene policeman_s40_unknown_house08
"Stranger" "Take your hands away from your face. SHOW ME YOUR FACE, NOW!"
scene policeman_s40_unknown_house09
"Stranger" "Damn, John! You scared me! Why are you coming in from the back yard? Pff. Come inside."

scene policeman_s40_unknown_house10
p "(That is that second cop. Uff, looks like I’m in a safe place.)"
pol "I haven’t seen you for a few days? What happened? How’s business going? I haven’t had any new information from you, and it was making me a little nervous, to be honest."
p "(He must be -that Frank- Scarlett wrote about?”)"
p "Oh, I’m sorry. I’ve been really busy, for the last few days."
pol "Apologising to me? Hah! Funny. Doesn’t matter. Looks like you are here for some fun, right?"
pol "Don’t worry, she’s been waiting for you all this time... And nobody touched her. "
scene policeman_s40_unknown_house11
pol "Just take the keys from the key rack in front of the door to the  basement. She is in room 4. I will take Kim in room 3 tonight."
scene policeman_s40_unknown_house12
p "(Is he talking about Scarlett?  If she’s here, how will I rescue her?)"
p "(Of course, I could just wait for the cops that will arrive after 40 minutes...)"
$ inventory.add(room4_key)
$ hints_counter += 1
jump den_basement


label interaction_den_basement_locked_door:
    scene _unknown_house_basement
    p "I only have the key to room 4 now."
    jump den_basement

#label interaction_den_basement_upstairs_door:
#    scene _unknown_house_basement
#    p "It would look suspicious if I went back upstairs now."
#    jump den_basement

label interaction_den_basement_room1_window_look:
    scene unknown_house_room1
    p "Just an empty room. Looks like some kind of jail."
    if not have_checked_den_basement_room_1:
        $ have_checked_den_basement_room_1 = True
    jump den_basement

label interaction_den_basement_room2_window_look:
    scene unknown_house_room2
    p "I can’t see anything here. Only some light coming from a small window above the door."
    if not have_checked_den_basement_room_2:
        $ have_checked_den_basement_room_2 = True
    jump den_basement

label interaction_den_basement_room3_window_look:
    scene unknown_house_room3
    p "There is some girl, I remember her name is Kim. This room is really disgusting."
    if not have_checked_den_basement_room_3:
        $ have_checked_den_basement_room_3 = True
    jump den_basement

label interaction_den_basement_room4:
    scene _unknown_house_basement
    if have_checked_den_basement_room_1 and have_checked_den_basement_room_2 and have_checked_den_basement_room_3 and have_checked_den_basement_room_5:
            scene unknown_house_room_scarlett
            p "Hmmm... this room looks much nicer than the other ones. But I don’t see anybody inside."
            scene black_screen with fade
            jump scene_finding_scarlett_in_den_room4
    else:
        p "Room 4. I should check out the other rooms before going in there."
    jump den_basement

label interaction_den_basement_chair:
    scene _unknown_house_basement
    p "Right, I can use that chair to look through the windows into other rooms."
    if not thought_about_using_chair_in_den_basement:
        $ thought_about_using_chair_in_den_basement = True
    jump den_basement

label interaction_den_basement_room5_window_look:
    scene unknown_house_room5
    p "Another girl. Hope she is just sleeping. That Frank must be using them as prostitutes to make money."
    if not have_checked_den_basement_room_5:
        $ have_checked_den_basement_room_5 = True
    jump den_basement

label scene_finding_scarlett_in_den_room4:
    scene policeman_s40_unknown_house13
    scrlt "Aaaahmmm..."
    p "Oh shit..! She scared me."
    p "(It’s Scarlett! I found her. I can go inside the room now.)"
    scene policeman_s40_unknown_house14
    scrlt "Hi, Frank."
    p "(Frank?! No... nononono. That can’t be...)"
    p "Hi, Scarlett."
    scene policeman_s40_unknown_house15
    scrlt "You haven’t been here in a while. Please, I don’t want to be here anymore. I will do anything you want, but please release me. I will never tell anybody about you and your activities, I promise... PLEASE..!!"
    menu:
        "Release her":
            $ reputation_number += 1
            jump scene_den_room4_scarlet_release
        "Take advantage":
            $ reputation_number -= 2
            $ fucked_scarletts_ass_in_den_room4 = True
            jump scene_den_room4_scarlett_take_advantage

label scene_den_room4_scarlet_release:
    scene policeman_s40_unknown_house15
    p "Fine, I will release you, but I need you to do one thing."
    scene policeman_s40_unknown_house16
    scrlt "Of course. No problem. I will do anything."
    p "Don’t worry, it will be simple and easy for you."
    scene policeman_s40_unknown_house15
    scrlt "Okay, so what do I need to do?"
    p "Okay, first of all, tie me to that examination chair. Don’t try to run because there are other people in the house, and you know what will happen if you try to go out without me."
    scrlt "Of course, I wasn’t planning to."
    scene policeman_s40_unknown_house49
    p "Great! I cannot move. Good job. And now one last thing: Give me a nice kiss and you are free..."
    scrlt "Sure."
    #TODO joraell possession sounds add
    scene policeman_s40_unknown_house_possesion01
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion06
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion05
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion04
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion03
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion02
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion03
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion04
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion05
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion06
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion01
    $ renpy.pause(1.0)
    scene policeman_s40_unknown_house38
    p "Shit! It really happened!"
    scene policeman_s40_unknown_house41
    p "I’m a girl now!"
    p "First, I need to change out of these clothes into something normal."
    scene policeman_s40_unknown_house45
    p "The only clothes here... that shirt. Really great… I still can’t believe that this worked. I’m in a girl’s body. Oh, this feeling, I will need to get used to."
    scene policeman_s40_unknown_house40
    p "Ouch!!!"
    scene policeman_s40_unknown_house44
    p "Same as with these high heels. I almost broke my ankles! How can girls walk or even dance in this shit... There are no other shoes. And I don’t want to make noise: these heels are really noisy."
    scene policeman_s40_unknown_house43
    p "Much better."
    scene policeman_s40_unknown_house42
    p "Time to leave this hellhole. Before I leave, I will carefully check Kim's room."
    scene black_screen with fade
    scene unknown_house_room4
    "Great! The Cop is having his fun with Kim. I blocked the  door with the chair and unlocked the rest of the doors. Time to leave this house. The cops will be here in a matter of minutes."
    scene black_screen with fade
    jump scene_park_scarlett_sleeping_on_bench

label scene_den_room4_scarlett_take_advantage:
    scene policeman_s40_unknown_house15
    p "Of course I will release you, but I think we can have some fun for the last time. What do you think?"
    scene policeman_s40_unknown_house16
    scrlt "Sure, we can have some… fun."
    scene policeman_s40_unknown_house17
    p "Great! This time you will remember the ride for a long time."
    scrlt "Oh...What is that?"
    scene policeman_s40_unknown_house18
    p "You will see. Come here..."
    scene policeman_s40_unknown_house19
    p "Do you feel how hard it already is?"
    scene policeman_s40_unknown_house20
    scrlt "Yes, and it’s getting bigger."
    p "Yeah. Now lie on your belly on that bed."
    scene policeman_s40_unknown_house21
    p "(Damn, she looks so cute... Maybe I can have fun with her more than once. Isn’t it a good idea?)"
    scene policeman_s40_unknown_house22
    p "And that yummy butt... It’s perfect and firm, even without using the pills."
    scene policeman_s40_unknown_house23
    scrlt "Ohhh."
    p "What are you looking at? It’s time to give me that favor."
    scene policeman_s40_unknown_house24
    scrlt "But, it's much bigger than the last time."
    scene policeman_s40_unknown_house23b
    p "Start sucking..."
    scene policeman_s40_unknown_house_transition01
    $ renpy.movie_cutscene("scenes/Policeman/40_unknown_house/webm/scarlett_s40_bj2.webm", loops=0,delay=-1, stop_music=False)
    scene policeman_s40_unknown_house_transition03
    $ renpy.movie_cutscene("scenes/Policeman/40_unknown_house/webm/scarlett_s40_bj_loop2.webm", loops=0,delay=-1, stop_music=False)
    scene policeman_s40_unknown_house_transition02
    $ renpy.movie_cutscene("scenes/Policeman/40_unknown_house/webm/scarlett_s40_bj1.webm", loops=0,delay=-1, stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/40_unknown_house/webm/scarlett_s40_bj_loop1.webm", loops=0,delay=-1, stop_music=False)
    scene policeman_s40_unknown_house24b
    p "Woow!! You are really great, slut. Now, jump on that examination chair."
    scene policeman_s40_unknown_house27
    p "Hah, that’s a pretty nice view."
    scene policeman_s40_unknown_house26
    scrlt "Please be careful..."
    p "Of course! (Hah! I’m in the lead and I will do what I want.)"
    scene policeman_s40_unknown_house28
    scrlt "Hmmm, nice and tight and warm. And those big lips..."
    scene policeman_s40_unknown_house29
    scrlt "Fffffffssss...."
    scene policeman_s40_unknown_house31
    p "That was fun, but now it's time for anal."
    scene policeman_s40_unknown_house26
    scrlt "No! I don’t like it! I’ve never done it and I don’t want to..."
    scene policeman_s40_unknown_house46
    p "It will be okay, you will see. You will like it!!! Haha!!"
    scene policeman_s40_unknown_house47
    scrlt "No, please!!! I can’t!"
    scene policeman_s40_unknown_house48
    scrlt "Please!"
    scene policeman_s40_unknown_house_transition06
    $ renpy.movie_cutscene("scenes/Policeman/40_unknown_house/webm/scarlett_s40_anal2.webm", loops=0,delay=-1, stop_music=False)
    scene policeman_s40_unknown_house_transition04
    $ renpy.movie_cutscene("scenes/Policeman/40_unknown_house/webm/scarlett_s40_anal_loop2.webm", loops=0,delay=-1, stop_music=False)
    scene policeman_s40_unknown_house_transition05
    $ renpy.movie_cutscene("scenes/Policeman/40_unknown_house/webm/scarlett_s40_anal1.webm", loops=0,delay=-1, stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/40_unknown_house/webm/scarlett_s40_anal_loop1.webm", loops=0,delay=-1, stop_music=False)
    scene policeman_s40_unknown_house31
    p "I’m almost done. Your ass was really nice and tight - it’s bringing me to the edge."
    p "On your knees. Time for the last part. Now suck me until I cum."
    scene policeman_s40_unknown_house32
    p "Suck. SUCK!!! Or you will stay here."
    scene policeman_s40_unknown_house33
    scrlt "However you want. Just let me tease you a little."
    scene policeman_s40_unknown_house31
    p "Yeah, that's good. I knew you would do it. Keep going."
    scene policeman_s40_unknown_house33
    scrlt "Anything you want."
    scene policeman_s40_unknown_house34
    scrlt "I will squeeze your balls until they blow out through your ears!!!"
    scene policeman_s40_unknown_house35
    p "Aaaaaaaaahh!!!!"
    scene policeman_s40_unknown_house36
    p "Oh, my God! What  pain!!! You SLUT!"
    scrlt "Watch your language, Frank."
    scene policeman_s40_unknown_house37
    play sound 'sounds/effects/punch_sound.ogg'
    $ renpy.pause(0.2, hard=True)
    p "Ouhhhhhhh...... pfffff...."
    scene policeman_s40_unknown_house51
    play sound 'sounds/effects/punch_sound.ogg'
    $ renpy.pause(1.1, hard=True)
    scene black_screen
    p "(Owwwuuuuuuuuu, my head is spinning and this horrible pain between my legs…. I must have passed out.)"
    scene policeman_s40_unknown_house42 with fade
    p "(There’s Scarlett! She’s going to leave me here!)"
    scene policeman_s40_unknown_house39
    p "Where do you think you’re going?!!"
    #TODO joraell possession sounds add
    scene policeman_s40_unknown_house_possesion15
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion14
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion13
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion12
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion11
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion10
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion11
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion12
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion13
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion14
    $ renpy.pause(0.5)
    scene policeman_s40_unknown_house_possesion15
    $ renpy.pause(1.0)
    scene policeman_s40_unknown_house45
    p "Great..."
    p "Now I’m a girl. That is really great... FUCK."
    p "I must run away from here now"
    scene policeman_s40_unknown_house40
    p "Ouch..."
    scene policeman_s40_unknown_house44
    p "I can’t run with these stupid shoes! Ouch! I almost broke my ankles. How can girls walk or dance in this shit!! It is impossible!. And they make a loud noise. I will hold  them in my hands."
    scene policeman_s40_unknown_house43
    p "Time to leave this shithole. Before I leave, I will carefully check Kim's room."
    scene black_screen with fade
    scene unknown_house_room4
    "Great! The Cop is having his fun with Kim. I blocked the  door with the chair and unlocked the rest of the doors. Time to leave this house. The cops will be here in a matter of minutes."
    scene black_screen with fade
    scene black_screen with fade
    jump scene_park_scarlett_sleeping_on_bench


label scene_park_scarlett_sleeping_on_bench:
    scene scarlett_s01_park_bench00
    p "Damn, I’m feeling so weak and sleepy. I must take a little rest."
    if not given_hobo_cursed_dollar:
        scene scarlett_s01_park_bench01
        hobo "Ghmm ehm..."
        scene scarlett_s01_park_bench02
        p "Oh! Please! Don’t hurt me, please!"
        hobo "Don’t worry, calm down."
        scene scarlett_s01_park_bench03
        hobo "I didn’t mean to scare you, but I saw you here on this cold night, only in that thin shirt, and wanted to help. Here, take this blanket. It will help you, trust me."
        p "Okay, I’m sorry for screaming. (What the heck is wrong with me?)"
        scene scarlett_s01_park_bench04
        hobo "It’s okay, take rest."
        p "Yes, I will..."

    if fucked_scarletts_ass_in_den_room4:
        p "(Damn, this ass hurts like hell. Looks like I fucked her too rough.)"
    scene black_screen with Fade (2.0, 0.0, 0.5)
    scene scarlett_s02_wakeup01 with dissolve
    p "Uaaahh... Hmm, what nice warm sunlight."
    scene scarlett_s02_wakeup02
    p "Damn, my neck feels like a dancefloor after a really crazy party. What was I doing yesterday?"
    scene scarlett_s02_wakeup04
    p "Wait a second.... I have red nails..? OH MY GOD! That wasn't a dream?!"
    scene scarlett_s02_wakeup05
    p "And I have boobs... ehm... tits, eeeee... I’m really a girl!"
    p "Unfortunately, there's not much to play with. Pfft!"
    scene scarlett_s02_wakeup07
    a "Hi, sleepy. How are you doing in your new body?"
    p "Not the best..."
    a "It’s already afternoon. But, I didn’t want to wake you up early. And plus, it was so nice, seeing you sleeping here, legs spread, with people walking around…"
    if fucked_scarletts_ass_in_den_room4:
        a "And by the way... How's your ass? Hihi... Serves you right!"
    scene scarlett_s02_wakeup03
    p "Haha! Really funny..."
    scene scarlett_s02_wakeup07
    a "Heh, and the best part has yet to come..."
    p "What part? What happened?"
    a " During the time you spent, sleeping it off on this bench - many things."
    p "So then, just tell me... please."
    scene scarlett_s02_wakeup08
    a "I think it will be better, to show you. Check it out!"
    scene scarlett_s02_wakeup09 with Pause (2.0)
    scene scarlett_s02_wakeup10 with Pause (2.0)
    scene scarlett_s02_wakeup27
    "Police" "We are at the place..."
    scene scarlett_s02_wakeup28
    "Police" "Upstairs looks clear... Going into the basement..."
    scene scarlett_s02_wakeup29
    "Police" "Clear the area carefully, room by room..."
    scene scarlett_s02_wakeup11
    "Police" "One room door is barred with a chair."
    scene scarlett_s02_wakeup12
    "Police" "Put your weapon down!!!"
    scene scarlett_s02_wakeup13
    pol "Fuck you! You will let me go out!"
    p "Hah! That idiot is trying to hide his face under her panties? The Fuck?!"
    "Police" "Last chance! Put your weapon down!"
    pol "I will shoot her! I WILL..!"
    play sound 'sounds/effects/gunshot_sound.ogg'
    scene scarlett_s02_wakeup15 with Pause (2.0)
    scene scarlett_s02_wakeup14 with Pause (2.0)
    "Police" "Target down!"
    scene scarlett_s02_wakeup28 with Pause (2.0)
    "Police" "Checking other rooms."
    if fucked_scarletts_ass_in_den_room4:
        scene scarlett_s02_wakeup17
    else:
        scene scarlett_s02_wakeup16
    "Police" "We have another body here - killed by knife. No one else appears to be here."
    if helped_trapped_girl:
        scene scarlett_s02_wakeup18
        trpd "Sorry, officer, I didn't hear or see anything suspicious in the last few days..."
    scene scarlett_s02_wakeup19
    beth "What are YOU doing here?!!"
    sop "He called you too?!"
    scene scarlett_s02_wakeup20
    beth "Eeee... Yes. THAT bastard!"
    sop "I think we may have to pay him back for it."
    beth "Yeah!"
    "Police" "Hands up!! Police!"
    scene scarlett_s02_wakeup21
    beth "What the..."
    scene scarlett_s02_wakeup22
    "Police" "Get out, girls. This place is not safe."
    scene scarlett_s02_wakeup23
    "Police" "We are going inside."
    scene scarlett_s02_wakeup25 with Pause (2.0)
    scene scarlett_s02_wakeup24
    "Police" "Doesn't seem anybody got here before we did. Looks like Matrix was really Frank."
    scene scarlett_s02_wakeup26
    "Police" "Boss, looks like we have found some new type of drug."
    scene scarlett_s02_wakeup07
    a "Interesting, right?"
    p "Ouuufff… What have I done?"
    a "Hah, that was the first really good deed you have done during these last weeks."
    p "What?"
    if fucked_scarletts_ass_in_den_room4:
        a "Fine, maybe you didn't want to, but you saved Scarlett."
        p "Ehm, Saved? My ass is still on fire..."
        a "I don’t like the way you went about it, but a good thing happened and next time you may remember not to do that, hih..."
    else:
        a "You saved Scarlett and didn’t use her situation for your own satisfaction."
    a "And you have taken down one of the biggest rising gangsters in this city. And saved Kim and Brandon too."
    p "And what will happen next?"
    a "Next? It is your decision. But I think you might want to first think about a change of clothes."
    p "Hmm, true... Scarlett lived with Ivana. I will start with her."
    a "Good luck."
    $ currently_possessed_cop = False
    $ currently_possessed_scarlett = True
    $ time_of_day = Set_Time_of_Day('SABAH')
    #$ are_hints_available = False # TEMP july
    $ hints_counter += 1
    jump city_map
    #stop music fadeout 1.0
    #play music "sounds/music/Menu_intro_music.ogg" fadein 3.0
    #scene outro
    #$ renpy.pause(15.0, hard=True)
    #$ renpy.quit()
