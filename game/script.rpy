
define p = DynamicCharacter("player_name", color="#58D3F7")
define a = Character("Melek", color="#ffffff")
define d = Character("Şeytan", color="#ff0000")
define dr = Character("Sürücü", color="#ca1cff")
define meg = Character("Megan", color="#5765cd")
define iva = Character("Ivana", color="#5765cd")#TODO
define jor = Character("Joraell", color="#5a45c1")
define sop = Character("Sophia", color="#FF6600")
define pol = Character("Polis", color="#3366ff")
define kat = Character("Kate", color="#3366ff")
define asn = Character("Kız", color="#3366ff")
define trpd = Character("Sarışın", color="#3366ff")

define pp = Character("Sapık Polis", color="#3366ff")
define cllr = Character("Caller", color="#3366ff")#maybe same text colour as pp
define kdnppr = Character("Hırsız", color="#3366ff")#maybe same text colour as pp

define sec = Character("Kampüs Güvenliği", color="#3366ff")
define bncr = Character("Koruma", color="#3366ff")
define ownr = Character("Kulüp Sahibi", color="#3366ff")
define burt = Character("Burt", color="#3366ff")
define brst = Character("Barista", color="#3366ff")
define andr = Character("Bay Anders", color="#3366ff")
define hobo = Character("Evsiz Adam", color="#3366ff")
define beth = Character("Bethany", color="#3366ff")
define bran = Character("Brandon", color="#3366ff")
define dean = Character("Dekan", color="#3366ff")
define trcy = Character("Tracy", color="#3366ff")
define mom = Character("Annemin arkadaşı", color="#3366ff")
define scrlt = Character("Scarlett", color="#3366ff")
define brook = Character("Brooke", color="#c92886")
define comm = Character("Yorumcu", color="#3366ff")
define cap = Character("Kaptan", color="#3366ff")
define nick = Character("Nick", color="#3366ff")
define nrs = Character("Hemşire", color="#3366ff")
define bab = Character("Bayan Baber", color="#3366ff")
define jen = Character("Jen", color="#3366ff")
define reb = Character("Rebecca", color="#3366ff")
define crdlr = Character("Araba Satıcısı", color="#3366ff")
define sound_phone_ringing = "sounds/effects/Phone_ringing_sound.ogg"
define sound_snoring = "sounds/effects/snooring_effect_sound.ogg"
define sound_whipping = "sounds/effects/whip_sound.ogg"
define sound_knock = "sounds/effects/knocking_sound.ogg"
define sound_crash = "sounds/effects/broken_notebook.ogg"#TEMP
define sound_sms = "sounds/effects/sms_sound.ogg"
default saw_megan_scene_in_wc = False
default saw_ivana_scene_in_class = False
default saw_sophia_scene_in_apartment = False
default listened_to_sophia_with_policeman_in_mc_room = False
default mc_looked_at_small_box = False
default mc_looked_at_wardrobe = False
default mc_looked_at_bedside_table = False
default mc_looked_at_computer = False
default have_policemen_left_the_apartment = False
default currently_posessed_homeless_guy = False
default has_learned_about_posession = False
default have_taken_keys_from_sewer = False
default looking_for_someone_to_possess = False
default have_asked_intro_control_will_question = False
default have_asked_intro_invisibility_question = False
default have_asked_intro_why_rules_question = False
default money = 0
default tried_to_possess_hobo_during_day = False
default currently_possessed_brandon = False
default cost = 0
default mc_room_window_opened = False
default have_found_wire_at_warehouse = False
default can_show_inventory_button = True #
default in_cutscene_or_idle_scene = False
default have_showered_as_hobo = False
default bethany_and_brandon_in_pond = False
default return_label = ""
default special_inventory_display = False
default seen_hobo_mad = False
default have_looked_in_brandons_locker = False
default classes_have_started = False
default need_to_access_flash_drive_at_home = False
default need_to_access_flash_drive_at_school = False
default sophia_roommate_ad_placed = False
default ready_for_call_from_dealer = False
default beth_waiting_in_female_wc = False
default called_to_deans_office = False
default have_cursed_dollar_for_hobo = False
default mom_in_main_hallway = False
default given_hobo_cursed_dollar = False
default menu_can_show_inventory_hover = False
default menu_can_show_phone_hover = False
default menu_can_show_hint_hover = False
default gallery_added_to_phone = False#
default reputation_number = 0
default deans_password_count = 0
default deans_password_failed_attempts = 0
default deans_password_guess_highlanders = 0
default deans_password_guess_best_teacher = 0
default deans_password_guess_salou = 0
default deans_password_guess_brooke = 0
default deans_password_guess_mirapill = 0
default deans_password_guess_certificates = 0
default deans_office_know_about_lab = False
default deans_office_have_got_on_computer = False
default have_brandons_phone = False # TODO update variable for old saves
default are_hints_available = True #
default enable_shopping = False
default has_stuff_been_moved_from_apartment = False
default is_taxi_stand_available = False
default need_to_take_taxi_to_brandons_house = False
default seen_secret_pics_mc_computer = False ## TODO updat variable
default seen_secret_pics_brandon_flash_drive = False
default current_screen = ""
default deans_office_secret_found = False
default secret_locker_secret7_found = False
default sophia_waiting_for_cop_in_her_apartment = False
default sophia_in_her_room_for_webshow = False
default had_first_web_show_with_sophia_as_scarlett = False


