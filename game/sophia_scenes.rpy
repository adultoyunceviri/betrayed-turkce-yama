label sophia_main_hall_talking:

scene sophias02_mainhall_talking02
scene sophias02_mainhall_talking05
sop "You know, we were only roommates. But it’s not nice if something happens to someone you know."
scene sophias02_mainhall_talking04
iva "Yes, you are right. But things will soon get better - you will see."
scene sophias02_mainhall_talking06
sop "You are right."
scene sophias02_mainhall_talking03
iva "And what about Mr. Anders? Still looking at me?"
sop "Yes. He hasn’t moved his eyes from your butt, all the time we’ve been standing here."
iva "Hihi... I really like teasing him. But at the right time, I have no problem to go fuck him."
scene sophias02_mainhall_talking01
sop "You're crazy, girl. I still don’t know what you see in him? There are many other really hot guys - like Brandon and others..."
scene sophias02_mainhall_talking03
iva "He is a lecturer, but looks like a bad boy - That’s really turning me on."
iva "Brandon looks like a girl with trousers. Just another guy who thinks that if he has money, he can get with any girl he wants."
scene sophias02_mainhall_talking01
sop "Hah! Girl with trousers... You're funny."
scene mranderss00_mainhall_looking01
andr "(Oh damn! These russian girls... So slutty, but so innocent looking at the same time.)"
andr "(I must figure out how to get her alone. Maybe she feels the same as me.)"
scene mranderss00_mainhall_looking02
andr "(Argh… Get a hold of yourself... She is 10 years younger and you are her Biology teacher.)"
andr "(This will be the end of your career, you fool!)"
p "Haha! What do we have here? Some banned, school romance."
jump ivana_spy_in_class


label sophia_apartment_policeman_dreaming:
scene black_screen
$ renpy.pause(0.1, hard=True)
show bathroom_policeman
p "What the hell is THIS pervert doing!"
p "Huh? Can I hear his thoughts..."
pp "(Yeah! Rub that pussy harder, bitch!)"

scene black_screen
stop music
play music "sounds/music/Sexy_music2_necking_topher.ogg"

$ Show("scenes/Sophia/S01_policeman_dreaming/sophias01_01.webm")
#$renpy.pause()
$ Hide("scenes/Sophia/S01_policeman_dreaming/sophias01_01.webm")

$ delay_time = 3.0

#image tutorial_zoom_animation = Movie(channel="scenes/Sophia/S01_policeman_dreaming/SophiaAS01_oblicej_loop.webm", play="scenes/Sophia/S01_policeman_dreaming/SophiaAS01_oblicej_loop.webm", size=(1280,720), loops=0)
#show tutorial_zoom_animation
show sophias01_01 with Pause (1.0)

scene sophias01_trans1
$ renpy.movie_cutscene("scenes/Sophia/S01_policeman_dreaming/Video/SophiaAS01_oblicej_camerazoom.webm", loops=0, stop_music=False)
$ renpy.movie_cutscene("scenes/Sophia/S01_policeman_dreaming/Video/SophiaAS01_oblicej_loop.webm", loops=1, stop_music=False)
scene sophias01_trans2
$ renpy.movie_cutscene("scenes/Sophia/S01_policeman_dreaming/Video/SophiaAS01_pussycam1B_loop.webm", loops=2, stop_music=False)
scene sophias01_trans2
$ renpy.movie_cutscene("scenes/Sophia/S01_policeman_dreaming/Video/SophiaAS01_pussycam1A_complete.webm", loops=1, stop_music=False)
scene sophias01_trans2
$ renpy.movie_cutscene("scenes/Sophia/S01_policeman_dreaming/Video/SophiaAS01_pussycam1A_handchange.webm", loops=0, stop_music=False)
scene sophias01_trans3
$ renpy.movie_cutscene("scenes/Sophia/S01_policeman_dreaming/Video/SophiaAS01_pussycam1A_loop.webm", loops=2, stop_music=False)
scene sophias01_trans4
$ renpy.movie_cutscene("scenes/Sophia/S01_policeman_dreaming/Video/SophiaAS01_pussycam2A_loop.webm", loops=2, stop_music=False)
scene sophias01_trans5
$ renpy.movie_cutscene("scenes/Sophia/S01_policeman_dreaming/Video/SophiaAS01_pussycam3A_loop.webm", loops=1, stop_music=False)
scene sophias01_trans6
$ renpy.movie_cutscene("scenes/Sophia/S01_policeman_dreaming/Video/SophiaAS01_face_finalle.webm", loops=0, stop_music=False)
scene sophias01_02
stop music fadeout (2.0)
$renpy.pause()

