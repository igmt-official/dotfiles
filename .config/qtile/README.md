# Qtile (Arch Based)

# Installing My Qtile

If you want to use my own config, then follow all my steps.

Install Dependencies:

First download the font that i'm using **[JetBrainsMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/JetBrainsMono.zip)**.

Now install ```Python Pip``` and ```Psutil```:

```bash
sudo pacman -S python-pip # This is for pip installer.
pip install psutil # Required for some widget on the bar.
```

Clone this repository and copy my configs:

```bash
git clone https://github.com/igmt-official/dotfiles.git
cp -r dotfiles/.config/qtile ~/.config
```

# My Qtile Application

If you only want specific features from my qtile customized, you can check it below.

### Theme

**[Dracula](https://www.gnome-look.org/s/Gnome/p/1687249)**

### Fonts

**[JetBrainsMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/JetBrainsMono.zip)**

### Application Launcher

**[Rofi](https://wiki.archlinux.org/title/Rofi)**:

```bash
sudo pacman -S rofi
```

### File Manager

**[Thunar](https://wiki.archlinux.org/title/thunar)**:

```bash
sudo pacman -S thunar
```

### Browser

**[QuteBrowser](https://wiki.archlinux.org/title/Qutebrowser)**:

```bash
sudo pacman -S qutebrowser
```
