label tutorial:
#Start with zoom animation. and little pause at the end.
#image tutorial_zoom_animation = Movie(channel="scenes/Megan/S00_tutorial/Megan_zoom.webm", play="scenes/Megan/S00_tutorial/Megan_zoom.webm", size=(1280,720), loops=0)
#show tutorial_zoom_animation
#$ renpy.pause(3.0, hard=True)
stop music fadeout (1.0)
play music "sounds/music/Funny_music_sugar_zone.ogg"
$ renpy.movie_cutscene("scenes/Megan/S00_tutorial/Megan_zoom.webm", delay=2.0, loops=0, stop_music=True) # TODO maybe a whoosing sound effect during animation.

scene megans00_02 #important lower_case
meg "Oh! Hello there. You look familiar. Have we met before? My name is Megan. And yours is?"

$ player_name = renpy.input("İsminiz nedir?")
$ player_name = player_name.strip()

if player_name == "":
    $ player_name = "MC"

meg "Nice to meet you, [player_name]. Welcome to this brand new game from Joraell."
jor "Apologies for breaking the 4th wall..."

scene megans00_02
meg "Have you played other games from Joraell before?"

menu:

    "Yes":
        scene megans00_03
        meg "I like hearing that! So as you can see, here you can also meet characters from previous titles, like me."

    "No":
        scene megans00_04
        "That’s a bit of a shame, but no need to worry. This is a brand new story - and maybe after finishing this one you will like it and give the previous games a try. You can find them on Joraell’s patreon site."


scene megans00_05
meg "So let’s start with the tutorial."
scene megans00_06
meg "On the top-right corner, you can see buttons showing you what part of the day it currently is now, in the game world."
meg "On this map: travelling couldn’t be easier - just one click on the place you want to visit, and your character is at that location. No more boring and repetitive walking."
scene megans00_07
meg "Larger buildings and destinations have their own smaller map - like this map of the school. You can just click on a room you want to go to, and you are there. No more path-finding in corridors required."
scene megans00_08
meg "Your character will have some special skills to utilise. Don’t worry. The game will introduce you to these at the appropriate time, and you can use them if you want."
meg "About graphics and animations: As always, there are some improvements from before, as you will see."
scene megans00_09
meg "And much like previous games, there will be a lot of new nice girls who you can hang out with."
scene megans00_10
meg "This game also has some secret galleries and bonus scenes. You can discover them during gameplay, and view them by clicking on the phone icon and then the gallery icon. Try to find all the secret galleries in the game."
scene megans00_01
$ renpy.pause()
jor "And that is it! We are at the end of the tutorial! Yay! Enjoy this game and let me know your thoughts by contacting me."

menu:
    jor "Do you want to watch the introduction? There is some really important information, to help you understand what you have to do in the game. If you haven’t seen it yet, I suggest watching it first.)"

    "Yes":
        jump play_intro

    "No":
        stop music
        jump mc_room
