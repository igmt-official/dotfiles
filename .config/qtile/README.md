# Qtile (Arch Based)

## Installing My Qtile

If you want to use my own config, then follow all my steps.

If you not downloaded yet my repository:

```bash
git clone https://github.com/igmt-official/dotfiles.git
```

Copy my configs:

```bash
cp -r dotfiles/.config/qtile ~/.config
```

Install Dependencies:

First download the font that i'm using **[JetBrainsMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/JetBrainsMono.zip)**.

Now install ```Python Pip``` and ```Psutil```:

```bash
sudo pacman -S python-pip # This is for pip installer.
pip install psutil # Required for some widget on the bar.
```

Test it with **[Xephyr](https://wiki.archlinux.org/index.php/Xephyr)**:

```bash
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 qtile
```

## My Qtile Application

If you only want specific features from my qtile customized, you can check it below.

### Application Launcher

Install **[Rofi](https://wiki.archlinux.org/title/Rofi)**.

If you want to use dracula theme like on my rofi,
just follow the steps **[here](https://github.com/igmt-official/dotfiles/tree/main/.config/rofi)**.

```bash
sudo pacman -S rofi
```

### File Manager

Install **[Thunar](https://wiki.archlinux.org/title/thunar)**:

```bash
sudo pacman -S thunar
```

### Browser

Install **[QuteBrowser](https://wiki.archlinux.org/title/Qutebrowser)**.

Copy my **[Conifg](https://github.com/igmt-official/dotfiles/tree/main/.config/qutebrowser)** for the theme.

```bash
sudo pacman -S qutebrowser
```

### Theme

Download **[Dracula](https://www.gnome-look.org/s/Gnome/p/1687249)** or just copy my config:

```bash
cp -r dotfiles/.gtkrc-2.0 ~ # This will be placed on Root Folder.
cp -r dotfiles/.config/gtk-3.0 ~/.config
```

### Notification

Install **Dunst**.

And if you want to use my config, just copy my config **[Dunst](https://github.com/igmt-official/dotfiles/tree/main/.config/dunst)**

```bash
sudo pacman -S dunst
```

### Screenshot

Install **Scrot**.
```bash
sudo pacman -S scrot
```

And if you want to use my script for my key binding, copy my script **[Scrot](https://github.com/igmt-official/dotfiles/tree/main/.config/scrot)**, now add this key binding on **Keys.py**:

```python
    ([mod], "s", lazy.spawn(os.path.expanduser('~/.config/scrot/screenshot'))), # To screenshot whole window.
    ([mod, "shift"], "s", lazy.spawn(os.path.expanduser('~/.config/scrot/screenshot select'))), # To select area what you want to screenshot.
    ([mod, "control", "shift"], "s", lazy.spawn(os.path.expanduser('~/.config/scrot/screenshot window'))), # To screenshot only where you focus window.
```

### Fonts

Download **[JetBrainsMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/JetBrainsMono.zip)**
