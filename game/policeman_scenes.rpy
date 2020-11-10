label scene_first_steps_as_cop:
    scene policeman_s03_00
    $ hint_system_dict = {0: 'Hint: Looks like you cannot touch anything. Try to check everything in the room.',
    1: 'Hint: Try to find out what Sophia and the Policeman are talking about.',
    2: 'Hint: You have learned all you can here. The door is now open, Try to explore the rest of the house and see what or who you can find.',
    3: 'Hint: Nothing to do yet. Might as well follow Sophia to the school.',
    4: 'Hint: Locked in the school? Might as well pass the time by reading some stuff.',
    5: 'Hint: Potential possession victim. Why not take a closer look?',
    6: 'Hint: Time to look around town for someone susceptible to possess.',
    7: 'Hint: The hobo is not drunk enough yet. Why not rest up nearby, while you wait.',
    8: 'Hint: The hobo should be drunk enough by now. Try out your possession power on him.',
    9: 'Hint: Now that you are able to touch things, there is an important item of yours at the crash site. You will need a tool.',
    10: 'Hint: You have found your apartment keys. Time to put them to use.',
    11: 'Hint: Look around the apartment for something that will help you. Also try to get rid of the hobo smell.',
    12: 'Hint: Sophia is home now. Better get out without her noticing.',
    13: 'Hint: No money. Had to leave your apartment. Looks like it\'s the park bench again tonight.',
    14: 'Hint: There are some noises coming from the pond. Might want to check them out.',
    15: 'Hint: You have a locker key. Look for locker 125.',
    16: 'Hint: Who is this woman? Get a closer look.',
    17: 'Hint: You have found a strange flash drive. Look at it on your apartment computer.',
    18: 'Hint: Your computer is no longer in the apartment. Try the computers at school and find out what is on the flash drive.',
    19: 'Hint: Bethany is waiting in the girls toilet. Go see what she wants.',
    20: 'Hint: The school Dean is waiting upstairs in her office.',
    21: 'Hint: Look around the the office for possible answers to the password hints.',
    22: 'Hint: The devil said to give the hobo this $100 bill. He is usually staying under the bridge in the park.',
    23: 'Hint: Now you know where Brandon lives. You can take a taxi to get there. The taxi parking is near the shop.',
    24: 'Hint: Now you can visit the cop’s apartment.',
    25: 'Hint: Your clothes are not so comfortable. You need to change them. Also there is some information about the cop here.',
    26: 'Hint: Maybe you can check the cop’s computer for more information.',
    27: 'Hint: Time for bed.',
    28: 'Hint: You need to go to the Dean’s office, which is upstairs.',
    29: 'Hint: You have time to check the local hospital, to find out if Nick was there.',
    30: 'Hint: You have to meet with Brandon now at the warehouse.',
    31: 'Hint: Time for bed.',
    32: 'Hint: You need to go to the Dean’s office again, upstairs.',
    33: 'Hint: You need to visit Ivana in her apartment.',
    34: 'Hint: Nothing more to do right now. Go back to the cop’s apartment.',
    35: 'Hint: Time for bed.',
    36: 'Hint: Need to visit Megan in the school laboratory.',
    37: 'Hint: You have time to sneak into Anders’ office. His office is upstairs. You first need to find Anders and make sure he’s occupied.',
    38: 'Hint: Look around Anders’ office and find evidence to put him away.',
    39: 'Hint: You need to find Ivana right away. She should still be in one of the classes.',
    40: 'Hint: Ivana already went home to her apartment. Need to go and see her there.',
    41: 'Hint: You need to get the cop’s gun just in case Anders gets violent. Also there is time to collect the pills from Megan. Then go back to Ivana’s apartment for the sting operation.',
    42: 'Hint: First, you need to unload the gun.',
    43: 'Hint: Better go to bed. Tomorrow is going to be a long day.',
    44: 'Hint: You need to talk with Sophia at school.',
    45: 'Hint: You have something on Anders. Better to visit him during school hours at his office.',
    46: 'Hint: You need to visit Sophia at your old apartment.',
    47: 'Hint: You have nothing to do now. Better to go home.',
    48: 'Hint: You appear to have a visitor. Better see what she wants.',
    49: 'Hint: Time for a nice sleep after that nice wine.',
    50: 'Hint: You need to grab your stash of drugs and your gun and meet with Brandon at the warehouse.',
    51: 'Hint: You need to hide that gun first.',
    52: 'Hint: Better go to bed and leave this day behind.',
    53: 'Hint: You appear to have a visitor. Better see what she wants.',
    54: 'Hint: It’s time to visit your blonde neighbor.',
    55: 'Hint: You need to find Sophia at school. Ask around.',
    56: 'Hint: Sophia is in the Gym behind the school building. Go there.',
    }#TEMP
    p " I can’t just leave him lying there like that. Better take him and and leave him some other place."
    show black_screen
    play music "<from 25 to 40>sounds/music/commando_matrix.ogg" fadein 3.0
    $ renpy.movie_cutscene("scenes/policeman/03_go_from_park/shoes.webm", delay=-1, stop_music=False)
    scene policeman_s03_04
    $ renpy.pause(2.0, hard=True)
    $ renpy.movie_cutscene("scenes/policeman/03_go_from_park/shoes2.webm", delay=-1, stop_music=False)
    scene policeman_s03_01
    $ renpy.pause(2.0, hard=True)
    $ renpy.movie_cutscene("scenes/policeman/03_go_from_park/shoes.webm", delay=-1, stop_music=False)
    scene policeman_s03_06
    $ renpy.pause(2.0, hard=True)
    $ renpy.movie_cutscene("scenes/policeman/03_go_from_park/shoes2.webm", delay=-1, stop_music=False)
    scene policeman_s03_05
    $ renpy.pause(2.0, hard=True)
    scene policeman_s03_02
    play music "sounds/music/intro_music2_Classical_Piano.ogg" fadein 3.0
    p "It’s good that some cops have such big trucks. I can load him into this pickup."
    p "So where do I want to go? I need to go to where he lives. Now’s a good time to check his phone."
    scene policeman_s03_02
    play sound "sounds/effects/phone_ringing_sound.ogg"
    $ renpy.pause(2.0, hard=True)
    stop sound
    scene policeman_s03_03
    show phone_delivery_sms
    $ renpy.pause(4.0, hard=True)
    scene policeman_s03_03
    p "Hmm... great. He has an apartment near to this place."
    scene policeman_s03_07
    p "Good. This car has navigation. I think I can make it to his apartment. I’ll leave Brandon somewhere along the way."
    p "God bless automatic transmissions. Haha! Cop without a driving licence, what could happen?"
    $ is_cops_apartment_available = True
    $ hints_counter += 1
    jump city_map

label scene_cops_apartment_first_time:
    scene policeman_main
    p "First things first: I need to offload this gun before I blow my dick off with it."
    $ inventory.drop(gun)
    scene policeman_s17_gun
    p "This drawer should be safe enough."
    scene policeman_main
    p "These clothes are starting to itch. I should see what else this guy has to wear."
    $ hints_counter += 1
    jump cop_apartment_bedroom

label cop_apartment_bedroom_wardrobe:
    if not have_changed_clothes_as_cop:
        scene policeman_04_clothes_change
        p "Great! This suits me really well. Damn, I’ll need to get used to these muscles."
        $ have_changed_clothes_as_cop = True
        if have_left_panties_in_cops_bedroom:
            $ hints_counter += 1#split increment
    else:
        if have_left_panties_in_cops_bedroom:
            scene policeman_bedroom_panties
        else:
            scene policeman_bedroom
        p "I don't need anything from there right now."
    jump cop_apartment_bedroom

label cop_apartment_bedroom_pillow:
    if have_left_panties_in_cops_bedroom:
        scene policeman_bedroom_panties
    else:
        scene policeman_bedroom
    p "I don't need to sleep right now."
    jump cop_apartment_bedroom


label scene_cop_apartment_found_password:
    scene policeman_04_notebook
    p "Hmmm... his password really is a cop’s style! I always thought that only happens in stupid movies."
    p "So what  do we have here: Some trash and ads. Hmm, here is an e-mail from his boss."
    "Boss" "About this case of the missing girl, Scarlett. I’m giving it to you because Tavarez is absolutely useless and in two months he hasn’t found anything. So I’m expecting some good news from you as soon as possible."
    p "Looks like I have a task. If I find this Scarlett I will show that Angel that I’m not useless. What else do we have here?"
    p "Hmm... hmm... hmmm... ... (College student involved in a car accident... That's about me!) What's written here?"
    scene policeman_04_devil_come00
    d "Hi! How's my little cop doing?"
    scene policeman_04_devil_come01
    p "What are you doing here?"
    scene policeman_04_devil_come02
    if given_hobo_cursed_dollar:
        d "I decided to apologize to you, a little: for the way I acted before. You know, I’m..."
    else:
        d "I just decided to visit you. DO you have a problem with that?"
        p "No. I have a problem with the fact that you wanted to kill that hobo, who - by the way - just so happened to save my life, when he didn't have to. What if he hadn't been there because I gave him the money?"
        d "Heey! Calm down. If you had given him the bill, like I wanted, the same results would have happened just in another way. Do you think that I want you dead, you silly boy?"
        p "Fine... so why are you here?"
        d "Because I have a surprise for you."
    scene policeman_04_devil_come03
    play sound 'sounds/effects/notebook_smash.ogg'
    $ renpy.pause(2.0)
    stop sound
    $ devil_broke_cop_computer = True
    scene policeman_04_devil_come07
    if given_hobo_cursed_dollar:
        p "Really? Yeah, thanks... Some apology that is...."
    else:
        p "Really? Yeah, thanks... Some surprise that is...."
    scene policeman_04_devil_come04
    d "Ooohhh. I’m really sorry. I’m so awkward. Once again, sorry for that."
    scene policeman_04_devil_come05
    d "But on the other hand, it wasn’t yours."
    p "Which doesn’t mean you had to break it."
    d "Hey, I already apologised for that, and that is all you’ll get from me on that. But, why I came to you was for another matter. I have decided to teach you another skill."
    scene policeman_04_devil_come06
    p "Hmmm, and what is that?"
    d "When you touch anybody and look straight into their eyes, you can see some flashbacks from their life that could be important to you."
    p "Sounds helpful."
    d "It is! Especially since you are a cop now!"
    p "I have a question for you."
    scene policeman_04_devil_come05
    d "Yes, what is it?"
    p "Do you know where Scarlett is?"
    d "Yes. But as I already stated, my work is not free and…"
    p "Yeah, I know. I don’t need to hear about that again."
    d "Great! So that is all. Have a nice rest of the day and good luck with that case!"
    $ ready_to_sleep_first_time_as_cop = True
    $ hints_counter += 1
    scene black_screen with fade
    jump cop_apartment_main

label exit_block_ready_to_sleep_as_cop:
    scene policeman_main
    p "I'm done for the day. I should go to bed."
    scene black_screen
    jump cop_apartment_main

label scene_cop_sleep_in_bed_first_time:
    $ ready_to_sleep_first_time_as_cop = False
    scene policeman_bedroom_panties
    scene policeman_04_go_sleep with fade
    p "Fine. Everything seems to be good right now. Being a cop is not that bad."
    p "Tomorrow, I will start working on that Scarlett case and visit the Dean in her office. And during that time, I will get some of those pills for Bethany."
    scene black_screen with fade
    $ time_of_day = Set_Time_of_Day('SABAH')
    $ hints_counter += 1
    jump scene_cop_in_college


label scene_cop_in_college:
    scene main_hall_board
    show mainhall_board_roommate:
        xpos 300 ypos 400
    p "Before I go to the Dean’s office I will check out the notice-board for anything new."
    p "Hmm. Sophia’s looking for a new roommate. I’m curious who she will find."
    $ cop_needs_to_visit_dean = True
    jump main_hall_board

label scene_cop_visits_dean_in_office:
    scene policeman_05_dean_talk02
    dean "Hello. Mister...?"
    scene policeman_05_dean_talk04
    p "Matrix … John Matrix."
    scene policeman_05_dean_talk02
    dean "Aah, I was just reading in the newspapers about you. You are that brave cop, fighting against those dealers."
    scene policeman_05_dean_talk00
    p "Yes. That's me. Can we speak about the missing girl?"
    scene policeman_05_dean_talk02
    dean "Of course we can! What do you need to know?"


label scene_deans_office_scarlett_question:
    if scarlett_questions_address_asked and scarlett_questions_enemies_asked and scarlett_questions_issues_asked:
        jump scene_cop_in_laboratory
    scene policeman_05_dean_talk02
    menu:
        "Do you know Scarlett’s address during her time studying here in college?"if not scarlett_questions_address_asked:
            dean "Yes, she was living in the same apartment with that Russian student Ivana - but this, I've already mentioned to your colleague, before."
            $ scarlett_questions_address_asked = True
        "Did she have any enemies here or is there anything I need to know?"if not scarlett_questions_enemies_asked:
            dean "I don’t think so. Her biggest problem was what she was wearing to school, to make other girls jealous of her."
            $ scarlett_questions_enemies_asked = True
        "What about other school personnel. Anybody have any issues with her?"if not scarlett_questions_issues_asked:
            dean "Nooo... I don’t know about any problems. She was just going to Mr. Anders for tutoring on Biology, because she had some problems in that area."
            $ scarlett_questions_issues_asked = True
    jump scene_deans_office_scarlett_question

label scene_cop_in_laboratory:
    scene policeman_05_dean_talk02
    p "(So I need to talk with Ivana and Anders...)"
    scene policeman_05_dean_talk04
    p "Great. Now I’d like to see your school laboratory."
    scene policeman_05_dean_talk03
    dean "Lab… Laboratory? Why do you want to see it? How is this related to your case?"
    scene policeman_05_dean_talk01
    p "I’m just curious. And don’t worry, I know everything about the experiments you’re doing here..."
    p "...With your students."
    scene policeman_05_dean_talk03
    dean "But..."
    scene policeman_05_dean_talk00
    p "If you don’t want to have any more problems we should go there right now!"
    scene policeman_05_dean_talk03
    dean "Eeeh... Come with me."
    scene black_screen with fade
    scene megan_04_lab00 with fade
    p "(Damn. What a nice figure...)"
    dean "So, here we are."
    scene megan_04_lab01
    dean "This is Megan, our laboratory expert, and this is our brand new school lab."
    meg "Eeehm..."
    dean "This is Detective John Matrix. He just has a few questions for you. So tell him everything he will ask. I must go now."
    p "I’m glad to meet you, Megan."
    scene megan_04_lab03
    meg "Thank you, Detective."
    scene megan_04_lab04 with dissolve
    play sound 'sounds/effects/whoosh_sound.ogg'
    $ renpy.pause(4.0, hard=True)
    scene megan_04_lab05 with dissolve
    play sound 'sounds/effects/whoosh_sound2.ogg'
    $ renpy.pause(4.0, hard=True)
    scene megan_04_lab06 with dissolve
    play sound 'sounds/effects/whoosh_sound.ogg'
    $ renpy.pause(4.0, hard=True)
    p "(Wow! So Devil was right: that flashback skill is working. So, looks like Megan is being a little terrorised by the Dean, and she definitely has something going on with one of her test subjects.)"
    meg "So, Detective, what did you want to ask about?"
    scene megan_04_lab09 with dissolve
    p "I just wanted to see the place where the miracle pills were created."
    meg "Ah, you know about our experiment?"
    p "Yes. Are you the only one who’s working on that?"
    meg "Right now, yes. I have a good friend who came up with that idea, but…"
    p "But what?"
    scene megan_04_lab08
    meg "But I’ve not seen him in the last few weeks and hope he is alright."
    p "Who is he?"
    scene megan_04_lab09
    meg "His name is Nick."

    if deans_office_have_got_on_computer:
        p "Is he the guy from the recording?"
        meg "What recording do you mean?"
        p "I saw a security camera recording with you riding a guy that looked like he was dead."
        scene megan_04_lab08
        meg "Whaaaaat!!?!"
        p "You didn’t know about the recording?"
        meg "Of course not!"
        p "Hah... Do you have a photo of him?"
        meg "Sure. There is one."
        scene nick_photo
        $ inventory.add(photo)
        $ renpy.pause()

        scene megan_04_lab09
        p "Great. Back to these experiments: Can I have a few samples?"
    else:
        p "Is he one of the students?"
        meg "Yes he is. We are working together. But I don’t know his surname. But here is his photo."
        scene nick_photo
        $ inventory.add(photo)
        $ renpy.pause()
        scene megan_04_lab09
        p "Fine, I will look into this case. About these pills: can I get a few samples?"

    meg "Right now, no. Because I don’t have any."
    p "And when will you have some?"
    meg "Until I get a new sample from Nick, I can't do anything, even with all this new equipment. After I get that sample I won’t need another, because I can do a full analysis with this new stuff."
    p "And you said, Nick disappeared?"
    meg "I said, I haven’t seen him in a long time."
    p "And what happened when you saw him last?"
    meg "Last time? Hmm... Last time we met? I sent him to the local hospital, because we needed some detailed tests."
    p "Hmm, fine. I will take a look around at the hospital. What test was it?"
    meg "It was a complete body scan."
    scene megan_04_lab07
    p "So, Megan, it was nice to meet you. And when I have any information about Nick I will contact you."
    meg "I hope you can do it, Detective."
    $ cop_needs_to_visit_dean = False
    $ time_of_day = Set_Time_of_Day('ÖĞLEN')
    scene black_screen with fade
    jump scene_brandon_calling_cop