default DayOfWeek_Dict = { 1: 'PAZAR', 2: 'PAZARTESİ', 3: 'SALI', 4: 'ÇARŞAMBA', 5: 'PERŞEMBE', 6: 'CUMA', 7: 'CUMARTESİ' }
default day_of_week = DayOfWeek_Dict[ DayOfWeek_Dict.keys()[DayOfWeek_Dict.values().index('PAZARTESİ')] ]#mydict.keys()[mydict.values().index(16)]
default TimeOfDay_Dict = { 1: 'SABAH', 2: 'ÖĞLEN', 3: 'AKŞAM', 4: 'GECE' }
default time_of_day = TimeOfDay_Dict[ TimeOfDay_Dict.keys()[TimeOfDay_Dict.values().index('SABAH')] ]
default hints_counter = 0
default hint_system_dict = {0: 'Hint: Görünüşe göre hiçbir şeye dokunamıyorsun. Odadaki her şeyi kontrol etmeye çalış.',
1: 'Hint: Sophia ve polisin ne hakkında konuştuğunu öğrenmeye çalış.',
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
    57: 'Hint: You should go visit Ivana at her apartment.',
    58: 'Hint: There is something here. You just need to look carefully.',
    59: 'Hint: You shoud go back to the apartment.',
    60: 'Hint: You need to put together the evidence about Anders. Everything needed is on the table.',
    61: 'Hint: You\'re tired. You should go to bed',
    62: 'Hint: You need to make your way to the police station.',
    63: 'Hint: You should talk with Brandon.',
    64: 'Hint: You need to visit the computer class.',
    65: 'Hint: You need to deliver the Anders evidence to the Dean in her office.',
    66: 'Hint: You should hurry. Sophia is waiting for you on the beach.',
    67: 'Hint: It\'s been a long day. You should get some sleep.',
    68: 'Hint: You have a craving for coffee today. Get over to the shop.',
    69: 'Hint: You need to look over all the clues you have, at the apartment.',
    70: 'Hint: The key you found is for the locked door. See what other skeletons are in this cop\'s closet.',
    71: 'Hint: You have some time before meeting the girls. Go check out the address on the key.',
    72: 'Hint: You should find a way to check inside these rooms.',
    73: 'Hint: Scarlett was living with Ivana before she was kiddnaped. Try Ivana’s apartment first.',
    74: 'Hint: That did not go as well as expected. Hope that things go better with Sophia.',
    75: 'Hint: Remember, you need to pick up Scarlett\'s stuff at the police station.',
    76: 'Hint: You need to change out of these sex den clothes.',
    77: 'Hint: Choose the shoes you would be comfortable wearing.',
    78: 'Hint: Before going to bed, you should check out what\'s in that big box.',
    79: 'Hint: You should talk to Sophia and see what\'s new.',
    80: 'Hint: You should talk with the Dean about Scarlett\'s absence. She should be in her office upstairs.',
    81: 'Hint: You need to pee. You should probably take care of that, or your panties will experience a disaster.',
    82: 'Hint: You found Megan. You need to talk to her about the pills.',
    83: 'Hint: You need to find work, to make money for the rent. Maybe the coffee shop is hiring. You could also check the hospital, to see if your mom’s car is still there.',
    84: 'Hint: The barista joked about the strip bar. But maybe it\'s not such a bad idea. It could be a good oportunity to make fast money.',
    85: 'Hint: You didn\'t get the money for Sophia. You have no choice but to accept her offer. Hopefully she is still awake.',
    86: 'Hint: Sophia seems excited about doing the camshow with you. Why don\'t you try it?',
    87: 'Hint: One way or another, you have the money for the rent. Time to pay Sophia. Hopefully she is still awake.',
    88: 'Hint: It\'s been a long and stressful day. Time for bed.',
    89: 'Hint: You should check the hospital again for your mom\'s car.',
    90: 'Hint: Megan needs your help in the lab. You shouldn\'t keep her waiting too long.',
    91: 'Hint: You need to use the toilet again. Testing pills is hard work.',
    92: 'Hint: You need to check if your mom is still at the hospital.',
    93: 'Hint: Nothing else to do right now but go home.',
    94: 'Hint: Time for bed.',
    95: 'Hint: You found the pill in your clothes yesterday. You should return it to Megan.',
    96: 'Hint: You need to buy Megan her coffee. Did you forget?',
    96: 'Hint: You need to buy Megan her coffee. Did you forget?',
    97: 'Hint: You need to find Sophia and Ivana right now. Search the school.',
    98: 'Hint: There\'s someone in the stall.',
    99: 'Hint: They don\'t seem to be downstairs. Have you tried upstairs.',
    100: 'Hint: It would be better to hide the pills in a safe place in your apartment.',
    101: 'Hint: Head to the coffee shop with Megan.',
    102: 'Hint: The girls should already be waiting for you in your apartment.',
    103: 'Hint: Don\'t you think it\'s time for a shower?',
    104: 'Hint: You need to find a good place to hide the pills.',
    105: 'Hint: You need to be at the Dean’s office before Megan arrives.',
    106: 'Hint: You need to talk with Sophia. She should be in the computer classroom.',
    107: 'Hint: You saw Ivana leaving the school. See if you can catch up with her.',
    108: 'Hint: Now you have three options: Visit Anders\' office, go to the beach with Ivana or go shopping with Sophia.',
    109: 'Hint: You have another meeting with the girls in your living room.',
    110: 'Hint: You look really tired right now. Get some sleep.',
    111: 'Hint: Today is Vengeance Day! You have work to do in the school gym.',
    112: 'Hint: You need to find Brooke and Beth\'s locker room.',
    113: 'Hint: You need to find the locker room keys right now.',
    114: 'Hint: You have the locker room keys. Try them out.',
    115: 'Hint: You need to hide Scarlett somewhere. Search for a good place.',
    116: 'Hint: Now that interruptions are over, you must find both Brooke’s and Bethany’s lockers.',
    117: 'Hint: Everything is ready. Head over to the main sports hall.',
    118: 'Hint: Brooke and Bethany looked so damn horny in the sports hall. Might be fun to check on them.',
    119: 'Hint: You need to have some excuse for being inside their locker room. They must be all hot and sweaty after the tournament.',
    120: 'Hint: You have the drinks. Head over to the bad girls locker room.',
    121: 'Hint: You look tired after all that fucking and cumming. You need to find the keys to Anders’ apartment. He probably keps them in his office.',
    122: 'Hint: You look like a walking corpse. You probably won\'t make it to the apartment. You should find another place to rest for a bit.',
    123: 'Hint: You have a class to teach right now, and you are late. Remember which class was Anders\'?',
    124: 'Hint: Now you have time to find the keys for Anders\' apartment.',
    125: 'Hint: You found the keys. Time to check out Anders\' apartment.',
    126: 'Hint: After spending the night on Anders\' office couch, you stink like a pig.',
127: 'Hint: Did you search the whole flat?',
    128: 'Hint: Now is time for a proper sleep.',
    129: 'Hint: You have a class at school. And this time you don\'t want to be late.',
    130: 'Hint: You found out Scarlett is in the hospital. Better check on her and see what she remembers.',
    131: 'Hint: You smell like a doctor. Don\'t you hate that hospital smell? Better head home and wash up.',
    132: 'Hint: Rebecca is watching TV in the livingroom. Better go explain yourself to her.',
    133: 'Hint: It’s late. Better go to bed.',
    #After morning:
    134: 'Hint: You need to go to school and teach Anders’ class.',

    #After Megan talk:
    135: 'Hint: Remember, Anders’ class is in classroom one.',

    #After class:
    136: 'Hint: The class is taken care of. You should have time to check Anders’ laptop in his office.',

    #After checked laptop:
    137: 'Hint: You need to collect the Mirapill notes in Anders’ flat.',

    #Obtain Rebecca DNA:
    138: 'Hint: For the DNA, blood or bodily fluids is required. What about looking for some hygene products?',

    #after found toothbrushes:
    139: 'Hint: You now have everything you came for. Time to head to Megan’s lab.',

    #after Megan’s lab:
    140: 'Hint: Megan doesn’t have time to do the test, but referred you to her friend at the hospital.',

    #after hospital:
    141: 'Hint: It’s evening already. Rebecca is probably back home from town.',

    #before Rebecca goes to bed:
    142: 'Hint: You were too late to give Rebecca her present. Catch her before she goes to sleep',
    #next morning:
    143: 'Hint: As with every school morning, you have to give some work to Anders’ students.',


    #After class:
    144: 'Hint: It’s time to pick up the DNA results from the hospital.',

    #after hospital:
    145: 'Hint: Go get Rebecca from home and head out to the restaurant for lunch.',

    #after shopping:
    146: 'Hint: Now is a good time to tell Rebecca about the DNA results.',

    #After ressults talk:
    147: 'Hint: It’s about time to get some sleep.',

    #morning:
    148: 'Hint: Again, you need to give work to Anders’ class.',

    #after class:
    149: 'Hint: Time to pick up Rebecca.',

    #After shower:
    150: 'Hint: Rebecca is waiting for you in the livingroom, for the date.',

    #Rebecca left early:
    151: 'Hint: Rebecca went home early. But you have a party tomorrow. Get some rest.',

    #didnt fuck rebecca
    152: 'Hint: You didn\'t give in to temptation. Well done. Nothing more to do but go to bed.',

    #shower fucked rebecca secretly:
    153: 'Hint: You had your fun. Better get a shower now. Rebecca is leaving early tomorrow.',

    #shower fucked rebecca mutually:
    154: 'Hint: Rebecca is sleeping in, after last night. You have time for a shower. You stink.',

    #reb about to leave:
    155: 'Hint: Rebecca is leaving today. She\'s waiting for you in the living room.',

    #reb seen off:
    #156: 'Hint: You have that volleyball winners party today. Better head to class for now.',

    #After talking with Devil/Angel during TV:
    156: 'You need to visit the Dean’s office. As per her text.',

    #If working for Brooke:
    157: 'The Dean said Brooke was looking for you. She should be in the computer class.',

    #After dean:
    158: 'Your powered friend is waiting for you at the restaurant in the shopping centre.',

    #After lunch:
    159: 'Before going to the party, you need to look the part. Go get changed.',

    #after:
    160: 'Time to party! Head over to your old apartment.',

    #At party:
    161: 'You have time to look around and talk with some people.',

    #After talk to Sophia:
    162: 'Ivana is in the kitchen.',

    #After Ivana talk:
    #If working for Brooke:
    163: 'Now is the time to put the pills into drinks',

    #if not working for Brooke:
    164: 'Head to the living room. The girls want to get the party started.',

    #After party started:
    165: 'You need to get the pills from the hidden place in your old room.',

    #After talk to scarlett:
    166: 'You should help Scarlett to find her flash drive.',

    #after helped Scarlett:
    167: 'Now the room is clear. You can retrieve your pills.',

    #after:
    168: 'You have all the pills. Time to have some fun at the party. Go to the livingroom.',

    #after party:
    169: 'The party is over. It’s time to go to sleep.',

    #At morning:
    170: 'You need to talk with Megan in the lab.',

    ##after:
    171: 'Hopefully Brooke is in computer class.',

}
default current_hint = hint_system_dict[hints_counter]
default show_bonus_button_on_phone = False # TEMP
default show_exgf_button_on_phone = False
default told_truth_to_dean = False
default is_cops_apartment_available = False
default have_changed_clothes_as_cop = False
default have_left_panties_in_cops_bedroom = False
default devil_broke_cop_computer = False
default hospital_location_available = False
default scarlett_questions_address_asked = False
default scarlett_questions_enemies_asked = False
default scarlett_questions_issues_asked = False
default brandon_waiting_at_warehouse_for_cop = False
default ready_for_cop_asian_night_scene = False
default cop_needs_to_visit_dean = False
default cop_needs_to_visit_dean_again = False
default scarlett_questions_anders_relationship_with_her_asked = False
default scarlett_questions_often_meeting_with_anders_asked = False
default scarlett_questions_when_anders_saw_her_last_asked = False
default scarlett_questions_anders_relationship_with_ivana_asked = False
default scarlett_questions_ask_anders_if_anything_else_asked = False
default ivana_apartment_available = False
default scarlett_questions_ivana_relationship_with_her_asked = False
default scarlett_questions_is_ivana_russian_asked = False
default scarlett_questions_ivana_about_anders_asked = False
default scarlett_questions_ivana_last_time_saw_her_asked = False
default cop_can_hear_muffled_voice = False
default helped_trapped_girl = False
default cop_ready_to_request_pills_from_megan = False
default ready_to_sneak_into_anders_office_stage = 0
default looking_for_ivana_in_school_after_searching_anders_office = False
default been_to_ivanas_apartment_first_time = False
default made_entrapment_deal_with_ivana = False
default cop_ready_to_collect_pills_from_megan = False
default need_cops_gun = False
default know_sofias_room_is_unlocked = False
default ready_for_cop_angel_night_scene = False
default have_apointment_at_hospital = False
default anders_office_found_flash_drive = False
default anders_office_found_key = False
default ready_to_sleep_first_time_as_cop = False
default currently_possessed_cop = False
default anders_office_secret_found = False
default chose_to_sell_drugs_to_brandon = False
default cop_ready_for_night_sophia_dream = False
default sophia_arguing_with_brandon_in_main_hall = False
default scarlett_questions_sophia_relationship_with_her_asked = False
default scarlett_questions_sophia_last_time_saw_her_asked = False
default anders_office_trashed = False
default scarlett_questions_sophia_apartment_scarlett_anders_arangement_asked = False
default scarlett_questions_sophia_apartment_relationship_with_her_asked = False
default scarlett_questions_sophia_apartment_about_diary_asked = False
default drug_sell_choice_consequence_time = False
default time_to_meet_brandon_at_warehouse_for_drug_sale = False
default had_dinner_with_angel_after_no_drug_sell_and_helped_trapped_girl = False
default morning_after_drug_sell_choice_consequenses = False
default time_for_bed_after_drug_selling_choice_consequences = False
default devil_or_angel_explained_the_secret_of_the_pills = False
default accepted_devils_offer_for_anders_soul = False
default gym_location_available = False
default looking_for_sophia_about_pills_progress = False
default done_anders_sting_operation_at_ivanas = False
default anders_desk_secret_found = False
default as_cop_ready_to_search_for_scarlets_diary = False
default found_scarletts_flash_drive = False
default night_before_interrogation_consequence_time = False
default time_for_bed_before_interrogation = False
default police_station_location_available = False
default as_cop_ready_to_interrogate_brandon = False
default time_to_deliver_anders_documents_to_dean = False
default time_to_give_pills_to_sophia_for_bikini_competition = False
default time_to_look_at_scarletts_flash_drive = False
default time_for_coffee_and_researching_scarlett_case = False
define time_for_bed_after_bikini_competition = False
define asian_called_to_offer_work = False
define time_to_sort_through_scarlett_case_clues = False
define cop_apartment_closet_door_unlocked = False
define den_location_available = False
define thought_about_using_chair_in_den_basement = False
define have_checked_den_basement_room_1 = False
define have_checked_den_basement_room_2 = False
define have_checked_den_basement_room_2 = False
define have_checked_den_basement_room_3 = False
define have_checked_den_basement_room_5 = False
define fucked_scarletts_ass_in_den_room4 = False
default scarletts_room_secret_found = False
default currently_possessed_scarlett = False
default scarlett_kicked_out_of_ivanas_apartment = False
default strip_club_location_available = False
default have_gotten_old_apartment_room_back = False
default need_to_get_scarlets_stuff_from_police_station = False
default have_opened_scarletts_box = False
default have_changed_clothes_as_scarlett = False
default current_dildo_choice = 1
default settled_as_scarlett = False
default have_talked_to_sophia_in_kitchen_as_scarlett = False
default have_talked_to_dean_as_scarlett_to_reenroll = False
default need_to_pee_as_scarlett = False
default looking_for_a_job_as_scarlett = False
default turned_down_strip_club_owner = False
default have_talked_with_beth_and_brooke_in_dining_hall = False
default have_to_pay_first_rent_to_sophia_as_scarlett = False
default have_paid_first_rent_to_sophia_as_scarlett = False
default have_been_woken_up_morning_after_paid_first_rent = False
default double_check_the_hospital_after_paying_first_rent = False
default checking_hospital_again_after_first_lab_tests = False
default have_to_tell_sophia_about_beth_brooke_talk = False
default time_to_find_growing_pill_on_clothes = False
default need_to_sleep_after_finding_pill_on_clothes = False
default have_to_return_found_pill_to_meg = False
default have_to_get_meg_coffee_from_shop = False
default have_a_bunch_of_pills_to_test_on_ivana_and_sophia = False
default megan_desperately_needs_scarlett_in_lab = False
default as_scarlett_feeling_weird_after_first_lab_tests = False
default have_used_sex_toy_that_night_as_scarlett = False
default have_used_dildo_3_as_scarlett_before = False
default had_web_show_with_sophia_that_night = False
default cafeteria_room_secret_found = False
default mc_scarlett_upstairs_when_looking_for_ivana_n_sophia_available = False
default rep_choice_mc_scarlett_watched_meg_jacking_in_stall = False
default have_accepted_anders_offer_for_scarlett_help = False
default need_to_hide_unlabebeled_pills_in_apartment = False
default have_to_meet_megan_at_coffee_shop = False
default time_to_test_unlabelled_pills_on_ivana_n_sophia = False
default mc_scarlett_needs_shower_after_threesome = False
default need_to_hide_pills_after_threesome = False
default waking_up_in_the_morning_after_threesome = False
default mc_scarlett_leaving_apartment_morning_after_threesome = False
default need_to_meet_meg_in_deans_office_after_threesome = False
default need_to_tell_sophia_about_pills_colour_change = False
default time_to_see_ivana_after_threesome_outside_school = False
default time_for_afternoon_choices_after_pills_colouring = False
default time_to_meet_up_with_ivana_n_sophia_after_choices_afternoon = False
default mc_scarlett_refused_anders_offer_for_scarlett_help = False
default time_to_sleep_after_choices_afternoon = False
default time_to_punish_beth_n_brooke_in_sports_hall = False
default have_gym_janitors_key = False
default have_found_bad_girls_locker_room = False
default currently_possessed_anders = False
default mc_anders_need_to_hide_scarlett_somewhere = False
default mc_anders_needs_to_finish_what_mc_scarlett_started = False
default mc_anders_has_spiked_beths_drink = False
default mc_anders_has_spiked_brookes_drink = False
default mc_anders_spiked_drinks_fun_begins = False
default janitors_closet_secret_found = False
default mc_scarlett_accepted_devils_help_with_anders = False
default phone_secrets_current_page = 1
default phone_secrets_max_pages = 2
default bad_girls_lose_volleyball_horny = False
default mc_anders_has_drink_for_horny_bad_girls = False
default mc_anders_needs_to_find_anders_keys_in_office = False
default mc_anders_late_for_anders_class = False
default mc_anders_taught_anders_class = False
default mc_has_keys_to_anders_house = False
default mc_anders_has_whipped_devil = False
default anders_apartment_available = False
default mc_anders_found_cash_in_anders_bathroom_cabinet = False
default mc_anders_found_cash_in_anders_bedroom_drawer = False
default mc_anders_found_cash_in_anders_kitchen_drawer = False
default mc_anders_found_cash_in_anders_guestroom_drawer = False
default mc_anders_found_cash_in_anders_livingroom_drawer = False
default mc_anders_found_anders_life_savings_behind_loose_tile = False
default mc_anders_found_cash_in_anders_livingroom_vase = False
default mc_anders_settled_in_as_anders = False
default anders_livingroom_laptop_folders_visible = False
default mc_anders_took_a_shower_before_getting_settled = False
default mc_anders_found_anders_pills_connection_in_anders_livingroom = False
default mc_anders_caught_rebecca_in_shower_milestone = False
default mc_anders_wants_to_visit_scarlett_in_hospital = False
default mc_anders_needs_a_shower_after_visiting_hospital = False
default mc_anders_needs_to_apologise_to_rebecca_for_shower_incident = False
default rebecca_is_watching_movie_after_shower_incident = False
default rebecca_room_secret8_found = False
default toggle_mc_scarlett_chose_ivana = False
default toggle_mc_scarlett_chose_sophia = False
default toggle_searching_for_rebeccas_dna_toothbrush_enabled = False
default toggle_rebecca_left_anders_apartment_early = False
default toggle_mc_anders_had_sex_with_rebecca = False
default toggle_mc_anders_played_nice_with_rebecca = False
default toggle_mc_anders_took_second_chance_to_fool_around_with_rebecca = False
default onetime_mc_anders_needs_to_search_apartment_for_rebeccas_dna = False
default onetime_megan_asks_to_speak_to_mc_anders_in_school = False
default onetime_mc_anders_needs_to_teach_class_third_time = False
default onetime_mc_anders_needs_to_check_anders_laptop_for_pills_info = False
default onetime_mc_anders_needs_to_get_file_in_apartment_for_megan = False
default onetime_mc_anders_needs_to_deliver_pills_file_to_megan = False
default onetime_megan_referred_mc_anders_to_kate_at_hospital = False
default onetime_mc_anders_too_late_for_shopping_with_rebecca = False
default onetime_mc_anders_fourth_time_teaching = False
default onetime_mc_anders_needs_to_collect_dna_results = False
default onetime_mc_anders_out_on_the_town_with_rebecca = False
default onetime_mc_anders_heading_home_after_rebecca_restaurant_date = False
default onetime_mc_anders_needs_to_sleep_after_shopping_with_rebecca = False
default onetime_mc_anders_about_to_meet_scarlett_back_at_school = False
default onetime_mc_anders_asked_sophia_to_watch_his_fifth_class = False
default onetime_mc_anders_late_for_restaurant_date_with_rebecca = False
default onetime_mc_anders_heading_home_after_rebecca_restaurant_date = False
default onetime_time_for_bed_after_mc_anders_and_rebecca_restaurant_date = False
default onetime_mc_anders_needs_shower_after_night_with_rebecca = False
default onetime_time_for_bed_after_mc_anders_and_rebecca_restaurant_date = False
default onetime_mc_anders_needs_to_see_rebecca_off_in_the_morning = False
default onetime_mc_anders_has_seen_rebecca_off_and_is_ready_to_party = False
default milestone_mc_anders_took_pill_notes_in_apartment_for_megan = False
default milestone_mc_anders_received_dna_results = False
default milestone_mc_anders_went_shopping_with_rebecca = False
default milestone_mc_anders_showed_rebecca_dna_results = False
default mc_anders_and_rebecca_store_count = 0
default toggle_mc_anders_anders_didnt_have_enough_for_rebecca_shopping = False
default toggle_mc_anders_visited_jewelery_store_with_rebecca = False
default toggle_mc_anders_visited_clothing_store_with_rebecca = False
default numtype_mc_anders_bought_car_for_rebecca = 0
default rebecca_jewelery_view_counter = -1
default toggle_rebecca_jewelery_viewed_pearl_necklace = False
default toggle_rebecca_jewelery_viewed_gold_necklace = False
default toggle_rebecca_jewelery_viewed_gold_piercing = False
default toggle_rebecca_jewelery_viewed_golden_earrrings = False
default toggle_rebecca_jewelery_viewed_gold_ring = False
default jewelery_store_secret9_found = False
default toggle_rebecca_left_anders_apartment_happy = False
default onetime_mc_anders_needs_to_talk_to_dean_before_party = False
default onetime_mc_anders_time_for_restaurant_before_party = False
default onetime_mc_anders_needs_to_see_brooke_before_restaurant_party= False
default onetime_mc_anders_needs_to_find_clothes_for_the_party = False
default onetime_mc_anders_ready_for_winners_party = False
default toggle_mc_anders_talked_to_sophia_at_winners_party = False
default toggle_mc_anders_talked_to_tracyandbrandon_at_winners_party = False
default toggle_mc_anders_talked_to_ivana_at_winners_party = False
default toggle_mc_anders_fucked_ivana_in_office = False
default milestone_winners_party_sophia_asked_for_drinks = False
default onetime_mc_anders_looking_for_scarletts_flash_drive = False
default milestone_mc_anders_found_scarletts_flash_drive = False
default onetime_mc_anders_time_to_recover_pills_from_bedstand = False
default milestone_mc_anders_recovered_pills_from_scarletts_bedstand = False
default toggle_mc_anders_spilled_megans_spiked_drink_winners_party = False
default counter_sleeping_girls_winners_party = 0
default toggle_winners_party_sleeping_girls_chose_megan = False
default toggle_winners_party_sleeping_girls_chose_sophia = False
default toggle_winners_party_sleeping_girls_chose_tracy = False
default toggle_winners_party_sleeping_girls_chose_scarlett = False
default toggle_winners_party_sleeping_girls_chose_ivana = False
default toggle_mc_anders_used_horny_pill_on_megan_after_winners_party = False
default onetime_time_to_go_to_sleep_after_winners_party = False
default onetime_time_for_at_school_consequences_of_winners_party = False
default milestone_winners_party_over = False
default onetime_mc_anders_needs_talk_brooke_morning_after_winners_party = False
default onetime_mc_anders_has_idea_to_transfer_into_someone_close_to_brooke = False
default toggle_mc_anders_spiked_drinks_at_winners_party = False
default toggle_mc_anders_viewed_webshow_at_winners_party = False
default winners_party_livingroom_secret10_found = False
default winners_party_scarletts_room_secret11_found = False

