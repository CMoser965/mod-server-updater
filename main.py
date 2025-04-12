import os
import shutil

appdata_roaming = os.getenv('APPDATA')

minecraft_mods_dir = f"{appdata_roaming}\\.minecraft\\mods"

script_location = os.path.dirname(os.path.abspath(__file__))
all_mods_dir = f"{script_location}\\mods"

if(os.path.exists(minecraft_mods_dir)):
    print(f"Found Minecraft user mods location: {minecraft_mods_dir}")

    existingMods = []
    allMods = []

    for filename in os.listdir(minecraft_mods_dir):
        existingMods.append(filename)
        
    for filename in os.listdir(all_mods_dir):
        allMods.append(filename)
    
    missingMods = [mod for mod in allMods if mod not in existingMods]
    if(len(missingMods) > 0):
        print("Found missing mods!")
        for mod in missingMods:
            thisModPath = f"{all_mods_dir}\\{mod}"
            assert os.path.isfile(thisModPath)
            print(mod)
            shutil.copy2(thisModPath, minecraft_mods_dir)
            print(f"Copied {mod} to {minecraft_mods_dir}")
    else:
        print("Your mods are up to date.")