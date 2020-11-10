label ivana_spy_in_class:
scene black_screen
$ renpy.pause(0.1, hard=True)

scene ivanas01_04
$renpy.pause()
scene ivanas01_01
p "I guess I don't need to sit in classes anymore."
sop "(Poor [player_name]...)"
sop "(His whole life in front of him and he ends up like this. This world is so unfair...)"
scene ivanas01_02
p "Here's that foreign babe from the hallway..."
p "She seems to be really interested in what the teacher has to say."
iva "(He is so cute, talking about biology. I’m always really horny during his classes.)"
scene mranderss01_teaching01
p "Mr. Anders talking about biology? But nobody cares about that?"
scene ivanas01_03
p "Well she's definitely not shy about what she's wearing."
p "Now I’m really getting what Mr. Anders feels, when staring at her."
scene ivanas01_02
iva "(Hmm... I hope that package with the new bikini I ordered, arrives today. Damn, that will be nice.)"
p "It's really fun, hearing what they're thinking about."
scene ivanas01_05
d "Hehe... I see you're really enjoying this."
p "Yes, it's really good. Just... this form is starting to feel a little uncomfortable. "
d "It’s easy: Just find any simple victim for yourself and transform into them."
p "I was feeling around, but that looks unreachable for me. My skills seem to be too low for that."
scene ivanas01_06
d "Heh... Maybe it’s because you're looking in a school full of horny and smart girls."
d "For a start, you need to find someone really simple. And get a little practice on them."
p "Okay. But now I’m stuck in this classroom until Biology ends."
d "It's not a problem for me. Voila. Good luck!"
scene ivanas01_04
$ has_learned_about_posession = True
$ looking_for_someone_to_possess = True
$ hints_counter += 1
jump main_hall

label ivana_on_beach_after_class:
play music "sounds/music/Background_music2_Brunno.ogg"
scene ivanas02_beach1
p "Looks like she’s sleeping."
scene ivanas02_beach2
p "Oh! This spirit form has its benefits - I can enjoy all the finer details, up close."
scene ivanas02_beach3
p "Ivana is really hot! I will have to figure out, how to get with her."
scene ivanas02_beach4
$ renpy.pause()
p "I wonder if I can possess Ivana like this. No! That's not the way I want to be inside her. I should keep looking."
scene ivanas02_beach5
$ renpy.pause()
call screen beach_main