label scene_brandon_calling_cop:
    scene main_hall
    play sound "sounds/effects/phone_ringing_sound.ogg"
    $ renpy.pause(2.0, hard=True)
    show telephone00
    $ renpy.pause(0.02, hard=True)
    hide telephone00
    show telephone01
    $ renpy.pause(0.02, hard=True)
    hide telephone01
    show telephone02
    $ renpy.pause(0.02, hard=True)
    hide telephone02
    show telephone03
    $ renpy.pause(0.02, hard=True)
    hide telephone03
    show telephone04
    $ renpy.pause(0.02, hard=True)
    hide telephone04
    show telephone05
    $ renpy.pause(0.02, hard=True)
    hide telephone05
    show telephone06
    $ renpy.pause(0.02, hard=True)
    hide telephone06
    show telephone07
    $ renpy.pause(0.02, hard=True)
    hide telephone07
    show telephone08
    $ renpy.pause(0.02, hard=True)
    hide telephone08
    show telephone09
    $ renpy.pause(0.02, hard=True)
    hide telephone09
    show telephone10
    $ renpy.pause(0.02, hard=True)
    hide telephone10
    show telephone11
    $ renpy.pause(0.02, hard=True)
    hide telephone11
    show telephone12
    $ renpy.pause(0.02, hard=True)
    hide telephone12
    show telephone13
    $ renpy.pause(0.02, hard=True)
    hide telephone13
    show telephone14
    $ renpy.pause(0.02, hard=True)
    hide telephone14
    show telephone15
    $ renpy.pause(0.02, hard=True)
    hide telephone15
    show telephone16
    $ renpy.pause(0.02, hard=True)
    hide telephone16
    show telephone17
    $ renpy.pause(0.02, hard=True)
    hide telephone17
    show telephone18
    $ renpy.pause(0.02, hard=True)
    hide telephone18
    show telephone19
    $ renpy.pause(0.02, hard=True)
    hide telephone19
    show telephone20
    $ renpy.pause(0.02, hard=True)
    hide telephone20
    stop sound
    show phone_brandon_call
    p "What? Brandon is calling me?"
    bran "I’m really sorry, man! I’m really sorry."
    p "Hey, calm down. What do you need?"
    bran "Eeehh... I need to talk to you about that money. Please, it’s not my fault!"
    p "Yeah. Be at the warehouse at 9pm."
    p "Wooow. He sounds really scared."
    p "Fine. I have enough time to check out that hospital."
    $ hospital_location_available = True
    $ have_apointment_at_hospital = True
    $ hints_counter += 1
    jump city_map

label scene_hospital_first_time:
    scene policeman_s06_hospital04
    p "The city hospital."
    scene policeman_s06_hospital05
    p "Megan signed me up for a complete body scan. Same as they gave Nick before. I wonder what they have to say about me in this case."
    scene policeman_s06_hospital00
    kat "Hello, sir. My name is Kate, how may I help you?"
    scene policeman_s06_hospital_flashback00
    play sound "sounds/effects/whoosh_sound.ogg"
    p "She knows the Dean from the school. Interesting…."
    scene policeman_s06_hospital_flashback01
    play sound "sounds/effects/whoosh_sound2.ogg"
    $ renpy.pause(4.0, hard=True)
    scene policeman_s06_hospital_flashback02
    play sound "sounds/effects/whoosh_sound.ogg"
    p "So Nick was really here."
    scene policeman_s06_hospital_flashback03
    play sound "sounds/effects/whoosh_sound2.ogg"
    p "(Wait a second. Mom was here? Why was SHE here?)"
    scene policeman_s06_hospital01
    p "I’m here for a complete body scan. Here is my information."
    kat "Great! Hmm. From school? We normally have a queue for this, but in your case I can make an exception and we can begin this scan right away."
    scene policeman_s06_hospital02
    p "Actually I’m not here because of the scan. I’m actually a detective, and I'm working on the case of a missing person. And the last place he was heard from is that complete scan and your office. What can you tell me about this?"
    kat "Ehmm… I’m don’t know what you are talking about, Detective. We are a hospital. We are just doing our job here."
    p "So, then, why did you want to make an exception in my case?"
    kat "Because we have a deal with the school. We are helping them in their research."
    p "So you know  the Dean of the school pretty well?"
    kat "Yes, we’ve met a few times."
    p "I’m looking for a guy named Nick. Here is his photo. Do you know where he is? As I said before, I know he has been here, but after that he disappeared. And I know about the experiments the Dean has been doing in that school, so tell me the truth."
    scene policeman_s06_hospital03
    kat "Fine. Yes, he was here. I gave him that scan he ordered, but if you are looking for him, you must ask the Dean of the school, because he walked out of here with the results in hand."
    p "I Hope that you are being truthful with me. I will ask the Dean about him. Thanks for your help, Kate. Bye."
    kat "Bye, Detective."
    $ have_apointment_at_hospital = False
    $ time_of_day = Set_Time_of_Day('AKŞAM')
    $ hints_counter += 1
    # jump city_map_cop_ready_meet_brandon_at_warehouse


label city_map_cop_ready_meet_brandon_at_warehouse:
    scene city_map
    p "It is almost 9pm. It’s time to meet with Brandon at the warehouse."
    $ brandon_waiting_at_warehouse_for_cop = True
    jump city_map

label scene_cop_meets_brandon_at_warehouse:
    scene policeman_s08_warehouse00
    bran "H-Hey, Bud. How are ya? Heh..."
    scene policeman_s08_warehouse01
    p "You’re a little bit too happy, aren’t you?"
    scene policeman_s08_warehouse03
    p "I want that money in three days. If you cannot fix this you are useless to me - and I throw away useless things!"
    scene policeman_s08_warehouse04
    bran "Okay. Three days is enough. I’m really sorry about that. I don’t know what happened. I have a few days blank. One second I was doing fun stuff with Bethany at the pond near the park, and then I woke up somewhere else, a few days later."
    p "Heh. I’ll give you some good advice. Don’t use my drugs if you cannot handle them. That's the only thing I'll tell you."
    scene policeman_s08_warehouse01
    bran "And what about a new delivery? That last one, somebody must have stolen it, because I don’t have it and the secret stash place is empty."
    p "That's the one thing that I like about you. You are up to your knees in shit and have enough courage to ask for more stuff. Sure, if you give me the money I will give you more."
    p "(But first I must find out where the cop hides it.)"
    scene policeman_s08_warehouse00
    bran "Great! I will be here at the same time in three days with double the money. For what I owe you, and for the new batch."
    p "Deal. Don’t disappoint me!"
    $ time_of_day = Set_Time_of_Day('GECE')
    $ ready_for_cop_asian_night_scene = True
    $ brandon_waiting_at_warehouse_for_cop = False
    $ hints_counter += 1
    jump warehouse_main

label scene_asian_visits_cop_at_night:
    scene policeman_s07_asian00
    p "I feel really exhausted. Being another person is tough."
    scene policeman_s07_asian01
    p "Whaahfmmmf...."
    asn "Ssshh!"
    scene policeman_s07_asian02
    asn "I’m curious how can you go to sleep so easily?"
    p "(I’ve never seen her before, but looks like she knows this cop.)"
    p "What do you mean?"
    asn "I mean you've done a great job with that drug gang. Now the drug business is under our control. But I think you might want to be a little more vigilant. See how easy it was to sneak silently into your bed?"
    p "Yeah, I see. But what are you doing here?"
    scene policeman_s07_asian03
    asn "You are not happy to see me?"
    p "Of course I am!"
    scene policeman_s07_asian04
    asn "That's good, because I’m here to fulfill my second part of our deal."
    stop music fadeout 1.0
    play music "sounds/music/Background_music2_Brunno.ogg" fadein 3.0
    scene policeman_s07_asian05
    asn "For the great job you’ve done, you deserve the best ‘job’ too."
    p "I believe that you give the best blowjobs."
    scene policeman_s07_asian06
    asn "Blowjob? Hah, no that’s disgusting. But I’m the best at doing other things."
    scene policeman_s07_asian07
    asn "Be calm and relax."
    scene policeman_s07_asian08
    p "Wow, you have such smooth and warm feet."
    scene policeman_s07_asian09
    $ renpy.movie_cutscene("scenes/Policeman/07_asian_girl/policeman_s07_footjobcam1.webm", loops=2,delay=-1, stop_music=False)
    scene policeman_s07_asian09
    p "You are a real master at that."
    scene policeman_s07_asian10
    p "And that is just the beginning..."
    scene policeman_s07_asian11
    $ renpy.movie_cutscene("scenes/Policeman/07_asian_girl/policeman_s07_footjobcam2.webm", loops=2,delay=-1, stop_music=False)
    scene policeman_s07_asian11
    p "I’m on the edge!"
    p "Aaaaaa!!!"
    scene policeman_s07_asian12
    $ renpy.pause(2.0, hard=True)
    scene policeman_s07_asian13 with dissolve
    $ renpy.pause()
    asn "Hih! You came so fast."
    p "It was impossible to resist you any longer."
    asn "I know. That is how I was trained. I always get what I want. So our deal is fulfilled now."
    p "Will we meet again?"
    asn "Maybe. Sometimes I need a capable person like you. Now I must go. Bye bye!"
    scene policeman_s07_asian00
    p "Hmmm. It is always good to get a reward for no work. Hehe. But I know what I have to do. I should meet with the Dean first thing tomorrow."
    $ ready_for_cop_asian_night_scene = False
    $ cop_needs_to_visit_dean_again = True
    $ time_of_day = Set_Time_of_Day('SABAH')
    $ hints_counter += 1
    scene black_screen with fade
    jump cop_apartment_bedroom

label scene_cop_visits_dean_in_office_again:
    scene policeman_s13_dean_second00
    p "I have a few questions for you. First I want to say, I have no problem with the experiments you are doing here. It's not my business. So please answer my questions truthfully."
    dean "Sure, Detective."
    p "I’m looking for that guy named Nick. I believe he was one of your test subjects."
    dean "You have been misled. He was our initial test subject and the most important element in our research."
    p "So where is he? He disappeared."
    dean "Oh! Really? Who told you that? I just sent him on vacation with my niece Brooke."
    p "Wait? What vacation?"
    dean "As I said: he is our most important test subject. And we cannot afford to lose him or have him change his mind and stop cooperating with us. That would be a disaster for our experiment."
    dean "So I decided to give him a vacation from school, with my niece watching over him during that vacation. He is in love with her."
    p "(Who isn’t? Every guy in this school wants to fuck Brooke.)"
    dean "And during that vacation, Megan is rebuilding the laboratory so that we can continue working when they get back."
    p "That sounds plausible. But to be sure: do you have any proof of this?"
    dean "Sure. Here is a photo they sent me about a week ago."
    scene policeman_s13_dean_second01
    p "Oooh. Yes, they look happy."
    dean "I hope they are."
    scene policeman_s13_dean_second00
    dean "And for sure. Our new lab has been completed for a week, and Megan finished the last test recently, meaning their vacation is over. They will come back tonight, so you can meet with him tomorrow."
    p "(So Nick got to go on vacation with Brooke and just didn’t want to say anything to Megan. And she thinks he is in danger. Poor Megan...)"
    p "I think that won't be necessary. Thank you for your cooperation in this case. Now I need to visit Mr. Anders. Where can I find him?"
    dean "Yes. His office is just next door."
    p "Thank you and have a good day."
    scene policeman_s11_anders_visit00
    p "Here’s his office. *Knock knock*"
    andr "Come in."
    scene policeman_s11_anders_visit01
    andr "Hello?"
    p "Hello, Mr. Anders. My name is Matrix… John Matrix. I’m a detective in the local police department. I a have few questions about the missing student Scarlett Sage."
    scene policeman_s11_anders_flashback02
    play sound "sounds/effects/whoosh_sound2.ogg"
    p "(That is Ivana and Sophia. Is she teasing him?)"
    scene policeman_s11_anders_flashback00
    play sound "sounds/effects/whoosh_sound.ogg"
    $ renpy.pause(4.0, hard=True)
    scene policeman_s11_anders_flashback01
    play sound "sounds/effects/whoosh_sound.ogg"
    p "(That is Scarlett!!! He killed her! Right here in the office!)"
    scene policeman_s11_anders_flashback03
    play sound "sounds/effects/whoosh_sound2.ogg"
    p "(And he's fapping to Ivana's pictures. I need to have evidence to get him thrown in jail!)"
    scene policeman_s11_anders_visit02
    andr "Sure, Detective. Take a seat. I will try my best to answer your questions to help find Scarlett."
    p "(You bastard! Smiling right in my face while talking about her.)"

label scene_anders_office_ask_scarlet_questions:
    scene policeman_s11_anders_visit03
    if scarlett_questions_anders_relationship_with_her_asked and scarlett_questions_often_meeting_with_anders_asked and scarlett_questions_when_anders_saw_her_last_asked and scarlett_questions_anders_relationship_with_ivana_asked and scarlett_questions_ask_anders_if_anything_else_asked:
        $ cop_needs_to_visit_dean_again = False
        jump city_map_cop_need_to_talk_to_Ivana_in_her_apartment_first
    menu:
        "What was your relationship with Scarlett?"if not scarlett_questions_anders_relationship_with_her_asked:
            $ scarlett_questions_anders_relationship_with_her_asked = True
            p "What was your relationship with Scarlett?"
            andr "Our relationship was absolutely professional, Detective."
        "I hear she was often meeting with you?"if not scarlett_questions_often_meeting_with_anders_asked:
            $ scarlett_questions_often_meeting_with_anders_asked = True
            p "I hear she was often meeting with you?"
            andr "Yes, because she was having problems in my Biology class. She was behind the other students. So I was giving her a helping hand."
            p "(Yeah... literally.)"
        "When did you last see her?"if not scarlett_questions_when_anders_saw_her_last_asked:
            $ scarlett_questions_when_anders_saw_her_last_asked = True
            p "When did you last see her?"
            andr "The last time we met here, as always: on wednesdays at six o’clock."
            p "So you are the last person to have seen her?"
            andr "Probably, yes."
        "What is your relationship with Ivana Zelnikova?"if not scarlett_questions_anders_relationship_with_ivana_asked:
            $ scarlett_questions_anders_relationship_with_ivana_asked = True
            p "What is your relationship with Ivana Zelnikova?"
            andr "Eeh... She is just one of my students. We have no special relationship."
        "Can you tell me anything that could help me?"if not scarlett_questions_ask_anders_if_anything_else_asked:
            $ scarlett_questions_ask_anders_if_anything_else_asked = True
            p "Can you tell me anything that could help me?"
            andr "Maybe. Scarlett seemed a little nervous the last time. And she was talking about some guy that was going to take her to Europe. That's all."
            p "(You son of a bitch! Trying to send me on a wild goose chase!)"
            p "Great. Thank you... Mr. Anders."
            andr "No problem. Anytime. I’m here to help."

    jump scene_anders_office_ask_scarlet_questions

