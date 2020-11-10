label scene_bethany_and_brandon_in_pond:
stop music fadeout 1.0
play music "sounds/music/Sexy_music2_necking_topher.ogg" fadein 3.0
scene bethanys01_pond_romance01
p "Hmm..? Who do we have here?"
scene bethanys01_pond_romance02
p "Ahh - that looks like Bethany. I’ve seen that scorpion tattoo before."
p "But who is that, with her? He’s squeezing that nice ass, pretty tight."
scene bethanys01_pond_romance03
$ renpy.pause()
scene bethanys01_pond_romance04
p "Hmm... They have left their stuff here. Maybe there’s some money or something useful."
menu:
    "Steal their stuff.":
        pass

scene bethanys01_pond_romance05
bran "How about a nice selfie? What do you think?"
beth "Sure - why not. This will be great, for my snapshots."
bran "Cool! Stay right here. I’m going for my phone."
stop music fadeout 5.0
scene bethanys01_pond_romance06
bran "What the hell?! Where is all our stuff?! I need to find it, before she finds out."
scene bethanys01_pond_romance07
bran "Hey baby, I’m just going to take a piss. I’ll be back in a moment."
scene bethanys01_pond_romance08
bran "Damn! I think we were just robbed. Nothing left here."
scene bethanys01_pond_romance09
p "Aaah... So, this guy is Brandon..."
scene bethanys01_pond_romance010
play sound 'sounds/effects/punch_sound.ogg'
$ renpy.pause(2)
#TODO Sound of punch to head.
scene bethanys01_pond_romance011
p "Haha! This looks like a good opportunity to sleep in a better place tonight, than under the bridge!"
stop music
scene bethanys01_pond_romance012
p "Oh yes! It is working!"
$ renpy.movie_cutscene("scenes/Bethany/01_Pond_romance/BethanyS01_brandon_possesion.webm",delay=-1)
stop music fadeout 1.0
scene bethanys01_pond_romance014
#MC as Brandon (in next texts just MC):
p "Damn, that hurts! Why did I whack him with that brush so hard? Ouch!"
scene bethanys01_pond_romance015
play music "sounds/music/sexy_music1_monks_topher.ogg"
beth "Ohhh?! What happened here?"
scene bethanys01_pond_romance016
p "I noticed that our stuff was missing. So I tried to find it."
p "And saw this bum, stealing it. So, I knocked him out, just before you arrived."
scene bethanys01_pond_romance017
beth "Wow! Baby, you are so brave! Are you alright?"
scene bethanys01_pond_romance016
p "Of course I am! What can a hobo do against me? He was no trouble... Phef..."
scene bethanys01_pond_romance017
beth "I think you deserve a special reward, for your bravery."
p "You are right. But get your clothes on and let’s get out of here, so you’re safe."
scene bethanys01_pond_romance018
# TODO Here show new items to your inventory
$ inventory.drop(bath_brush)
$ inventory.add(car_key)
$ inventory.add(phone)
$ inventory.add(credit_card)
$ inventory.add(locker_key_125)
$ inventory.add(pills)
#$ inventory.add(lube)
$ return_label = "scene_bethany_and_brandon_in_pond_continued"
$ special_inventory_display = True
call screen inventory_screen

