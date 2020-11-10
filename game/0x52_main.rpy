init python:
    class x52Mod:
        version = '2.1'
        say = Character("AOC", color="#513c6d")
        
        @staticmethod
        def unlockSecrets():
            import re
            unlockCount = 0
            for varName in globals(): 
                if varName.startswith("seen_secret_") or re.match(".*_secret([0-9]+)?_found$", varName) != None or varName == "show_bonus_button_on_phone" or varName == "show_exgf_button_on_phone":
                    if globals()[varName] == False: 
                        globals()[varName] = True 
                        unlockCount += 1
            
            return unlockCount

    config.overlay_screens.append("cheats_button")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