label city_map_cop_need_to_talk_to_Ivana_in_her_apartment_first:
    scene city_map
    p "School already ended. I must visit Ivana at her home."
    $ time_of_day = Set_Time_of_Day('ÖĞLEN')
    $ hints_counter += 1
    $ ivana_apartment_available = True
    jump city_map


label scene_ivanas_apartment_first_time:
    scene policeman_s12_visit_ivana00
    iva "Hello, what do you need?"
    p "Hello, I’m Detective John Matrix from the local police department. I have a few questions for you about Scarlett Sage."
    scene policeman_s12_visit_ivana01
    iva "Ooh... Of course, Detective. I’m happy to see somebody is still working on that case. Please, come in."
    scene policeman_visit_ivana_flashback00
    play sound "sounds/effects/whoosh_sound2.ogg"
    p "(Looks like girls gone wild.)"
    scene policeman_visit_ivana_flashback01
    play sound "sounds/effects/whoosh_sound.ogg"
    p "(Again, Scarlett with Anders.)"
    scene policeman_visit_ivana_flashback02
    play sound "sounds/effects/whoosh_sound2.ogg"
    p "(Looks like she’s talking to someone who’s standing in the shadows. She had that exact outfit on when she went missing. Same one as in Anders’ office.)"
    scene policeman_s12_visit_ivana01
    iva "Come in, Detective, and take a seat."
    scene policeman_s12_visit_ivana02
    iva "DO you want some coffee or something?"
    p "No, thank you. I just have a few questions."
    scene policeman_s12_visit_ivana03
    iva "Okay, Detective. I’m ready."

label scene_ivanas_apartment_scarlett_questions:
    scene policeman_s12_visit_ivana03
    menu:
        "What is your relationship with Scarlett?"if not scarlett_questions_ivana_relationship_with_her_asked:
            iva "We are just friend and roommates. She was a fine girl - a little different than others, but a great friend."
            $ scarlett_questions_ivana_relationship_with_her_asked = True
        "You are Russian, right?"if not scarlett_questions_is_ivana_russian_asked:
            iva "Hmm, no actually. I’m from the Czech Republic, but you guys call us all Russians anyway."
            $ scarlett_questions_is_ivana_russian_asked = True
        "What about Mr. Anders?"if not scarlett_questions_ivana_about_anders_asked:
            scene policeman_s12_visit_ivana04
            iva "What about him?"
            p "Did Scarlett have any relationship with him?"
            iva "Yes, she was his student, same as me, during Biology classes."
            p "And?"
            iva "And she also went, every wednesday, to his office for Biology tutoring, because she was a little behind in class."
            p "And they didn’t have any special or... romantic relationship?"
            iva "I don’t think so."
            p "And you?"
            scene policeman_s12_visit_ivana05
            iva "Me!? With Anders? No!"
            $ scarlett_questions_ivana_about_anders_asked = True
        "When was the last time you saw Scarlett."if not scarlett_questions_ivana_last_time_saw_her_asked:
            scene policeman_s12_visit_ivana04
            iva "Last time I saw her was the night she went missing. She was talking with a tall guy hidden in the shadows. I don’t know who that guy was. He was barely visible in that light."
            p "Is it possible that this guy could be Mr. Anders?"
            scene policeman_s12_visit_ivana05
            iva "I really don’t know. As I said, I barely just saw a silhouette. And I hope that it is not Mr. Anders, because he is a really good teacher."
            $ scarlett_questions_ivana_last_time_saw_her_asked = True

    if scarlett_questions_ivana_relationship_with_her_asked and scarlett_questions_is_ivana_russian_asked and scarlett_questions_ivana_about_anders_asked and scarlett_questions_ivana_last_time_saw_her_asked:
        p "Fine. That was my last question."
        scene policeman_s12_visit_ivana00
        p "Thank you for your time and your assistance, Ivana."
        iva "My pleasure, Detective. I wish you good luck."
        p "(For today, I’ve had enough of all these interrogations. Time to go to the apartment and relax.)"
        $ time_of_day = Set_Time_of_Day('AKŞAM')
        $ cop_can_hear_muffled_voice = True
        $ been_to_ivanas_apartment_first_time = True
        $ hints_counter += 1
        jump city_map
    else:
        jump scene_ivanas_apartment_scarlett_questions

label scene_cops_apartment_hallway_can_hear_muffled_voice:
    scene black_screen
    p "(Nearly back at the apartment. Huh? What was that?)"
    scene policeman_s10_apartment_hall
    p "(Huh? I could have sworn I heard some kind of muffled voice coming from behind one of these doors.)"
    p "(Hmm, the door is unlocked. Let's check it out.)"
    scene policeman_s10_trapped_girl00
    p "(I’ve never seen anything like this.)"
    scene policeman_s10_trapped_girl01
    p "(Fair enough, seeing as it’s a woman in trouble.)"
    p "Hello?"
    scene policeman_s10_trapped_girl02
    trpd "Yes, finally. Is that you, Dylan?"
    p "No, sorry, I’m not Dylan."
    trpd "So who are you?"
    p "I was just walking by, and heard you calling for help."
    trpd "Oh God, you are awesome. I got trapped here. My hair is caught in the food disposal. I’ve been stuck here for a really long time."
    p "Nobody else home?"
    trpd "No. My husband comes home from work at 7 and the kids are with their grandparents."
    p "It’s 6:30 now."
    scene policeman_s10_trapped_girl03
    stop music fadeout 1.0
    play music "sounds/music/Background_music_Funk_Game_Loop.ogg" fadein 3.0
    p "Fine. If I’m going to help you, I need you to put your right leg up here on that bench. Because I need to have room to reach whatever is trapping your hair, under the sink."
    trpd "Yes, okay."
    scene policeman_s10_trapped_girl04
    p "Great."
    scene policeman_s10_trapped_girl05
    p "From here, I’ll have better access and view of it."
    scene policeman_s10_trapped_girl06
    trpd "Oh nooo! I forgot to..."
    scene policeman_s10_trapped_girl07
    p "Damn, such a nice one."
    menu:
        p "What should I do?"
        "Help her.":
            $ reputation_number += 1
            $ helped_trapped_girl = True
            $ ready_for_cop_angel_night_scene = True
            p "But I have more important work to do."
            scene policeman_s10_trapped_girl_help00
            trpd "Ohh, that hurts!"
            p "Just a second, lady... One more second..."
            p "Aaaand... voilaaa..."
            scene policeman_s10_trapped_girl_help01
            trpd "Aah, finally. I thought it would take forever. You've helped me a lot."
            scene policeman_s10_trapped_girl_help02
            p "W-Wow..! What about your husband?"
            trpd "My husband is just an alcoholic. I owe you one. Unfortunately, right now, we don’t have enough time. But I will not forget your help. What number is your apartment?"
            p "123..."
            trpd "Great! When I have some free time I will come to you."
            p "Cool. See you later."
            $ ready_for_cop_angel_night_scene = True
        "Have a little fun after a tough day.":
            $ reputation_number -= 2
            scene policeman_s10_trapped_girl08
            $ renpy.pause(2.0, hard=True)
            scene policeman_s10_trapped_girl09
            $ renpy.pause(2.0, hard=True)
            scene policeman_s10_trapped_girl06
            trpd "Hey! Stop! STOP!"
            scene policeman_s10_trapped_girl10
            a "What the hell are you doing?!"
            scene policeman_s10_trapped_girl14
            p "Oh. Hi, Angel."
            a "Don’t you hi Angel me! WHAT do you think you're doing!?"
            scene policeman_s10_trapped_girl15
            p "What? Just having a little fun."
            scene policeman_s10_trapped_girl16
            a "She has a husband and children. She's in a bad situation already, and you are doing this?"
            scene policeman_s10_trapped_girl12
            p "You know what I have here for you?"
            scene policeman_s10_trapped_girl11
            p "It's my time. And I will do whatever I want, so fuck off!"
            scene policeman_s10_trapped_girl13
            a "Blah! Do as you like, you little pervert!"
            scene policeman_s10_trapped_girl14
            p "BYE! I have better things to do."
            scene policeman_s10_trapped_girl06
            trpd "You fucking bastard! When my husband comes home, he'll beat the shit out of you, you fucking prick! You'll see!"
            p "I think you are talking too much and too loud. I have a great idea."
            scene policeman_s10_trapped_girl17
            $ renpy.pause()
            p "Much better. And you will get some vitamins as a bonus - Now that is what I call healthy. Hah!"
            trpd "Hmmm mmm!!!"
            scene policeman_s10_trapped_girl03
            p "Time for your punishment for those nasty words. So, the mother of little kids saying stuff like that? That is unacceptable!"
            scene policeman_s10_trapped_girl_anim
            $ renpy.movie_cutscene("scenes/Policeman/10_trapped_girl/webm/policeman_s10_slapcam1.webm", loops=2,delay=-1, stop_music=False)
            $ renpy.movie_cutscene("scenes/Policeman/10_trapped_girl/webm/policeman_s10_slapcam2.webm", loops=1,delay=-1, stop_music=False)
            scene policeman_s10_trapped_girl19
            p "Hmmm? You’re starting to like that, aren’t you? Your pussy's going to be nicely wet. You pervert mom, I think your pussy needs something inside."
            scene policeman_s10_trapped_girl18
            $ renpy.pause(2.0, hard=True)
            scene policeman_s10_trapped_girl_anim2
            $ renpy.movie_cutscene("scenes/Policeman/10_trapped_girl/webm/policeman_s10_bananacam1.webm", loops=2,delay=-1, stop_music=False)
            $ renpy.movie_cutscene("scenes/Policeman/10_trapped_girl/webm/policeman_s10_bananacam2.webm", loops=2,delay=-1, stop_music=False)
            scene policeman_s10_trapped_girl20
            p "Awesome! But our time together is coming to an end. So we must say goodbye."
            scene policeman_s10_trapped_girl22
            p "This will come in handy."
            scene policeman_s10_trapped_girl21
            p "There, now you have a knife near your left arm. Cut your hair and free yourself. Bye! Good luck!"
            trpd "Hmm mmmm!!!"
    scene policeman_main
    $ cop_can_hear_muffled_voice = False
    #$ ready_for_cop_asian_night_scene = False
    $ cop_ready_to_request_pills_from_megan = True
    $ time_of_day = Set_Time_of_Day('AKŞAM')
    $ hints_counter += 1
    p "Aaah... today was really tough. I’m sleepy as fuck."
    jump cop_apartment_main

label scene_angel_visits_cop_at_night:
    scene policeman_s09_angel_sleep00
    p "Aaargh! Is there a reason why you’re here… right now?"
    stop music fadeout 1.0
    play music "sounds/music/Background_music2_Brunno.ogg" fadein 3.0
    scene policeman_s09_angel_sleep01
    a "What, you're not happy to see me?"
    scene policeman_s09_angel_sleep00
    p "Actually, I’m really not sure... Why are you here? Came to give me another lecture?"
    scene policeman_s09_angel_sleep01
    a "Not really. I’m here to say, you did the right thing with that woman. I wasn’t expecting that, but it made a good impression on me."
    scene policeman_s09_angel_sleep02
    p "Great... You have nice clothes on today."
    a "Yeah? Thank you. You are so kind today. I almost didn't recognize you. I was ready to call it a day, but you surprised me so much with your act, that I decided to visit you."
    p "Great! So maybe I can get some reward. What do you think?"
    a "A reward? Maybe? What do you have in mind?"
    p "We can start with a blowjob, I think."
    scene policeman_s09_angel_sleep03
    a "Blow… WHAT?! NEVER! You are the still the same freak! You're only thinking about one thing. Harsch…."
    a "BYE!"
    scene policeman_s09_angel_sleep00
    p "Pff..! Still the same: Uptight."
    scene black_screen with fade
    stop music fadeout 2.0
    jump city_map_cop_ready_to_find_something_on_anders


label city_map_cop_ready_to_find_something_on_anders:
    scene black_screen
    scene city_map with fade
    $ time_of_day = Set_Time_of_Day('SABAH')
    $ hints_counter += 1
    p "Alright, school is already open. Today I need to find something on that bastard Anders. But first I need to visit Megan in her laboratory."
    jump city_map

label scene_cop_requesting_pills_from_megan:
    scene policeman_14_asking_pills00
    p "Hello, Megan."
    meg "Hello, Detective."
    p "So did Nick visit you?"
    scene policeman_14_asking_pills01
    meg "Yes. He was here just a moment ago. It seems it was a good decision to tell you about him."
    p "(I don’t think I will tell her the truth about Nick.)"
    p "That’s no problem. So you can make new pills now?"
    meg "Yes. I already started work on them. They will be ready this evening."
    p "That’s great. I have just one request: Please don't give them to anyone else yet. Tell the Dean and anyone else, development of these pills needs more time."
    meg "Sure, Detective... May I know why?"
    p "It's part of a case I’m working on. And it's top secret, of course."
    meg "Of course. So as I said, come in the evening, and the pills will be ready just for you."
    p "Great. You are the best, Megan. Bye."
    meg "Thank you, Detective. See you later."
    $ ready_to_sneak_into_anders_office_stage = 1
    $ cop_ready_to_request_pills_from_megan = False
    scene school_map
    p "I need to sneak into Anders' office. But first I should find out where he is. I need to check the classrooms."
    $ hints_counter += 1
    jump school

label anders_office_open_door:
    scene policeman_s11_anders_visit00
    p "His office was not locked. The door was just closed and stuck a bit. This was no problem, just took a little skill and force."
    scene black_screen with fade
    scene anders_office_main with fade
    p "Hmmm. I must search his office carefully."
    $ hints_counter += 1
    jump anders_office

label scene_cop_runs_into_anders_in_main_hall:
    scene leaving_office_meet_anders
    andr "Hello, Detective. How’s your case going? Were you looking for me?"
    p "(Of course I’m looking for you. To take you into jail, you freak!)"
    p "No, I was just visiting the Dean with a few more questions. And the case is going pretty well I think. In the near future, I will put that criminal in jail and hope Scarlett is still alive somewhere."
    andr "That is great news, Detective. I wish you the best of luck."
    p "Thanks... (That bastard has no shame.)"
    $ looking_for_ivana_in_school_after_searching_anders_office = True
    $ ready_to_sneak_into_anders_office_stage = 0
    $ classes_have_started = False
    $ hints_counter += 1
    jump school

label scene_looking_for_ivana_found_bethany:
    scene policeman_s16_bethany01
    p "Hello. Can you please tell me where I can find Ivana?"
    beth "Hi. Ivana already went home. Classes have ended."
    p "Ok, so I will visit her at home. You are Bethany, right?"
    beth "Yes. Who are you?"
    p "That's not so important."
    beth "Ah..."
    p "I have a question for you. Have you tried out those miracle growing pills?"
    beth "Eeemh... No. What'ya mean, growing pills?"
    p "(She’s playing me well.)"
    p "I mean, I will have a package of those pills, and maybe you would like to try them with me?"
    scene policeman_s16_bethany02
    beth "Hah?! What do you think I am? You see a pretty girl and think she will jump on your cock and give you the ride of your life? pfff..."
    p "Aaa..."
    scene policeman_s16_bethany03
    beth "Do you want anything else from me? I think not. Bye."
    $ looking_for_ivana_in_school_after_searching_anders_office = False
    jump beth_said_ivana_went_home

label beth_said_ivana_went_home:
    scene city_map
    $ time_of_day = Set_Time_of_Day('ÖĞLEN')
    $ hints_counter += 1
    p "Damn, she was pretty toxic. Hah! I will show her what opportunity she missed. What if another girl in school were to get these pills instead of her? Haha!"
    p "She would beg for them. But first I need to solve this case and talk with Ivana at her apartment."
    jump city_map