label scene_bethany_and_brandon_in_pond_continued:
scene bethanys01_pond_romance018
beth "So, let’s get back to your car."
p "Eeeeh... (Damn! I don’t know how to drive!)"
#Continued with scene: Bethany_car_sex_scene
scene bethanys02_car_sex01
beth "Where are we gonna go?"
beth "I know another nice place."
p "So do you want to drive, then?"
scene bethanys02_car_sex02
beth "You want to let ME drive?  You NEVER let me drive."
p "I see that you want this a lot - so why not? And I think you will be a great driver."
beth "Thank you!"
scene bethanys02_car_sex03
p "Like I said, you’re driving very well."
beth "Yes, it's great fun driving this car."
scene bethanys02_car_sex04
beth "We are at the place."
scene bethanys02_car_sex05
p "So secluded? What are we doing here?"
beth "I will show you what we're doing. Just relax... We’ve done this many times."
p "But never in the car, right?"
scene bethanys02_car_sex06
beth "Hihi... Yes, but there’s a first time for everything. Hmm... what do you have here, in your pocket?"
scene bethanys02_car_sex06b
beth "Miracle sex pills?"
p "Oooohmm..."
beth "It’s cool - I like to experiment. I see you have your last 2 pills. One is for you... and one’s for me."
p "Okay..."
$ inventory.drop(pills)
beth "What will they do?"
p "I really don’t know. This will be a surprise to me too."
scene bethanys02_car_sex07
beth "I like surprises!"
scene bethanys02_car_sex08
beth "Hello, buddy. I’ve missed you for a while."
#aimations:
scene bethanys02_trans1
$ renpy.movie_cutscene("scenes/Bethany/02_car_sex/BethanyS02_HJ_cam2_loop.webm", loops=1,delay=-1, stop_music=False)
scene bethanys02_trans3
$ renpy.movie_cutscene("scenes/Bethany/02_car_sex/BethanyS02_HJ_cam1_loop.webm", loops=1,delay=-1, stop_music=False)
$ renpy.movie_cutscene("scenes/Bethany/02_car_sex/BethanyS02_HJ_closecam_loop.webm", loops=1,delay=-1, stop_music=False)
scene bethanys02_car_sex09
$ renpy.movie_cutscene("scenes/Bethany/02_car_sex/BethanyS02_dickgrow.webm",delay=-1, stop_music=False)

