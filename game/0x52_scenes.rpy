
init 999 python:
    class x52Scene(object):
        def __init__(self, title, label, image="", scope={}, addInventory=[]):
            self.title = title
            self.label = label
            self.image = image
            self.scope = scope
            self.addInventory = addInventory
        
        def replay(self):
            fullScope = globals().copy() 
            for inventItem in self.addInventory:
                if inventItem in globals():
                    fullScope["inventory"].items.append(globals()[inventItem])
            fullScope.update(self.scope) 
            
            self._m1_0x52_scenes__replayStarted = False 
            self._m1_0x52_scenes__originalLabelCallback = config.label_callback 
            config.label_callback = self._m1_0x52_scenes__labelCallback 
            
            renpy.call_replay(self.label, fullScope) 
            
            config.label_callback = self._m1_0x52_scenes__originalLabelCallback 
        
        def _m1_0x52_scenes__labelCallback(self, label, called):
            if label == self.label: 
                self._m1_0x52_scenes__replayStarted = True
            elif label.endswith('_game_menu') or label.endswith('_return') or label == '_hide_windows':
                pass
            elif self._m1_0x52_scenes__replayStarted and called and label != self.label: 
                renpy.end_replay()

    class x52SceneImage(renpy.display.core.Displayable):
        
        def __init__(self, scene, desaturated=False):
            super(x52SceneImage, self).__init__()
            self.scene = scene
            self.desaturated = desaturated
        
        def render(self, width, height, st, at):
            rv = renpy.display.render.Render(width, height)
            
            if self.scene.image: 
                img = im.Scale(self.scene.image, width, height)
                
                if self.desaturated:
                    img = im.MatrixColor(img, im.matrix.desaturate())
                if not renpy.seen_label(self.scene.label):
                    img = im.Blur(img, 1.5)
                
                imgRender = renpy.display.render.render(img, width, height, st, at)
                rv.blit(imgRender, (0, 0))
            
            else: 
                if self.desaturated:
                    rv.fill(renpy.easy.color('#000'))
                else:
                    rv.fill(renpy.easy.color('#333'))
            
            return rv

    class x52SceneCharacter(object):
        def __init__(self, name, image):
            self.name = name
            self.image = image
            self.scenes = []
            if renpy.loadable(image):
                self.thumbnailH = im.Scale(image, 300, 169)
                self.thumbnail = im.MatrixColor(self.thumbnailH, im.matrix.desaturate())
            else:
                self.thumbnail = Solid('#222')
                self.thumbnailH = Solid('#333')
        
        def addScene(self, scene):
            """ Only add a scene if it actually exists """
            if renpy.has_label(scene.label):
                self.scenes.append(scene)
        
        @property
        def pages(self):
            """ Calculate how many pages we need """
            import math
            return int(math.ceil(float(len(self.scenes))/x52Scenes.itemsPerPage))

    class x52ScenesClass(object):
        def __init__(self):
            self.characters = []
            self._m1_0x52_scenes__selectedCharacter = None
            self.currentPage = 1
            self.itemsPerPage = 9
            
            char = x52SceneCharacter('Melek', 'scenes/introduction/intro_11.webp')
            char.addScene(x52Scene("Bay Anders ödülü", "scene_angel_rewards_mc_anders_for_not_being_naughty_with_rebecca", "scenes/Mranders/32_angel_hj/anders_s32_angel_hj02.WEBP"))
            self.addCharacter(char)
            
            char = x52SceneCharacter('Asyalı kız', 'scenes/Asian girl/01_sexy_photos/asiangirl_s01_sexy_photo01.webp')
            char.addScene(x52Scene("Geceleri polis ziyaretleri", "scene_asian_visits_cop_at_night", "scenes/Policeman/07_asian_girl/policeman_s07_asian02.webp"))
            self.addCharacter(char)
            
            char = x52SceneCharacter('Bethany', 'scenes/Bethany/03_Bethany_WC/BethanyS03_WC02.webp')
            char.addScene(x52Scene("Bethany ve Brandon gölette", "scene_bethany_and_brandon_in_pond", "scenes/Bethany/01_Pond_romance/BethanyS01_pond_romance02.webp", {}, ['bath_brush']))
            char.addScene(x52Scene("Araba seks", "scene_bethany_and_brandon_in_pond_continued", "scenes/Bethany/02_car_sex/BethanyS02_car_sex011.webp", {}, ['pills']))
            char.addScene(x52Scene("Bikini yarışması", "scene_beach_bikini_competition", "scenes/Policeman/35_bikini_competition/policeman_s35_bikini_competition39.WEBP"))
            char.addScene(x52Scene("Aşırı büyüme rüyası", "scene_bed_after_bikini_contest", "scenes/Policeman/39_bethany_overgrow_dream/policeman_s39_overgrow_dream21.webp"))
            char.addScene(x52Scene("Scarlett'in rüyası", "scene_meet_up_with_ivana_n_sophia_after_choices_afternoon", "scenes/Scarlett/36_dreaming/scarlett_s36_dreaming02.WEBP"))
            char.addScene(x52Scene("Maç sonrası üçlü", "scene_bad_girls_locker_room_horny_after_volleyball", "scenes/Mranders/04_aftermatch_threesome/anders_s04_aftermatch_threesome09.WEBP", {"mc_anders_has_drink_for_horny_bad_girls": True}))
            self.addCharacter(char)
            
            char = x52SceneCharacter('Brooke', 'scenes/Policeman/13_dean_second/policeman_s13_dean_second01.webp')
            char.addScene(x52Scene("Bikini yarışması", "scene_beach_bikini_competition", "scenes/Policeman/35_bikini_competition/policeman_s35_bikini_competition39.WEBP"))
            char.addScene(x52Scene("Scarlett'in rüyası", "scene_meet_up_with_ivana_n_sophia_after_choices_afternoon", "scenes/Scarlett/36_dreaming/scarlett_s36_dreaming02.WEBP"))
            char.addScene(x52Scene("Maç sonrası üçlü", "scene_bad_girls_locker_room_horny_after_volleyball", "scenes/Mranders/04_aftermatch_threesome/anders_s04_aftermatch_threesome09.WEBP", {"mc_anders_has_drink_for_horny_bad_girls": True}))
            self.addCharacter(char)
            
            char = x52SceneCharacter('Şeytan', 'scenes/introduction/intro_17.webp')
            char.addScene(x52Scene("Bay Anders kırbaçlama", "scene_mc_anders_whipping_devil", "scenes/Mranders/13_whipping_devil/anders_s13_whipping_devil11.WEBP"))
            self.addCharacter(char)
            
            char = x52SceneCharacter('Ivana', 'scenes/Policeman/12_visit_ivana/policeman_s12_visit_ivana01.webp')
            char.addScene(x52Scene("Bay Anders Laptop", "interaction_school_anders_office_laptop", "scenes/Policeman/15_searching_anders_office/policeman_s15_ivana_anim1.webp", {"anders_office_found_flash_drive": True}))
            char.addScene(x52Scene("Bikini yarışması", "scene_beach_bikini_competition", "scenes/Policeman/35_bikini_competition/policeman_s35_bikini_competition39.WEBP"))
            char.addScene(x52Scene("Lezbiyen Üçlü", "scene_mc_scarlett_with_ivana_n_sophia_threesome", "scenes/Scarlett/28_pills_test_threesome/scarlett_s27_lesbian_threesome00.WEBP"))
            char.addScene(x52Scene("Ofis seks", "scene_mc_anders_needs_to_check_anders_laptop_for_pills_info", "scenes/Mranders/16_ivana_sexscene/anders_s16_ivana_sex_in_office01.WEBP", {"mc_scarlett_accepted_devils_help_with_anders": False, "toggle_mc_scarlett_chose_sophia": False}))
            char.addScene(x52Scene("Uyku BJ", "scene_mc_anders_playing_with_sleeping_girls_at_winners_party", "scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_ivana_trans1.WEBP", {"counter_sleeping_girls_winners_party": 1}))
            self.addCharacter(char)
            
            char = x52SceneCharacter('Megan', 'scenes/Megan/S01_spy_on_wc/MeganS01_02.webp')
            char.addScene(x52Scene("Uyku BJ", "scene_mc_anders_playing_with_sleeping_girls_at_winners_party", "scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_megan_trans1.WEBP", {"counter_sleeping_girls_winners_party": 1}))
            self.addCharacter(char)
            
            char = x52SceneCharacter('Rebecca', 'scenes/Mranders/12_livingroom_with_rebecca/anders_s12_rebecca_living_room01.WEBP')
            char.addScene(x52Scene("Bay Anders' dream", "scene_mc_anders_dream_about_rebecca", "scenes/Mranders/11_dream_rebecca/anders_s11_rebecca_dream04.WEBP"))
            char.addScene(x52Scene("İçmek", "scene_anders_apartment_after_rebecca_restaurant_date", "scenes/Mranders/31_rebecca_evening/anders_s31_rebecca_evening01.WEBP", {"numtype_mc_anders_bought_car_for_rebecca": 2, "mc_anders_and_rebecca_store_count": 99}))
            char.addScene(x52Scene("Uyku sırasında", "scene_mc_anders_second_chance_to_fool_around_with_rebecca", "scenes/Mranders/33_fun_during_sleep/anders_s33_fun_during_sleep06.WEBP"))
            char.addScene(x52Scene("Sabah duşu", "scene_mc_anders_proper_shower_with_rebecca", "scenes/Mranders/34_morning_shower_with_rebecca/anders_s34_morning_shower_with_rebbeca06.WEBP"))
            self.addCharacter(char)
            
            char = x52SceneCharacter('Scarlett', 'scenes/Policeman/40_unknown_house/policeman_s40_unknown_house15.webp')
            char.addScene(x52Scene("Bilinmeyen ev", "scene_den_room4_scarlett_take_advantage", "scenes/Policeman/40_unknown_house/policeman_s40_unknown_house29.webp"))
            char.addScene(x52Scene("Oyuncak", "dildo_choices", "scenes/Scarlett/20_toys_play/scarlett_s20_toys03.webp"))
            char.addScene(x52Scene("Striptiz", "scene_as_scarlett_dancing_for_burt", "scenes/Scarlett/21_striptease/scarlett_s21_striptease02.webp"))
            char.addScene(x52Scene("Webcam şovu", "scenes_sophia_room_accept_webshow_offer", "scenes/Scarlett/22_webcam_show/scarlett_s22_webcam06.webp"))
            char.addScene(x52Scene("Lezbiyen Üçlü", "scene_mc_scarlett_with_ivana_n_sophia_threesome", "scenes/Scarlett/28_pills_test_threesome/scarlett_s27_lesbian_threesome00.WEBP"))
            char.addScene(x52Scene("Scarlett'in rüyası", "scene_meet_up_with_ivana_n_sophia_after_choices_afternoon", "scenes/Scarlett/36_dreaming/scarlett_s36_dreaming02.WEBP"))
            char.addScene(x52Scene("Anders tarafından kullanıldı", "scene_one_of_three_anders_office", "scenes/Scarlett/37_used_by_anders/scarlett_s37_used_by_anders10.WEBP"))
            char.addScene(x52Scene("Uyku BJ", "scene_mc_anders_playing_with_sleeping_girls_at_winners_party", "scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_scarlett_trans1.WEBP", {"counter_sleeping_girls_winners_party": 1}))
            char.addScene(x52Scene("Webcam şovu 2", "interaction_sofias_room_winners_party_computer", "scenes/Mranders/43_sophia_and_scarlett/WEBM/anders_s43_sophia_and_scarlett_transfer2.WEBP"))
            self.addCharacter(char)
            
            char = x52SceneCharacter('Sophia', 'scenes/Mom/02_restaurant/MomS02_restaurant3.webp')
            char.addScene(x52Scene("Polisin rüyası", "sophia_apartment_policeman_dreaming", "scenes/Sophia/S01_policeman_dreaming/SophiaS01_01.webp"))
            char.addScene(x52Scene("Soyunma odası", "sophia_cop_locker_room_sex_after_volleyball", "scenes/Policeman/28_locker_room_sophia_sex/policeman_s28_locker_room_sex_cumshot01.webp"))
            char.addScene(x52Scene("Bikini yarışması", "scene_beach_bikini_competition", "scenes/Policeman/35_bikini_competition/policeman_s35_bikini_competition39.WEBP"))
            char.addScene(x52Scene("Webcam şovu", "scenes_sophia_room_accept_webshow_offer", "scenes/Scarlett/22_webcam_show/scarlett_s22_webcam06.webp"))
            char.addScene(x52Scene("Lezbiyen Üçlü", "scene_mc_scarlett_with_ivana_n_sophia_threesome", "scenes/Scarlett/28_pills_test_threesome/scarlett_s27_lesbian_threesome00.WEBP"))
            char.addScene(x52Scene("Uyku BJ", "scene_mc_anders_playing_with_sleeping_girls_at_winners_party", "scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_sophia_trans1.WEBP", {"counter_sleeping_girls_winners_party": 1}))
            char.addScene(x52Scene("Webcam şovu 2", "interaction_sofias_room_winners_party_computer", "scenes/Mranders/43_sophia_and_scarlett/WEBM/anders_s43_sophia_and_scarlett_transfer2.WEBP"))
            self.addCharacter(char)
            
            char = x52SceneCharacter('Tracy', 'scenes/Brandon/06_brandon_house/BrandonS06_house3.webp')
            char.addScene(x52Scene("Mutfak seks", "scene_tracy_in_brandon_house", "scenes/Tracy/01_kitchen_sex/TracyS01_kitchen_sex12.webp"))
            char.addScene(x52Scene("Banyo seks", "scene_tracy_in_shower", "scenes/Tracy/02_bathroom_sex/TracyS02_bathroom3.webp"))
            char.addScene(x52Scene("Melek ile Bonus", "phone_bonus1_gallery", "scenes/Tracy/03_bonus1/bonus1_cumshot1.webp"))
            char.addScene(x52Scene("Uyku BJ", "scene_mc_anders_playing_with_sleeping_girls_at_winners_party", "scenes/Mranders/42_sleeping_bj/WEBM/anders_s42_sleeping_bj_tracy_trans1.WEBP", {"counter_sleeping_girls_winners_party": 1}))
            self.addCharacter(char)
            
            char = x52SceneCharacter('Diğer', 'scenes/introduction/intro_01.webp')
            char.addScene(x52Scene("Tuzağa düşmüş kız", "scene_cops_apartment_hallway_can_hear_muffled_voice", "scenes/Policeman/10_trapped_girl/policeman_s10_trapped_girl_anim.webp"))
            char.addScene(x52Scene("Nottan sonra", "scene_see_trapped_girl_after_note_left", "scenes/Policeman/29_blondie/policeman_s29_blondie01.webp", {"devil_or_angel_explained_the_secret_of_the_pills": True}))
            char.addScene(x52Scene("Showroom seks", "rebecca_date_car_showroom", "scenes/Mranders/30_showroom_sexscene/anders_s30_showroom_sexscene07.WEBP"))
            self.addCharacter(char)
        
        
        def addCharacter(self, char):
            """ Only add a character if it has scenes """
            if len(char.scenes) > 0:
                self.characters.append(char)
        
        @property
        def selectedCharacter(self):
            return self._m1_0x52_scenes__selectedCharacter
        
        @selectedCharacter.setter
        def selectedCharacter(self, char):
            self._m1_0x52_scenes__selectedCharacter = char
            self.currentPage = 1

    x52Scenes = x52ScenesClass()

    class x52ImageAutoScale(renpy.display.core.Displayable):
        def __init__(self, image, scaleHeight=False):
            super(x52ImageAutoScale, self).__init__()
            self._m1_0x52_scenes__image = image
            self._m1_0x52_scenes__scaleHeight = scaleHeight
        
        def render(self, width, height, st, at):
            newWidth = width
            newHeight = height
            
            
            imgSize = renpy.display.render.render(Image(self._m1_0x52_scenes__image), config.screen_width, config.screen_height, 0, 0)
            if self._m1_0x52_scenes__scaleHeight:
                scaleFactor = height / imgSize.height if height < imgSize.height else 1.0
                newWidth = imgSize.width * scaleFactor 
            else:
                scaleFactor = width / imgSize.width if width < imgSize.width else 1.0
                newHeight = imgSize.height * scaleFactor 
            
            img = im.FactorScale(self._m1_0x52_scenes__image, scaleFactor)
            if newHeight > height or newWidth> width:
                img = im.Crop(img, (0, 0, width, height))
            
            imgRender = renpy.display.render.render(img, width, height, st, at)
            rv = renpy.display.render.Render(width, height)
            rv.blit(imgRender, (0, 0))
            
            return rv
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