label scene_cop_makes_entrapment_deal_with_ivana:
    scene policeman_s17_helping_ivana00
    p "I have found some information about you in Anders’ office. I think you could possibly be his next victim."
    iva "What!? What next victim!? Did Anders do something to someone?"
    p "Just take a look."
    scene policeman_s17_helping_ivana01
    iva "Oh God. How could he get these? He must have been stalking me for a long time!"
    p "Yes, and that is why I think you could be in danger. But I think we can use you as bait, and get him."
    scene policeman_s17_helping_ivana02
    iva "That bastard! I will do everything I can to get him!"
    p "Great. Call him and invite him here, to your house. Dress in something a little more sexy. And we will wait for his move."
    iva "Okay."
    scene policeman_s17_helping_ivana03
    iva "Hello, Mr Anders. I must say, I’m a little lost with the new Biology chapter. And I think I will need your help."
    andr "Hello, Ivana. Sure, we can book a session after school tomorrow. What do you think?"
    iva "But don’t you have time today, at seven,  my home? I really need it."
    andr "Eehm Okay... Pff... Why not. So, at seven?"
    iva "Thank you, Professor."
    scene policeman_s17_helping_ivana00
    iva "He will be here in two hours."
    p "Good. I’m going to sort out a few things and we'll meet back here, just before seven."
    iva "Great."

    $ made_entrapment_deal_with_ivana = True
    $ cop_ready_to_collect_pills_from_megan = True
    $ hints_counter += 1
    jump city_map_cop_need_to_find_cops_gun

label city_map_cop_need_to_find_cops_gun:
    scene city_map
    p "I need to get the cop’s gun, just to be sure. I left it at his apartment. And that's right, I need to see Megan and get those pills today."
    $ need_cops_gun = True
    jump city_map

label finding_cops_gun:
    scene policeman_s17_gun
    p "Now this will come in handy."
    scene policeman_s17_getting_gun
    p "You talkin' to me? Are you talkin' to me?!"
    python:
        gun = Item("Gun", element="PuzzleItem17", image="gun_inventory", cost=0)#TEMP
    $ inventory.add(gun)
    scene black_screen with fade
    jump cop_apartment_main

label scene_sting_operation_at_ivanas:
    scene policeman_s17_helping_ivana12
    p "Pretty clothes. I think he will be here any moment now. I will hide in this room. Act naturally and just try to get information from him or seduce him a little. And the moment he tries anything with you, we will have him."
    iva "Fine."
    scene policeman_s17_helping_ivana04
    iva "Hello, Professor. Take a seat. Want some coffee or can I make something for you?"
    andr "No. No, thank you, Ivana."
    scene policeman_s17_helping_ivana05
    andr "So, what part of today’s lesson is problematic for you?"
    iva "Actually, that part about reproduction. The general stuff is okay, of course, but the complex parts of this process are not too clear for me."
    andr "Oooh. Okay. Well,  I brought here some study materials. So I can show it to you with some examples."
    iva "Great! I think an example is the best way to teach something. Hih."
    scene policeman_s17_helping_ivana07
    p "(Damn, if I was him I would already be fucking her, here, from behind, bent over that table. That guy has some fucking self-control.)"
    scene policeman_s17_helping_ivana05
    andr "You see, it's like a chain reaction. One action after another. The female body reacts immediately with each change."
    iva "That's really interesting. I think I’m slowly getting it."
    scene policeman_s17_helping_ivana07
    p "(He's still absolutely calm. Fine. It’s not going to work this way. So let’s try this the hard way!)"
    scene policeman_s17_helping_ivana06
    stop music fadeout 1.0
    play music "sounds/music/Background_music.ogg" fadein 3.0
    p "Put your hands up!"
    andr "God!! What..? What is this?"
    p "It’s over, you freak! I know you killed Scarlett and Ivana is your next planned victim."
    scene policeman_s17_helping_ivana08
    andr "No! That's not true! Is this part of some stupid fucking game?"
    p "No it isn’t. Many students saw you hanging out with Scarlett after school and in school, just days before she disappeared. And I know you choked her in your office!"
    p "And now I have proof that your next victim is Ivana. I saw all that stuff you have on the flash drive in your office."
    scene policeman_s17_helping_ivana11
    andr "Aaah. You think you are a smart one, right?"
    andr "Now listen!"
    andr "I have not killed Scarlett. And I don’t know where she is. The truth is: I’m really, in love with Ivana. That is the truth. But I’m her professor, and any relationship between teachers and students is forbidden in our school."
    andr "And then along comes Scarlett. She wanted to earn money for some trip to Europe. And saw how I was watching Ivana during all those hours in school. She confronted me one day and offered me Ivana’s photos for some money."
    andr "I bought those photos from her. And after some time, again and again. She started stalking her roommate and selling me all that stuff: photos, videos, her diary."
    andr "I know that it was wrong, but I could not resist. But after a while, Scarlett starting demanding more and more money. Once I decided to stop with the deal, she came in and threatened me: That is the end of me."
    andr "That she would go tell the Dean of the school and, of course, her roomate Ivana."
    p "And in that moment you choked her to death in your office!"
    scene policeman_s17_helping_ivana08
    andr "NO!"
    andr "I was mad. And yes, I choked her. But I did not kill her. I calmed down and told her to leave my office. And that I never wanted to talk to her again. I resigned myself to the truth: that if she were to tell someone, I was done."
    andr "Before she left, she just started yelling at me, that she knew someone who'd get me back for what I did."
    scene policeman_s17_helping_ivana11
    p "That is an interesting story, but I think you’re lying to us here."
    scene policeman_s17_helping_ivana09
    andr "Take a look at my phone. I have messages from her, from that day."
    scene policeman_s17_helping_ivana10
    iva "Looks like he is right. Phone number really belongs to Scarlett."
    scrlt "You fuckin’ freak. I will show you. You think you can beat me up, just like that? My guy will make short work of you! After he beats all the money out of you, I will be the one smiling, right in your face!"

label scene_sting_operation_at_ivanas_after_sms:
    iva "That was the last day I saw her. That day she was wearing that jacket all day. I think she was trying to hide those bruises on her neck, from him. At the end of the day, I saw her talking with some guy standing in the shadows."
    p "(DAMN! Maybe he really is innocent.)"
    scene policeman_s17_helping_ivana11
    andr "Look, I’ve done some bad things and I failed as a professor, but I’m not a murderer."
    p "(He has done a bad thing, but not relevant to my case. I’m not here investigating student and teacher relationships.)"
    p "Aaaaah. Okay. Go away."
    scene policeman_s17_helping_ivana12
    p "I’m sorry, Ivana. He did do some bad things, especially to you, but it's not enough to arrest him."
    iva "It’s okay. It was a little bit my fault too. I was teasing him many times in school. Never thought it could be so dangerous."
    p "I must find more clues about this guy standing in the shadows, you mentioned. See you later, Ivana."
    iva "Bye, Detective."
    $ time_of_day = Set_Time_of_Day('GECE')
    scene policeman_visit_ivana_flashback02
    p "I will find you."
    stop music fadeout 1.0
    #play music "sounds/music/Menu_intro_music.ogg" fadein 3.0
    #scene outro
    #$ renpy.pause(15.0, hard=True)
    #$ renpy.quit()
    #TODO put end of version stuff here

    #jump city_map

    $ need_cops_gun = False
    $ hints_counter = 42#+= 1 #MAGIC
    $ done_anders_sting_operation_at_ivanas = True
    scene city_map_night

    jump city_map

    #jump scene_cop_in_apartment_angry


label scene_cop_collecting_pills_from_megan:
    scene policeman_s18_getting_pills01
    p "Hello, Megan. Do you have those pills ready for me?"
    meg "Sure, Detective."
    scene policeman_s18_getting_pills02
    meg "Here you go."
    p "Great! And please give me your phone number. Also, is there anything I need to know about them?"
    scene policeman_s18_getting_pills03
    meg "Yes. Do not combine them with other medicine or alcohol. It can be dangerous."
    p "Great, Megan. You did an excellent job. And don’t forget: don't be giving them to anybody else. It's important to my case."
    meg "As you wish, Detective."
    scene policeman_s18_getting_pills04
    p "(The true fun can start now!)"
    $ cop_ready_to_collect_pills_from_megan = False
    $ inventory.add(pills)
    jump city_map


label scene_cop_in_apartment_angry:

    scene policeman_s17_gun with fade
    p "Back in the drawer you go."
    $ inventory.drop(gun)
    $ need_cops_gun = False
    scene policeman_s19_angry_cop00
    p "All of that time spent was for nothing! I’m just fucking useless!"
    scene policeman_s19_angry_cop01
    p "What the hell is this thing?! Damn! I need to blow some steam."
    scene policeman_s19_angry_cop02
    p "Aarrgh!!"
    scene policeman_s19_angry_cop03
    play sound 'sounds/effects/drop_sound.ogg'
    $ renpy.pause(0.5, hard=True)
    stop sound
    p "FUuuuck..!! This fucking thing won’t even break! Aaarr!!"
    play sound "sounds/effects/sms_sound.ogg"
    $ renpy.pause(1.0, hard=True)
    scene policeman_s19_angry_cop04
    p "Who the hell is sending me an SMS right now?"
    bran "Hi, I want to say sorry that I didn’t make the deal within those three days, as promised. But I have the money on me now, so can we meet tomorrow at the usual spot?"
    scene policeman_s19_angry_cop01
    p "And just my luck, I still don’t even know where all these drugs are hidden! FUCK!"
    scene policeman_s19_angry_cop06
    d "Hello? You look a little annoyed."
    scene policeman_s19_angry_cop05
    p "Really?! Are you here to \“help\” me again?!"
    scene policeman_s19_angry_cop06
    d "Sure, if you want my help? But you know the rules."
    scene policeman_s19_angry_cop09
    p "Yes I know them, and don’t want to kill someone or anything like that. So please, GET lost!"
    scene policeman_s19_angry_cop08
    d "Why are you being so rude to me? That was not my fault. Everything was your decision, not mine!"
    scene policeman_s19_angry_cop07
    d "Maybe you will do better without me..."
    scene policeman_s19_angry_cop09
    p "Great..! Now I’ve offended her."
    scene policeman_s19_angry_cop10
    p "Fuck this day, and this cop work, and this fucking one month!!!"
    scene policeman_s19_angry_cop11
    play sound 'sounds/effects/hitting_wood_sound.ogg'
    $ renpy.pause(0.5, hard=True)
    stop sound
    p "Hmm… After that hard hit, something fell down, under that cabinet. Looks like a secret compartment."
    scene policeman_s19_angry_cop13
    p "Heh… What luck. Sometimes anger is a good thing."
    p "Fine. Now I have the drugs. But still, is it okay to sell these drugs to students? It could be a good way to make a larger amount of money that I could use to enjoy myself during the rest of the month. But, on the other hand, it's really wrong to do that."
    $ hints_counter += 1
    menu:
        "What should I do?"
        "Sell drugs to Brandon.":
            jump option_sell_drugs_to_brandon
        "Don't sell drugs.":
            jump option_dont_sell_drugs_to_brandon

label option_sell_drugs_to_brandon:
    $ chose_to_sell_drugs_to_brandon = True
    $ reputation_number -= 1
    scene policeman_s19_angry_cop12
    p "Hey, Brandon. I’m really happy that you got that money together and things don’t need to get rough, if you know what I mean."
    bran "Yes! Sorry for being one day late. I will compensate you somehow."
    p "Fine. So tomorrow at 8 at the warehouse."
    bran "I will be there on time."
    p "Great."
    jump made_drug_selling_decision_time_for_bed

label option_dont_sell_drugs_to_brandon:
    scene policeman_s19_angry_cop12
    p "Hey Brandon, I’ve made a decision to not sell you these drugs."
    bran "But? Why? Is it this one day late issue? I will compensate you, like I said."
    p "Look: I just don’t work with unreliable people."
    bran "But please, that was just that last case. Please give me just one last chance."

    menu:
        "Last chance? Should I sell?"
        "Yes":
            $ reputation_number -= 1
            $ chose_to_sell_drugs_to_brandon = True
            p "You're lucky I'm in a good mood. But this is your last chance."
            p "Be there tomorrow at the warehouse at 8. And don't be late."
            pass
        "No":
            $ reputation_number += 1
            p "My final word. No."
            bran "... Fine... And what now? Will you kill me?"
            p "You've been watching too many movies, kid. I'm not Don Pablo. You may be of use in the future. I'll stay in touch. Bye!"
            pass
    jump made_drug_selling_decision_time_for_bed

label made_drug_selling_decision_time_for_bed:
    scene policeman_s19_angry_cop04
    $ cop_ready_for_night_sophia_dream = True
    #$ time_of_day = Set_Time_of_Day('GECE')
    p "Uhmmm... I’m tired. Better to go to bed."
    jump cop_apartment_main


label scene_cop_sophia_dream:
    scene policeman_bedroom_panties
    scene black_screen with fade
    scene policeman_s20_dreams00
    p "(Hmmmm....)"
    scene policeman_s20_dreams04
    p "(What is that?)"
    scene policeman_s20_dreams01
    p "(Wait a second. I didn't know about Scarlett and Sophia. Did she have some sort of romantic relationship with her.)"
    scene policeman_s20_dreams03
    p "ZzzzZzzz…."
    scene policeman_s20_dreams02
    play sound 'sounds/effects/Car_accident_sound.ogg'
    p "Oh! SHIT!"
    stop sound
    scene policeman_s20_dreams05
    p "NOOOO!"
    scene policeman_s20_dreams06
    p "That was a nightmare… It's already morning. Better not to do any work. I need to talk with Sophia at school."
    $ sophia_arguing_with_brandon_in_main_hall = True
    $ cop_ready_for_night_sophia_dream = False
    $ time_of_day = Set_Time_of_Day('SABAH')
    $ hints_counter += 1
    jump cop_apartment_bedroom

label scene_sophia_arguing_with_brandon_in_main_hall:
    scene policeman_s21_sophia_and_brandon00
    sop "You know what? I’m really angry with you. Do you even know how I was feeling?"
    bran "As I said, I really don’t know what you are talking about? What dinner?"
    scene policeman_s21_sophia_and_brandon01
    sop "Don’t act stupid! We both went to dinner after moving [p]’s stuff out."
    bran "I’m really sorry, but I don't remember that. I have to go now."
    scene policeman_s21_sophia_and_brandon02
    sop "Phff!"
    p "Can we have a talk?"
    sop "Who are you? I’m a little short on time."
    p "I’m Detective John Matrix. And I have a few question for you about Scarlett."
    scene policeman_s21_sophia_and_brandon03
    sop "Yes... Scarlett. What would you like to know?"
    jump scene_sophia_main_hall_scarlett_questions


label scene_sophia_main_hall_scarlett_questions:
    scene policeman_s21_sophia_and_brandon03
    menu:
        "When was the last time you saw Scarlett?" if not scarlett_questions_sophia_last_time_saw_her_asked:
            sop "I don’t know exactly, but it was about two days before she went missing."
            $ scarlett_questions_sophia_last_time_saw_her_asked = True
            pass
        "Do you and Scarlett have some kind of romantic relationship?" if not scarlett_questions_sophia_relationship_with_her_asked:
            sop "Eh? What? No! Of course not. We are just good friends."
            $ scarlett_questions_sophia_relationship_with_her_asked = True
            pass
    if scarlett_questions_sophia_last_time_saw_her_asked and scarlett_questions_sophia_relationship_with_her_asked:
        scene policeman_s21_sophia_and_brandon04
        sop "Look, Detective, I have to go to class now, but how about you visit me later today at this address?"
        p "Sure."
        scene school_map
        p "Better to check on Anders again."
        $ sophia_arguing_with_brandon_in_main_hall = False
        $ anders_office_trashed = True
        $ hints_counter += 1
        jump school
    else:
        jump scene_sophia_main_hall_scarlett_questions

