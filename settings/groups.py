# Qtile workspaces

from libqtile.config import Key, Group
from libqtile.command import lazy
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
    Group('1', label="HOME", layout="monadtall"),
    Group(name='2', label="WEB", matches=[Match(wm_class='qutebrowser')], layout="monadtall"),
    Group(name='3', label="DEV", matches=[Match(wm_class='Alacritty')], layout="monadtall"),
    Group(name='4', label="CHAT", layout='monadtall')
]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])
