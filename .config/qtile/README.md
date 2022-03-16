# Qtile (Arch Based)

# About

Why i use **Qtile**?
so i am new in arch linux and installing of display manager or window manager,
i tried to install different window manager and it took me weeks to expirement each different window manager,
and i'm and stuck and struggle because i don't know how i will customize it from scratch because i don't understand what language they are,
so while i'm exploring different window manager, i fount **Qtile** is written **Python** language, now here's the thing why i decide to use **Qtile**,
it because i am a **Python Developer** so it easy to me to understand what code inside their config, and i can customize it from scratch.

# Installing My Qtile

If you want to use my own config, then follow all my steps.

If you not downloaded yet my repository:

```bash
git clone https://github.com/igmt-official/dotfiles.git
```

First Install Our Dependencies:

Download the font that i'm using **[JetBrainsMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/JetBrainsMono.zip)**.

Now install **Python Pip** and **Psutil**:

```bash
sudo pacman -S python-pip # This is for pip installer.
pip install psutil # Required for some widget on the bar.
```

Copy my configs:

```bash
cp -r dotfiles/.config/qtile ~/.config
```

Test it with **[Xephyr](https://wiki.archlinux.org/index.php/Xephyr)**:

```bash
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 qtile
```

# My Qtile Features

If you only want specific features from my qtile customized, you can check it below.

## Terminal

Install **Alacritty**.

If you want to use dracula theme like on my alacritty,
just follow the steps **[here](https://github.com/igmt-official/dotfiles/tree/main/.config/alacritty)**.

```bash
sudo pacman -S alacritty
```

## Text Editor

Install **Neovim**:

```bash
sudo pacman -S neovim
```

## Fonts

Download **[JetBrainsMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/JetBrainsMono.zip)**

## ZSH

Install **Zsh**:

```bash
sudo pacman -S zsh
```

Setup our zsh and make it default shell:

```bash
zsh
0 # To create .zshrc file for customizing.

chsh -l # To list all installed shells.
chsh -s /usr/bin/zsh # And to set one as default for your user do.

# And now reboot your pc.
```

## Application Launcher

Install **[Rofi](https://wiki.archlinux.org/title/Rofi)**.

If you want to use dracula theme like on my rofi,
just follow the steps **[here](https://github.com/igmt-official/dotfiles/tree/main/.config/rofi)**.

```bash
sudo pacman -S rofi
```

## File Manager

Install **[Thunar](https://wiki.archlinux.org/title/thunar)**:

```bash
sudo pacman -S thunar
```

## Browser

Install **[QuteBrowser](https://wiki.archlinux.org/title/Qutebrowser)**.

Copy my **[Conifg](https://github.com/igmt-official/dotfiles/tree/main/.config/qutebrowser)** for the theme.

```bash
sudo pacman -S qutebrowser
```

## Theme

Download **[Dracula](https://www.gnome-look.org/s/Gnome/p/1687249)** or just copy my config:

```bash
cp -r dotfiles/.gtkrc-2.0 ~ # This will be placed on Root Folder.
cp -r dotfiles/.config/gtk-3.0 ~/.config
```

## Notification

Install **Dunst**.

And if you want to use my config, just copy my config **[Dunst](https://github.com/igmt-official/dotfiles/tree/main/.config/dunst)**

```bash
sudo pacman -S dunst
```

Also i have **[Custom Scripts](https://github.com/igmt-official/dotfiles/tree/main/.local/bin)**, for wifi, screenshot, and volume notificiation.

## Screenshot

Install **Scrot**:

```bash
sudo pacman -S scrot
```

And if you want to use my script for my key binding, copy my script **[Scrot](https://github.com/igmt-official/dotfiles/tree/main/.config/scrot)**, now add this key binding on **Keys.py**:

```python
    ([mod], "s", lazy.spawn(os.path.expanduser('~/.config/scrot/screenshot'))), # To screenshot whole window.
    ([mod, "shift"], "s", lazy.spawn(os.path.expanduser('~/.config/scrot/screenshot select'))), # To select area what you want to screenshot.
    ([mod, "control", "shift"], "s", lazy.spawn(os.path.expanduser('~/.config/scrot/screenshot window'))), # To screenshot only where you focus window.
```