label scene_anders_looking_for_bug_in_office:
    scene policeman_s22_anders_office0
    andr "Hello, Detective."
    p "What happened here?"
    scene policeman_s22_anders_office1
    andr "You mean this mess? Oh... yes, I was searching for a hidden camera or microphone."
    p "Why?"
    andr "Because there is no other way you could have known that Scarlett was here and that I was choking her."
    p "There are no hidden devices, I promise."
    andr "So how..?"
    p "That doesn’t matter now. Just a police secret. But I’m here because of another matter."
    scene policeman_s22_anders_office0
    andr "What is it?"
    p "First, I want to apologise for that gun. It was not necessary."
    andr "Apology accepted."
    p "And second, I want to see you delete all that stuff about Ivana now."
    andr "Fine."
    scene policeman_s22_anders_office2
    $ renpy.pause()
    scene policeman_s22_anders_office3
    $ renpy.pause()
    scene policeman_s22_anders_office4
    andr "Done. I must say, I feel better now."
    p "That's good."
    andr "Just one question. Did you say anything about this to the Dean of the school?"
    p "No, that is not my style, and also it's my part of my apology for that gun."
    andr "I’m really thankful for that."
    p "It's fine. Bye now."
    scene black_screen with fade
    scene city_map
    p "School is finished for the day. Sophia wanted me to come over to my old apartment to ask some more questions. I should do that."
    $ time_of_day = Set_Time_of_Day('ÖĞLEN')
    $ sophia_waiting_for_cop_in_her_apartment = True
    $ anders_office_trashed = False
    $ hints_counter += 1
    jump city_map

label scene_cop_questions_sophia_in_apartment_about_scarlett:
    scene policeman_s23_sophia_visit00
    play sound "sounds/effects/doorbell_sound.ogg"
    $ renpy.pause(3.0, hard=True)
    stop sound
    play sound "sounds/effects/door_open_sound.ogg"
    $ renpy.pause(1.0, hard=True)
    stop sound
    scene policeman_s23_sophia_visit01
    sop "Hello, Detective. Come in."
    scene policeman_s23_sophia_visit02
    sop "I was in a little bit of a hurry at school. I believe you had more questions for me."
    p "That’s right."
    scene policeman_s23_sophia_visit03
    sop "Fine. What do you want to know?"

label scene_sophias_apartment_ask_scarlet_questions:
    scene policeman_s23_sophia_visit03
    menu:
        "Ask about the arrangement between Anders and Scarlett." if not scarlett_questions_sophia_apartment_scarlett_anders_arangement_asked:
            p "Do you know about the arrangement between Anders and Scarlett?"
            sop "Yes, she told me about that."
            p "So you know about his relationship with Ivana too?"
            sop "What I know is that Scarlett was really jealous of Ivana. Because Anders was interested in her, and I think he is in love with her."
            p "Anything else?"
            sop "No, that's all."
            $ scarlett_questions_sophia_apartment_scarlett_anders_arangement_asked = True
            pass
        "You lied about your relationship with Scarlett." if not scarlett_questions_sophia_apartment_relationship_with_her_asked:
            scene policeman_s23_sophia_visit10
            p "You told me that you and Scarlett were just friends, but I know from another source, that this is not true."
            sop "Eeeeh... Fiiine..! Okay, I’m into girls too. And Scarlett was one of the girls here at school that liked to experiment. And she REALLY liked it."
            p "Fine, but what is your relationship with Brandon if you are into..."
            sop "Detective, I think that is not important for your case, and I don’t want to talk about this anymore."
            p "Okay."
            $ scarlett_questions_sophia_apartment_relationship_with_her_asked = True
            pass
        "Ask about Scarlett's diary." if not scarlett_questions_sophia_apartment_about_diary_asked:
            p "Do you know about any diary? I mean, did Scarlett have a diary or something like that?"
            sop "Eeehm... I don’t think so. But it would be better to have a talk with Ivana about that. She was her roommate."
            $ scarlett_questions_sophia_apartment_about_diary_asked = True
            pass

    if scarlett_questions_sophia_apartment_scarlett_anders_arangement_asked and scarlett_questions_sophia_apartment_relationship_with_her_asked and scarlett_questions_sophia_apartment_about_diary_asked:
        jump scene_cop_offers_sophia_pills
    else:
        jump scene_sophias_apartment_ask_scarlet_questions

label scene_cop_offers_sophia_pills:
    scene policeman_s23_sophia_visit03
    p "Okay. That is all that I want to know for now. But I have to talk to you about another, more private matter."
    sop "Sure. What do you need, Detective?"
    p "Please call me John from now on."
    scene policeman_s23_sophia_visit04
    p "You know, you are a really pretty girl. But I know that you are a little jealous of Bethany. What if I could offer you some special pills?"
    sop "What kind of pills are those?"
    p "They are some new pills developed by a really talented scientist. And by using them, your boobs can grow larger, as well as maybe, some other parts."
    scene policeman_s23_sophia_visit05
    sop "That sounds a little stupid."
    p "Yes, I know. But you can try them and you will see for yourself."
    sop "But, is it safe?"
    p "Yes, of course!"
    scene policeman_s23_sophia_visit06
    sop "Fine, I will try one."
    scene policeman_s23_sophia_visit05
    sop "Tastes like candy. How long 'till it starts working?"
    p "It might be almost instant."
    scene black_screen
    "After 20 minutes..."
    scene policeman_s23_sophia_visit10
    sop "Hmm, looks like your pills are not working, John?"
    p "Strange... Here, try one more."
    scene policeman_s23_sophia_visit07
    sop "Hope this one will do better than the first one."
    scene policeman_s23_sophia_visit08
    sop "Ehm... I’m starting to feel a little dizzy and there’s some heat."
    p "That means it’s starting to work."
    scene black_screen
    "After another 20 minutes..."
    scene policeman_s23_sophia_visit08
    p "I don’t know what happened. It's not working."
    scene policeman_s23_sophia_visit09
    sop "Looks like you just want to make a fool out of me, right? Is this some joke of Bethany's? I think it would be better for you to leave now."
    p "Fine. Anyway, thank you for your help in the Scarlett case."
    $ drug_sell_choice_consequence_time = True
    $ sophia_waiting_for_cop_in_her_apartment = False
    $ time_of_day = Set_Time_of_Day('AKŞAM')
    if chose_to_sell_drugs_to_brandon: #MAGIC
        $ hints_counter = 50
    else:
        $ hints_counter = 47
    scene city_map
    p "Nothing else to do. I should go back to the cop's apartment."
    jump city_map

label idle_cop_apartment_drug_sale_reminder:
    scene policeman_main
    p "That's right. I need to meet idiot Brandon at the warehouse tonight, to sell him drugs. I should grab them and go."
    python:
        drugs = Item("Drugs", element="PuzzleItem20", image="drugs_inventory", cost=0)
    jump cop_apartment_main

label idle_cop_apartment_tired_after_bikini_competition:
    scene policeman_main
    p "After today, I have both girls in my lap. A threesome with them sounds good to me. Haha. Let’s go to bed."
    jump cop_apartment_main

label scene_cop_get_drugs_and_gun_for_deal:
    scene policeman_taking_gun_red
    p "Better grab the gun too. You never know."
    scene policeman_taking_drugs_red
    p "Now I’m ready for my first drug deal ever."
    $ inventory.add(gun)
    $ inventory.add(drugs)
    $ need_cops_gun = True
    $ drug_sell_choice_consequence_time = False
    $ time_to_meet_brandon_at_warehouse_for_drug_sale = True
    $ time_of_day = Set_Time_of_Day('GECE')
    jump cop_apartment_main

label scene_cop_brandon_drug_sale_at_warehouse:
    $ time_to_meet_brandon_at_warehouse_for_drug_sale = False
    play music "sounds/music/police_action_music.ogg" fadein 3.0
    scene policeman_s24_drug_deal00
    p "Good. I’m glad that you're here. I was a little worried about your commitment."
    bran "No, I’m all in."
    play sound 'sounds/effects/police_siren_sound.ogg'
    $ renpy.pause(2.0, hard=True)
    scene policeman_s24_drug_deal01
    $ renpy.pause(2.0, hard=True)
    scene policeman_s24_drug_deal02
    p "Fuck! What the hell?!"
    $ renpy.pause(2.0, hard=True)
    scene policeman_s24_drug_deal03
    p "You must be kidding!"
    $ renpy.pause(2.0, hard=True)
    play sound 'sounds/effects/car_braking_sound.ogg'
    $ renpy.pause(2.0, hard=True)
    scene policeman_s24_drug_deal07
    $ renpy.pause(2.0, hard=True)
    scene policeman_s24_drug_deal08
    $ renpy.pause(2.0, hard=True)
    scene policeman_s24_drug_deal04
    $ renpy.pause(2.0, hard=True)
    scene policeman_s24_drug_deal05
    $ renpy.pause(2.0, hard=True)
    scene policeman_s24_drug_deal06
    $ renpy.pause(2.0, hard=True)
    stop sound
    scene policeman_s24_drug_deal09
    "Police" "Drop your weapons and lay on the ground! NOW!"
    scene policeman_s24_drug_deal03
    p "Fuck them!"
    scene policeman_s24_drug_deal12
    bran "Don’t shoot!"
    scene policeman_s24_drug_deal11
    p "What am I going to do now? I’m pretty much fucked now! I don’t want to spend the rest of this fucking month in the JAIL!"
    scene policeman_s24_drug_deal14
    "Voice" "I think you will! Drop that weapon! And take off that stupid mask!"
    p "(Oh shit.)"
    "Voice" "Turn around!"
    scene policeman_s24_drug_deal15
    d "Surprise!!!"
    scene policeman_s24_drug_deal16
    p "Are you kidding me?! I almost shit my pants! Jesus Christ!"
    scene policeman_s24_drug_deal15
    d "Calm down… Looks like you need a little help. So here I am."
    p "You want to shoot them down, or what?"
    d "Of course not, silly."
    scene policeman_s24_drug_deal17
    d "Fine. I will shoot them down, then."
    scene policeman_s24_drug_deal19
    d "You?! Look at you?! You wanted to act like a drug dealer, and walked here in a red shirt with skulls on it and sports shoes. You look more like some hair gel commercial than a drug dealer. These guys are S.W.A.T, not doughnut eaters."
    scene policeman_s24_drug_deal18
    d "And by the way, how do you expect to shoot them without ammunition or even a magazine? You didn’t even realise that the gun is not loaded."
    scene policeman_s24_drug_deal20
    p "Fine! What do you want?"
    scene policeman_s24_drug_deal19
    d "Glad you asked."
    p "So..?"
    d "Anders' soul."
    p "No! Not again!"
    d "Hey, calm down. What I want is just for you to tell the Dean about what Anders did to Ivana. That's all. Just this one thing. Take the report about that case and give it to the Dean."
    p "And if I refuse?"
    d "Then you will probably die here."
    p "I’m already dead."
    d "Yeah. But, you kill that cop and your soul will go to the place described in our deal."
    p "Ah, great... I don’t want to know any more."
    scene policeman_s24_drug_deal15
    menu:
        d "So now what do you have to say to me?"
        "Accept her offer.":
            jump scene_cop_accepted_devils_offer_for_anders_soul
        "Refuse her offer.":
            jump scene_cop_refused_offer_for_anders_soul

label scene_cop_accepted_devils_offer_for_anders_soul:
    scene policeman_s24_drug_deal15
    d "I’m really happy with your decision."
    p "So how do you want me to do this?"
    scene policeman_s24_drug_deal31
    d "Just escape using this sewer and leave the rest to me. I will play with them a little and keep them occupied."
    scene policeman_s24_drug_deal16
    p "S-S-Se..? Sewer? What?!"
    d "What? Afraid you will ruin your hair? You can still die here, if you want?"
    scene policeman_s24_drug_deal20
    p "Phft..! Fine! I’m on my way."
    scene policeman_s24_drug_deal15
    d "Great! Now, time to have some fun!"
    play sound 'sounds/effects/assault_rifle_sound.ogg'
    scene policeman_s24_drug_deal32
    $ renpy.pause(2.0, hard=True)
    stop sound
    play sound 'sounds/effects/assault_rifle_sound.ogg'
    $ renpy.movie_cutscene("scenes/Policeman/24_drug_car_chase/webm/Devil_shooting_cam1.webm", stop_music=False)
    stop sound
    play sound 'sounds/effects/assault_rifle_sound.ogg'
    scene policeman_s24_drug_deal10
    $ renpy.pause(2.0)
    $ renpy.movie_cutscene("scenes/Policeman/24_drug_car_chase/webm/Devil_shooting_cam2.webm", stop_music=False)
    scene black_screen with fade


    stop sound fadeout 2.0
    play music "sounds/music/intro_music2_Classical_Piano.ogg" fadein 3.0
    "After some time, back in the cop’s apartment..."
    scene policeman_stink
    p "That was a really great idea... Now I stink like a pig. I will take a shower and go straight to bed. This day really sucked."
    scene black_screen with fade
    $ accepted_devils_offer_for_anders_soul = True
    jump scene_back_at_cop_apartment_after_drug_sell_choice_consequence

label scene_cop_refused_offer_for_anders_soul:
    scene policeman_s24_drug_deal20
    p "I will not do that! I can’t! I already gave Anders my word, that I would not talk about his case with the Dean."
    scene policeman_s24_drug_deal18
    d "However you want. Enjoy the rest of your day. And that magazine is a gift from me. Good luck."
    scene policeman_s24_drug_deal09
    "Police" "Your time is running out. Throw down your weapon and show yourself."
    play sound 'sounds/effects/car_engine_sound.ogg'
    scene policeman_s24_drug_deal22
    $ renpy.pause(2.0, hard= True)
    scene policeman_s24_drug_deal21
    $ renpy.pause(1.0, hard= True)
    scene policeman_s24_drug_deal24
    $ renpy.pause(1.0, hard= True)
    scene policeman_s24_drug_deal23
    $ renpy.pause(1.0, hard= True)
    stop sound
    scene policeman_s24_drug_deal25
    asn "Hey! Need a ride?"
    p "Ooou!! Of course!"
    scene policeman_s24_drug_deal26
    asn "Jump in!"
    play sound 'sounds/effects/assault_rifle_sound.ogg'
    $ renpy.pause(0.5, hard=True)
    #TODO machine gun sounds needed
    scene policeman_s24_drug_deal10
    $ renpy.pause(2.0, hard= True)
    play sound 'sounds/effects/car_engine_sound.ogg'
    scene policeman_s24_drug_deal27
    $ renpy.pause(2.0, hard= True)
    scene policeman_s24_drug_deal28
    $ renpy.pause(2.0, hard= True)
    scene policeman_s24_drug_deal29
    $ renpy.pause(2.0, hard= True)
    scene policeman_s24_drug_deal30
    $ renpy.pause(2.0, hard= True)
    stop sound
    play music "sounds/music/intro_music2_Classical_Piano.ogg" fadein 3.0
    scene black_screen with fade
    "After some time laying low..."
    scene policeman_s24_drug_deal26
    asn "So... we are at your place..."
    p "You have no idea how much you've helped me."
    asn "It’s fine. Just watch your back. But, when I'll need help with something in the future, I'm counting on you."
    p "Fine. But still, thank you once again. I’ll see you soon."
    p "You don’t want to come upstairs for a bit, do you?"
    asn "... Bye..."
    scene black_screen with fade
    jump scene_back_at_cop_apartment_after_drug_sell_choice_consequence

label scene_not_sell_drugs_consequence_angel_visit:
    scene policeman_s25_angel_visit00
    a "Hello."
    p "Is there something you need?"
    scene policeman_s25_angel_visit02
    a "What? You’re not happy to see your guardian angel?"
    $ drug_sell_choice_consequence_time = False
    $ time_of_day = Set_Time_of_Day('GECE')
    if reputation_number < 1:
        jump angel_visit_short_stay
    elif not helped_trapped_girl:
        jump angel_visit_short_stay
    else:
        jump angel_visit_long_stay

