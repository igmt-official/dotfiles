# -*- coding: utf-8 -*-
# Main Modules
import os
import subprocess
from typing import List 
from libqtile import hook
# from libqtile.utils import guess_terminal

# Separate Modules
from settings.key import keys, mouse
from settings.layouts import groups, layouts, widget_defaults, screens

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
