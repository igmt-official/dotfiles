import os
from libqtile import qtile
from libqtile.config import Key
from libqtile.lazy import lazy

# Qtile keybindings

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.reload_config()),
    ([mod, "control", "shift"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Gimp
    ([mod], "d", lazy.spawn("discord")),

    # Gimp
    ([mod], "g", lazy.spawn("gimp-2.10")),

    # Spotify
    ([mod], "q", lazy.spawn("spotify")),
    
    # Dmenu
    # ([mod, "shift"], "Return", lazy.spawn("dmenu_run -p 'Run: '")),

    # Menu
    ([mod], "m", lazy.spawn(os.path.expanduser('~/.config/rofi/launchers/colorful/launcher.sh'))),
    #([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("qutebrowser")),

    # File Explorer
    ([mod], "e", lazy.spawn("alacritty -e ranger")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    # ([mod], "r", lazy.spawn("redshift -O 2400")),
    # ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    # ([mod], "s", lazy.spawn('screenshot')),
    # ([mod, "shift"], "s", lazy.spawn('screenshot select')),
    # ([mod, "control", "shift"], "s", lazy.spawn('screenshot window')),
    ([mod], "s", lazy.spawn(os.path.expanduser('~/.config/scrot/screenshot'))),
    ([mod, "shift"], "s", lazy.spawn(os.path.expanduser('~/.config/scrot/screenshot select'))),
    ([mod, "control", "shift"], "s", lazy.spawn(os.path.expanduser('~/.config/scrot/screenshot window'))),
    # ([mod], "s", lazy.spawn("scrot")),
    # ([mod, "shift"], "s", lazy.spawn("scrot -s")),
    # ([mod, "control", "shift"], "s", lazy.spawn("scrot --focused")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    # ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    # ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]

