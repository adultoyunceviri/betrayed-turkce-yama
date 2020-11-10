label scene_mom_walking_in_main_hall:
scene moms01_first_time01
p "(I think I know her... That looks like...)"
scene moms01_first_time02
p "(Oh! That’s my MOM!)"
scene moms01_first_time03
p "(She’s going into the dean’s office.)"
scene moms01_first_time04
p "(I need to talk with her.)"
scene moms01_first_time05
d "Hey! What do you think you are doing?"
scene moms01_first_time06
p "That is my mom!"
d "I know who she is - but what were you planning to do?"
p "I want to talk to her."
scene moms01_first_time08
d "About what? Did you even think about this?"
d "What were you going to say to her: Hi, Mom! It’s me - your dead son. But now I’m in this new body! Really..?"
p "Eeehm... you’re right. What was I thinking..?"
p "Okay, I will leave her alone."
scene moms01_first_time06
d "Good... I think it would be better for you to try and figure out where Brandon lives."
p "And YOU don’t know that?"
d "I know everything! But, as you know: my services aren’t cheap."
p "Oh, okay... I guess I’ll have to find that out. I’m sure it will be easy!"
#jor "This is the end of the current content in this version. Game will now self-destruct. Thanks for playing! See you in the next version."
#jump start
#scene outro with Pause (30.0)
#$ MainMenu(confirm=False)
#$ renpy.quit()
scene moms01_first_time09
d "Also, I mentioned to you before: should you need my help, you just have to ask."
d "I will give you my card."
scene moms01_first_time10
p "Hmm... Impossible made possible?"
d "Now you have two options. Good luck!"
p "(I guess I should look on my computer what this flash drive contains. It might have Brandon's info.)"
$ need_to_access_flash_drive_at_home = True
$ mom_in_main_hallway = False
$ hints_counter += 1
#TEMP
python:
    cursed_dollar = Item("Cursed Dollar", element="PuzzleItem12", image="100bill_inventory", cost=0)
    devil_card = Item("Devil Calling Card", element="PuzzleItem13", image="devil_card_inventory", cost=0)
$ inventory.add(devil_card)
jump main_hall


label scene_mom_and_sophia_in_restaurant:
    scene moms02_restaurant1
    mom "I must thank you again for your help, with all my son’s stuff."
    scene moms02_restaurant3
    sop "It’s fine: we’re both happy to help. Isn’t that right, Brandon?"
    scene moms02_restaurant4
    p "Of course!"
    scene moms02_restaurant2
    mom "And what are you both studying? Are you both on the same course?"
    scene moms02_restaurant3
    sop "I’m studying economics management and only see Brandon when we have a joined subject, like computers class."
    scene moms02_restaurant4
    p "Yeah, I’m helping her with computers, all the time."
    scene moms02_restaurant2
    mom "I see you’re never too busy to lend a helping hand. That is very nice of you."
    scene moms02_restaurant4
    p "Yes, my parents raised me properly."
    scene moms02_restaurant2
    mom "Being a parent is hard work and they have done a really good job with you."
    scene black_screen with dissolve
    $ renpy.pause(1.0)
    "Later that night..."
    scene brandon_sleeping_in_car with dissolve
    $ renpy.pause(1.0)
    p "(I really need to find out where Brandon lives...)"
    $ time_of_day = TimeOfDay_Dict[ TimeOfDay_Dict.keys()[TimeOfDay_Dict.values().index('SABAH')] ]
    $ hints_counter += 1
    jump city_map