label angel_visit_short_stay:
    scene policeman_s25_angel_visit02
    p "I’m not sure if I want to see you again."
    a "Can I ask why you are being so rude?"
    p "It's easy. Everything that I do goes to shit. From that accident onwards, nothing went the way I wanted."
    scene policeman_s25_angel_visit00
    a "Maybe you need to be listening more to other..."
    p "You mean listen more to you, right? Hah, no thanks."
    a "Fine. Look, the main reason why I’m here is because you decided to not sell drugs to that student. You made the right decision, in my eyes, and want to say thank you for that. You did a good thing."
    a "And to show you, you can get rewards for making good decisions, I can tell you a secret."
    p "And that is..?"
    a "The reason why the pills do not work is because pills are activated by lust. Lust is the catalyst that causes the pills to react. Megan doesn’t know about it yet, but you know it now."
    p "That's something, I guess..."
    scene policeman_s25_angel_visit03
    a "And now I must go. More decisions like that, and you can be proud of yourself. See ya!"
    scene black_screen with fade
    scene policeman_main
    p "Now that I know the secret to the pills, I should let Sophia know."
    $ devil_or_angel_explained_the_secret_of_the_pills = True
    jump scene_back_at_cop_apartment_after_drug_sell_choice_consequence

label angel_visit_long_stay:
    scene policeman_s25_angel_visit02
    p "Of course I’m happy to see you. Just wondering why you are visiting me this time."
    scene policeman_s25_angel_visit01
    a "You know, I just don’t have better things to do and I’m a little lonely and bored. So I was just thinking maybe you wouldn’t mind keeping me company… maybe with a bottle of good wine?"
    p "But you’re paying, right?"
    scene policeman_s25_angel_visit03
    a "Of course! Let’s go!"
    scene policeman_s25_angel_visit04
    p "Hah! That’s some magic. My favorite restaurant - only empty, and with only one table."
    scene policeman_s25_angel_visit06
    play sound "sounds/effects/Megan_heels_claping_sound.ogg"
    p "For the two of us."
    stop sound
    scene policeman_s25_angel_visit05
    p "(Damn, she can be hotter than hell sometimes.)"
    scene policeman_s25_angel_visit08
    a "I heard that. But thanks. Are you feeling comfortable enough?"
    scene policeman_s25_angel_visit07
    p "Oops... Yes, I’m fine."
    scene policeman_s25_angel_visit09
    a "I have a great idea. I think this will make you happy."
    scene policeman_s25_angel_visit17
    p "Oh God! Oops.. sorry… to be saying that. But I’m so excited! This is my own body!"
    scene policeman_s25_angel_visit18
    a "Looks like you like it."
    p "That is the most awesome gift I‘ve gotten in a long time. Does this mean, you can give me back my body?"
    a "No, sorry. The deal is the deal, but for this dinner I can do almost anything."
    scene policeman_s25_angel_visit19
    p "Ah... fine."
    a "So how about a little more fun?"
    p "You mean...? Eh... You want to..?"
    scene policeman_s25_angel_visit11
    a "I mean a bottle of wine."
    p "Oh! Yes. I’m an idiot. But I don’t see any wine here?"
    a "The waitress is on the way."
    scene policeman_s25_angel_visit13
    brook "Hello, sir. We have a special wine today. Chardonnay 1980."
    scene policeman_s25_angel_visit12
    p "How can this be? Is this your magic?"
    a "Of course."
    p "I was thinking that only the devil had these kind of powers."
    a "No, we are almost at the same level, to tell the truth. We can talk about it later. Brooke? Please open that wine and leave us alone."
    brook "Yes, Mistress."
    scene policeman_s25_angel_visit14
    a "So what should we drink to?"
    p "What about the best night in a long time?"
    scene policeman_s25_angel_visit15
    a "Why not!"
    a "Cheers!"
    scene black_screen with fade
    "After some time and a bottle of wine later..."
    scene policeman_s25_angel_visit16
    p "So you said your powers are almost equal to the devil's?"
    a "They are, but we must both play by the rules we have."
    p "What rules?"
    a "About that: I can’t discuss them with you. Let's just say, she and I both... we can’t break them."
    p "And what happens if you do?"
    a "Same as in your world: If you break the rules, you get punished."
    p "Right."
    p "How long have you lived?"
    a "I’ve been here for a few centuries, but the devil, she’s been here much longer than that."
    p "How is that possible?"
    a "My predecessor broke the rules..."
    a "Anyway...I had a really good time with you. But now I must go!"
    p "Hope that we'll meet again soon."
    a "Sure, why not."
    #TODO angel kiss here
    a "See you next time."
    $ had_dinner_with_angel_after_no_drug_sell_and_helped_trapped_girl = True

    jump scene_back_at_cop_apartment_after_drug_sell_choice_consequence

label scene_back_at_cop_apartment_after_drug_sell_choice_consequence:
    scene black_screen
    scene policeman_main with fade
    $ time_for_bed_after_drug_selling_choice_consequences = True
    if had_dinner_with_angel_after_no_drug_sell_and_helped_trapped_girl or chose_to_sell_drugs_to_brandon:
        p "What a night..."
    if chose_to_sell_drugs_to_brandon:
        $ inventory.drop(gun)
        scene policeman_s17_gun
        $ need_cops_gun = False
        $ hints_counter += 1
        p "Back you go."
    $ hints_counter += 1
    if helped_trapped_girl:#had_dinner_with_angel_after_no_drug_sell_and_helped_trapped_girl
        jump scene_cop_finds_note_from_trapped_girl
    else:
        p "I think I'll call it a day and head straight to bed."
        jump cop_apartment_main

label scene_day_after_drug_sell_choice_consequences:
    scene black_screen
    scene policeman_04_go_sleep with fade
    if had_dinner_with_angel_after_no_drug_sell_and_helped_trapped_girl or chose_to_sell_drugs_to_brandon:
        p "That was some night..."
    p "Time to get up."
    if helped_trapped_girl:
        "I need to go see that blonde woman who left me the note."
    $ time_for_bed_after_drug_selling_choice_consequences = False
    $ morning_after_drug_sell_choice_consequenses = True
    $ time_of_day = Set_Time_of_Day('SABAH')
    if chose_to_sell_drugs_to_brandon:#MAGIC
        $ hints_counter = 53
    elif not chose_to_sell_drugs_to_brandon:
        if helped_trapped_girl:
            $ hints_counter = 54
        else:
            $ hints_counter = 55
    jump cop_apartment_bedroom

label scene_cop_finds_note_from_trapped_girl:
    scene policeman_letter_under_door
    p "What’s that? There's something under the door."
    scene policeman_letter_under_door2
    p "Aaah... it’s a letter from that woman with her hair in the sink. She wants to see me tomorrow morning. Great. Should be fun, but now I’m ready for bed."
    jump cop_apartment_main

label scene_sell_drugs_consequence_devil_visit:
    scene policeman_s26_devil_morning2
    d "So, how did you sleep?"
    scene policeman_s26_devil_morning3
    p "Actually, pretty good after what happened yesterday."
    scene policeman_s26_devil_morning2
    d "But you don’t look too happy."
    scene policeman_s26_devil_morning3
    p "You’re right. I’m not. You know, since that time you helped me after my accident, I think everything I have done is working against me."
    scene policeman_s26_devil_morning0
    d "Hmmm... I know what you mean."
    p "No, I don’t think you do. I’m going from one problem to another. Even those stupid pills are not working now!"
    scene policeman_s26_devil_morning1
    d "Because they only work, with the secret ingredient."
    p "What?! What ingredient? Megan didn’t mention anything about another ingredient?"
    d "Because she doesn’t know it yet either."
    p "Fine. Then can you tell it to me? What the ingredient is? For free? No killing or betraying someone or anything else."
    d "Hah! Fine. Yes, I will tell you. The secret ingredient is lust."
    p "Lust?? What?"
    d "Yes, lust or sexual appetite if you prefer. When you took them as Brandon with Bethany, they worked because you were both really excited."
    p "Now I get it."
    scene policeman_s26_devil_morning0
    d "Great. Now I have other business to attend to."
    if accepted_devils_offer_for_anders_soul:
        d "And don’t forget to give the Dean that folder about Anders. You owe me, now."
        p "Yes, I will make the report during the next few days."
        d "Fine."
    $ devil_or_angel_explained_the_secret_of_the_pills = True
    scene policeman_main
    p "Now that I know the secret to the pills, I should let Sophia know."
    if helped_trapped_girl:
        $ hints_counter = 54 #MAGIC
    else:
        $ hints_counter = 55 #MAGIC
    jump cop_apartment_main