scene bethanys02_car_sex09
p "Whoow... What just happened?"
beth "I don’t know - but I really like it. Maybe those pills..."
p "Maybe..."
scene bethanys02_car_sex010
beth "(It’s almost as big as my head! I don’t want to wait anymore, to taste him.)"
#Animation:
scene black_screen
$ renpy.movie_cutscene("scenes/Bethany/02_car_sex/BethanyS02_BJ_in_car.webm",delay=-1, stop_music=False)
#
scene bethanys02_car_sex011
p "That was awesome, Beth! Why did you stop?"
beth "Thanks! I really enjoyed it too. But now there is this heat..."
p "Take off your top and sit here. Fresh air will do you some good."
scene bethanys02_car_sex011b
p "Better?"
beth "No! This heat is really everywhere! All over my body! Aahh..!"
#Animation:
scene black_screen
$ renpy.movie_cutscene("scenes/Bethany/02_car_sex/BethanyS02_boobsgrow.webm",delay=-1, stop_music=False)
#
scene bethanys02_car_sex011c
beth "Oh Brandon!! Take a look at theeese..."
p "-Melooons!!"
scene bethanys02_car_sex012
p "Wow! Beth! I mean it - you look stunning!"
beth "I agree! I really like them. They are so big and heavy."
p "What about some nice photos?"
beth "Of course! All the girls will be so jealous!"
scene bethanys02_car_sex013
$ renpy.pause()
scene bethanys02_car_sex015
$ renpy.pause()
scene bethanys02_car_sex015b
p "You look really awesome!"
scene bethanys02_car_sex016
beth "And I’m getting really horny. Give me that giant dick, here. I want to taste it again."
scene bethanys02_car_sex017
beth "And keep doing it until you blow!"
p "Anything you want."
beth "(This is going to be rough...)"
#Animation:
scene black_screen
$ renpy.movie_cutscene("scenes/Bethany/02_car_sex/BethanyS02_BJ_carhood.webm",delay=-1, stop_music=False)
scene bethanys02_car_sex017b
beth " *Cough* *Cough*"
scene bethanys02_car_sex018a
p "I’m cumming!!! Aaaah!"
beth "Aaarghhh..!!"
scene bethanys02_car_sex018
beth "Damn, you filled me up, almost full. Hih... But I must say, it tastes delicious."
p "That was the most awesome BJ I have ever had!"
beth "And that is just the start."
p "What do you mean?"
beth "You know, I have my... ehm... time of the month right now. But after that BJ, I’m so fucking horny."
beth "How about, you fuck my ass? I know you wanted to, but I didn’t let you before. But today, I think we can really try it."
p "Ooouh..."
scene bethanys02_car_sex019
beth "But be really careful and gentle - and please use lube. That giant dick looks dangerous for my - tender, untrained, tight ass."
p "(Dammit! I don’t have any lube. What am I going to do now?)"
scene bethanys02_car_sex020
d "Wow! It looks like you have a... big problem. Hih!"
p "Hey! What are you doing here?"
d "What? You don’t like seeing me? Maybe I can help you in this situation."
p "How?"
scene bethanys02_car_sex021
d "How about, giving you this lube? Hmm... I must admit, she looks really nice. And with those huge boobs - mmmnnn... so yummy."
scene bethanys02_car_sex022
d "And looking at you, I see you finally picked someone good looking and with nice equipment. Hihi..."
p "Yes... that time as a homeless man was... ehm... I don’t want to talk about that..."
d "Hah! Damn, she must be an athlete - that butt is so hard and firm. So here, you can use this lube. Now - you owe me 20 bucks."
p "Okay..."
d "That was a joke, silly. As a first time service, my help is for free this time."
d "But don’t go getting used to it. Next time I will want something in-return for my services."
d "So have your good fun. Aaaand... be careful with that equipment! Haha!"
scene bethanys02_car_sex019
beth "Huh? That’s weird... It felt like I blacked out for a second, there. Must be the heat..."
p "Okay baby, don’t worry. We will both enjoy this."
scene bethanys02_car_sex023
p "First a little lube here."
scene bethanys02_car_sex024
p "Aaand... sloowly... inside."
scene bethanys02_car_sex027
beth "It feels good, so far."
p "Great! I will add one finger."
scene bethanys02_car_sex025
p "And slowly... go inside."
scene bethanys02_car_sex026
p "Here it is..."
scene bethanys02_car_sex028
beth "Ehmmmmmm..."
p "You are so brave, girl. So, are you ready for my cock, baby?"
scene bethanys02_car_sex029
beth "I hope so... Please be really gentle."
p "Sure, baby."
scene bethanys02_car_sex032
$ renpy.pause()
scene bethanys02_car_sex031
$ renpy.pause()
scene bethanys02_car_sex033
$ renpy.pause()
scene bethanys02_car_sex034
$ renpy.pause()
scene bethanys02_car_sex030
p "Here it comes..."
beth "(Oh God! Oh God... I’m really doing it…) Aaaahmmm..."
scene black_screen
$ renpy.movie_cutscene("scenes/Bethany/02_car_sex/BethanyS02_anal_behind.webm", loops=1,delay=-1, stop_music=False)
scene bethanys02_car_sex029
beth "That was great! But why did you stop..?"
p "Because I want you up on top of me."
scene bethanys02_car_sex027
beth "Great!!"
scene black_screen
$ renpy.movie_cutscene("scenes/Bethany/02_car_sex/BethanyS02_anal_rideB.webm", loops=0,delay=-1, stop_music=False)
$ renpy.movie_cutscene("scenes/Bethany/02_car_sex/BethanyS02_anal_rideA.webm", loops=0,delay=-1, stop_music=False)
$ renpy.movie_cutscene("scenes/Bethany/02_car_sex/BethanyS02_anal_rideB.webm", loops=0,delay=-1, stop_music=False)
$ renpy.movie_cutscene("scenes/Bethany/02_car_sex/BethanyS02_anal_rideA.webm", loops=0,delay=-1, stop_music=False)
scene bethanys02_car_sex035b
p "I’m on the edge!"
beth "Cum on my face, babe!"
scene bethanys02_car_sex035
p "Aaahhrrr!!!"
beth "So warm….. Aaah... Baby, that was the best ride I have ever had."
p "Me to!"
beth "You MUST buy more of those pills. I really like them!"
p "Hah! Okay. (I need to figure out where Brandon got them from.)"
beth "Time to go home. Do you want to drive me home?"
p "Uhm... You can drive back, as a reward for your bravery - If your butt isn’t too sore. Haha!"
stop music fadeout 2.0
scene brandons01_car_drive1
beth "Bye, Brandon! And thanks for this wonderful night!"
scene brandons01_car_drive2
p "See you, Beth! I will pick you up in the morning!"
scene brandons01_car_drive3
p "Fuck! I have no idea where Brandon even lives..."
p "And I don’t know how to drive properly. So I will move slowly behind the corner and will sleep in the car."
scene brandon_sleeping_in_car
p "Much better than a cardboard box under a bridge... or on a park bench...."
$ time_of_day = Set_Time_of_Day('SABAH')
$ currently_posessed_homeless_guy = False
$ currently_possessed_brandon = True
$ bethany_and_brandon_in_pond = False
$ have_brandons_phone = True
scene black_screen
p "(Ahh... I slept like a baby... Hmm, it's morning already. I should pick up Bethany, for school."
scene brandons01_car_drive4
beth "Hi, Brandon!"
p "Hi, Beth. I see your boobs are back to normal now."
beth "Yes... such a shame. I wanted to show them off to the girls at school. And make the other bitches jealous. But you will buy more of those pills, right?"
p "Definitely!"
p " Ready to go to school? You can drive again, if you want?"
beth "Of course I do!"
jump school

