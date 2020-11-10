label scene_megan_wc_spy:
stop music
play music "sounds/music/Sexy_music2_necking_topher.ogg"
scene megans01_01
p "She is really pretty..."
meg "Pfft! She thinks that she knows what is best for my experiments? What a bitch!"
meg "Now... she gives MY pills for testing, to some other students - not thinking about how dangerous that can be."
scene megans01_02
meg "I’m the only one here who knows what to do. And it worked pretty well on Nick before."
meg "I still have the image of that - pumping huge monster, right in front of my eyes."
scene megans01_03
p "She definitely has the right shapes."
scene megans01_04
p "And up here too. Smaller, but great shape."
scene megans01_05
stop music fadeout 2.0
p "Oh, she’s leaving. I need to go with her, if I don’t want to be stuck here."
$ saw_megan_scene_in_wc = True

$ time_of_day = Increment_Time_Of_Day()
$ hints_counter += 1
jump city_map


label scene_megan_going_into_wc:
show main_hall_board
stop music fadeout 1.0
play sound "sounds/effects/Megan_heels_claping_sound.ogg"
show main_hall_board with Pause (3)
stop sound
p "Hmmm... someone is here?"
play sound "sounds/effects/Megan_heels_claping_sound.ogg"
play movie "scenes/Megan/S02_Megan_walk/MeganS02_walk_camA.webm"
show black_screen
$ renpy.pause(2.0, hard=True)
stop movie
play movie "scenes/Megan/S02_Megan_walk/MeganS02_walk_camB.webm"
$ renpy.pause(4, hard=True)
stop movie
stop sound
scene megans02_walk
p "What a hot chick!"
p "Hmm... I saw her around before, in this school, but never met with her in any class."
p "She's going to the bathroom. Maybe I will see something interesting here."
$ hints_counter += 1
jump female_wc_with_megan

label idle_female_wc_with_megan_back_button_cant_leave:
show female_wc_main_megan
p "The door closed behind us. I can't leave till she does."
call screen female_wc_with_megan
