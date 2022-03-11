from libqtile.lazy import lazy

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice
myBrowser = "qutebrowser"    # My browser of choice

keys = [
    # The essentials
    Key([mod], "Return", lazy.spawn(myTerm), desc='Launches My Terminal'),
    Key([mod, "shift"], "Return", lazy.spawn("dmenu_run -p 'Run: '"), desc='Run Launcher'),
    Key([mod], "b", lazy.spawn(myBrowser), desc='QuteBrowser'),
    Key([mod], "Tab", lazy.next_layout(), desc='Toggle through layouts'),
    Key([mod, "shift"], "c", lazy.window.kill(), desc='Kill active window'),
    Key([mod, "shift"], "r", lazy.restart(), desc='Restart Qtile'),
    Key([mod, "shift"], "q", lazy.shutdown(), desc='Shutdown Qtile'),
    # Window controls
    Key([mod], "j", lazy.layout.down(), desc='Move focus down in current stack pane'),
    Key([mod], "k", lazy.layout.up(), desc='Move focus up in current stack pane'),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), lazy.layout.section_down(), desc='Move windows down in current stack'),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), lazy.layout.section_up(), desc='Move windows up in current stack'),
    Key([mod], "h", lazy.layout.shrink(), lazy.layout.decrease_nmaster(), desc='Shrink window (MonadTall), decrease number in master pane (Tile)'),
    Key([mod], "l", lazy.layout.grow(), lazy.layout.increase_nmaster(), desc='Expand window (MonadTall), increase number in master pane (Tile)'),
    Key([mod], "n", lazy.layout.normalize(), desc='normalize window size ratios'),
    Key([mod], "m", lazy.layout.maximize(), desc='toggle window between minimum and maximum sizes'),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),
    # Stack controls
    Key([mod, "shift"], "Tab", lazy.layout.rotate(), lazy.layout.flip(), desc='Switch which side main pane occupies (XmonadTall)'),
    Key([mod], "space", lazy.layout.next(), desc='Switch window focus to other pane(s) of stack'),
    Key([mod, "shift"], "space", lazy.layout.toggle_split(), desc='Toggle between split and unsplit sides of stack'),
]