default anders_phone = Item("Telefon", element="PuzzleItem25", image="andersphone_inventory", cost=0)
default unlabeled_pills = Item("Etiketsiz Haplar", element="PuzzleItem26", image="unlabeledpills_inventory", cost=0)
default shrinking_pills = Item("Küçültücü Haplar", element="PuzzleItem27", image="shrinkingpills_inventory", cost=0)
default horny_pills = Item("Azdırıcı Haplar", element="PuzzleItem28", image="hornypills_inventory", cost=0)
default anders_keys  = Item("Anders'ın Anahtarları", element="PuzzleItem29", image="anderskeys_inventory", cost=0)
default money_bag  = Item("Para Çantası", element="PuzzleItem30", image="money_bag_inventory", cost=0)
default assorted_pills = Item("Çeşitli Haplar", element="PuzzleItem31", image="assortedpills_inventory", cost=0)
default sleeping_pills = Item("Uyku Hapları", element="PuzzleItem32", image="sleepingpills_inventory", cost=0)
default growing_pills = Item("Büyütücü Pills", element="PuzzleItem33", image="growingpills_inventory", cost=0)
default reducing_pills = Item("Azaltıcı Haplar", element="PuzzleItem34", image="reducingpills_inventory", cost=0)

#if music_continue == True:
        #$ music_continue = False
        #$ renpy.music.stop(channel="music1", fadeout=1)
        #$ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)

label splashscreen3:
    scene black
    $ renpy.pause(1.0, hard=True)

    show news with dissolve
    $ renpy.pause(0.5, hard=True)
    $ renpy.pause(4.5)

    scene black with dissolve
