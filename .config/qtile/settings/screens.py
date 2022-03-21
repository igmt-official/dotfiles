import os
from libqtile import bar, widget, qtile
from libqtile.config import Screen

from .colors import colors

decor = {
    "background": colors['background'],
    "borderwidth": 3,
    "padding": 5,
    "highlight_method": 'text',
    "rounded": "true",
    "disable_drag": True,
    "inactive": colors['comment'],
    "active": colors['white'],
    "highlight_color": colors['background'],
    "this_current_screen_border": colors['red'],
    "block_highlight_text_color": colors['red'],
    # "this_screen_border": colors['foreground'],
    # "other_current_screen_border": colors['foreground'],
    # "other_screen_border": colors['foreground'],
    # "this_screen_border": colors['foreground'],
    # "decorations": [
    #        RectDecoration(
    #               use_widget_background=True,
    #               radius=17,
    #               filled=True,
    #               colour = colors['background'],
    #               padding_y = 5
    #               )
    #        ],
}

screens = [
    Screen(
        wallpaper='Pictures/Wallpaper/arch.jpg',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.Sep(
                       linewidth=0,
                       padding=5,
                       foreground=colors['background'],
                       background=colors['background']
                ),
                widget.TextBox(
                    text="",
                    padding=5,
                    fontsize=30,
                    foreground=colors['red'],
                    background=colors['background']
                ),
                # widget.TextBox(
                #        font = "UbuntuMono Nerd Font",
                #        text = '\uE0B0',
                #        background = colors['background'],
                #        foreground = colors['background'],
                #        padding = 0,
                #        fontsize = 25
                #        ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.GroupBox(
                    **decor,
                    font='JetBrainsMono Bold',
                    fontsize=10
                ),
                widget.TextBox(
                    text='\uE0B0',
                    background=colors['current_line'],
                    foreground=colors['background'],
                    padding=0,
                    fontsize=25
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['current_line'],
                    background=colors['current_line']
                ),
                widget.WindowName(
                    padding=5,
                    background=colors['current_line'],
                    foreground=colors['foreground'],
                    empty_group_string="Desktop",
                    max_chars=130,
                ),
                widget.TextBox(
                    text='\uE0B2',
                    background=colors['current_line'],
                    foreground=colors['background'],
                    padding=0,
                    fontsize=25
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.TextBox(
                    font="JetBrainsMono Bold",
                    text='UPDATES: ',
                    background=colors['background'],
                    foreground=colors['red'],
                    padding=0,
                    fontsize=10
                ),
                widget.CheckUpdates(
                    font="JetBrainsMono Bold",
                    fontsize=10,
                    update_interval=1800,
                    distro="Arch",
                    display_format="{updates}",
                    no_update_string='NO UPDATES',
                    foreground=colors['white'],
                    colour_have_updates=colors['green'],
                    colour_no_updates=colors['white'],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                        'alacritty' + ' -e sudo pacman -Syu')},
                    padding=5,
                    background=colors['background']
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.ThermalSensor(
                    font="JetBrainsMono Bold",
                    fontsize=10,
                    foreground=colors['green'],
                    background=colors['background'],
                    threshold=90,
                    fmt='THERMAL: {}',
                    padding=5
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.Memory(
                    font="JetBrainsMono Bold",
                    fontsize=10,
                    foreground=colors['yellow'],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                        "alacritty" + ' -e htop')},
                    fmt='MEMORY: {}',
                    padding=5,
                    background=colors['background']
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.CPU(
                    font="JetBrainsMono Bold",
                    fontsize=10,
                    foreground=colors['blue'],
                    background=colors['background'],
                    format='CPU: {freq_current}GHz {load_percent}%',
                    padding=5
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.Clock(
                    font="JetBrainsMono Bold",
                    fontsize=10,
                    foreground=colors['magenta'],
                    background=colors['background'],
                    format="%B %d %a %I:%M %p",
                    padding=5
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.Systray(
                    background=colors['background'],
                    icon_size=10,
                    padding=5
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.QuickExit(
                    background=colors['background'],
                    foreground=colors['red'],
                    default_text="",
                    fontsize=10,
                    padding=5,
                    countdown_start=5,
                    countdown_format="",
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
            ],
            24,
            background=colors['current_line'],
            margin=[0, 0, 21, 0],
        ),
        bottom=bar.Gap(18),
        left=bar.Gap(18),
        right=bar.Gap(18),
    ),
]
