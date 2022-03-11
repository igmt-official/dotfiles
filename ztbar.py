from libqtile.bar import Bar

from libqtile.widget.groupbox import GroupBox
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.cpu import CPU
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.systray import Systray
from libqtile.widget.clock import Clock
from libqtile.widget.spacer import Spacer

from colors import zerotwo

bar = Bar([
    CurrentLayout(
        background = zerotwo['bg'],
    ),

    Spacer(length=10),
    
    WindowCount(
        text_format='缾 {num}',
        background = zerotwo['fg'],
        show_zero = True
    ),

    Spacer(length=10),

    Clock(
        background = zerotwo['fg'],
        format=' %Y-%m-%d %a %I:%M %p'),

    Spacer(length=10),

    # Prompt(foreground=gruvbox['fg']),

    WindowName(foreground = zerotwo['fg']),

    GroupBox(
        disable_drag = True,
        active = zerotwo['gray'],
        inactive = zerotwo['darkGray'],
        highlight_method = 'blockx',
        block_highlight_text_color= zerotwo['fg'],
        borderwidth = 0,
        highlight_color = gruvbox['darkBg'],
        background = zerotwo['bg']
    ),

    Spacer(length=100),

    Systray(
        padding=15,
        # background='#00000000'
    ),

    Spacer(length=10),

    CPU(
        format =' {freq_current}GHz {load_percent}%',
        background = zerotwo['bg']),

    Spacer(length=10),

    Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background = gruvbox['bg']),

    Spacer(length=10),

    Net(
        background = zerotwo['bg']
    ),
],
    margin=[10, 10, 5, 10],
    background='#00000000',
    opacity=1,
    size=25,
)
