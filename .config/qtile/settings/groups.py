# Qtile workspaces

from libqtile.config import Key, Group, Match
from libqtile.lazy import lazy
from .keys import mod, keys


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons: 
# nf-fa-firefox, 
# nf-fae-python, 
# nf-dev-terminal, 
# nf-fa-code, 
# nf-oct-git_merge, 
# nf-linux-docker,
# nf-mdi-image, 
# nf-mdi-layers

# Groups
groups = [
    Group(name = '1', label = "", layout = "monadtall"),
    Group(name = '2', label = "", matches = [Match(wm_class = 'qutebrowser')], layout = "monadtall"),
    Group(name = '3', label = "", matches = [Match(wm_class = 'Alacritty')], layout = "monadtall"),
    Group(name = '4', label = "ﭮ", matches = [Match(wm_class = 'discord')], layout = 'max'),
    Group(name = '5', label = "", matches = [Match(wm_class = 'gimp-2.10')], layout = 'max'),
    Group(name = '6', label = "阮", matches = [Match(wm_class = 'spotify')], layout = 'max'),
    Group(name = '7', label = "", matches = [Match(wm_class = 'vlc')], layout = 'max'),
]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])
