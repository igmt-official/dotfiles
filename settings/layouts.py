
from libqtile import bar, layout, widget
from libqtile.config import Group, Key, Match, Screen
from libqtile.lazy import lazy

# Seperate Modules
from settings.keys import keys, mod
from settings import colors

# Groups
groups = [
    Group('1', label="HOME", layout="monadtall"),
    Group(name='2', label="WEB", matches=[Match(wm_class='qutebrowser')], layout="monadtall"),
    Group(name='3', label="DEV", matches=[Match(wm_class='Alacritty')], layout="monadtall"),
    Group(name='4', label="CHAT", layout='monadtall')
]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])
    
# Layouts
layout_theme = {"border_width": 2,
                "margin": 20,
                "border_focus": colors.bg,
                "border_normal": colors.darkBg
                }

layouts = [
    MonadTall(**layout_theme)
]

# Widgets
widget_defaults = dict(
    font = "sans",
    fontsize = 10,
    padding = 2,
    foreground = colors.fg,
    background = colors.bg
)

extension_defaults = widget_defaults.copy()

# Screens
screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Extras
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