label scene_bethany_waiting_in_female_wc:
    scene bethanys03_wc01
    p "Ah, there she is."
    scene bethanys03_wc02
    beth "Finally, you are here. So, do you have those pills for me? Those bitches said it was a photoshopped image, and didn’t believe me. I want to show them who’s right!"
    p "No. Sorry. My source doesn’t have them right now."
    scene bethanys03_wc03
    beth "I thought you said you would get them?"
    p "Yes, I will get them, but you must be patient."
    scene bethanys03_wc04
    beth "Okay, but you must remember to get them."
    scene bethanys03_wc05
    beth "I’m the only girl you have right now, right? You wouldn’t be giving these to another girl, would you?"
    p "Definitely not!"
    scene bethanys03_wc06
    beth "So, do you like what I’m doing, right now?"
    p "Ohhhm... Your hand feels great, in my pants."
    beth "So, try your best, because this is the last time you get some, until you get those pills for me. Got it?!"
    p "(Damn, she is absolutely obsessed with those pills and her big boobs.)"
    $ beth_waiting_in_female_wc = False
    $ called_to_deans_office = True
    dean "This is an anouncement. Will Brandon Walshe report to the Dean's office."
    p "I guess I'd better go upstairs..."
    $ hints_counter += 1
    jump school

label scene_bethany_sophia_in_main_hall_after_class:
    scene brandons03_computer_class03
    p "Another boring day of classes..."
    play music "sounds/music/Sexy_music3_Sunday_Plans.ogg"
    scene sophias04_mainhall_with_beth2
    sop "So what are your plans for today? Maybe we can go to my apartment and hang out."
    sop "You know, I have the whole flat to myself, right now..."
    scene sophias04_mainhall_with_beth1
    p "Ohm, yes, that doesn’t sound bad."
    scene sophias04_mainhall_with_beth3
    play sound "sounds/effects/Megan_heels_claping_sound.ogg"
    scene sophias04_mainhall_with_beth4
    sop "(Argh! Bethany is here.) So, can we go right now?"
    scene sophias04_mainhall_with_beth5
    sop "(Damn, how much I hate her: her juicy boobs and everything about her.)"
    stop sound
    scene sophias04_mainhall_with_beth7
    sop "What the heck?!! Aaa..."
    scene sophias04_mainhall_with_beth6
    beth "Hmmmmmmm... mmmm..."
    scene sophias04_mainhall_with_beth8
    beth "Don’t say anything. I hope you have it for me. I will call you later. Tonight we’ll have super fun together."
    scene sophias04_mainhall_with_beth9
    sop "What are you doing, you bitch!? Brandon?!! BRANDON?! What's she talking about?"
    scene sophias04_mainhall_with_beth10
    beth "So, wait for my call? See you later, Brandon."
    p "(Damn, she is super hot, as always.)"#I really need to get some of those pills
    scene sophias04_mainhall_with_beth11
    p "Heh... Sophia, I think I need to go pee, right now, and fix some... you know: things... See you later."
    scene sophias04_mainhall_with_beth12
    sop "Wha-...? (That BITCH! That is all because of her big boobs and firm butt. If I had the same, I could get Brandon easily.)"
    stop music fadeout 1.0
    play music "sounds/music/intro_music2_Classical_Piano.ogg"
    scene brandons07_hijacked1
    $ renpy.pause()
    scene brandons07_hijacked2
    $ renpy.pause()
    scene black_screen
    jor "You wake up after a few hours later on the park bench"
    $ time_of_day = Set_Time_of_Day('GECE')
    jump scene_brandon_wake_up_after_hijack
