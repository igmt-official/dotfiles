import os

from libqtile import bar, widget, qtile
from libqtile.config import Screen

# from qtile_extras.widget.decorations import RectDecoration
# from qtile_extras import widget

from .colors import colors

decor = {
       "background": colors['darkBg'],
       "borderwidth": 3,
       "padding": 5,
       "highlight_method": 'line',
       "rounded": "true",
       "disable_drag": True,
       "inactive": colors['inactive'],
       "active": colors['active'],
       "highlight_color": colors['darkBg'],
       "this_current_screen_border": colors['fg'],
       "block_highlight_text_color": colors['fg'],
       # "this_screen_border": colors['bg'],
       # "other_current_screen_border": colors['bg'],
       # "other_screen_border": colors['bg'],
       # "this_screen_border": colors['bg'],
       # "decorations": [
       #        RectDecoration(
       #               use_widget_background=True, 
       #               radius=17, 
       #               filled=True, 
       #               colour = colors['darkBg'], 
       #               padding_y = 5
       #               )
       #        ],
}

screens = [
       Screen(
              wallpaper = 'Downloads/4431856.jpg',
              wallpaper_mode = 'fill',
              top = bar.Bar(
              [
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['fg'],
                            background = colors['fg']
                            ),
                     widget.TextBox(
                            text = "",
                            padding = 5,
                            fontsize = 35,
                            foreground = colors['darkBg'],
                            background = colors['fg']
                            ),
                     widget.TextBox(
                            font = "Ubuntu Mono Nerd Font",
                            text = '\uE0B0',
                            background = colors['darkBg'],
                            foreground = colors['fg'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.GroupBox(
                            **decor,
                            fontsize = 25
                            ),
                     widget.TextBox(
                            font = "Ubuntu Mono Nerd Font",
                            text = '\uE0B0',
                            background = colors['bg'],
                            foreground = colors['darkBg'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['fg'],
                            background = colors['bg']
                            ),
                     widget.WindowName(
                            padding = 5,
				background = colors['bg'],
				foreground = colors['fg'],
				empty_group_string = "Desktop",
				max_chars = 130,
				),
                     widget.Systray(
                            background = colors['bg'],
                            padding = 5
                            ),
                     widget.Sep(
                            linewidth = 0,
                            padding = 5,
                            foreground = colors['fg'],
                            background = colors['bg']
                            ),
                     widget.TextBox(
                            font = "Ubuntu Mono Nerd Font",
                            text = '\uE0B2',
                            background = colors['bg'],
                            foreground = colors['fg'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.ThermalSensor(
                            font = "Ubuntu Mono Nerd Font",
                            foreground = colors['darkBg'],
                            background = colors['fg'],
                            threshold = 90,
                            fmt = 'Temp: {}',
                            padding = 5
                            ),
                     widget.TextBox(
                            font = "Ubuntu Mono Nerd Font",
                            text = '\uE0B2',
                            background = colors['fg'],
                            foreground = colors['darkBg'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.Memory(
                            font = "Ubuntu Mono Nerd Font",
                            foreground = colors['fg'],
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("alacritty" + ' -e htop')},
                            fmt = ' {}',
                            padding = 5,
                            background = colors['darkBg']
                            ),
                     widget.TextBox(
                            font = "Ubuntu Mono Nerd Font",
                            text = '\uE0B2',
                            background = colors['darkBg'],
                            foreground = colors['fg'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.CPU(
                            font = "Ubuntu Mono Nerd Font",
                            foreground = colors['darkBg'],
                            background = colors['fg'],
                            format = ' {freq_current}GHz {load_percent}%',
                            padding = 5
                            ),
                     widget.TextBox(
                            font = "UbuntuMono Nerd Font",
                            text = '\uE0B2',
                            background = colors['fg'],
                            foreground = colors['darkBg'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.TextBox(
                            text = '',
                            background = colors['darkBg'],
                            foreground = colors['fg'],
                            padding = 5,
                            fontsize = 20
                            ),
                     widget.CheckUpdates(
                            font = "Ubuntu Mono Nerd Font",
                            update_interval = 1800,
                            distro = "Arch",
                            display_format = "Updates: {updates} ",
                            foreground = colors['fg'],
                            colour_have_updates = colors['fg'],
                            colour_no_updates = colors['darkBg'],
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty' + ' -e sudo pacman -Syu')},
                            padding = 5,
                            background = colors['darkBg']
                            ),
                     widget.TextBox(
                            font = "Ubuntu Mono Nerd Font",
                            text = '\uE0B2',
                            background = colors['darkBg'],
                            foreground = colors['fg'],
                            padding = 0,
                            fontsize = 25
                            ),
                     widget.TextBox(
                            text = '',
                            background = colors['fg'],
                            foreground = colors['darkBg'],
                            padding = 5,
                            fontsize = 20
                            ),
                     widget.Clock(
                            font = "Ubuntu Mono Nerd Font",
                            foreground = colors['darkBg'],
                            background = colors['fg'],
                            format = "%B %d %a %I:%M %p",
                            padding = 5
                            ),
              ],
              24,
              background = colors['bg'],
		margin = [0, 0, 21, 0],
		),
		bottom = bar.Gap(18),
		left = bar.Gap(18),
		right = bar.Gap(18),
       ),
]
