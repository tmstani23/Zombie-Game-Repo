import cx_Freeze
import os
import sys

os.environ['TCL_LIBRARY'] = "C:\\Users\\tmstani23\\AppData\\Local\\Programs\\Python\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\tmstani23\\AppData\\Local\\Programs\\Python\\Python35-32\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("main.py")]
excludes = ['Tkinter']
files = ['manBlue_gun.png', 'manBlue_machinegun.png', 'manBlue_shotgun.png', 'bullet.png', 'zombie1_hold.png', 'whitePuff15.png', 
    'whitePuff16.png', 'whitePuff17.png', 'whitePuff18.png', 'splat red.png', "light_350_med.png", 'health_pack.png', 
    'obj_shotgun.png', 'weapon_machine.png','weapon_gun.png', 'tileGreen_39.png', 'spritesheet_tiles.png', 'espionage.ogg', 
    '8.wav', '9.wav', '10.wav', '11.wav', 'brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav', 
    'zombie-roar-3.wav', 'zombie-roar-5.wav', 'zombie-roar-6.wav', 'zombie-roar-7.wav', 'splat-15.wav', 'gun_silenced.wav', 
    'pistol.wav', 'shotgun.wav', 'level_start.wav', 'health_pack.wav', 'gun_pickup.wav', "level1.tmx", "l2.tmx", "level3.tmx", 
    'Impacted2.0.TTF', 'ZOMBIE.TTF', "attributions.txt"]
includes = ["settings", "sprites", "tilemap"]
cx_Freeze.setup(
    name = "Zombie Crawl",
    options = {"build_exe": {"packages": ["pygame", "os", "sys", "pytmx","pytweening", "itertools"], 'excludes': excludes, 'includes': includes, "include_files": files}},
    description ="Zombie Crawl",
    executables = executables
)

def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)

#shift right click open command window in root file 
#type python setup.py build   to create a build folder with all the files or,
#type python setup.py bdist_msi in the command window to create the windows installer