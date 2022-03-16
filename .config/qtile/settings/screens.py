import os

from libqtile import bar, widget, qtile
from libqtile.config import Screen

# from qtile_extras.widget.decorations import RectDecoration
# from qtile_extras import widget

from .colors import colors

decor = {
       "background": colors['background'],
       "borderwidth": 3,
       "padding": 5,
       "highlight_method": 'line',
       "rounded": "true",
       "disable_drag": True,
       "inactive": colors['comment'],
       "active": colors['cyan'],
       "highlight_color": colors['background'],
       "this_current_screen_border": colors['purple'],
       "block_highlight_text_color": colors['purple'],
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
              wallpaper = 'Pictures/Wallpaper/arch.png',
              wallpaper_mode = 'fill',
              top = bar.Bar(
              [
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['background'],
                            background = colors['background']
                            ),
                     widget.TextBox(
                            text = "",
                            padding = 5,
                            fontsize = 30,
                            foreground = colors['purple'],
                            background = colors['background']
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
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['background'],
                            background = colors['background']
                            ),
                     widget.GroupBox(
                            **decor,
                            fontsize = 20
                            ),
                     widget.TextBox(
                            text = '\uE0B0',
                            background = colors['current_line'],
                            foreground = colors['background'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['current_line'],
                            background = colors['current_line']
                            ),
                     widget.WindowName(
                            padding = 5,
				background = colors['current_line'],
				foreground = colors['foreground'],
				empty_group_string = "Desktop",
				max_chars = 130,
				),
                     widget.TextBox(
                            text = '\uE0B2',
                            background = colors['current_line'],
                            foreground = colors['cyan'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.TextBox(
                            font = "JetBrainsMono Bold",
                            text = '',
                            background = colors['cyan'],
                            foreground = colors['background'],
                            fontsize = 15
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['cyan'],
                            background = colors['cyan']
                            ),
                     widget.CheckUpdates(
                            font = "JetBrainsMono Bold",
                            update_interval = 1800,
                            distro = "Arch",
                            display_format = "{updates} ",
                            foreground = colors['background'],
                            colour_have_updates = colors['red'],
                            colour_no_updates = colors['background'],
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty' + ' -e sudo pacman -Syu')},
                            padding = 5,
                            background = colors['cyan']
                            ),
                     widget.TextBox(
                            text = '\uE0B2',
                            background = colors['cyan'],
                            foreground = colors['purple'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['purple'],
                            background = colors['purple']
                            ),
                     widget.TextBox(
                            font = "JetBrainsMono Bold",
                            text = '',
                            background = colors['purple'],
                            foreground = colors['background'],
                            fontsize = 15
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['purple'],
                            background = colors['purple']
                            ),
                     widget.ThermalSensor(
                            font = "JetBrainsMono Bold",
                            foreground = colors['background'],
                            background = colors['purple'],
                            threshold = 90,
                            fmt = '{}',
                            padding = 5
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['purple'],
                            background = colors['purple']
                            ),
                     widget.TextBox(
                            text = '\uE0B2',
                            background = colors['purple'],
                            foreground = colors['cyan'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['cyan'],
                            background = colors['cyan']
                            ),
                     widget.TextBox(
                            font = "JetBrainsMono Bold",
                            text = '',
                            background = colors['cyan'],
                            foreground = colors['background'],
                            fontsize = 20
                            ),
                     widget.Memory(
                            font = "JetBrainsMono Bold",
                            foreground = colors['background'],
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("alacritty" + ' -e htop')},
                            fmt = '{}',
                            padding = 5,
                            background = colors['cyan']
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['cyan'],
                            background = colors['cyan']
                            ),
                     widget.TextBox(
                            text = '\uE0B2',
                            background = colors['cyan'],
                            foreground = colors['purple'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['purple'],
                            background = colors['purple']
                            ),
                     widget.TextBox(
                            font = "JetBrainsMono Bold",
                            text = '',
                            background = colors['purple'],
                            foreground = colors['background'],
                            fontsize = 15
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['purple'],
                            background = colors['purple']
                            ),
                     widget.CPU(
                            font = "JetBrainsMono Bold",
                            foreground = colors['background'],
                            background = colors['purple'],
                            format = '{freq_current}GHz {load_percent}%',
                            padding = 5
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['purple'],
                            background = colors['purple']
                            ),
                     widget.TextBox(
                            text = '\uE0B2',
                            background = colors['purple'],
                            foreground = colors['cyan'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['cyan'],
                            background = colors['cyan']
                            ),
                     widget.TextBox(
                            font = "JetBrainsMono Bold",
                            text = '',
                            background = colors['cyan'],
                            foreground = colors['background'],
                            fontsize = 20
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['cyan'],
                            background = colors['cyan']
                            ),
                     widget.Clock(
                            font = "JetBrainsMono Bold",
                            foreground = colors['background'],
                            background = colors['cyan'],
                            format = "%B %d %a %I:%M %p",
                            padding = 5
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['cyan'],
                            background = colors['cyan']
                            ),
                     widget.TextBox(
                            text = '\uE0B2',
                            background = colors['cyan'],
                            foreground = colors['purple'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.Systray(
                            background = colors['purple'],
                            padding = 5
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['purple'],
                            background = colors['purple']
                            ),
                     widget.TextBox(
                            text = '\uE0B2',
                            background = colors['purple'],
                            foreground = colors['background'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.QuickExit(
                            background = colors['background'],
                            foreground = colors['red'],
                            default_text = "",
                            fontsize = 20,
                            padding = 5,
                            countdown_start = 5,
                            countdown_format = "",
                     ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['background'],
                            background = colors['background']
                            ),
              ],
              24,
              background = colors['current_line'],
		margin = [0, 0, 21, 0],
		),
		bottom = bar.Gap(18),
		left = bar.Gap(18),
		right = bar.Gap(18),
       ),
]