label scene_see_trapped_girl_after_note_left:
    play music "sounds/music/sexy_music4_Tripst_topher.ogg" fadein 3.0
    scene policeman_s29_blondie01
    trpd "Oh, hello, my savior."
    p "Hi. I found the letter from you under my door."
    trpd "Yes. I’m glad that you accepted my offer. Come in. Nobody else is home."
    scene policeman_s29_blondie02
    trpd "Here, take a seat and feel at home. I will be back in a moment."
    p "Sure."
    scene policeman_s29_blondie03
    p "Hmmm... this day is starting off really nice..."
    if devil_or_angel_explained_the_secret_of_the_pills:
        "(I hope the pills kick in soon. Need to add lust, huh?)"
    else:
        p "(The only bad thing is that the pills are not working. I used one after waking up, and nothing happened. But this cop has a good size, so I don’t need them right now.)"
        p "Maybe I can talk about this with Megan after I’m done here."
    trpd "I’m back."
    scene policeman_s29_blondie04
    p "Oh! Wwwwwoooow!"
    scene policeman_s29_blondie05
    trpd "You like that?"
    scene policeman_s29_blondie08
    p "Of course! You look awesome!"
    scene policeman_s29_blondie07
    trpd "And that is not my only surprise for you."
    scene policeman_s29_blondie06
    p "Really? I like surprises!"
    trpd "Me too. Let me sit on you, first."
    scene policeman_s29_blondie10
    trpd "Yes! Lick my tits."
    scene policeman_s29_blondie09
    p "Hmmmm... You smell so nice!"
    scene policeman_s29_blondie11
    trpd "Am I starting to feel something getting harder in your pants?"
    scene policeman_s29_blondie12
    p "You’re right. That's because you are doing a really good job with that lap dance."
    trpd "You flatterer. Now here is my second surprise..."
    scene policeman_s29_blondie13
    p "Wha...!? Is that..?"
    trpd "Yes. I really like that. Hope you do too?"
    scene policeman_s29_blondie14
    p "You can bet your ass on it! Haha ! Of course I like it! I love it! Damn, I didn’t expect this. You are awesome! How big is it inside?"
    trpd "You can take it out and see. But first, take off my clothes."
    scene policeman_s29_blondie16
    p "What a nice view. One of the best I've ever seen."
    scene policeman_s29_blondie15
    $ renpy.pause(2.0, hard=True)
    trpd "Thanks! Keep going..."
    trpd "Want to start with a blowjob?"
    p "Of course! If you want to do it..."
    trpd "I would like to show you how good I am."
    scene policeman_s29_trans01
    $ renpy.movie_cutscene("scenes/Policeman/29_blondie/webm/blonde_S01_bj1.webm", loops=1, stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/29_blondie/webm/blonde_S01_bj2.webm", loops=1, stop_music=False)
    scene policeman_s29_blondie15b
    trpd "Now please, take that buttplug out."
    trpd "But be careful. It’s a really big size. It is the first time I used such a big one."
    p "I will be."
    scene policeman_s29_trans02
    $ renpy.movie_cutscene("scenes/Policeman/29_blondie/webm/blonde_s01_plug_remove.webm", stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/29_blondie/webm/blonde_s01_plug_remove2.webm", stop_music=False)
    scene policeman_s29_blondie17
    p "Now taste it."
    scene policeman_s29_blondie18
    p "You like it?"
    trpd "Opfl clofuse phfff. Tfles gleat…"
    p "Now, sit on me, and show me how a mommy rides."
    scene policeman_s29_blondie19
    p "Hmmm, your ass feeeels... sooo... great!"
    scene policeman_s29_blondie20
    trpd "Yef. I fil sfou yuf."
    scene policeman_s29_blondie21
    p "(It’s starting to feel like... like... like my dick is growing… Her ass is getting tighter and tighter!)"
    scene policeman_s29_trans04
    $ renpy.movie_cutscene("scenes/Policeman/29_blondie/webm/blonde_S01_anal_ride_grow.webm", stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/29_blondie/webm/blonde_s01_anal_ride_grow2.webm", stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/29_blondie/webm/blonde_s01_anal_ride_grow3.webm", stop_music=False)
    scene policeman_s29_blondie22
    p "Oh God! That feeels so great!"
    p "(The pills are working!)"
    if devil_or_angel_explained_the_secret_of_the_pills:
        p "(The Devil was right!)"
    scene policeman_s29_blondie23
    a "I see you are having some good fun this morning."
    scene policeman_s29_blondie24
    p "Hey? What are you doing here?"
    a "I was just curious, what reward she would give you. And you must admit, sometimes it’s better to help someone and maybe get a better reward, than just take advantage of the situation."
    p "Yeah, you are right in this case."
    if devil_or_angel_explained_the_secret_of_the_pills:
        a "I understand you already know about the pills' effects?"
        p "Yeah, activated by lust."
        if chose_to_sell_drugs_to_brandon:
            a "I'm not happy with how you obtained this information, but have your fun."
        else:
            a "Have fun!"
    else:
        a "About those pills, you still don’t know how they work, right?"
        p "On some people they work, but for sophia, no. Maybe it's, some people are just immune to the effect of the pills?"
        a "Of course not! Just that the catalyst for these pills is lust. A person’s lust starts the effect."
        p "Oh?? Good to know that. Thanks, Angel."
        a "So, have fun..."
    scene policeman_s29_blondie25
    p "I will."
    scene policeman_s29_trans04
    $ renpy.movie_cutscene("scenes/Policeman/29_blondie/webm/blonde_s01_anal_ride_grow2.webm", stop_music=False)
    scene policeman_s29_trans05
    $ renpy.movie_cutscene("scenes/Policeman/29_blondie/webm/blonde_s01_anal_plug_drop.webm", stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/29_blondie/webm/blonde_s01_anal_ride_loop2.webm", loops=1, stop_music=False)
    scene policeman_s29_blondie26
    trpd "Aaaah..!!  (My ass is on fire now! He feels much bigger than just a moment ago. But I like it and need more..!)"
    scene policeman_s29_trans03
    $ renpy.movie_cutscene("scenes/Policeman/29_blondie/webm/blonde_s01_anal_ride_loop1.webm", loops=1, stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/29_blondie/webm/blonde_s01_anal_ride_loop3.webm", loops=1, stop_music=False)
    scene policeman_s29_blondie28
    $ renpy.movie_cutscene("scenes/Policeman/29_blondie/webm/blonde_s01_anal_ride_loop2.webm", loops=1, stop_music=False)
    scene policeman_s29_blondie28
    p "I cannot resist any moreeee!! Uhmmmm..!"
    scene policeman_s29_blondie27
    trpd "Oooouuuu!! (He's filling me with his cum!)"
    scene policeman_s29_blondie30
    trpd "(I’m so full inside... I don’t know if I can handle more...)"
    scene policeman_s29_blondie29
    trpd "(But on the other hand, it feels so great. What a pleasurable moment!!)  Give me moooore!! More cum! Please!"
    scene policeman_s29_blondie31
    p "Damn! What a trip! You are a great rider, babe..."
    trpd "And you are a great lover. My ass feels like I had a 10 men gangbang... and so full."
    p "Yeah, cum is slowly dripping on the floor from your ass."
    scene policeman_s29_blondie33
    trpd "I must taste it!"
    scene policeman_s29_blondie32
    trpd "Hmmmmm..! So good..."
    scene policeman_s29_blondie34
    trpd "That was the best sex I have ever had! I think we can do it again in the future. I will leave a letter under your door again when I have the apartment to myself next time. But I’m already horny for the next time..."
    scene black_screen with fade
    scene policeman_main with fade
    p "Wow, I can’t believe what just happened!"
    if chose_to_sell_drugs_to_brandon:
        p "The Devil was right!"
    else:
        "Angel must be right."
    p "School is still open. I should head over there."
    $ morning_after_drug_sell_choice_consequenses = False
    if not devil_or_angel_explained_the_secret_of_the_pills:
        $ devil_or_angel_explained_the_secret_of_the_pills = True
    jump time_to_check_on_sophias_progess_with_pills


label time_to_check_on_sophias_progess_with_pills:
    $ morning_after_drug_sell_choice_consequenses = False
    $ looking_for_sophia_about_pills_progress = True
    $ time_of_day = Set_Time_of_Day('SABAH')
    scene city_map
    p "I should go and see how Sophia is getting on with the pills' effect, now that I know how they work. I should look around school for her."
    $ hints_counter = 55
    jump city_map

label scene_ask_anders_where_sophia_is_and_unlock_gym:
    scene policeman_anders_classroom
    andr "Hello, Detective. Are you looking for someone?"
    p "Yes, actually. I’m looking for Sophia."
    andr "Sophia and the other girls are at the gym behind the school. They have volleyball training now."
    p "(I’m surprised Anders is not already there, watching. Maybe he really is trying to change.)"
    p "Great. I will visit her at the gym. Thank you, Anders."
    andr "No problem. Remember, you said you wouldn’t say anything to the Dean."
    if accepted_devils_offer_for_anders_soul:
        p "(Sorry, buddy. If it was up to me...)"
        p "Keep your nose clean, and everything should be okay..."
    else:
        p "I remember. Don’t worry about it."
    andr "Thank you, Detective."
    $ gym_location_available = True
    $ hints_counter += 1
    jump class1

label scene_girls_playing_volleyball_at_gym:
    scene policeman_s27_gym_volleyball00
    p "(The girls are already playing. Brooke with Bethany against Sophia and Ivana. They all look so good in their sports kits.)"
    scene policeman_s27_gym_volleyball01
    p "Wow! (Bethany can really smash that ball.)"
    scene policeman_s27_gym_volleyball02
    $ renpy.pause(1.0, hard=True)
    scene policeman_s27_gym_volleyball03
    $ renpy.pause(0.5, hard=True)
    play sound 'sounds/effects/punch_sound.ogg'
    $ renpy.pause(1.0, hard=True)
    scene policeman_s27_gym_volleyball04
    $ renpy.pause(1.0, hard=True)
    scene policeman_s27_gym_volleyball06
    $ renpy.pause(1.0, hard=True)
    beth "Haha! We win again."
    scene policeman_s27_gym_volleyball05
    sop "Ouuuch! That was a strong spike."
    brook "Hey Sophie..! Are we playing again or are you just going to lie on the floor."
    beth "Haha! You know you girls can never beat us."
    brook "As Beth said, you’ve never beaten us, and never will."
    scene policeman_s27_gym_volleyball08
    iva "How about we show them that we have enough power to beat them today?"
    scene policeman_s27_gym_volleyball05
    sop "Yes. Just give me a second. I’m feeling a little dizzy now."
    scene black_screen
    $ renpy.movie_cutscene("scenes/policeman/27_volleyball_gym/animations/sophia_s27_gym_grow1.webm", stop_music=False)
    scene policeman_s27_gym_volleyball08b
    $ renpy.movie_cutscene("scenes/policeman/27_volleyball_gym/animations/sophia_s27_gym_grow2.webm", stop_music=False)

    p "(She grew bigger! Those pills really work!)"
    scene policeman_s27_gym_volleyball08
    iva "If you are not feeling well, we can just end this."
    scene policeman_s27_gym_volleyball08b
    sop "No, it’s okay, I feel much better now. Let’s beat them, Ivana!"
    scene policeman_s27_gym_volleyball09
    sop "So, ladies, are you ready for your first loss?"
    scene policeman_s27_gym_volleyball10
    brook "That must have been a really hard hit you took to your head, darling."
    beth "She must be bonkers."
    brook "Let’s go!"
    scene policeman_s27_gym_volleyball11
    p "(The girls started a new match.)"
    scene black_screen
    "15 minutes later..."
    scene policeman_s27_gym_volleyball16
    p "(Really interesting match. Sophia and Ivana are leading by 10 points and are one point from winning. Sophia is literally devastating them with really great smashes with her high jump.)"
    p "(Bethany and Brooke look really nervous now.)"
    scene policeman_s27_gym_volleyball12
    sop "Now you are done, girls!"
    scene policeman_s27_gym_volleyball13
    p "(Brooke set that ball nicely, above the net.)"
    scene policeman_s27_gym_volleyball14
    p "(Bethany is continuing with a great smash. But Sophia was in place and jumped really high to block that ball.)"
    scene policeman_s27_gym_volleyball15
    p "(And Brooke is playing far too safe for this situation.)"
    scene policeman_s27_gym_volleyball17
    p "(Bethany and Brooke lost, for the first time, it looks like.)"
    brook "How is this possible? How is she jumping so high today?"
    beth "What happened..?"
    scene policeman_s27_gym_volleyball18
    iva "Hooraaay!!! Winners!"
    sop "Great game!"
    scene policeman_s27_gym_volleyball19
    p "That was a really interesting game, girls."
    iva "Oh... hello, Detective! Yes! We literally beat them down."
    p "Yes, Sophia plays like a pro."
    sop "Thank you... John."
    iva "Oooohh... Okay... I’m going to shower and go home. Bye."
    scene policeman_s27_gym_volleyball20
    sop "So, did you just happen to be here, or..?"
    p "No, I’m here because of our little experiment with those pills."
    sop "Did you find out why they didn’t work?"
    p "They did! Didn’t you notice that?"
    sop "Eh???"
    sop "(Damn, why am I so horny? Wish Scarlett was here right now.)"
    sop "Do you have some spare time, John?"
    p "Sure."
    sop "Great! Come with me."
    scene black_screen with fade
    jump sophia_cop_locker_room_sex_after_volleyball

label sophia_cop_locker_room_sex_after_volleyball:
    scene black_screen
    scene policeman_s28_locker_room_sex00 with fade
    iva "See you tomorrow! Great game!"
    sop "Bye, Ivana!"
    play music "sounds/music/Sexy_music1_monks_topher.ogg" fadein 3.0
    scene policeman_s28_locker_room_sex01
    sop "So... you really think the pills worked?"
    p "Yes!"
    sop "So give me another one. I want to see what you’re talking about."
    p "You’ve already grown bigger. Look at how tall you are now."
    scene policeman_s28_locker_room_sex02
    sop "Damn, you're right! I’m bigger than these lockers. I was wondering why my suit was so tight today."
    scene policeman_s28_locker_room_sex03
    sop "But you only talked about boobs, and they still look the same."
    scene policeman_s28_locker_room_sex04
    sop "They're definitely,  still the same."
    p "(Uhh...)"
    scene policeman_s28_locker_room_sex05
    sop "Same as my butt... What’s wrong, Detective? Cat got your tongue?"
    p "N-Not really. But I thought you said you are into girls."
    sop "Sure am, but I’m not one to reject boys either. Especially if you have more of those pills for me."
    scene policeman_s28_locker_room_sex06
    $ renpy.pause(1.0, hard=True)
    p "You mean this pill?!"
    sop "Definitely that one!"
    scene policeman_s28_locker_room_sex07
    sop "(I think this will be great fun...)"
    scene policeman_s28_locker_room_sex08
    sop "So will it happen soon?"
    p "I think this time, yes."
    scene policeman_s28_locker_room_sex09
    sop "Jeees..! Yes, I feel it! Daaamn, that feels so good..!"
    scene black_screen
    $ renpy.movie_cutscene("scenes/Policeman/28_locker_room_sophia_sex/webm/sophia_s28_boobsgrow2.webm", stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/28_locker_room_sophia_sex/webm/sophia_s28_boobsgrow3.webm", stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/28_locker_room_sophia_sex/webm/sophia_s28_boobsgrow.webm", stop_music=False)
    scene policeman_s28_locker_room_sex11
    sop "It worked!!!"
    scene policeman_s28_locker_room_sex10
    sop "You were right! I’m so happy right now!"
    p "You look really stunning, Sophia."
    scene policeman_s28_locker_room_sex12
    sop "And this is all thanks to you, John.  Hmm... I feel something big and stiff here. You are using them too, right?"
    p "Eeeh... not yet."
    scene policeman_s28_locker_room_sex13
    sop "I think I owe you a favor right now."
    scene policeman_s28_locker_room_sex14
    sop "Damn, John! I think, you don’t need any pills."
    scene policeman_s28_locker_room_sex15
    $ renpy.pause()
    scene policeman_s28_locker_room_sex16
    sop "(Mmmm... I’m horny like never before...)"
    scene policeman_s28_trans04
    $ renpy.movie_cutscene("scenes/Policeman/28_locker_room_sophia_sex/webm/sophia_s28_cam2_bj.webm", stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/28_locker_room_sophia_sex/webm/sophia_s28_cam1_bj.webm", loops=1, stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/28_locker_room_sophia_sex/webm/sophia_s28_cam2_bj.webm", stop_music=False)
    scene policeman_s28_locker_room_sex17
    sop "(Oh God! I can’t..!)"
    scene policeman_s28_locker_room_sex14
    sop "I don’t know what to say. First I wanted to give you just a blowjob, but damn! I cannot resist you any longer. I need to feel that cock inside me, right now!"
    scene policeman_s28_trans03
    $ renpy.movie_cutscene("scenes/Policeman/28_locker_room_sophia_sex/webm/sophia_s28_cam1_side.webm", stop_music=False)
    $ renpy.movie_cutscene("scenes/Policeman/28_locker_room_sophia_sex/webm/sophia_s28_cam2_side.webm", stop_music=False)
    scene policeman_s28_trans01
    sop "You are awesome, John! Now please do me from behind!"
    scene policeman_s28_locker_room_sex19
    $ renpy.movie_cutscene("scenes/Policeman/28_locker_room_sophia_sex/webm/sophia_s28_teasing.webm", stop_music=False)
    scene policeman_s28_locker_room_sex19
    p "Let’s do this!"
    scene policeman_s28_locker_room_sex18
    sop "Hey! Stop! That is my ass! I don’t like anal and don’t want to even try it. Use my pussy, not my ass!"
    p "Okay, calm down..."
    scene policeman_s28_trans02
    $ renpy.movie_cutscene("scenes/Policeman/28_locker_room_sophia_sex/webm/sophia_s28_cam1_from_behind.webm", loops=1, stop_music=False)
    scene policeman_s28_locker_room_sex_cumshot01
    $ renpy.movie_cutscene("scenes/Policeman/28_locker_room_sophia_sex/webm/sophia_s28_cam2_from_behind.webm", loops=2, stop_music=False)
    scene policeman_s28_locker_room_sex_cumshot01
    sop "That was great! Now please spray that jizz on my new juicy tits for me."
    p "As you wish!"
    scene policeman_s28_locker_room_sex_cumshot03
    scene policeman_s28_locker_room_sex_cumshot02 with dissolve
    sop "Ooooh..! So much cum!  You covered all of these nice boobs. We will definitely see each other in the future. I will need more of those pills."
    p "Sure, why not."
    scene city_map
    play sound "sounds/effects/phone_ringing_sound.ogg"
    $ renpy.pause(2.0, hard=True)
    stop sound
    show police_boss_sms
    $ renpy.pause()
    hide police_boss_sms
    #$ are_hints_available = False # TEMP
    $ hints_counter = 57 #MAGIC
    $ time_of_day = Set_Time_of_Day('ÖĞLEN')
    #stop music fadeout 1.0
    #play music "sounds/music/Menu_intro_music.ogg" fadein 3.0
    #scene outro
    #$ renpy.pause(15.0, hard=True)
    #$ renpy.quit()
    p "Cool. I’ve never been part of an interrogation before. This might be fun and hopefully I will get some new information."
    p "But now, I have some time till night. I should go visit Ivana and talk about Scarlett’s diary, because there's no mention of a diary in the logged evidence. Hope she'll be at home."
    $ looking_for_sophia_about_pills_progress = False
    $ as_cop_ready_to_search_for_scarlets_diary = True
    jump city_map

label scene_search_for_scarlet_diary_at_ivanas:
    scene policeman_s30_searchin_diary02
    iva "Hello, Detective. That was fast… hihi."
    p "Ehm... Hello, Ivana. I’m here again because of Scarlett’s case."
    iva "Sure. What do you need?"
    p "Can I see her room? I think there might be something that my colleagues missed."
    iva "Of course. Come in."
    scene policeman_s30_searchin_diary01
    iva "So here it is. Everything here is how she left it."
    p "Great. I will look around."
    iva "Take your time."
    $ hints_counter += 1
    jump ivana_apartment_scarlett_room

label scene_leaving_scarlett_room_after_finding_drive:
    scene policeman_s30_searchin_diary04
    iva "So, did you find something?"
    p "Yes, I found this usb."
    p "Unfortunately I don’t have a computer to access it. The Devil broke my laptop."
    scene policeman_s30_searchin_diary04
    iva "Who?"
    p "Aaaargh…. I mean my colleague, haha. That’s his nickname. Do you have a computer?"
    iva "No, sorry. I just use my phone for most things."
    p "That’s okay.. Enjoy the rest of your day, Ivana."
    scene policeman_s30_searchin_diary03
    iva "Yes, and please tell me If you find anything interesting."
    p "Of course!"
    $ as_cop_ready_to_search_for_scarlets_diary = False
    scene city_map
    p "I will look into this usb in the computer class, at school tomorrow. I still need to have a talk with Megan, so I will do it all in one run. Now it's time to go back home."
    $ time_of_day = Set_Time_of_Day('AKŞAM')
    $ night_before_interrogation_consequence_time = True

    $ hints_counter +=1
    jump city_map

label sophia_upset_in_school_on_bikini_competition_day:
    scene policeman_s32_upset_sophia01
    p "Hello, Sophia. Why so sad?"
    scene policeman_s32_upset_sophia02
    sop "Those pills only work for a short time? Look at me! I’m almost back to normal again."
    p "These pills are still in the experimental phase, so nobody knows how they fully work."
    sop "Okay, but I need more of them, just for today."
    p "Why? Why today?"
    sop "Because today, right after school is the big bikini competition on the beach. And this year, I want to beat Brooke, and especially Bethany. You have to help me! Please!"
    p "Fine, fine... I will visit you just before the competition, and bring you some more."
    sop "Great! I will wait for you. Don’t be late."
    scene school_map
    p "That old \“girls problem\”, haha. But why don’t I take advantage of that."
    scene policeman_school_pc_blue with fade
    p "Alright,  finally I can look at what's on this flashdrive."
    p "BINGO! \“My lovely diary\”..."
    p "Hmm... hmmm… hmm… tons of \“girly\” shit…."
    p "Here's something interesting..!"
    scrlt "Anders seems to be dumber than I thought. He actually paid me 300$ for these photos of Ivana. That's a gold mine for me.  And as a bonus, he promised me that I would pass Biology, just like that. What a deal!"
    p "Seems like Anders was being 100\% truthful with me."
    if accepted_devils_offer_for_anders_soul:
        p "Unfortunately, I must betray him now. The Devil’s deal is the Devil’s deal."
    p "Here. 5 Days before she went missing."
    scrlt "Frank is absolutely great. He will give me the money for my whole trip over Europe and says he'll join me on my trip in Rome."
    scrlt "So, in Paris, I will be alone. What a shame. On the other hand, I’m supposed to meet up there, with Frank’s friend, Pierre. Maybe he will be really cute, and maybe be my guide during my visit in Paris. I’m so excited!"
    p "Three days before she went missing."
    scrlt "Frank is so thoughtful. He bought me brand new luggage for my trip. They look really stylish. It made my day that much better. After that issue with Anders,. I don’t know if I should tell Frank about it - he might probably kill Anders. I think I will leave it as it is."
    p "The day she went missing."
    scrlt "This is really crazy! While I was packing my things, I discovered that my luggage, that Frank gave me as a surprise present, has a secret compartment full of some kind of drugs!"
    scrlt "What am I going to do? Act like nothing’s wrong, and go to Europe, hoping nobody finds out? Or hide somewhere? Or say to Frank, that I changed my mind about the trip, and pretend I know nothing?  Or go to the police? I don’t know what to do now!!"
    p "Here her diary ended."
    p "Damn. Looks like Scarlett stepped into some really serious shit. I must find this Frank."
    $ time_to_look_at_scarletts_flash_drive = False
    scene school_map
    if accepted_devils_offer_for_anders_soul:
        p "Now I need to deliver these papers about Anders to the Dean. Then I will visit Megan in the lab."
        $ time_to_deliver_anders_documents_to_dean = True
        $ hints_counter += 1
        jump school
    else:
        p "But now I should visit Megan in the lab."
        $ hints_counter += 2
        jump scene_tell_megan_about_pills_secret_ingredient

label scene_delivering_anders_documents_to_deans_office:
    scene policeman_s36_deans_door
    play sound 'sounds/effects/hitting_wood_sound.ogg'# TEMP need knock on door sound TODO
    $ renpy.pause(0.5, hard=True)
    p "Damn, she’s not here. Okay I'll just put the documents under the door."
    scene policeman_s36_under_door_clues
    p "I think that will be enough. Now I'll visit Megan in the lab."
    $ inventory.drop(anders_evidence)
    $ time_to_deliver_anders_documents_to_dean = False
    $ hints_counter += 1
    jump scene_tell_megan_about_pills_secret_ingredient


label scene_tell_megan_about_pills_secret_ingredient:
    scene policeman_s33_megan_lust01
    meg "Hello, Detective, What brings you here again?"
    p "Hi, Megan. I think I have some interesting news about your experiments."
    scene policeman_s33_megan_lust02
    meg "Really? What is it?"
    p "I think I know why sometimes the pills don’t seem to work and why sometimes they work very well."
    p "Because to make them work, each person needs to add the secret ingredient."
    scene policeman_s33_megan_lust03
    meg "Secret ingredient? There is no secre..."
    p "Yes there is! It's lust…"
    meg "Lust? What do you mean by that?"
    p "It's easy. To make the pills work, the subject needs to have lust, of any kind. I tested it, and it really works."
    scene policeman_s33_megan_lust04
    meg "Hmmm... That is really interesting. But, yes, it could make sense. Not from a scientific point of view, but somehow, yes..."
    scene policeman_s33_megan_lust02
    p "How is it going with the Dean?"
    meg "Okay, so far. She is getting a little nervous, but it's alright for now. But ,please don’t waste any time, because I think she will want to see some progress this week."
    p "It’s okay, I think I will have enough time. (Like today, in the bikini competition. Yay!)"
    p "So, see you later, Megan."
    meg "Bye, Detective."
    scene city_map
    p "Damn, time is running out, fast. I need to  run over to the beach. I hope I get to Sophia in time."
    $ time_to_give_pills_to_sophia_for_bikini_competition = True
    $ time_of_day = Set_Time_of_Day('ÖĞLEN')
    jump city_map

label scene_beach_bikini_competition:
    scene policeman_s34_sophia_bikini_cabin01
    sop "Ah! Finally, you're here! I’m absolutely lost!"
    p "What happened?"
    scene policeman_s34_sophia_bikini_cabin02
    sop "What happened?! Just look at me..!"
    p "What?"
    scene policeman_s34_sophia_bikini_cabin03
    sop "My boobs! They are small again. And maybe even smaller than normal..."
    scene policeman_s34_sophia_bikini_cabin04
    sop "I bought this new bikini, and look at this! It’s too big! My tits don’t even fill it. I can’t go like this into the competition."
    scene policeman_s34_sophia_bikini_cabin05
    sop "Please, you must help me! Please! I will do anything you want..."
    p "Really?"
    sop "Really."
    scene policeman_s34_sophia_bikini_cabin06
    p "Fine. Here, I brought two for you."
    sop "Thank you so much!"
    scene policeman_s34_sophia_bikini_cabin07
    sop "Let’s see what they can do."
    scene policeman_s34_sophia_bikini_cabin_translate03
    $ renpy.movie_cutscene("scenes/Policeman/34_Sophia_bikini_grow/webm/sophia_s34_boobs_grow1.webm", loops=0, stop_music=False)
    scene policeman_s34_sophia_bikini_cabin_translate04
    $ renpy.movie_cutscene("scenes/Policeman/34_Sophia_bikini_grow/webm/sophia_s34_belly_grow2.webm", loops=0, stop_music=False)
    scene policeman_s34_sophia_bikini_cabin_translate01
    $ renpy.movie_cutscene("scenes/Policeman/34_Sophia_bikini_grow/webm/sophia_s34_legs_grow1.webm", loops=0, stop_music=False)
    scene policeman_s34_sophia_bikini_cabin_translate02
    $ renpy.movie_cutscene("scenes/Policeman/34_Sophia_bikini_grow/webm/sophia_s34_boobs_grow2.webm", loops=0, stop_music=False)
    scene policeman_s34_sophia_bikini_cabin_translate05
    $ renpy.movie_cutscene("scenes/Policeman/34_Sophia_bikini_grow/webm/sophia_s34_belly_grow1.webm", loops=0, stop_music=False)
    scene policeman_s34_sophia_bikini_cabin09
    $ renpy.movie_cutscene("scenes/Policeman/34_Sophia_bikini_grow/webm/sophia_s34_legs_grow2.webm", loops=0, stop_music=False)
    scene policeman_s34_sophia_bikini_cabin09
    sop "(Wow, that's... Just WOW!)"
    scene policeman_s34_sophia_bikini_cabin08
    sop "So, what do you think?"
    p "I have no wo... I’m speechless."
    sop "Thank you... for everything."
    scene policeman_s34_sophia_bikini_cabin10
    sop "I’m ready for the competition now!"
    p "Let’s go!"
    scene black_screen with fade
    scene policeman_s35_bikini_competition01
    comm "Are you ready for this year’s bikini competition?"
    "people" "*Yell* *Yell*"
    comm "I think this year’s competition will be really tough. I saw some girls modelling  in their bikinis, and I must admit, they’ve been working on their bodies really hard. So let’s begin!"
    scene policeman_s35_bikini_competition02 #TODO fix image resolution
    comm "First we have Bethany! Some of you may know her as a top volleyball player. Here you can see how sport is good for defining your body."
    scene policeman_s35_bikini_competition03
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition04
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition05
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition06
    $ renpy.pause(2.0, hard=True)
    p "Ohmm... Beth is hot and full of confidence. But I can’t wait to see her face when she sees Sophia enter."
    scene policeman_s35_bikini_competition07
    comm "Second girl is student Ivana modelling a classic bikini. Her hair shines like the sun."
    scene policeman_s35_bikini_competition08
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition09
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition10
    $ renpy.pause(2.0, hard=True)
    p "And that ass… Just bite...."
    scene policeman_s35_bikini_competition11
    comm "And next, we have Brooke! Last year’s winner! I think she is one of the favorites for this year too. Just take a look!"
    scene policeman_s35_bikini_competition12
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition13
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition14
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition15
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition16
    $ renpy.pause(2.0, hard=True)
    p "Yeah, Brooke - everybody in school wants to get her in bed. I think they’ll lose their nerve when they find out she’s the Dean’s niece."
    scene policeman_s35_bikini_competition28
    brook "(What the fuck?!)"
    iva "D..amnnnn, girl!"
    beth "How is that possible?!"
    scene policeman_s35_bikini_competition27
    brook "*gulp*"
    scene policeman_s35_bikini_competition17
    comm "And the last girl is Sophia. Looks like Sophia trained really hard this year. And that hard work beared fruits."
    scene policeman_s35_bikini_competition18
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition19
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition20
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition21
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition22
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition23
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition24
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition25
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition26
    $ renpy.pause(2.0, hard=True)
    p "Haha! (Hard work... ha!)"
    p "(Hard work will come later. I cannot wait to fuck her again. This time, the way I want....)"
    scene policeman_s35_bikini_competition30
    comm "So, there we have it. Our lovely bikini girls for this year."
    scene policeman_s35_bikini_competition29
    $ renpy.pause()
    scene policeman_s35_bikini_competition31
    brook "(I need to figure out, how this happened...)"
    sop "Hihi..."
    scene policeman_s35_bikini_competition32
    p "(I think the winner is obvious. It’s me, of course! Haha!)"
    scene policeman_s35_bikini_competition35
    beth "(That bastard! He give those pills to her.)"
    comm "So girls, show us your poses, and we will pick the winner."
    scene policeman_s35_bikini_competition34
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition36
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition37
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition38
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition39
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition40
    $ renpy.pause(2.0, hard=True)
    scene policeman_s35_bikini_competition41
    $ renpy.pause(2.0, hard=True)
    comm "I think it’s time to pick a winner."
    scene policeman_s35_bikini_competition46 # TODO add image
    sop "(Hmm... I’m feeling it again.)"
    scene policeman_s35_bikini_competition_translate01
    $ renpy.movie_cutscene("scenes/Policeman/35_bikini_competition/webm/sophia_s35_bikini_boobsgrow_boobsgrow_fast.webm", loops=0, stop_music=False)
    scene policeman_s35_bikini_competition46b
    $ renpy.movie_cutscene("scenes/Policeman/35_bikini_competition/webm/sophia_s35_bikini_boobsgrow_boobsgrow2.webm", loops=0, stop_music=False)
    scene policeman_s35_bikini_competition46b
    brook "Whaaa..?"
    scene policeman_s35_bikini_competition42
    comm "Ivana or Bethany?"
    scene policeman_s35_bikini_competition43
    comm "Sophia or Brooke? There can only be one winner."
    comm "And the winner is..."
    scene policeman_s35_bikini_competition44
    comm "Sophia!!"
    scene policeman_s35_bikini_competition33
    p "Haha! As planned."
    scene policeman_s35_bikini_competition45
    sop "First place, this year! Wow!"
    brook "(You plastic bitch... I will show you.)"
    scene policeman_s35_bikini_competition32
    p "Time for my reward..."
    scene policeman_s38_infront_cabin01 with dissolve
    beth "Hello, Detective?..."
    p "Oh... Bethany. What are you doing here?"
    scene policeman_s38_infront_cabin02
    beth "I have an offer for you."
    p "Which is?"
    beth "I know that you gave those pills to Sophia. But I remember first you wanted to give them to me, right?"
    p "Maybe?"
    beth "So how about a little fun as a reward for some pills?"
    p "Maybe. I will call you later. "
    beth "You have my number?"
    p "Yes... a friend gave it to me. (Thank you, Brandon.)"
    beth "Great!"
    scene policeman_s38_infront_cabin04
    sop "Hey, Beth... How are you..? Do you know my good friend?"
    beth "Yes, we've already met, a few times."
    sop "Great. By the way: How did you enjoy the competition?"
    scene policeman_s38_infront_cabin05
    beth "Nnn..! Shut up! You… You  plastic slut!"
    sop "No need to be so rude… I know what you want..."
    scene policeman_s38_infront_cabin06
    sop "You just want to hug them, right? Do you feel how heavy and smooth they are?"
    scene policeman_s38_infront_cabin07
    sop "Give them a kiss..."
    scene policeman_s38_infront_cabin08
    beth " Fu-Fuck you! Sophia! Fuck you!"
    scene policeman_s38_infront_cabin09
    beth "You will regret this."
    sop "We will see..."
    scene policeman_s38_infront_cabin03
    p "So, what about my reward?"
    sop "I will give you what you want, as I promised. Don’t you worry..."
    p "Great. I will call you later."
    sop "Oh... okay then. Once again, thank you for everything, truly."
    p "No problem."
    scene black_screen with fade
    scene city_map_night
    p "Phew, this was a really exciting day. Time to go back to the apartment."
    $ time_to_give_pills_to_sophia_for_bikini_competition = False
    $ time_of_day = Set_Time_of_Day('GECE')
    $ time_for_bed_after_bikini_competition = True
    $ hints_counter += 1
    jump city_map

label scene_coffee_shop_before_researching_scarlett_case:
    scene policeman_s36_coffee_shop01
    p "It’s quite busy in here today."
    scene policeman_s36_coffee_shop02
    p "What should I order? Something cheap... I don’t have much money."
    scene policeman_s36_coffee_shop03
    p "Shit!!!"
    mom "Owwuuuu!"
    scene policeman_s36_coffee_shop04
    p "I’m so sorry, Mom. I didn’t mean to!"
    scene policeman_s36_coffee_shop05
    p "Arghhh... I meant ma’am. I’m an idiot..."
    p "(Mom is still in the city?)"
    play sound 'sounds/effects/whoosh_sound.ogg'
    scene policeman_s36_flashback01 with dissolve
    p "(Again, Mom’s car in front of the hospital?)"
    scene policeman_s36_flashback01
    $ renpy.pause(4.0, hard=True)
    scene policeman_s36_flashback02 with dissolve
    play sound 'sounds/effects/whoosh_sound2.ogg'
    p "(And that’s Kate from the hospital. What does this mean? I must ask her.)"
    scene policeman_s36_flashback02
    $ renpy.pause(4.0, hard=True)
    scene policeman_s36_coffee_shop05
    stop sound fadeout 1.0
    p "Can I have..."
    play sound "sounds/effects/phone_ringing_sound.ogg"
    $ renpy.pause(1.0,hard=True)
    scene policeman_s36_coffee_shop06
    p "(...your number?)"
    mom "Yes... yes. I’m on the way."
    stop sound
    mom "I’m sorry, young man, but I must go now."
    scene policeman_s36_coffee_shop07
    p "Bye..."
    scene policeman_s36_coffee_shop08
    p "(...Mom.)"
    scene city_map
    p "Why is Mom still hanging around after the accident? I'm dead, right?"
    p "I should get back. I have things to do on Scarlett’s case, but later I must figure out why Mom is still in the city."
    $ time_for_coffee_and_researching_scarlett_case = False
    $ time_to_sort_through_scarlett_case_clues = True
    $ hints_counter += 1
    jump city_map

label scene_cop_apartment_sorting_through_scarlett_case_info:
    scene city_map
    scene black_screen with fade
    scene policeman_s36_clues01 with dissolve
    $ renpy.pause(2.0)
    scene policeman_s36_clues02
    p "I’ve spent a few hours sorting through all the clues, and what I’ve managed to piece together is:"
    scene policeman_s36_clues03
    p "Scarlett was hijacked by someone named Frank - or maybe it’s just a Nickname, because she’s protecting his identity - because she doesn’t want to transport drugs to Europe."
    p "He is going to be a big name in the criminal underworld of this city, so maybe she is dead already, for going against him, and I’m just wasting my time."
    p "I should sleep on it or maybe have some fun…. What about a threesome with Bethany and Sophia? Let’s call them..."
    scene policeman_s36_phoning_with_asia with dissolve
    p "Hello, Sophia, it’s John."
    sop "Hi, what do you need?"
    p "How about my reward?"
    sop "Of course! Do you want to visit me today?"
    p "No. Come to my apartment at 7:15 pm. The address is ……"
    scene policeman_s36_phoning_with_asia with fade
    sop "Sure, and have those pills ready too."
    p "Of course."
    p "Fine, and now Bethany."
    scene black_screen with fade
    $ renpy.pause(1.0)
    scene policeman_s36_phoning_with_asia with fade
    p "Hi, Beth. John Matrix here. I was thinking about you."
    beth "And..?"
    p "And what about if I give you a bottle of those pills for something in return?"
    beth "Aaahmmm... In about an hour at my flat?"
    p "No, I don’t have time before 7 pm."
    beth "Okay..."
    p "So how about visiting me at my apartment at 7 pm. The address is……"
    scene black_screen with fade
    $ renpy.pause(1.0)
    scene policeman_s36_phoning_with_asia with fade
    beth "Fine. See you tonight."
    p "Bye."
    p "Fine. Fun time has been ordered. Maybe I could clean the apartment a little, to make a better impression on the girls."
    scene policeman_s42_hidden_key01 # TEMP
    $ renpy.pause(1.0)
    scene policeman_s42_hidden_key02
    $ renpy.pause(1.0)
    scene policeman_s42_hidden_key03
    p "I don't think this will go down too well with the girls."
    scene policeman_s42_hidden_key04
    p "What's this? A key, obviously hidden behind here. I think I know, just the door it unlocks."
    $ cop_apartment_closet_door_unlocked = True
    $ hints_counter += 1 #TEMP
    #$ hints_counter = 72 # TEMP
    jump cop_apartment_closet