show bathroom_policeman
pp "(Mmmm... that smells good... Anyway - Time for lunch!)"

$ have_policemen_left_the_apartment = True
scene s00_sophia_talking_policeman03
p "I should leave, while I can..."
pol "That was everything we needed, miss."
pp "Yeah. Exactly what I needed! Many thanks for your patience. If we need anything more, we will call you."
pol "And of course, if you remember something else, you can call in at the local police department."
sop "Thank you, officers, for your service."
p "Hah! That perv cop is hilarious. He didn’t even TRY to hide those panties right."
$ time_of_day = Increment_Time_Of_Day()
$ hints_counter += 1
jump city_map


#image tutorial_zoom_animation = Movie(channel="scenes/Megan/S00_tutorial/Megan_zoom.webm", play="scenes/Megan/S00_tutorial/Megan_zoom.webm", size=(1280,720), loops=0)
#show tutorial_zoom_animation
#$ renpy.pause(3.0, hard=True)

label scene_sophia_policeman_mc_room_entering:
scene s00_sophia_talking_policeman00

sop "This was his room, in here."
$ hints_counter += 1
call screen mc_room_with_sofia_and_policeman

label scene_sophia_policeman_mc_room_conversation:
scene s00_sophia_talking_policeman01

sop "We’d known each other... only 3 months. Just from the beginning of - this school year."
sop "He was the same as most students: All day long, he would be “who knows where” - and here, he only came in to sleep."
sop "Why would you even investigate this? Wasn't it an accident?"

scene s00_sophia_talking_policeman02
pol "Yes - most likely. This is just normal procedure. We must rule out the possibility of this being a suicide, among other things."
p "Pfff... Suicide? What an idiot..."
$ hints_counter += 1
$ listened_to_sophia_with_policeman_in_mc_room = True

call screen mc_room_with_sofia_and_policeman

label idle_sophia_policeman_mc_room_conversation:
    scene mc_room_day_cathy_policeman
    p "I've learned everything I'm going to, here. I better leave, while I can."
    call screen mc_room_with_sofia_and_policeman

label scene_sophia_comes_home_when_hobo_there:
# TODO possible key in door sound here
p "Fuck! Someone is at the door. Sophia must be home early."
p "I need to hide."
scene sophia_comming_home
sop "I guess I have to get used to living here on my own, for a while."
sop "Maybe I'll need to put out an ad for a new roommate soon."
$ have_showered_as_hobo = True
$ hints_counter += 1
call screen mc_room

label scene_sophia_sees_brandon_main_hall:
    scene sophias03_mainhall_talking_brandon01
    sop "Hiii, BRANDON. I’m over here!"
    p "(Oh God... She is a fine girl, but she’s acting like a kid who lost her toy.)"
    p "Hi, Sophia..."
    scene sophias03_mainhall_talking_brandon02
    sop "How are you?"
    p "Great! I slept like a baby."
    sop "What will we be doing today?"
    p "Eeeehh..."
    scene sophias03_mainhall_talking_brandon03
    sop "It’s okay, you can think about that during computer class."
    p "Great..! Let’s go."
    jump main_hall