init -1 python:

    renpy.music.register_channel("music1", "music")
    renpy.music.register_channel("music2", "music")
    def HaveLookedAtAllItemsInMCRoom():
        if mc_looked_at_small_box and mc_looked_at_wardrobe and mc_looked_at_bedside_table and mc_looked_at_computer:
            return True
        else:
            return False
    def Set_Time_of_Day(timeValue):
        return TimeOfDay_Dict[ TimeOfDay_Dict.keys()[TimeOfDay_Dict.values().index(timeValue)] ]
    def Increment_Time_Of_Day():
            if time_of_day == 'SABAH':
                temp = Set_Time_of_Day('ÖĞLEN')
            elif time_of_day == 'ÖĞLEN':
                temp = Set_Time_of_Day('AKŞAM')
            elif time_of_day == 'AKŞAM':
                temp = Set_Time_of_Day('GECE')
            else:
                temp = 'GECE'
            return temp
    def BuyItems():
        for item in shop_stock.items:
            inventory.buy(item)
            if item.isSelected == True:
                inventory.buy(item)
                #shop_stock.drop(item)

    import renpy.store as store
    import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
    from operator import attrgetter # we need this for sorting items

    inv_page = 0 # initial page of teh inventory screen
    item = None
    class Player(renpy.store.object):
        def __init__(self, name, max_hp=0, max_mp=0, element=None):
            self.name=name
            self.max_hp=max_hp
            self.hp=max_hp
            self.max_mp=max_mp
            self.mp=max_mp
            self.element=element
    player = Player("Derp", 100, 50)

    class Item(store.object):
        def __init__(self, name, player=None, hp=0, mp=0, element="", image="", cost=0, isSelected=False):
            self.name = name
            self.player=player # which character can use this item?
            self.hp = hp # does this item restore hp?
            self.mp = mp # does this item restore mp?
            self.element=element # does this item change elemental damage?
            self.image=image # image file to use for this item
            self.cost=cost # how much does it cost in shops?
            self.isSelected=isSelected
        def use(self): #here we define what should happen when we use the item
            if self.hp>0: #healing item
                player.hp = player.hp+self.hp
                if player.hp > player.max_hp: # can't heal beyond max HP
                    player.hp = player.max_hp
                inventory.drop(self) # consumable item - drop after use
            elif self.mp>0: #mp restore item
                player.mp = player.mp+self.mp
                if player.mp > player.max_mp: # can't increase MP beyond max MP
                    player.mp = player.max_mp
                inventory.drop(self) # consumable item - drop after use
            else:
                player.element=self.element #item to change elemental damage; we don't drop it, since it's not a consumable item

    class Inventory(store.object):
        def __init__(self, money=10, isShop = False):
            self.money = money
            self.items = []
            self.isShop = isShop
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)
        def buy(self, item):
            if self.money >= item.cost:
                self.items.append(item)
                self.money -= item.cost
        def empty(self):
            del self.items [:]

    def item_use():
        item.use()

    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"
    style.tips_top.size=14
    style.tips_top.color="fff"
    style.tips_top.outlines=[(3, "6b7eef", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    style.tips_top.size=20
    style.tips_bottom.outlines=[(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.tips_bottom.kerning = 2

    style.button.background=Frame("gui/frame.png",25,25)
    style.button.yminimum=52
    style.button.xminimum=52
    style.button_text.color="000"


    showitems = True #turn True to debug the inventory
    # def display_items_overlay():
        # if showitems:
            # inventory_show = "Money:" + str(inventory.money) + " HP: " + str(player.hp) + " bullets: " + str(player.mp) + " element: " + str(player.element) + "\nInventory: "
            # for i in range(0, len(inventory.items)):
                # item_name = inventory.items[i].name
                # if i > 0:
                    # inventory_show += ", "
                # inventory_show += item_name

            # ui.frame()
            # ui.text(inventory_show, color="#000")
    # config.overlay_functions.append(display_items_overlay)

#screen inventory_button:
    #textbutton "Show Inventory" action [ Show("inventory_screen"), Hide("inventory_button")] align (.95,.96)
    #if can_show_inventory_button == False and in_cutscene_or_idle_scene == False:
    #    imagebutton:
    #        idle "inventory_button_idle"
    #        hover "inventory_button_glow"
    #        xpos 3 ypos 3
    #        action [Show("inventory_screen"), SetVariable("can_show_inventory_button", False)] #activate_sound "sounds/se_backpack.ogg"

screen inventory_screen:


    add "inventory/inventory.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    #use battle_frame(char=player, position=(.97,.20)) # we show characters stats (mp, hp) on the inv. screen
    #use battle_frame(char=dog, position=(.97,.50))
    #hbox align (0.95,0.96) spacing 20:
    #    textbutton "Close Inventory" action [ Hide("inventory_screen"), Show("inventory_button")]#Return(None)
    imagebutton:
        idle "inventory_close"
        hover "inventory_close_glow"
        xpos 605 ypos -1
        if special_inventory_display:
                action [SetVariable("can_show_inventory_button", True), Hide("inventory_screen"), SetVariable("special_inventory_display", False), Jump(return_label)]
        else:
            action [SetVariable("can_show_inventory_button", True), Hide("inventory_screen")]
    text _("{color=#004503}[money]"):
        xpos 545 ypos 690
        size 25
    $ x = 140 # coordinates of the top left item position
    $ y = -30
    $ i = 0

    $ sorted_items = sorted(inventory.items, key=attrgetter('element'), reverse=True) # we sort the items, so non-consumable items that change elemental damage (guns) are listed first
    $ next_inv_page = inv_page + 1
    if next_inv_page > int(len(inventory.items)/9):
        $ next_inv_page = 0
    for item in sorted_items:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 200
            if i%3==0:
                $ y += 200
                $ x = 140
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "") # we use tooltips to describe what the item does.
            imagebutton:
                idle pic
                hover pic.replace("inventory", "inventory_glow")
                xpos x
                ypos y
                action [Hide("gui_tooltip"), SetVariable("item", item), item_use] hovered [ Play ("sound", "sfx/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) ] unhovered [Hide("gui_tooltip")] at inv_eff
                #Hide("inventory_screen")
            if player.element and (player.element==item.element): #indicate the selected gun
                add "gui/selected.png" xpos x ypos y anchor(.5,.5)
        $ i += 1
        if len(inventory.items)>9:
            textbutton _("Next Page") action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")] xpos .475 ypos .83

screen shopping_screen:

    add "inventory/shop.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    #use battle_frame(char=player, position=(.97,.20)) # we show characters stats (mp, hp) on the inv. screen
    #use battle_frame(char=dog, position=(.97,.50))
    #hbox align (0.95,0.96) spacing 20:
    #    textbutton "Close shopping" action Hide("shopping_screen")#Return(None)
    imagebutton:
        idle "inventory_close"
        hover "inventory_close_glow"
        xpos 605 ypos -1
        action [Hide("shopping_screen")]
    imagebutton:
        idle "buy_button"
        hover "buy_button_glow"
        xpos 476 ypos 745
        action Function(BuyItems)

    text _("{color=#004503}[cost]"):
        xpos 535 ypos 690
        size 25
    $ x = 140 # coordinates of the top left item position
    $ y = -30
    $ i = 0

    $ sorted_items = sorted(shop_stock.items, key=attrgetter('element'), reverse=True) # we sort the items, so non-consumable items that change elemental damage (guns) are listed first
    $ next_inv_page = inv_page + 1
    if next_inv_page > int(len(shop_stock.items)/9):
        $ next_inv_page = 0
    for item in sorted_items:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 200
            if i%3==0:
                $ y += 200
                $ x = 140
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "") # we use tooltips to describe what the item does.
            imagebutton:
                idle pic
                hover pic.replace("inventory", "inventory_glow")
                xpos x
                ypos y
                action [Hide("gui_tooltip"), SetVariable("item", item), item_use] hovered [ Play ("sound", "sfx/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) ] unhovered [Hide("gui_tooltip")] at inv_eff
                #Hide("shopping_screen")
            if player.element and (player.element==item.element): #indicate the selected gun
                add "gui/selected.png" xpos x ypos y anchor(.5,.5)
                $ cost = item.cost
        $ i += 1
        if len(shop_stock.items)>9:
            textbutton _("Next Page") action [SetVariable('inv_page', next_inv_page), Show("shopping_screen")] xpos .475 ypos .83

screen gui_tooltip (my_picture="", my_tt_xpos=58, my_tt_ypos=687):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos
    #frame:
    #    xalign 0.5 yalign 0.5
    #    hbox:
    #        text inventory.money


init -1:
    transform inv_eff: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
        zoom 0.6 xanchor 0.5 yanchor 0.5
        on idle:
            linear 0.2 alpha 1.0
        on hover:
            linear 0.2 alpha 2.5

    image information = Text("BİLGİ", style="tips_top")
    #Tooltips-inventory:
    #image tooltip_inventory_chocolate=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Generic chocolate to heal\n40 points of health.", style="tips_bottom"))
    #image tooltip_inventory_banana=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("A healthy banana full of potassium! You can also use it as ammo for your guns! O.O Recharges 20 bullets.", style="tips_bottom"))
    #image tooltip_inventory_gun=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("An gun that looks like something a cop would\ncarry around. Most effective on humans.", style="tips_bottom"))
    #image tooltip_inventory_laser=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("An energy gun that shoots photon beams.\nMost effective on aliens.", style="tips_bottom"))
    image tooltip_inventory_wire_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Depodan bir kablo parçası.\nBükülüyor.", style="tips_bottom"))
    image tooltip_inventory_apartmentkeys_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Apartmanın için anahtarlar.\nKaza sırasında kaybet.", style="tips_bottom"))
    image tooltip_inventory_carkey_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Brandon'un arabası için anahtarlar.\nKim bulduysa onundur.", style="tips_bottom"))
    image tooltip_inventory_condoms_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Kondomlar.\nSeksten sonra nafaka almamanın en iyi yolu.", style="tips_bottom"))
    image tooltip_inventory_lockerkey125_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Dolap anahtarı 125.\nBrandon'un kolej dolabının anahtarı.", style="tips_bottom"))
    image tooltip_inventory_lube_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Yağ.\nDar şeyleri gevşetmek için.", style="tips_bottom"))
    image tooltip_inventory_money_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Para.\nSatın almak için gereken şey.", style="tips_bottom"))
    image tooltip_inventory_phone_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Brandon'ın Telefonu.\nŞu onda ona ihtiyacı yok.", style="tips_bottom"))
    image tooltip_inventory_sexpills_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Seks Hapları.\nGarip efektleri olan haplar.", style="tips_bottom"))
    image tooltip_inventory_credit_card_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Kredi Kart.\nBrandon'un parasına erişim.", style="tips_bottom"))
    image tooltip_inventory_flash_drive_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Flaş Bellek.\nBrandon'un dolabında çıktı.", style="tips_bottom"))
    image tooltip_inventory_100bill_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Lanetlenmiş Para.\nLanetli 100'lük banknot.\nİnsanın ruhunu çalmak için.", style="tips_bottom"))
    image tooltip_inventory_devil_card_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Şeytan çağırma kağıdı.\nŞeytanla iletişime geçmek için\n Acil durumlarda", style="tips_bottom"))
    image tooltip_inventory_bath_brush_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Banyo fırçası.\nKullanılmış gibi durmuyor.", style="tips_bottom"))
    image tooltip_inventory_cop_phone_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Polisin Telefonu.\nSuçlayıcı delil ile dolu.", style="tips_bottom"))
    image tooltip_inventory_cop_car_key_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Polisin arabasının anahtarı.\nPolisin arabası için anahtar.", style="tips_bottom"))
    image tooltip_inventory_panties_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Külotlar.\nBaygın aroması var.", style="tips_bottom"))
    image tooltip_inventory_gun_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Silah.\nCebimdeki silah.", style="tips_bottom"))
    image tooltip_inventory_photo_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Fotoğraf.\nKaybolmuş çocuk Nick'in fotoğrafı.", style="tips_bottom"))
    image tooltip_inventory_copapartmentkeys_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Polisin evi için anahtar.\nLüks evin anahtarı.", style="tips_bottom"))
    image tooltip_inventory_drugs_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Uyuşturucular.\nSatılacak uyuşturucuların gizli zulası.", style="tips_bottom"))
    image tooltip_inventory_scarlett_drive_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Scarlett\'in Arabası.\nİçinden oyuncak ayı çıktı.", style="tips_bottom"))
    image tooltip_inventory_anders_evidence_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Anders aleyhine deliller.\nDekan için.", style="tips_bottom"))
    image tooltip_inventory_den_key_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Polis\'in klozetindeki anahtar(?).\nÜstünde adresi var.", style="tips_bottom"))
    image tooltip_inventory_room4_key_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Oda 4 için anahtar.\nDen bodrumu için bir anahtar.", style="tips_bottom"))
    image tooltip_inventory_shrinkingpills_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Küçülen Haplar.\nTest edildi ve onaylandı.", style="tips_bottom"))
    image tooltip_inventory_hornypills_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Azgınlık Hapları.\nTest edildi ve onaylandı.", style="tips_bottom"))
    image tooltip_inventory_unlabeledpills_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Etiketsiz haplar.\nAyırt etmek imkansız.", style="tips_bottom"))
    image tooltip_inventory_andersphone_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Anders'ın Telefonu.\nYani, bilgisiyarını gördün...", style="tips_bottom"))
    image tooltip_inventory_anderskeys_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Anders'ın Anahtarları.\nOfis ve ev anahtarları.", style="tips_bottom"))
    image tooltip_inventory_money_bag_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Anders'ın Birikimleri.\nArtık yok.", style="tips_bottom"))
    image tooltip_inventory_assortedpills_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Çeşitli Haplar.\nBütün isteklerin ve ihtiyaçlarını karşılayacak haplar.", style="tips_bottom"))
    image tooltip_inventory_sleepingpills_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Uyku Hapları.\nKüçük bir şekerlemeye yardım eden haplar.", style="tips_bottom"))
    image tooltip_inventory_growingpills_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Büyüme Hapları.\nBüyümeye yardım eden haplar.", style="tips_bottom"))
    image tooltip_inventory_reducingpills_inventory=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Küçültme Hapları.\nKüçülmeye yardım eden haplar", style="tips_bottom"))

#image sidewalk = "Sidewalk.jpg"

screen phone_screen:
    add "other_things/phone_gui/phone_gui.png"#"other_things/phone_gui/phone_gui_test.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown

    imagebutton:
        idle "phone_call"
        hover "phone_call_glow"
        xpos 680 ypos 95
        action NullAction()

    imagebutton:
        idle "phone_sms"
        hover "phone_sms_glow"
        xpos 715 ypos 320
        action NullAction()

    #if seen_secret_pics_mc_computer or seen_secret_pics_brandon_flash_drive:
    imagebutton:
        idle "phone_gallery"
        hover "phone_gallery_glow"
        xpos 745 ypos 520
        action Hide("phone_screen"), SetVariable("phone_secrets_current_page", 1), Show("phone_secrets_screen")
        #action Hide("phone_screen"), Jump("phone_gallery")

    imagebutton:
        idle "phone_quit"
        hover "phone_quit_glow"
        xpos 780 ypos 705
        action [Hide("phone_screen")]

screen phone_secrets_screen:
    add "other_things/phone_gui/phone_gui.png"#"other_things/phone_gui/phone_gui_test.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    if phone_secrets_current_page == 1:
        imagebutton:
            xpos 660 ypos 95
            if seen_secret_pics_mc_computer:
                idle "secret1"
                hover "secret1_glow"
                action Hide("phone_secrets_screen"), Jump("phone_gallery")
            else:
                idle "secret1_not"

        imagebutton:
            xpos 840 ypos 95
            if deans_office_secret_found:
                idle "secret2"
                hover "secret2_glow"
                action Hide("phone_secrets_screen"), Jump("phone_megan_gallery")
            else:
                idle "secret2_not"

        imagebutton:
            xpos 660 ypos 205
            if seen_secret_pics_brandon_flash_drive:
                idle "girls"
                hover "girls_glow"
                action Hide("phone_secrets_screen"), Jump("phone_girls_gallery")
            else:
                idle "girls_not"

        imagebutton:
            xpos 840 ypos 205
            if show_bonus_button_on_phone:
                idle "bonus1"
                hover "bonus1_glow"
                action Hide("phone_secrets_screen"), Jump("phone_bonus1_gallery")
            else:
                idle "bonus1_not"

        imagebutton:
            xpos 660 ypos 315
            if show_exgf_button_on_phone:
                idle "exgf"
                hover "exgf_glow"
                action Hide("phone_secrets_screen"), Jump("phone_exgf_gallery")
            else:
                idle "exgf_not"

        imagebutton:
            xpos 840 ypos 315
            if anders_office_secret_found:
                idle "secret3"
                hover "secret3_glow"
                action Hide("phone_secrets_screen"), Jump("phone_girl_pairs_gallery")
            else:
                idle "secret3_not"

        imagebutton:
            xpos 660 ypos 425
            if anders_desk_secret_found:
                idle "secret4"
                hover "secret4_glow"
                action Hide("phone_secrets_screen"), Jump("angel_devil_battle_gallery")
            else:
                idle "secret4_not"

        imagebutton:
            xpos 840 ypos 425
            if scarletts_room_secret_found:
                idle "secret5"
                hover "secret5_glow"
                action Hide("phone_secrets_screen"), Jump("angel_devil_battle_gallery2")
            else:
                idle "secret5_not"
        imagebutton:
            xpos 660 ypos 535
            if cafeteria_room_secret_found:
                idle "secret6"
                hover "secret6_glow"
                action Hide("phone_secrets_screen"), Jump("angel_devil_battle_gallery3")
            else:
                idle "secret6_not"
        imagebutton:
            xpos 840 ypos 535
            if janitors_closet_secret_found:
                idle "bonus2"
                hover "bonus2_glow"
                action Hide("phone_secrets_screen"), Jump("angel_christmas_bonus")
            else:
                idle "bonus2_not"
    elif phone_secrets_current_page == 2:
        imagebutton:
            xpos 660 ypos 95
            if secret_locker_secret7_found:
                idle "secret7"
                hover "secret7_glow"
                action Hide("phone_secrets_screen"), Jump("angel_devil_battle_gallery4")
            else:
                idle "secret7_not"
        imagebutton:
            xpos 840 ypos 95
            if rebecca_room_secret8_found:
                idle "secret8"
                hover "secret8_glow"
                action Hide("phone_secrets_screen"), Jump("angel_devil_battle_gallery5")
            else:
                idle "secret8_not"
        imagebutton:
            xpos 660 ypos 205
            if jewelery_store_secret9_found:
                idle "secret9"
                hover "secret9_glow"
                action Hide("phone_secrets_screen"), Jump("angel_bar_then_room_gallery")
            else:
                idle "secret9_not"
        imagebutton:
            xpos 840 ypos 205
            if winners_party_livingroom_secret10_found:
                idle "secret10"
                hover "secret10_glow"
                action Hide("phone_secrets_screen"), Jump("angel_mc_gallery1")#
            else:
                idle "secret10_not"
        imagebutton:
            xpos 660 ypos 315
            if winners_party_scarletts_room_secret11_found:
                idle "secret11"
                hover "secret11_glow"
                action Hide("phone_secrets_screen"), Jump("angel_mc_gallery2")#
            else:
                idle "secret11_not"



    if phone_secrets_current_page > 1:
        imagebutton:
            xpos 685 ypos 670
            idle "phone_previous_button"
            hover "phone_previous_button_glow"
            action SetVariable("phone_secrets_current_page", phone_secrets_current_page-1)
    if phone_secrets_current_page < phone_secrets_max_pages:
        imagebutton:
            xpos 960 ypos 670
            idle "phone_next_button"
            hover "phone_next_button_glow"
            action SetVariable("phone_secrets_current_page", phone_secrets_current_page+1)
    imagebutton:
        idle "phone_back"
        hover "phone_back_glow"
        xpos 795 ypos 705
        action [Hide("phone_secrets_screen"), Show("phone_screen")]

label phone_gallery:
    if seen_secret_pics_mc_computer:
        show latex_angel1
        $ renpy.pause()
        hide latex_angel1
        show latex_angel2
        $ renpy.pause()
        hide latex_angel2
        show latex_angel3
        $ renpy.pause()
        hide latex_angel3
        show megan_and_ivana1
        $ renpy.pause()
        hide megan_and_ivana1
        show megan_and_ivana2
        $ renpy.pause()
        hide megan_and_ivana2
        show megan_and_ivana3
        $ renpy.pause()
        hide megan_and_ivana3
        show megan_and_ivana4
        $ renpy.pause()
        hide megan_and_ivana4
        show megan_and_ivana5
        $ renpy.pause()
        hide megan_and_ivana5
        show mom_bath1
        $ renpy.pause()
        hide mom_bath1
        show mom_bath2
        $ renpy.pause()
        hide mom_bath2
        show mom_bath3
        $ renpy.pause()
        hide mom_bath3
        show mom_bath4
        $ renpy.pause()
        hide mom_bath4

    jump current_screen_selector

label phone_girls_gallery:
    if seen_secret_pics_brandon_flash_drive:
        show brandons05_brooke
        $ renpy.pause()
        hide brandons05_brooke
        show brandons05_jasmine
        $ renpy.pause()
        hide brandons05_jasmine
        show brandons05_tracy
        $ renpy.pause()
        hide brandons05_tracy
    if asian_called_to_offer_work:
        show asiangirl_s01_sexy_photo01
        $ renpy.pause()
        hide asiangirl_s01_sexy_photo01
        show asiangirl_s01_sexy_photo02
        $ renpy.pause()
        hide asiangirl_s01_sexy_photo02
        show asiangirl_s01_sexy_photo03
        $ renpy.pause()
        hide asiangirl_s01_sexy_photo03

    jump current_screen_selector

label phone_exgf_gallery:

    show exgfs01_at_beach01
    $ renpy.pause()
    hide exgfs01_at_beach01
    show exgfs01_at_beach02
    $ renpy.pause()
    hide exgfs01_at_beach02
    show exgfs01_at_beach03
    $ renpy.pause()
    hide exgfs01_at_beach03
    show exgfs01_at_beach04
    $ renpy.pause()
    hide exgfs01_at_beach04

    jump current_screen_selector

label phone_megan_gallery:
    show megan_bonus0
    $ renpy.pause()
    hide megan_bonus0
    show megan_bonus1
    $ renpy.pause()
    hide megan_bonus1
    show megan_bonus2
    $ renpy.pause()
    hide megan_bonus2
    show megan_bonus3
    $ renpy.pause()
    hide megan_bonus3
    show megan_bonus4
    $ renpy.pause()
    hide megan_bonus4
    show megan_bonus5
    $ renpy.pause()
    hide megan_bonus5
    show megan_bonus6
    $ renpy.pause()
    hide megan_bonus6
    show megan_bonus7
    $ renpy.pause()
    hide megan_bonus7
    show megan_bonus8
    $ renpy.pause()
    hide megan_bonus8
    $ renpy.movie_cutscene("scenes/secrets/02version/Megan_Boobsplay.webm", loops=-1,delay=-1, stop_music=False)
    jump current_screen_selector

label phone_bonus1_gallery:
    scene black_screen
    jor "Note: This scene is not storyline based and doesn't affect the flow of this game. It is just a bonus scene for players."
    show bonus1_01
    play music "sounds/music/Sexy_music1_monks_topher.ogg" fadein 3.0
    p "Hmmm... Tracy is in the shower. Why not surprise her a little?"
    hide bonus1_01
    show bonus1_02
    p "Hello there."
    trcy "Oh! You scared me a little... Hihi. What is that I'm feeling between my legs, hmmm?"
    hide bonus1_02
    show bonus1_03
    a "Hmmm... I’m getting horny, just watching them, cuddle in the shower. Why not have some fun too?"
    hide bonus1_03
    show bonus1_04
    trcy "Hmmmm... My lovely boy. We'll both have some fun now."
    a "Let’s try some magic."
    show cam1grow00
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_dickgrow1.webm", stop_music=False)
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_dickgrow2.webm", stop_music=False)
    hide cam1grow00
    hide bonus1_04
    show bonus1_05
    trcy "WHAT!!? What just happened?!?"
    hide bonus1_05
    show bonus1_06
    trcy "Oh damn! He is soo BIG! And thick!"
    hide bonus1_06
    show bonus1_07
    a "Hmmm... Tastes almost like a real one."
    hide bonus1_07
    show bonus1_09
    a "Fits perfectly."
    show insert00
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angelbj.webm", loops=4, stop_music=False)
    show insert58
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_tracybj-toobig.webm", stop_music=False)
    trcy "Uhmmmmm pffhmmm..."
    hide insert00
    hide insert58
    hide bonus1_09
    show bonus1_08
    trcy "I’m sooo sorry. But it won't fit. My mouth is too small for your big cock. I’m so sorry. If it was a little smaller..."
    hide bonus1_08
    show bonus1_10
    a "Argh... Why must I listen to all this moaning. It’s too biiig... It won't fit.. bla bla..."
    hide bonus1_10
    show bonus1_11
    a "Hello there. I think I can help you with this... giant problem. "
    p "You want to make it smaller?"
    a "Nope. Just a little change to help Tracy with... her problem"
    hide bonus1_11
    show bonus1_12
    p "But Tracy doesn’t know you. You will scare her more."
    a "Look. The devil is not the only one that can use some powers. The girl will be perfectly calm."
    hide bonus1_12
    show bonus1_13
    a "Let’s do this."
    hide bonus1_13
    show bonus1_14
    a "Don’t worry, baby. Just let me lead your head slowly."
    hide bonus1_14
    show bonus1_15
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_Tracy_bjinsertionwithhelp.webm", stop_music=False)
    a "Perfect! GOOD girl."
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_Tracybjloop.webm", loops=1, stop_music=False)
    hide bonus1_15
    show bonus1_16
    p "Oh damn, her throat is sooo tight. I will cum in a second..."
    hide bonus1_16
    show bonus1_17
    a "Not yet, big boy. We are not done here yet."
    a "Just a little trick..."
    hide bonus1_17 with dissolve
    scene black_screen
    show bonus1_18 with dissolve
    $ renpy.pause(1.0, hard=True)
    hide bonus1_18 with dissolve
    show bonus1_19 with dissolve
    $ renpy.pause(1.0, hard=True)
    hide bonus1_19 with dissolve
    show bonus1_20 with dissolve
    $ renpy.pause(1.0, hard=True)
    a "Woooo!!"
    a "All good? That trick was a little bigger than I was expecting."
    hide bonus1_20
    show bonus1_21
    p "That feels so great!"
    hide bonus1_21
    show bonus1_22
    a "I think now is our time to have some fun too."
    hide bonus1_22
    show bonus1_23
    p "Damn, you look incredible in those stockings."
    hide bonus1_23
    show bonus1_24
    a "Thank you! Come here, lie on the bed."
    hide bonus1_24
    show bonus1_25
    trcy "Hmmm... That feeels great... His tongue is so soft."
    hide bonus1_25
    show bonus1_26
    trcy "(And her lips... I feel a huge amount of heat flowing through my whole body.)"
    a "Now it's time to ride him, Tracy."
    hide bonus1_26
    show bonus1_27
    trcy "But I don’t know how. I've never had something that big inside of me."
    a "Okay. I will start first, and you will see there's no reason to be scared."
    hide bonus1_27
    show bonus1_28
    a "(Ooooh... I’m sooo horny, just thinking about that big one, pulsating inside of me...)"
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angelsit.webm", stop_music=False)
    hide bonus1_28
    show bonus1_29
    a "Uuhmm... He is much bigger than I thought. I feel how it's almost tearing my pussy from the inside. But all of it feels amazing!"
    scene angelcam2ride000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angelridecam1.webm", loops=1, stop_music=False)
    scene angelride000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angelridecam2.webm", loops=1, stop_music=False)
    scene angelcam2ride000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angelridecam1.webm", loops=1, stop_music=False)
    scene angelride000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angelridecam2.webm", loops=1, stop_music=False)
    hide angelride000
    hide angelcam2ride000
    hide bonus1_29
    show bonus1_30
    a "Now it's your turn, Tracy."
    trcy "But..."
    a "Don’t worry. As I said, I will help you. Just trust me. You both, come with me."
    hide bonus1_30
    show bonus1_31
    a "Great! Now... er, Brandon... lift her up."
    trcy "Whaatt!?"
    a "You will love it. Trust me."
    scene tracyup000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_Tracyupcam2.webm", loops=1, stop_music=False)
    scene tracycam1up000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_tracyupcam1.webm", loops=1, stop_music=False)
    scene tracyup000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_Tracyupcam2.webm", loops=1, stop_music=False)
    scene tracycam1up000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_tracyupcam1.webm", loops=1, stop_music=False)
    hide tracycam1up000
    hide tracyup000
    hide bonus1_31
    show bonus1_32
    a "That was amazing! But now I want you inside again, and from behind!"
    p "Of course! I'd like to fuck you again."
    a "Great! And do it really hard, don’t worry about me. I want to cum HARD. Haven’t had in ages!"
    p "Fine by me."
    hide bonus1_32
    show bonus1_33
    p "So get ready. This will be your best fuck ever!"
    scene angelcam1doggy000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angeldoggycam1.webm", stop_music=False)
    scene angeldoggy000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angeldoggycam2.webm", loops=1, stop_music=False)
    scene angelcam1doggy000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angeldoggycam1.webm", loops=1, stop_music=False)
    scene angeldoggy000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angeldoggycam2.webm", stop_music=False)
    hide bonus1_33
    show bonus1_34
    p "(That is amazing! But she wanted it really hard, right?) Now I will take you to heaven!!!"
    hide bonus1_34
    show bonus1_35
    p "Hmmm... Sooo tight!"
    hide bonus1_35
    show bonus1_36
    a "Whaaaa..! Hold!! Aaaaaaahhhhh!!"
    scene angelcam1anal000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angelanaldoggycam1.webm", stop_music=False)
    scene angelcam2anal000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angelanaldoggycam2_slow.webm", loops=1, stop_music=False)
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angelanaldoggycam2_fast.webm", loops=1, stop_music=False)
    scene angelcam1anal000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angelanaldoggycam1.webm", stop_music=False)
    scene angelcam2anal000
    $ renpy.movie_cutscene("scenes/Tracy/03_bonus1/webm/Bonus1_angelanaldoggycam2_fast.webm", stop_music=False)
    hide angelcam1anal000
    hide angelcam2anal000
    hide bonus1_36
    show bonus1_37
    a "AAaaaah!! I’m coming! Aaaah..."
    hide bonus1_37
    show bonus1_38
    p "Meee tooo!!"
    hide bonus1_38
    scene black_screen
    show bonus1_cumshot2
    $ renpy.pause()
    hide bonus1_cumshot2
    show bonus1_cumshot1
    $ renpy.pause()
    hide bonus1_cumshot1
    show bonus1_cumshot3
    $ renpy.pause()
    hide bonus1_cumshot3
    show bonus1_cumshot4
    $ renpy.pause()
    hide bonus1_cumshot4
    show bonus1_cumshot5
    $ renpy.pause()
    hide bonus1_cumshot5
    show bonus1_cumshot5b
    $ renpy.pause()
    hide bonus1_cumshot5b
    show bonus1_cumshot6
    $ renpy.pause()
    hide bonus1_cumshot6
    show bonus1_cumshot_last
    $ renpy.pause()
    hide bonus1_cumshot_last
    show bonus1_cumshot_last2
    $ renpy.pause()
    trcy "Ouuuff... That was unbelievable!"
    a "Yes, great fun. The best I ever had. Thanks to both of you!"
    hide bonus1_cumshot_last2
    jump current_screen_selector

label phone_girl_pairs_gallery:
    show secret3_image00
    $ renpy.pause()
    hide secret3_image00
    show secret3_image01
    $ renpy.pause()
    hide secret3_image01
    show secret3_image02
    $ renpy.pause()
    hide secret3_image02
    show secret3_image03
    $ renpy.pause()
    hide secret3_image03
    show secret3_image04
    $ renpy.pause()
    hide secret3_image04
    show secret3_image05
    $ renpy.pause()
    hide secret3_image05
    show secret3_image06
    $ renpy.pause()
    hide secret3_image06
    show secret3_image07
    $ renpy.pause()
    hide secret3_image07
    show secret3_image08
    $ renpy.pause()
    hide secret3_image08
    show secret3_image09
    $ renpy.pause()
    hide secret3_image09
    show secret3_image10
    $ renpy.pause()
    hide secret3_image10
    jump current_screen_selector

label angel_devil_battle_gallery:
    show secret4_image20
    d "Nice to see you here. I think we will both have some good fun together."
    hide secret4_image20
    show secret4_image01
    a "I don’t think so. You will pay for all you’ve done."
    hide secret4_image01
    show secret4_image01a
    d "We will see."
    hide secret4_image01a
    show secret4_image02a
    $ renpy.pause()
    hide secret4_image02a
    show secret4_image02b
    a "Ouuuuch..."
    hide secret4_image02b
    show secret4_image02
    a "Nooo!"
    hide secret4_image02
    show secret4_image03
    d "Hahaha..!! Now, the fun will begin..."
    hide secret4_image03
    show secret4_image04
    d "I have a good friend in mind for you. I think its size will suit you well."
    hide secret4_image04
    show secret4_image05
    a "You can't..!!"
    d "I can do what I want… And now - I want to punish your holes with this toy."
    hide secret4_image05
    show secret4_image06
    a "But it cannot fit inside!"
    d "Hahaha! It will, you will see... and feel it."
    hide secret4_image06
    show secret4_image07
    a "Ouhmmmmmm!"
    hide secret4_image07
    show secret4_image08
    d "Yes! Up and down! Take it whole you angelic slut. Tell me you like it, you slut!!"
    hide secret4_image08
    show secret4_image09
    a "Oh... Pleaseee...."
    d "Good slut, I think you will enjoy it more, upside down."
    hide secret4_image09
    show secret4_image10
    a "Oh! Nooo..! It is too much!"
    hide secret4_image10
    show secret4_image11
    d "And slowly, fully inside. That toy is big, it's spreading your ass too. Don't worry your ass will have it's fun too."
    hide secret4_image11
    show secret4_image12
    d "I see you are really enjoying it. Your nipples are as hard as stone. Let me taste them."
    hide secret4_image12
    show secret4_image13
    d "Hmmm... so HARD."
    hide secret4_image13
    show secret4_image14
    a "Don't bite me... you bitch!"
    hide secret4_image14
    show secret4_image15
    d "Ouuuuwww...."
    hide secret4_image15
    show secret4_image16
    $ renpy.pause()
    hide secret4_image16
    show secret4_image17
    d "Eeeeh..."
    hide secret4_image17
    show secret4_image21
    a "Surprise, bitch!"
    hide secret4_image21
    show secret4_image18
    d "Eeh... What happened?!"
    hide secret4_image18
    show secret4_image22
    a "Now I will have my fun with you..!"
    hide secret4_image22
    show secret4_image19
    a "Don't think you are the only one who knows how punishment works."
    hide secret4_image19
    show secret4_image23
    $ renpy.pause()
    hide secret4_image23
    jump current_screen_selector

label angel_devil_battle_gallery2:
    scene black_screen
    show secret5_image01
    a "Let me show you my magic."
    hide secret5_image01
    show secret5_image03
    d "Uhm..."
    hide secret5_image03
    show secret5_image02
    a "I don't believe you've met my favorite toy."
    d "It's nothing special, to be honest."
    hide secret5_image02
    show secret5_image04
    a "We'll see how arrogant you'll be when it stuffs your throat..."
    hide secret5_image04
    show secret5_image05
    a "...and ass!"
    d "No! You can't do this to me!! I will not allow it!"
    hide secret5_image05
    show secret5_image06
    a "I think you will, just like that! And you don’t need those clothes anymore. And now obediently open your mouth."
    hide secret5_image06
    show secret5_image07
    a "Good girl..."
    hide secret5_image07
    show secret5_image09
    a "Hmmm, it's going in, so nice and easy. You must have been training it for centuries, right?"
    hide secret4_image09
    show secret5_image10
    d "Ohmpfff...  tffff..."
    hide secret5_image10
    show secret5_image08
    a "Oh, if you want to say something, say it now!"
    hide secret5_image08
    show secret5_image11
    d "Oggrrrrhmmm... pffff... gulp... chrrrmpff..."
    a "YES! Take it whole, you dirty girl!"
    hide secret5_image11
    show secret5_image12
    a "YES! YES! More, Take it more!"
    d "Pfffhmpff...  chrmmpff..."
    a "Damn, you have a really deep throat. Haha! Pun intended."
    hide secret5_image12
    show secret5_image08
    a "Good girl... Now, it's time for your ass. Let's see how deep it goes. Haha!"
    hide secret5_image08
    show secret5_image13
    d "Eeek!"
    a "Haha, how does that feel, hmmm? Haha! Now that is what I call punishment."
    scene secret5_image14
    $ renpy.pause()
    show secret5_image15
    a "Damn! (I’m getting so wet from this...)"
    hide secret5_image15
    show secret5_image16
    a "Deeper and deeper."
    scene secret5_image17
    $ renpy.pause()
    show secret5_image18
    d "Hmmm... yes please... I want more."
    scene secret5_image20
    $ renpy.pause(2.0)
    a "WHAT?! I’m not here to be pleasing you! Only to punish you!!"
    hide secret5_image20
    show secret5_image19
    d "Yeah, whatever... Ahmmm... Anyything you want, just please, don’t stop..."
    scene secret5_image21 with dissolve
    jump current_screen_selector

label angel_devil_battle_gallery3:
    scene black_screen
    scene secret6_image01
    a "I am not continuing! You've been laughing at me the whole time?!"
    scene secret6_image02
    d "Yeah. Wasn’t that fun? Let’s continue. I’m not done yet."
    scene secret6_image01
    a "No fucking way! I’m not here to please you!"
    scene secret6_image02
    d "Cool. As you wish - We can do it the hard way… For you, of course."
    #(dissolve)
    scene secret6_image03 with dissolve
    a "FINE! Stop it. I will do it."
    d "Good girl."
    scene secret6_image04 with fade
    $ renpy.pause(1.5)
    scene secret6_image05
    d "Get down, girl."
    scene secret6_image06
    a "Ouhh?!"
    d "Down, on your back. I want to ride that cock."
    scene secret6_image07 with fade
    $ renpy.pause(3.0)
    d "Oh, yes! That’s what I needed. Stay as you are."
    scene secret6_image08
    a "Ehmm... Fine…"
    scene secret6_image09
    $ renpy.pause(1.0)
    d "Hmmmm... So deeep..."
    scene secret6_image12
    $ renpy.pause(1.0)
    d "That’s really great."
    scene secret6_image10
    $ renpy.pause(1.0)
    d "Yeah…. I am going to cum…"
    scene secret6_image11
    d "Yes!! Take that, you angelic slut!!"
    scene secret6_image11
    $ renpy.pause(1.0)
    scene secret6_image19 with dissolve
    $ renpy.pause(2.0)

    scene secret6_image18 with dissolve
    $ renpy.pause(2.0)
    d "Aaaah!!!!"
    scene secret6_image20
    $ renpy.pause(2.0)

    scene secret6_image21 with fade
    a "Ehm….."
    scene secret6_image13
    d "Oopsiee…."
    d "Hmmm… You made me cum once. Now, fuck my pussy hard. I want to cum again."
    scene secret6_image15
    $ renpy.pause(1.0)
    a "Like this?"
    d "Yeaaah! Harder!!!"
    scene secret6_image14
    $ renpy.pause(2.0)

    scene secret6_image16
    $ renpy.pause(2.5)

    scene secret6_image17
    $ renpy.pause(1.0)
    "Unknown" "Aaah... Anybody need my help here?"
    "To be continued!"
    scene black with fade

    jump current_screen_selector

label angel_christmas_bonus:
    scene christmas_bonus_angel01
    p "Hmmmpf.. Christmas again. And again I’m alone. Others are celebrating but I hate this time."

    scene christmas_bonus_angel03
    a "Hello there."
    scene christmas_bonus_angel02
    p "Ohh… Hi. I wasn’t expecting anybody."
    scene christmas_bonus_angel04
    a "I can go, if you'd like."
    p "Nooo! Of course not. Come here, sit."
    a "I have a present for you."

    scene christmas_bonus_angel05
    p "Thank you, but I don’t have anything for you…"
    a "It’s okay. Don’t ruin the mood."
    a "I’m here to spend some quality time with you. Not for presents."
    a "So, aren't you curious about what's inside?"

    scene christmas_bonus_angel06
    p "Of course. What could a man get on Christmas from an angel, right?"
    scene christmas_bonus_angel07
    p "It’s empty?"
    scene christmas_bonus_angel08
    a "Is it? Really?"
    scene christmas_bonus_angel09
    a "You know, the surprise is not inside. The surprise is me. And because today is a special day and I really like you, I can make some wishes come true for you."
    p "What kind of wishes?"
    a "Hehe, I know pretty well what wishes you have."

    scene christmas_bonus_angel10
    p "Really?"
    a "Yes. I’m your angel and today I will fulfill all of your wishes."
    p "Okay. I want some fine Moldavian champagne."

    scene christmas_bonus_angel11
    a "Haha, good try, but you cannot lie to me."

    scene christmas_bonus_angel12
    p "Damn, you know what my favorite is?"
    a "I’m your angel. But I think that was not what you want the most right now."

    scene christmas_bonus_angel11
    a "Let’s see if I’m right…."
    #scene christmas_bonus_angel13
    #$ renpy.pause()
    scene christmas_bonus_angel14
    p "HOLY!!!  Oh sorry…  My GOD... Aaaarghhh…"
    scene black
    $ renpy.movie_cutscene("scenes/MC/02_christmas_bonus_angel/WEBM/christmas_bonus_angel_foot.webm", loops=0, delay=-1, stop_music=False)

    scene christmas_bonus_angel15
    a "Those words, I’ll forgive you for. Haha. So?"
    scene christmas_bonus_angel14
    p "You look….. like… Like a HOT angel, WOw.. I cannot even describe how stunning you look. Shit! That’s so arousing."
    scene christmas_bonus_angel16
    a "And we are just getting started..."
    scene christmas_bonus_angel17
    $ renpy.pause(1.5)
    scene christmas_bonus_angel18
    $ renpy.pause(1.5)
    scene christmas_bonus_angel19
    a "I think we won't be needing these anymore."
    scene christmas_bonus_angel20 with fade
    p "Definitely..."

    scene christmas_bonus_angel22
    a "C'mon. Grab my hair and do me like you wanted to, from behind."
    scene christmas_bonus_angel23
    p "Oooopffff."
    scene christmas_bonus_angel21
    $ renpy.pause(1.5)

    a "So, what are you waiting for? Next Christmas ?."
    p "NONONOOOO!! I’m just thrilled and frozen by what I'm hearing and seeing right now . Woooow!"

    scene christmas_bonus_angel25 with fade
    $ renpy.pause(1.5)

    a "Mmmmmmmm….."
    p "Wow, you are so tight and wet already. It feels like a dream."

    scene christmas_bonus_angel26
    $ renpy.pause(1.5)

    a "Yes, take me. Take me, like in your deepest wishes. I’m your slut today."
    scene christmas_bonus_angel24
    $ renpy.pause(1.5)

    a "Aaaaah…"
    p "I’ don’t know how much longer I can hold it. You are so hot!!! Fuck, I never thought this would ever happen."
    a "Don’t worry. You will be able to hold it much longer today…"
    a "Lay on the ground."
    scene black with fade
    $ renpy.movie_cutscene("scenes/MC/02_christmas_bonus_angel/WEBM/christmas_bonus_angel_ride_side.webm", loops=0, delay=-1, stop_music=False)
    $ renpy.movie_cutscene("scenes/MC/02_christmas_bonus_angel/WEBM/christmas_bonus_angel_ride_front1.webm", loops=0, delay=-1, stop_music=False)
    $ renpy.movie_cutscene("scenes/MC/02_christmas_bonus_angel/WEBM/christmas_bonus_angel_ride_side_old.webm", loops=0, delay=-1, stop_music=False)
    $ renpy.movie_cutscene("scenes/MC/02_christmas_bonus_angel/WEBM/christmas_bonus_angel_ride_front2.webm", loops=0, delay=-1, stop_music=False)
    scene christmas_bonus_angel27
    p "Now you're riding like a real cowgirl…"
    scene christmas_bonus_angel27
    p "I’m still on the edge…. How"
    a "I told you will be able to hold it.  Hihi."

    scene christmas_bonus_angel28
    p "I love the way your pussy feels."
    scene christmas_bonus_angel29
    p "What about we try your ass tooo?"
    a "Heh. Hey now…"
    p "What? I though you would fulfill all my wishes today."
    a "Fine, all but one wish, which I will keep for your next christmas present. But I will give you another pleasure you never got."
    scene black with fade

    scene christmas_bonus_angel30 with fade
    $ renpy.pause(0.5)
    p "Oooohm!!!!"
    p "YES!"
    scene christmas_bonus_angel31 with dissolve
    $ renpy.pause(1.5)
    a "How does that feel?"
    scene christmas_bonus_angel32 with dissolve
    $ renpy.pause(1.5)
    p "I think my cock will explode. And my head too. I've been thinking 'I would cum any second now' for the past 10 minutes."
    scene christmas_bonus_angel33 with dissolve
    $ renpy.pause(0.5)
    a "And do you want to already?"
    p "YES! Make me cum like never before! Now, please!!"
    hide window
    scene christmas_bonus_angel34 with dissolve
    $ renpy.pause(1.5, hard=True)
    p "AAAaaaaargh!!!!!!!"
    hide window
    scene christmas_bonus_angel35 with dissolve
    $ renpy.pause(0.5)
    scene christmas_bonus_angel36 with dissolve
    $ renpy.pause(1.5)
    scene christmas_bonus_angel37 with dissolve
    $ renpy.pause(1.5)
    a "Hehe. I think that was the best cumshot of your life."
    p "Mmmmm… probably. Haha."

    scene black with fade


    jump current_screen_selector

label angel_devil_battle_gallery4:
    scene black_screen
    scene secret7_image01
    "Stranger" "Come here…"
    d "Uhh?!"
    scene secret7_image02
    "Stranger" "Now you will feel real punishment."
    d "Ooooh?!"

    scene secret7_image03 with dissolve
    scene secret7_image04 with dissolve
    scene secret7_image05 with dissolve
    scene secret7_image06 with dissolve

    scene secret7_image07
    d "Ooohmm. YES! That’s it! Thick and deep!"
    "Stranger" "What?"
    scene secret7_image08
    a "Hey, Sis! Finally, you came. Why so late?"
    scene secret7_image09
    "Angel's sis" "I had some work at the church."
    d "Mmmmn…"
    "Angel's sis" "What’s happening here? I thought you needed help?"
    scene secret7_image10
    a "Yeah, sure, I did, but we already solved our problems. Why not for once in centuries, enjoy some good action?"
    scene secret7_image07
    d "Hey… stop talking and start moving your hips. I want to feel this big one thrusting inside of me hard."
    "Angel's sis" "Ehh. You are more kinky than I thought."
    d "I’m the devil, baby… Did you forget?  Hah!"
    scene secret7_image11
    d "Yes! That’s what I love."
    scene secret7_image12
    a "Hey Sis, now go as deep as you can."
    scene secret7_image13
    d "Aaaah… I need mooore!"
    scene secret7_image10
    a "As you want. Give us a second."
    scene secret7_image14
    $ renpy.pause(2.0)
    d "Damn! You are such kinky angels. Fucking with mortals is so fucking boring compared to this." with dissolve
    scene secret7_image15
    d "Mmmmmmm... mmm…"
    scene secret7_image16
    d "Fuck! I’m cumming!!!! Arghh…"
    scene secret7_image17 with dissolve
    d "AAaaaaaahh!"
    scene secret7_image18
    "Angel's sis" "Hah, look at her, sis!! We did her goood!"
    scene secret7_image19
    a "Yeah, pretty good!"
    scene secret7_image20
    $ renpy.pause(1.0)
    d "Aahhh.. Uhmmm... mmmmm.."
    d "You two kinky sluts. You made me feel like no one has for centuries."
    a "We're still not done! Come here, you devil bitch!"
    scene secret7_image21
    a "Now you taste our cum."
    scene secret7_image22
    $ renpy.pause(1.0)
    d "Yeeees! Make me all sticky!"
    scene secret7_image23
    $ renpy.pause(1.0)
    "Angel's sis" "Aaaaah!"
    scene secret7_image24
    $ renpy.pause(1.0)
    a "Here it comes!"
    scene secret7_image21
    $ renpy.pause(0.5)
    scene secret7_image25 with dissolve
    $ renpy.pause(0.5)
    scene secret7_image26 with dissolve
    $ renpy.pause(1.0)
    scene secret7_image28 with dissolve
    $ renpy.pause(1.5)
    scene secret7_image27 with fade
    $ renpy.pause(1.0)
    scene secret7_image29 with dissolve
    $ renpy.pause(1.0)
    d "Mmmmm… tastes great…"
    $ renpy.pause(2.0,)
    scene secret7_image30 with fade
    jor "To be Continued? VOTE on my patreon PAGE!"

    scene black with fade

    jump current_screen_selector


label angel_devil_battle_gallery5:
    scene black_screen
    scene secret8_image01
    d "Well, you did me pretty good. And to show you, that I’m not just a heartless bitch, I have for you both the reward you deserve."
    scene secret8_image06
    "Angel's sis" "That’s nice of you..."
    a "Hey, don’t get too cozy with her, she is still the same old Devil lady."
    scene secret8_image02
    d "Hey… Just have a little faith."
    d "Here he comes..."
    scene secret8_image03
    $ renpy.pause()

    scene secret8_image07
    "Angel's sis" "Mmmm... Good start."
    a "A mortal is going to please us? You must have a very low standard friend."
    scene secret8_image04
    d "Don’t worry ladies, looks can be deceiving. Soon he will show you what real fun and pleasures are."
    scene secret8_image08
    "Angel's sis" "Hi, stranger."
    scene secret8_image05
    "Stanger" "Hi."
    d "Oh, I almost forgot to introduce you."
    d "This is my good old friend, mostly known as 'The Dark Wanderer'."
    "Stranger" "But, you two can just call me Aidan, hehe."
    scene secret8_image06
    "Angel's sis" "So what are we waiting for now? Aidan?"
    scene secret8_image04
    d "I see, you girls are already pretty horny. Hahaha! Anyway, I will leave you alone with him. I have to take care of an urgent business on earth."
    d "(Even though I would love to watch you both getting dominated. I have to attend this urgent matter.)"
    d "(Shhsshshhsss)"
    scene secret8_image09
    "Angel's sis" "I like tall guys."
    scene secret8_image10
    a "And I like guys with girth."
    "Aidan" "Hehe. I think, tonight I can fulfil all your wishes, girls."
    a "So let me hug you."
    scene secret8_image12
    "Angel's sis" "Hey Sis, I thought you were worried about him the Devil's reward."
    a "Mmmm…. Shut up and take off his clothes."
    scene secret8_image11
    "Angel's sis" "This will be fun."
    scene secret8_image13
    "Aidan" "Are you ready, girls?"
    a "C'mon. Don’t keep us waiting."
    "Angel's sis" "(Hope he will be really big...)"
    scene secret8_image21
    a "Uuuuu. Pff… Wow."
    scene secret8_image22
    "Angel's sis" "Eeh? You gotta be kidding me? I've seen mortals with better cocks. It looks like a small sausage."
    scene secret8_image14
    "Aidan" "You girls look dissatisfied."
    "Angel's sis" "That word doesn't even begin to describe how I feel. Try pissed…."
    a "She got us again, Sis."
    "Aidan" "Just give me a minute, girls. I know exactly what you both want to see…"

    scene secret8_image15 with dissolve
    "Aidan" "Mmmmm….."
    $ renpy.pause(2.0)
    scene secret8_image16 with dissolve
    $ renpy.pause(2.0)
    scene secret8_image17 with dissolve
    $ renpy.pause(2.0)
    scene secret8_image18 with dissolve
    $ renpy.pause(2.0)
    scene secret8_image19 with dissolve
    $ renpy.pause(2.0)
    scene secret8_image20
    "Angel's sis" "What the holy hell…..?"
    a "Watch your language, Sis."
    scene secret8_image59 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image60 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image61 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image62 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image63 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image64 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image65 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image66 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image67 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image68 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image69 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image70 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image71 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image72 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image73 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image74 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image75 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image76 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image77 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image78 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image79 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image80 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image81 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image82 with dissolve
    $ renpy.pause(1.0)
    scene secret8_image83 with dissolve
    $ renpy.pause(1.0)
    ###All with dissolve from 59 to 83 image
    scene secret8_image23
    "Aidan" "AAaarghhh!!!!"
    a "WHAT the HOLY fuck ?!!!"
    "Angel's sis" "Pssst.."
    scene secret8_image24
    a "Didn’t I tell you we couldn't trust her."
    "Angel's sis" "Eeeh... Hey, at least he has a fine dick now."
    scene secret8_image26
    a "Fine dick? Did you even notice all that monster attached to that dick?"
    scene secret8_image25
    "Angel's sis" "Eheh. Yeees, but he is here as our reward, right?"
    scene secret8_image27
    "Aidan" "You don't get it do you? You are here as MY reward. I shall enjoy dominating both of you."
    scene secret8_image28
    "Angel's sis" "Well. You were right. She screwed us again."
    a "I think, for once, I’m not happy I was right. I would have liked that not to be true."
    scene secret8_image27
    "Aidan" "STOP with all that whining and show me some love."
    scene secret8_image30
    "Aidan" "Yes. That’s a good start. Devil said, that you are a big mouth angel, but not big enough for my dick hahaha. Take it deeper!"
    "Angel's sis" "I’m trying, but I can’t. You are too thick."
    "Aidan" "I thought you said you like thick ones, didn’t you?"
    "Angel's sis" "Yes, but that is too much."
    scene secret8_image29
    "Aidan" "So we will try to see how your sis can handle me with her pussy."
    a "Are you crazy? This monster can’t fit inside."
    "Aidan" "Don’t worry. My size will adjust you to it. To stretch you to the max and completely fill your insides. I’m here to please myself, not to kill you."
    a "Oookay…."
    scene secret8_image31
    a "Holy SHIT!"
    "Angel's sis" "*giggles* *mimics her sister* bad words lead to damnation."
    a "But! He is really fucking big."
    scene secret8_image32
    a "But actually, that monster dick is going smoothly inside."

    scene secret8_image36 with dissolve
    $ renpy.pause(1.0,hard=True)
    scene secret8_image37 with dissolve
    $ renpy.pause(1.0,hard=True)
    a "Arrrgh!!! He is expanding me. I'm full and yet it looks like my vagina is still swallowing his schlong."

    scene secret8_image33 #
    a "That’s fucking ama... *moans* amazing!!!"
    scene secret8_image35
    "Angel's sis" "His tongue stretches my deepest parts inside of me, oh this is so awesome. It feels like a giant snake inside of my womb."
    scene secret8_image34
    "Angel's sis" "Sister I cannot handle myself anymore. I came so many times and it feels like this fiend hasn't tired yet. Sis, I don’t know how long I can handle such pleasure."
    scene secret8_image39
    a "Uuuuuuuuu... I'm cumming tooo."
    scene secret8_image40
    $ renpy.pause(2.0,hard=True)
    scene secret8_image41 with dissolve
    $ renpy.pause(1.0,)

    scene secret8_image42 wiith fade
    a "Aaaaaaaahh…  Mmmmm."
    "Angel's sis" "Sis, you litterally soaked his cock with your cum."
    scene secret8_image43
    a "Mmmm. I’m so weak now. I can feel how my pussy is still wide open and dripping. He broke me."
    scene secret8_image44
    "Angel's sis" "Wow. I don't even know how you managed to push that monster inside."
    "Aidan" "I will show you how. Now it's your turn."
    "Angel's sis" "Eeeh. I was thinking… maybe we could continue with just your tongue?"
    scene secret8_image45
    "Angel's sis" "That's a no, right?"
    "Angel's sis" "*terrified by his size* be at least gentle..."
    "Aidan" "Hold still..."

    scene secret8_image45b with dissolve
    "Angel's sis" "AAAAARGH!!!!"
    scene secret8_image46
    "Angel's sis" "Not so DEEEEP!!! Arrrgh!!"
    "Aidan" "Haha! Now you're literally impaled on my dick, you little slut."
    "Angel's sis" "Sis!!! Arrrgh, Hh hel help mee!! Arrgg…..."
    scene secret8_image48
    a "Mmmm, I’m soo weak after that huge orgasm."
    scene secret8_image47
    "Angel's sis" "I've had enough !! Aaah!!!"
    scene secret8_image49
    "Aidan" "But I haven't. And I think your sis needs some more fun too."
    scene secret8_image53
    "Aidan" "Hey, I broke your nice pussy but your butthole hasn't been corrupted yet. I shall enjoy tearing apart your last sacred place hahaha. Much tighter than your pussy."
    scene secret8_image51
    a "Oh, Sis! He's tearing apart my ass! His finger is much thicker than the usual cock is."
    "Angel's sis" "Aaaah…"
    scene secret8_image52
    a "I cannot endure it anymore…!"
    scene secret8_image54
    "Aidan" "Well, angels, you served me really well. Now, on your knees and drink my cum."
    scene secret8_image56
    "Aidan" "AAAARGHH!!!!!"
    scene secret8_image55
    a "Mllglg….."
    scene secret8_image57
    "Angel's sis" "He has... so much of it."
    scene secret8_image58
    a "Arghh… finally, it’s over."
    "Angel's sis" "I've had enough sex for the next century."
    scene secret8_image86
    "Aidan" "It is not over, my little angels."
    scene secret8_image84
    a "What? What do you mean by that?"
    scene secret8_image87
    "Aidan" "That’s easy. There is no escape from here; so you too will serve me and my minions, for all eternity."
    scene secret8_image85
    "Angel's sis" "Looks like she tricked us again, Sis."
    a "Yeah…."


    scene black with fade

    jump current_screen_selector

label angel_bar_then_room_gallery:
    scene black_screen
    scene secret9_image01
    "Disclaimer: This is a secret scene and does not affect the storyline or gameplay progress. Enjoy the scene."

    "Unknown Girl" "Double Jack Daniels, please."
    scene secret9_image02
    p "(Hmmm, this one in the pink dress looks really nice. Maybe I can try the horny pills on her.)"
    scene secret9_image03
    "Bartender" "Here you go."
    scene secret9_image04
    "Unknown Girl" "And some cigarettes please."
    scene secret9_image05
    p "(I could drop a couple of pills in her drink, at the right moment."
    scene secret9_image06
    "Blond Girl" "Bartender, please, while you have the bottle, same, double Jack for me too please."
    scene secret9_image09
    p "(Huh? What a lovely tone of voice.)"

    scene secret9_image07
    $ renpy.pause()

    scene secret9_image06
    p "(Whoow! What an attractive blonde.)"
    scene secret9_image08
    p "(With a really unique style of dressing. I must definitelly get with her!)"
    scene secret9_image10
    p "Hello, Miss. Can I pay for your drink?"
    scene secret9_image11
    "Blond Girl" "Aha, yeah sure. Of course you can. Mister..?"
    p "Ah, my name is [p]."
    #disolve
    scene secret9_image12 with dissolve
    "Blonde Girl" "That’s a pretty nice and uncommon name. I’m glad to meet you. My name is Angel."
    scene secret9_image13
    p "Wow, that name suits you perfectly. You look like an angel."
    p "(So far, so good. At the right moment I will use the pills on her.)"
    scene secret9_image12
    a "Thank you."
    #disolve
    scene secret9_image11 with dissolve
    a "You know: I really like you. I feel an interesting energy when I’m conversing with you. I have a hotel room here. Do you want to accompany me for a bottle of good wine?"
    p "(WOW! Everything going perfect!)"
    p "*Cough* I must say, there is nothing I want to do more right now. (Apart from bending you over that bar stool behind you, haha.)"
    a "Well, let’s go."
    scene secret9_image14 with fade
    a "Make yourself comfortable. I’ll be back in a moment. This dress is becoming annoying. You can pour out that wine while you're waiting."
    scene secret9_image15
    p "Yeah, sure."
    scene secret9_image19 with fade
    p "(Hmmm. Quite a pricey wine. This girl has style.)"
    scene secret9_image20
    p "(Just to be sure. Haha. Now you are all mine!)"
    scene secret9_image16
    p "(Pretty comfy bed. Fucking her on here will be like heaven.)"
    a "I’m back."
    scene secret9_image17
    $ renpy.pause(1.0)

    p "Oohahah, *gulp*."
    scene secret9_image18
    $ renpy.pause(1.0)

    a "You like the view?" with dissolve
    scene secret9_image21
    $ renpy.pause(1.0)

    p "I’m almost speechless. Wow, you really ARE an angel."
    scene secret9_image22
    $ renpy.pause(1.0)

    a "Thank you. Now just lie on the bed and get comfy." with dissolve
    p "Yeah, sure. What about that wine?"
    a "I think we can try it later. Now I have another appetite in mind."
    p "(Haha, yeah, fuck the horny pills. I don’t need them.)"
    scene secret9_image23
    p "So, lady, I’m ready."
    #animation: secret9_angel_bra
    $ renpy.movie_cutscene("scenes/Angel/secret9/WEBM/secret9_angel_bra.webm", loops=0, delay=-1, stop_music=False)
    #TODO jor transition images
    #animation: secret9_angel_panty
    $ renpy.movie_cutscene("scenes/Angel/secret9/WEBM/secret9_angel_panty.webm", loops=0, delay=-1, stop_music=False)

    scene secret9_image24
    $ renpy.pause(1.0)

    a "Mmmmm…." with dissolve
    p "Damn, you are so fucking perfect, in every way."
    #animation: secret9_angel_panty_drop
    $ renpy.movie_cutscene("scenes/Angel/secret9/WEBM/secret9_angel_panty_drop.webm", loops=0, delay=-1, stop_music=False)
    scene secret9_image25
    a "Naked is the most comfy."
    scene secret9_image26
    p "WOW! WOW! Just wow! I’m living the dream right now!"
    a "And this is just the beginning."
    p "I can't wait to see what comes next."
    scene secret9_image27
    a "Mmmmm… You will love it."
    scene secret9_image28
    p "I’m in love with you now."
    #disolve
    scene secret9_image29 with dissolve
    p "Hey careful, it’s my favorite one."
    a "Now I am your favorite."
    #disolve:
    scene secret9_image30 with dissolve
    p "HAHA, you are really wild. I love it."
    a "I know…"
    scene secret9_image31 with dissolve
    $ renpy.pause(1.0)

    p "Ohohoh. Hmmmm… I’m really in heaven with a true angel."

    "*TO BE CONTINUED*"

    scene black with fade

    jump current_screen_selector


label angel_mc_gallery1:
    scene black
    scene secret10_image01
    a "And we are just getting started…"
    scene secret10_image02
    a "I don’t think we will need all these clothes anymore."
    p "Definitely."
    scene secret10_image03
    a "Woow. You surprise me a lot."
    scene secret10_image04
    a "I don’t think I ever saw a dick that BIG!"
    scene secret10_image05
    a "Do you like it?"
    scene secret10_image06
    p "Of course! You are doing really well!"
    scene secret10_image07
    a "Mmmmm..."
    scene secret10_image08
    p "Ooooh…. So tight."
    scene secret10_image09
    p "(She can barely take me inside. Hah.)"
    scene secret10_image11
    a "*gulp* Mmmm…."
    scene secret10_image12
    p "Aaah. I'm starting to feel your tight throat…."
    scene secret10_image09
    $ renpy.pause(0.5)
    scene secret10_image13 with dissolve
    $ renpy.pause(0.5)
    scene secret10_image10
    $ renpy.pause(0.5)
    scene secret10_image14 with dissolve
    $ renpy.pause(0.5)
    scene secret10_image10 with dissolve
    $ renpy.pause(0.5)
    scene secret10_image14 with dissolve
    $ renpy.pause(0.5)
    scene secret10_image10 with dissolve
    $ renpy.pause(0.5)
    scene secret10_image09
    $ renpy.pause(0.5)
    scene secret10_image13 with dissolve
    $ renpy.pause(0.5)
    scene secret10_image08
    $ renpy.pause(0.5)
    scene secret10_image11 with dissolve
    $ renpy.pause(0.5)
    scene secret10_image19
    p "Oh God, you are so great! I’m going to cum! Take it deep as you can pleaseee!!!"
    scene secret10_image10
    scene secret10_image14 with dissolve
    scene secret10_image18 with dissolve
    scene secret10_image17
    p "AAAH YEEES!!!! SUCK it aaalll!!"
    scene secret10_image19
    scene secret10_image15 with dissolve
    p "Ahaha! That was sooo awesome."

    scene secret10_image20
    a "Looks like you enjoyed it a lot.  Mmmmm."
    scene secret10_image22
    p "I can’t disagree."
    scene secret10_image21
    $ renpy.pause()

    scene secret10_image23
    a "Soo tasty…."
    p "(Woow she is sooo perfect. She sucked all my sperm out, and is licking the rest around…)"
    scene secret10_image24
    $ renpy.pause(0.5)
    scene secret10_image25 with dissolve
    a "Mmmmm…. I love it."

    scene secret10_image51 with dissolve
    scene secret10_image52 with dissolve
    scene secret10_image53 with dissolve
    scene secret10_image54 with dissolve
    scene secret10_image55 with dissolve
    scene secret10_image56 with dissolve
    scene secret10_image57 with dissolve
    scene secret10_image58 with dissolve
    scene secret10_image59 with dissolve
    scene secret10_image60 with dissolve
    scene secret10_image61 with dissolve

    scene secret10_image40 with dissolve
    scene secret10_image41 with dissolve
    scene secret10_image42 with dissolve
    scene secret10_image43 with dissolve
    scene secret10_image44 with dissolve
    scene secret10_image45 with dissolve
    scene secret10_image46 with dissolve
    scene secret10_image47 with dissolve
    scene secret10_image48 with dissolve
    scene secret10_image49 with dissolve
    scene secret10_image50 with dissolve

    scene secret10_image63 with dissolve
    scene secret10_image64 with dissolve
    scene secret10_image65 with dissolve
    scene secret10_image66 with dissolve
    scene secret10_image67 with dissolve
    scene secret10_image68 with dissolve
    scene secret10_image69 with dissolve
    scene secret10_image70 with dissolve
    scene secret10_image71 with dissolve
    scene secret10_image72 with dissolve
    scene secret10_image73 with dissolve

    scene secret10_image29 with dissolve
    scene secret10_image30 with dissolve
    scene secret10_image31 with dissolve
    scene secret10_image32 with dissolve
    scene secret10_image33 with dissolve
    scene secret10_image34 with dissolve
    scene secret10_image35 with dissolve
    scene secret10_image36 with dissolve
    scene secret10_image37 with dissolve
    scene secret10_image38 with dissolve
    scene secret10_image39 with dissolve

    p "Woow.. Your booobs look… bigger?"

    scene secret10_image26
    $ renpy.pause(1.5)
    a "Really?  I think you are just too excited. Hihi. Ready for another round?"  with dissolve
    scene secret10_image27
    p "Like never before. Haha."
    scene secret10_image28 with dissolve
    a "Good….."
    "*To be continued*"

    scene black with fade

    jump current_screen_selector
label angel_mc_gallery2:
    scene black
    scene secret11_image01
    p "Ooooh…"
    scene secret11_image02
    a "Mmmmm."
    scene secret11_image03
    a "Ahh.. You are really BIG…."
    #animations:
    #secret11_ride1
    $ renpy.movie_cutscene("scenes/secrets/11version/WEBM/secret11_ride1.webm", loops=-1,delay=-1, stop_music=False)
    #secret11_ride1_fast
    $ renpy.movie_cutscene("scenes/secrets/11version/WEBM/secret11_ride1_fast.webm", loops=-1,delay=-1, stop_music=False)
    #secret11_ride2
    $ renpy.movie_cutscene("scenes/secrets/11version/WEBM/secret11_ride2.webm", loops=-1,delay=-1, stop_music=False)
    #secret11_ride2_fast
    $ renpy.movie_cutscene("scenes/secrets/11version/WEBM/secret11_ride2_fast.webm", loops=-1,delay=-1, stop_music=False)
    #secret11_ride3
    $ renpy.movie_cutscene("scenes/secrets/11version/WEBM/secret11_ride3.webm", loops=-1,delay=-1, stop_music=False)
    #secret11_ride3_fast
    $ renpy.movie_cutscene("scenes/secrets/11version/WEBM/secret11_ride3_fast.webm", loops=-1,delay=-1, stop_music=False)
    scene secret11_image03
    a "YES! I can't get enough of your giant dick!! YES! C'mon fuck me harder!"
    p "AAAAhmm…. it’s too much……."

    scene secret11_image02
    scene secret11_image04 with dissolve
    p "AAARGHhh!!!"
    scene secret11_image05 with dissolve
    scene secret11_image06
    a "Ooouhhh….. it feels great."

    scene secret11_image39 with dissolve
    scene secret11_image40 with dissolve
    scene secret11_image41 with dissolve
    scene secret11_image42 with dissolve
    scene secret11_image43 with dissolve
    scene secret11_image44 with dissolve
    scene secret11_image45 with dissolve
    scene secret11_image46 with dissolve
    scene secret11_image47 with dissolve
    scene secret11_image48 with dissolve
    scene secret11_image49 with dissolve

    scene secret11_image28 with dissolve
    scene secret11_image29 with dissolve
    scene secret11_image30 with dissolve
    scene secret11_image31 with dissolve
    scene secret11_image32 with dissolve
    scene secret11_image33 with dissolve
    scene secret11_image34 with dissolve
    scene secret11_image35 with dissolve
    scene secret11_image36 with dissolve
    scene secret11_image37 with dissolve
    scene secret11_image38 with dissolve

    scene secret11_image17 with dissolve
    scene secret11_image18 with dissolve
    scene secret11_image19 with dissolve
    scene secret11_image20 with dissolve
    scene secret11_image21 with dissolve
    scene secret11_image22 with dissolve
    scene secret11_image23 with dissolve
    scene secret11_image24 with dissolve
    scene secret11_image25 with dissolve
    scene secret11_image26 with dissolve
    scene secret11_image27 with dissolve

    a "Aaaahh.. I love that feeeeling…"
    scene secret11_image10
    p "God, that was a hell of a ride."
    a "Hah, yeah! Ready to continue? Maybe between these juicy boobs?"
    scene secret11_image08
    p "Eeeh.. You want to go again?"
    scene secret11_image09 with dissolve
    p "You know, you are really stunning, and fucking you is the best thing I have ever done. But I’m feeling so tired now."
    scene secret11_image10
    scene secret11_image11 with dissolve
    a "Tired, you say?"
    a "That’s a shame…."
    scene secret11_image12 with dissolve
    a "I thought that we might fuck more. 'Cause maaaybe…."
    scene secret11_image08
    p "Maybe?"
    scene secret11_image13
    a "Nothing. I just thought that you would want to fuck my tight asshole?"
    scene secret11_image14
    a "What do you think? I was curious if your big cock could stretch my ass to a huge gape."
    p "Oh my God!"
    p "(Woow, what a nice sweet hole.)"
    scene secret11_image15
    a "Mmmm...  Such a shame. I was really eager to feel that cock inside of my tight asshole."
    scene secret11_image08
    scene secret11_image16 with dissolve
    p "Eeeh.. I think I changed my mind…."

    "*To be continued*"

    scene black with fade

    jump current_screen_selector

# The game starts here.
label start:
    python:
        player = Player("Derp", 100, 50)
        #player.hp = 50
        #player.mp = 10
        wire = Item("Tel", element="PuzzleItem01", image="wire_inventory", cost=0)
        apartment_keys = Item("Apartment Keys", element="PuzzleItem02", image="apartmentkeys_inventory", cost=0)
        car_key = Item("Araba Anahtarı", element="PuzzleItem03", image="carkey_inventory", cost=0)
        condoms = Item("Prezervatif", element="PuzzleItem04", image="condoms_inventory", cost=10)
        locker_key_125 = Item("Soyunma Odası Anahtarı 125", element="PuzzleItem05", image="lockerkey125_inventory", cost=0)
        lube = Item("Yağ", element="PuzzleItem06", image="lube_inventory", cost=20)
        cash = Item("Nakit", element="PuzzleItem07", image="money_inventory", cost=0)
        phone = Item("Telefon", element="PuzzleItem08", image="phone_inventory", cost=0)
        pills = Item("Seks Hapları", element="PuzzleItem09", image="sexpills_inventory", cost=0)
        credit_card = Item("Kredi Kartı", element="PuzzleItem10", image="credit_card_inventory", cost=0)
        bath_brush = Item("Banyo Fırçası", element="PuzzleItem11", image="bath_brush_inventory", cost=0)


        #chocolate = Item("Chocolate", hp=40, image="gui/inv_chocolate.png")
        #banana = Item("Banana", mp=20, image="gui/inv_banana.png")
        #gun = Item("Gun", element="bullets", image="gui/inv_gun.png", cost=7)
        #laser = Item("Laser Gun", element="laser", image="gui/inv_laser.png")
        inventory = Inventory()
        shop_stock = Inventory(isShop=True)

        shop_stock.add(condoms)
        shop_stock.add(lube)

        flash_drive = Item("USB", element="PuzzleItem11", image="flash_drive_inventory", cost=0)
        cursed_dollar = Item("Lanetli Dolar", element="PuzzleItem12", image="100bill_inventory", cost=0)
        devil_card = Item("Şeytan Arama Kartı", element="PuzzleItem13", image="devil_card_inventory", cost=0)

        cop_phone = Item("Telefon", element="PuzzleItem14", image="cop_phone_inventory", cost=0)
        cop_car_key = Item("Polis Araba Anahtarı", element="PuzzleItem15", image="cop_car_key_inventory", cost=0)
        panties = Item("Külot", element="PuzzleItem16", image="panties_inventory", cost=0)
        gun = Item("Silah", element="PuzzleItem17", image="gun_inventory", cost=0)
        photo = Item("Fotoğraf", element="PuzzleItem18", image="photo_inventory", cost=0)
        cop_apartment_keys = Item("Polis Daire Anahtarları", element="PuzzleItem19", image="copapartmentkeys_inventory", cost=0)
        drugs = Item("Uyuşturucu", element="PuzzleItem20", image="drugs_inventory", cost=0)
        scarlett_drive = Item("Scarletts Drive", element="PuzzleItem21", image="scarlett_drive_inventory", cost=0)
        anders_evidence = Item("Anders Kanıt", element="PuzzleItem22", image="anders_evidence_inventory", cost=0)
        den_key = Item("Ev Anahtarı", element="PuzzleItem23", image="den_key_inventory", cost=0)
        room4_key = Item("Oda 4 Anahtar", element="PuzzleItem24", image="room4_key_inventory", cost=0)

        #inventory.add(wire)
        #inventory.add(wire)
        #inventory.add(wire)
        #inventory.add(wire)
        #inventory.money = 10
        #add items to the initial inventory:
        #inventory.add(chocolate)
        #inventory.add(chocolate)
        #inventory.add(banana)


    scene black
    #centered "{size=+25}TODO need warning screen about adult content here{/size}"
    scene black_screen
    with fade

    $ renpy.pause(1.0)

    scene content_warning

    $ renpy.pause()
    scene black_screen
    menu:
        "Are you 18 years or older?"

        "Yes":
            jump tutorial

        "No":
            return
